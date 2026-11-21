#!/usr/bin/env python3
"""Portable ECOSYSTEM_CONTRACT v1.1.0 core validator reusable across all suites.

Validates domain-neutral invariants:
  1. suite.yaml v1.1.0 manifest structure
  2. Director SKILL.md v1.1.0 contract (frontmatter, headings, Verdict Envelope v1.1.0)
  3. Exact <suite_id>- rule namespacing & harness caps
  4. Portability & privacy leak gate
  5. Live multi-suite coexistence & anti-recursive-discovery test + CPU scanner self-test
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REQUIRED_DIRECTOR_H2 = [
    "When To Use",
    "Do Not Use When",
    "Required Inputs",
    "Orchestration Protocol",
    "Mandatory Closing Output",
    "Guardrails",
]
ALLOWED_SYNTHESIS_MODES = {"conjunctive_gate", "weighted_panel"}
MAX_DIRECTOR_DISCOVERY_CHARS = 384  # name <= 64 + description <= 320


def _extract_h2(body: str) -> list[str]:
    h2s: list[str] = []
    in_code = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code and line.startswith("## "):
            h2s.append(line[3:].strip())
    return h2s


def check_suite_manifest(repo_root: Path) -> tuple[bool, list[str], dict[str, Any]]:
    errors: list[str] = []
    suite_path = repo_root / "suite.yaml"
    if not suite_path.is_file():
        return False, ["Missing suite.yaml at repository root"], {}
    try:
        data = yaml.safe_load(suite_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return False, [f"suite.yaml YAML error: {exc}"], {}
    if not isinstance(data, dict):
        return False, ["suite.yaml must parse as a YAML mapping"], {}

    if data.get("ecosystem_contract_version") != "1.1.0":
        errors.append(f"suite.yaml: ecosystem_contract_version must be '1.1.0', got {data.get('ecosystem_contract_version')!r}")
    if data.get("synthesis_mode") not in ALLOWED_SYNTHESIS_MODES:
        errors.append(f"suite.yaml: synthesis_mode must be in {sorted(ALLOWED_SYNTHESIS_MODES)}")
    for req in ("suite_id", "repo_name", "director_slug", "judgment_file", "schema_version"):
        if not isinstance(data.get(req), str) or not data[req].strip():
            errors.append(f"suite.yaml: missing or empty '{req}'")

    scope = data.get("sdlc_scope")
    if not isinstance(scope, dict) or not scope.get("primary_artifacts") or not scope.get("sdlc_stages"):
        errors.append("suite.yaml: sdlc_scope must declare primary_artifacts and sdlc_stages")

    tooling = data.get("tooling")
    if not isinstance(tooling, dict) or "accepted_formats" not in tooling:
        errors.append("suite.yaml: missing tooling block with accepted_formats")
    elif tooling.get("pre_scanner"):
        scanner_path = repo_root / tooling["pre_scanner"]
        if not scanner_path.is_file():
            errors.append(f"suite.yaml: tooling.pre_scanner '{tooling['pre_scanner']}' does not exist")

    targets = data.get("handoff_targets")
    if not isinstance(targets, list) or not targets:
        errors.append("suite.yaml: handoff_targets must be a non-empty list")
    else:
        for idx, t in enumerate(targets):
            if not isinstance(t, dict) or not t.get("suite_id") or not t.get("trigger_condition"):
                errors.append(f"suite.yaml: handoff_targets[{idx}] missing suite_id or trigger_condition")

    return len(errors) == 0, errors, data


def check_director_contract(repo_root: Path, suite_data: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    director_slug = suite_data.get("director_slug", "")
    suite_id = suite_data.get("suite_id", "")
    director_path = repo_root / "committee" / director_slug / "SKILL.md"
    if not director_path.is_file():
        return False, [f"Missing committee/{director_slug}/SKILL.md"]

    text = director_path.read_text(encoding="utf-8")
    if len(text.splitlines()) > 500:
        errors.append(f"committee/{director_slug}/SKILL.md exceeds 500-line ceiling")

    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return False, [f"committee/{director_slug}/SKILL.md missing valid YAML frontmatter"]
    fm = yaml.safe_load(m.group(1))
    body = m.group(2)

    if fm.get("name") != director_slug:
        errors.append(f"director SKILL.md: name '{fm.get('name')}' != '{director_slug}'")
    desc = fm.get("description", "")
    if not isinstance(desc, str) or len(desc) == 0 or len(desc) > 320:
        errors.append(f"director SKILL.md: description length {len(str(desc))} invalid (must be 1..320)")
    meta = fm.get("metadata", {})
    for rk in ("schema_version", "suite_id", "author"):
        if rk not in meta:
            errors.append(f"director SKILL.md: metadata missing '{rk}'")
    if meta.get("suite_id") != suite_id:
        errors.append(f"director SKILL.md: metadata.suite_id '{meta.get('suite_id')}' != '{suite_id}'")

    h2s = _extract_h2(body)
    if h2s != REQUIRED_DIRECTOR_H2:
        errors.append(f"director SKILL.md: H2 mismatch expected={REQUIRED_DIRECTOR_H2}, actual={h2s}")

    for tok in (
        "verdict_envelope:",
        'envelope_version: "1.1.0"',
        f'suite_id: "{suite_id}"',
        "evidence_tier:",
        "evidence:",
        "visited_suites:",
        "max_hops:",
        "escalations:",
    ):
        if tok not in body:
            errors.append(f"director SKILL.md: Verdict Envelope v1.1.0 missing '{tok}'")

    return len(errors) == 0, errors


def check_adapters_and_namespacing(repo_root: Path, suite_data: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    suite_id = suite_data.get("suite_id", "")

    agents_md = repo_root / "AGENTS.md"
    if not agents_md.is_file():
        errors.append("Missing AGENTS.md")
    elif len(agents_md.read_text(encoding="utf-8")) >= 4000:
        errors.append("AGENTS.md exceeds 4,000-char limit")

    claude_md = repo_root / "CLAUDE.md"
    if not claude_md.is_symlink() or os.readlink(claude_md) != "AGENTS.md":
        errors.append("CLAUDE.md must be a relative symlink to 'AGENTS.md'")

    ag_rule = repo_root / "adapters" / "antigravity" / f"{suite_id}-bootstrap.md"
    if not ag_rule.is_file():
        errors.append(f"Missing adapters/antigravity/{suite_id}-bootstrap.md (must use exact <suite_id>- prefix)")
    elif ag_rule.stat().st_size >= 24000:
        errors.append(f"{ag_rule.name} >= 24,000 bytes limit")

    cur_rule = repo_root / "adapters" / "cursor" / f"{suite_id}-director.mdc"
    if not cur_rule.is_file():
        errors.append(f"Missing adapters/cursor/{suite_id}-director.mdc (must use exact <suite_id>- prefix)")
    else:
        ctext = cur_rule.read_text(encoding="utf-8")
        if "alwaysApply: false" not in ctext or "globs:" not in ctext:
            errors.append(f"{cur_rule.name} missing required Cursor frontmatter (alwaysApply: false, globs)")

    ws_rule = repo_root / "adapters" / "windsurf-devin" / f"{suite_id}-director.md"
    if not ws_rule.is_file():
        errors.append(f"Missing adapters/windsurf-devin/{suite_id}-director.md (must use exact <suite_id>- prefix)")
    elif len(ws_rule.read_text(encoding="utf-8")) >= 12000:
        errors.append(f"{ws_rule.name} >= 12,000-char hard limit")

    install_sh = repo_root / "adapters" / "install.sh"
    if not install_sh.is_file() or not os.access(install_sh, os.X_OK):
        errors.append("adapters/install.sh must exist and be executable (chmod +x)")

    dsh_plugin = repo_root / "adapters" / "deepseek-harness" / "dsh-plugin.json"
    if not dsh_plugin.is_file():
        errors.append("Missing adapters/deepseek-harness/dsh-plugin.json")
    else:
        try:
            json.loads(dsh_plugin.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"dsh-plugin.json invalid JSON: {exc}")

    return len(errors) == 0, errors


def check_portability_and_privacy(repo_root: Path) -> tuple[bool, list[str]]:
    errors: list[str] = []
    mac_home_re = re.compile(r"/" + r"[U]sers" + r"/[A-Za-z0-9._-]+")
    win_home_re = re.compile(r"[A-Za-z]:\\" + r"[U]sers" + r"\\[A-Za-z0-9._-]+")
    hidden_session_re = re.compile(r"(?:^|[^A-Za-z0-9_-])" + r"\." + r"[d]sh/")
    email_re = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    allowed_email_domains = {"example.com", "example.org", "example.net", "acme.test"}

    for path in sorted(repo_root.rglob("*")):
        if ".git" in path.parts or "__pycache__" in path.parts or ".venv" in path.parts:
            continue
        if not path.is_file() or path.is_symlink():
            continue
        rel = str(path.relative_to(repo_root))
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            if mac_home_re.search(line):
                errors.append(f"{rel}:{lineno}: local macOS home path detected")
            if win_home_re.search(line):
                errors.append(f"{rel}:{lineno}: local Windows home path detected")
            if hidden_session_re.search(line):
                if not (rel == ".gitignore" and line.strip() == "." + "dsh/"):
                    errors.append(f"{rel}:{lineno}: internal hidden session directory reference detected")
            for m in email_re.finditer(line):
                addr = m.group(0)
                if addr.split("@", 1)[1].lower() not in allowed_email_domains:
                    errors.append(f"{rel}:{lineno}: personal/real email address detected ({addr})")
    return len(errors) == 0, errors


def check_multisuite_coexistence(repo_root: Path, suite_data: dict[str, Any]) -> tuple[bool, list[str]]:
    """Live integration test: install suite + mock sibling suite into one workspace."""
    errors: list[str] = []
    suite_id = suite_data.get("suite_id", "")
    director_slug = suite_data.get("director_slug", "")
    install_sh = repo_root / "adapters" / "install.sh"
    if not install_sh.is_file():
        return False, ["Cannot run coexistence test: adapters/install.sh missing"]

    with tempfile.TemporaryDirectory(prefix="ecosys-coexist-") as tmp:
        dest = Path(tmp)
        # Pre-seed an existing regular CLAUDE.md and a mock sibling suite
        (dest / "CLAUDE.md").write_text("# Existing Project CLAUDE.md\nKeep me intact.\n", encoding="utf-8")
        sib_dir = dest / ".agents" / "skills" / "verification-director"
        sib_dir.mkdir(parents=True, exist_ok=True)
        (sib_dir / "SKILL.md").write_text(
            "---\nname: verification-director\ndescription: Mock sibling suite for coexistence verification.\n---\n# Mock\n",
            encoding="utf-8",
        )
        (dest / ".agents" / "rules").mkdir(parents=True, exist_ok=True)
        (dest / ".agents" / "rules" / "verification-eval-bootstrap.md").write_text("# Sibling rule\n", encoding="utf-8")

        proc = subprocess.run(
            ["bash", str(install_sh), "--target", "all", "--mode", "director-only", "--scope", "workspace", "--dest", str(dest)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if proc.returncode != 0:
            return False, [f"install.sh failed (rc={proc.returncode}): {proc.stderr.strip()}"]

        # 1. Sibling intact
        if not (sib_dir / "SKILL.md").is_file() or not (dest / ".agents" / "rules" / "verification-eval-bootstrap.md").is_file():
            errors.append("Coexistence FAIL: sibling suite files were clobbered")

        # 2. Anti-recursive-discovery: strictly 2 SKILL.md files under .agents/skills
        found_skills = sorted((dest / ".agents" / "skills").rglob("SKILL.md"))
        if len(found_skills) != 2:
            rels = [str(p.relative_to(dest)) for p in found_skills]
            errors.append(f"Coexistence FAIL: expected exactly 2 recursive SKILL.md files, found {len(found_skills)}: {rels}")

        # 3. Installed director self-contained assets
        installed_dir = dest / ".agents" / "skills" / director_slug
        if not (installed_dir / "references" / "suite.yaml").is_file():
            errors.append("Coexistence FAIL: installed director missing references/suite.yaml")
        if not (installed_dir / "dsh-plugin.json").is_file():
            errors.append("Coexistence FAIL: install_deepseek failed to install dsh-plugin.json")
        else:
            plugin_cfg = json.loads((installed_dir / "dsh-plugin.json").read_text(encoding="utf-8"))
            for k in ("suite_manifest",):
                rel_p = plugin_cfg.get(k)
                if rel_p and not (installed_dir / rel_p).is_file():
                    errors.append(f"Coexistence FAIL: dsh-plugin.json {k}='{rel_p}' does not resolve in installed dir")

        # 4. Exact <suite_id>- rules installed
        for rpath in (
            dest / ".agents" / "rules" / f"{suite_id}-bootstrap.md",
            dest / ".cursor" / "rules" / f"{suite_id}-director.mdc",
            dest / ".devin" / "rules" / f"{suite_id}-director.md",
            dest / ".windsurf" / "rules" / f"{suite_id}-director.md",
        ):
            if not rpath.is_file():
                errors.append(f"Coexistence FAIL: missing installed rule {rpath.relative_to(dest)}")

        # 5. Pre-existing regular CLAUDE.md preserved AND updated with fenced block
        claude_txt = (dest / "CLAUDE.md").read_text(encoding="utf-8")
        if "Keep me intact." not in claude_txt or f"<!-- BEGIN {suite_data.get('repo_name')} -->" not in claude_txt:
            errors.append("Coexistence FAIL: existing regular CLAUDE.md was not preserved + upserted")

        # 6. Execute installed CPU pre-scanner on a synthetic buggy HTML file
        scanner = suite_data.get("tooling", {}).get("pre_scanner")
        if scanner:
            installed_scanner = installed_dir / scanner
            if not installed_scanner.is_file():
                errors.append(f"Coexistence FAIL: installed pre_scanner missing at {installed_scanner.relative_to(dest)}")
            else:
                sample = dest / "sample_buggy.html"
                sample.write_text(
                    '<!DOCTYPE html><html><head><style>.a{animation:x 1s infinite}@keyframes x{to{box-shadow:0 0 10px red}}</style></head>'
                    '<body><button id="x">✕</button><script>function f(){return missingFn(1);}</script></body></html>\n',
                    encoding="utf-8",
                )
                sproc = subprocess.run(
                    [sys.executable, str(installed_scanner), "--format", "json", str(sample)],
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                if sproc.returncode != 0:
                    errors.append(f"Coexistence FAIL: installed pre_scanner exited {sproc.returncode}: {sproc.stderr}")
                else:
                    sdata = json.loads(sproc.stdout)
                    rule_ids = {f["rule_id"] for f in sdata["results"][0]["findings"]}
                    for exp in ("CPU-JS-UNDEF", "CPU-MOTION-REDUCED", "CPU-A11Y-ICON-BTN"):
                        if exp not in rule_ids:
                            errors.append(f"Coexistence FAIL: pre_scanner missed expected synthetic defect '{exp}' (got {sorted(rule_ids)})")

    return len(errors) == 0, errors
