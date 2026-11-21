#!/usr/bin/env python3
"""Master deterministic CI validation suite for best-ui-ux-designers."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

import yaml

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None  # type: ignore[assignment]

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import check_anti_cliche  # noqa: E402
import check_routing_math  # noqa: E402
import check_skill_frontmatter  # noqa: E402

ROSTER_SLUGS = {
    "dieter-rams",
    "don-norman",
    "edward-tufte",
    "jef-raskin",
    "ben-shneiderman",
    "susan-kare",
    "bret-victor",
    "karri-saarinen",
    "luke-wroblewski",
    "rasmus-andersson",
    "rauno-freiberg",
    "agentic-flow-architect",
}
VALID_REGIMES = {
    "ai_native_desktop_ide",
    "saas_b2b_intensive",
    "mobile_consumer_capture",
    "analytics_dense_telemetry",
    "landing_onboarding_conversion",
}
REQUIRED_DESIGN_SECTIONS = [
    "1. Operational Worldview",
    "2. Regime Boundaries & Out-of-Universe Rationale",
    "3. Signal Detection Protocol",
    "4. Hard Filters & Veto Playbook",
    "5. Executable Heuristics & Code Patterns",
    "6. Blind Spots & Counterweights",
    "7. Adversarial Debate Positions",
    "8. Primary Source Notes",
]


def _native_schema_validate(instance: Any, schema: dict[str, Any], root: dict[str, Any], path: str = "$") -> list[str]:
    """Structural JSON Schema Draft 2020-12 fallback when jsonschema package is absent."""
    errs: list[str] = []
    if "$ref" in schema:
        ref = schema["$ref"]
        parts = ref.lstrip("#/").split("/")
        target: Any = root
        for p in parts:
            target = target[p]
        return _native_schema_validate(instance, target, root, path)

    if "const" in schema and instance != schema["const"]:
        errs.append(f"{path}: expected const {schema['const']!r}, got {instance!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errs.append(f"{path}: value {instance!r} not in enum {schema['enum']}")

    expected_type = schema.get("type")
    if expected_type is not None:
        types = expected_type if isinstance(expected_type, list) else [expected_type]
        type_ok = False
        for t in types:
            if t == "object" and isinstance(instance, dict):
                type_ok = True
            elif t == "array" and isinstance(instance, list):
                type_ok = True
            elif t == "string" and isinstance(instance, str):
                type_ok = True
            elif t == "integer" and isinstance(instance, int) and not isinstance(instance, bool):
                type_ok = True
            elif t == "number" and isinstance(instance, (int, float)) and not isinstance(instance, bool):
                type_ok = True
            elif t == "boolean" and isinstance(instance, bool):
                type_ok = True
        if not type_ok:
            errs.append(f"{path}: expected type {expected_type}, got {type(instance).__name__}")
            return errs

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errs.append(f"{path}: length {len(instance)} < minLength {schema['minLength']}")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errs.append(f"{path}: length {len(instance)} > maxLength {schema['maxLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errs.append(f"{path}: '{instance}' does not match /{schema['pattern']}/")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errs.append(f"{path}: {instance} < minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errs.append(f"{path}: {instance} > maximum {schema['maximum']}")

    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                errs.append(f"{path}: missing required key '{req}'")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(instance.keys()) - set(props.keys())
            if extra:
                errs.append(f"{path}: disallowed additional properties {sorted(extra)}")
        for k, v in instance.items():
            if k in props:
                errs.extend(_native_schema_validate(v, props[k], root, f"{path}.{k}"))

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errs.append(f"{path}: {len(instance)} items < minItems {schema['minItems']}")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errs.append(f"{path}: {len(instance)} items > maxItems {schema['maxItems']}")
        if schema.get("uniqueItems") and len(instance) != len(set(json.dumps(x, sort_keys=True) for x in instance)):
            errs.append(f"{path}: duplicate items found where uniqueItems=true")
        if "items" in schema:
            for idx, item in enumerate(instance):
                errs.extend(_native_schema_validate(item, schema["items"], root, f"{path}[{idx}]"))
        if "prefixItems" in schema:
            for idx, sub in enumerate(schema["prefixItems"]):
                if idx < len(instance):
                    errs.extend(_native_schema_validate(instance[idx], sub, root, f"{path}[{idx}]"))

    return errs


def check_suite_yaml(repo_root: Path) -> tuple[bool, list[str]]:
    errors: list[str] = []
    suite_path = repo_root / "suite.yaml"
    if not suite_path.is_file():
        return False, ["Missing suite.yaml at repository root"]
    try:
        data = yaml.safe_load(suite_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return False, [f"suite.yaml YAML error: {exc}"]

    expected = {
        "ecosystem_contract_version": "1.0.0",
        "suite_id": "ui-ux",
        "repo_name": "best-ui-ux-designers",
        "director_slug": "design-director",
        "judgment_file": "DESIGN.md",
        "schema_version": "1.0.0",
    }
    for k, v in expected.items():
        if data.get(k) != v:
            errors.append(f"suite.yaml: '{k}' must be {v!r}, got {data.get(k)!r}")

    targets = data.get("handoff_targets")
    if not isinstance(targets, list) or len(targets) == 0:
        errors.append("suite.yaml: handoff_targets must be a non-empty list")
    else:
        for idx, t in enumerate(targets):
            if not isinstance(t, dict) or not t.get("suite_id") or not t.get("trigger_condition"):
                errors.append(f"suite.yaml: handoff_targets[{idx}] missing suite_id or trigger_condition")
    return len(errors) == 0, errors


def check_design_files(repo_root: Path) -> tuple[bool, list[str], dict[str, dict[str, Any]]]:
    errors: list[str] = []
    parsed_designs: dict[str, dict[str, Any]] = {}
    schema_path = repo_root / "validators" / "schema_design.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    validator = None
    if jsonschema is not None:
        validator = jsonschema.Draft202012Validator(schema)

    design_paths = sorted((repo_root / "skills").glob("*/DESIGN.md"))
    if len(design_paths) != 12:
        errors.append(f"Expected 12 skills/*/DESIGN.md files, found {len(design_paths)}")

    found_slugs: set[str] = set()
    for path in design_paths:
        rel = str(path.relative_to(repo_root))
        folder_slug = path.parent.name
        found_slugs.add(folder_slug)
        text = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
        if not m:
            errors.append(f"{rel}: malformed YAML frontmatter or glued closing delimiter")
            continue
        fm_raw, body = m.group(1), m.group(2)
        if body and not body.startswith("\n"):
            errors.append(f"{rel}: missing blank line after frontmatter closing ---")
        try:
            fm = yaml.safe_load(fm_raw)
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: YAML parse error: {exc}")
            continue

        if validator is not None:
            for err in sorted(validator.iter_errors(fm), key=lambda e: list(e.path)):
                loc = ".".join(str(p) for p in err.path) or "$"
                errors.append(f"{rel}: schema violation at {loc}: {err.message}")
        else:
            for err in _native_schema_validate(fm, schema, schema):
                errors.append(f"{rel}: schema violation {err}")

        if not isinstance(fm, dict):
            continue
        parsed_designs[folder_slug] = fm

        ident_slug = fm.get("identity", {}).get("slug")
        if ident_slug != folder_slug:
            errors.append(f"{rel}: identity.slug '{ident_slug}' != folder '{folder_slug}'")

        # Referential integrity of source_id
        src_ids = {s.get("id") for s in fm.get("primary_sources", []) if isinstance(s, dict)}
        for ev in fm.get("identity", {}).get("skin_in_the_game_evidence", []):
            if ev.get("source_id") not in src_ids:
                errors.append(f"{rel}: skin_in_the_game_evidence references unknown source_id '{ev.get('source_id')}'")
        for sig in fm.get("high_weight_signals", []):
            if sig.get("source_id") not in src_ids:
                errors.append(f"{rel}: signal {sig.get('id')} references unknown source_id '{sig.get('source_id')}'")
        for heur in fm.get("concrete_heuristics", []):
            if heur.get("source_id") not in src_ids:
                errors.append(f"{rel}: heuristic {heur.get('id')} references unknown source_id '{heur.get('source_id')}'")

        # Roster integrity of counterweight_designer and opposing_designer
        for bs in fm.get("blind_spots", []):
            cw = bs.get("counterweight_designer")
            if cw not in ROSTER_SLUGS:
                errors.append(f"{rel}: blind_spots {bs.get('id')} has invalid counterweight_designer '{cw}'")
        for dbt in fm.get("debate_triggers", []):
            opp = dbt.get("opposing_designer")
            if opp not in ROSTER_SLUGS:
                errors.append(f"{rel}: debate_triggers {dbt.get('id')} has invalid opposing_designer '{opp}'")

        # Exact 8 H2 headings outside code fences + balanced fences + zero split ||
        h2s: list[str] = []
        in_code = False
        for lineno, line in enumerate(body.splitlines(), start=1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                if re.search(r"[^|]\|\s*$", line) or line.strip() == "|":
                    errors.append(f"{rel}: broken split '|' operator in code block near body line {lineno}")
            elif line.startswith("## "):
                h2s.append(line[3:].strip())
        if in_code:
            errors.append(f"{rel}: unbalanced markdown code fence")
        req_order = fm.get("markdown_contract", {}).get("required_sections_order", [])
        if h2s != REQUIRED_DESIGN_SECTIONS or req_order != REQUIRED_DESIGN_SECTIONS:
            errors.append(f"{rel}: H2 section order mismatch (actual={h2s})")

    if found_slugs != ROSTER_SLUGS:
        errors.append(f"skills/ directory slugs mismatch roster: missing={sorted(ROSTER_SLUGS - found_slugs)}, extra={sorted(found_slugs - ROSTER_SLUGS)}")

    return len(errors) == 0, errors, parsed_designs


def check_evals_files(repo_root: Path, designs: dict[str, dict[str, Any]]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    eval_paths = sorted((repo_root / "skills").glob("*/evals/evals.json"))
    if len(eval_paths) != 12:
        errors.append(f"Expected 12 skills/*/evals/evals.json files, found {len(eval_paths)}")

    for path in eval_paths:
        rel = str(path.relative_to(repo_root))
        slug = path.parent.parent.name
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}: invalid JSON: {exc}")
            continue

        if data.get("skill_name") != slug:
            errors.append(f"{rel}: skill_name '{data.get('skill_name')}' != '{slug}'")
        if data.get("schema_version") != "1.0.0":
            errors.append(f"{rel}: schema_version must be '1.0.0'")
        cases = data.get("evals")
        if not isinstance(cases, list) or len(cases) < 5:
            errors.append(f"{rel}: expected >= 5 eval cases")
            continue

        trig_true = sum(1 for c in cases if c.get("expected_trigger") is True)
        trig_false = sum(1 for c in cases if c.get("expected_trigger") is False)
        if trig_true < 3 or trig_false < 2:
            errors.append(f"{rel}: expected >=3 trigger=true and >=2 trigger=false, got {trig_true}/{trig_false}")

        design = designs.get(slug)
        vmap = {v["id"]: v["severity"] for v in design.get("veto_triggers", [])} if design else {}
        fset = {f["id"] for f in design.get("hard_filters", [])} if design else set()
        smap = {s["id"]: s["weight"] for s in design.get("high_weight_signals", [])} if design else {}

        for idx, c in enumerate(cases):
            cid = c.get("id", f"idx-{idx}")
            if not c.get("prompt") or not isinstance(c.get("assertions"), list) or len(c["assertions"]) == 0:
                errors.append(f"{rel}[{cid}]: missing prompt or assertions")
            if c.get("expected_scope") not in VALID_REGIMES:
                errors.append(f"{rel}[{cid}]: invalid expected_scope '{c.get('expected_scope')}'")
            eo = c.get("expected_output")
            if not isinstance(eo, dict):
                errors.append(f"{rel}[{cid}]: expected_output must be a structured JSON object")
                continue

            if c.get("expected_trigger") is True:
                if eo.get("in_universe") is not True:
                    errors.append(f"{rel}[{cid}]: in-universe case must set expected_output.in_universe=true")
                if eo.get("posture") not in {"APPROVE", "REVISE", "BLOCK"}:
                    errors.append(f"{rel}[{cid}]: invalid posture '{eo.get('posture')}'")
                for lk in ("triggered_vetos", "failed_filters", "failed_signals"):
                    if not isinstance(eo.get(lk), list):
                        errors.append(f"{rel}[{cid}]: expected_output.{lk} must be a list")
                if design and isinstance(eo.get("triggered_vetos"), list) and isinstance(eo.get("failed_filters"), list) and isinstance(eo.get("failed_signals"), list):
                    bad_v = [v for v in eo["triggered_vetos"] if v not in vmap]
                    bad_f = [f for f in eo["failed_filters"] if f not in fset]
                    bad_s = [s for s in eo["failed_signals"] if s not in smap]
                    if bad_v or bad_f or bad_s:
                        errors.append(f"{rel}[{cid}]: unknown IDs vetos={bad_v} filters={bad_f} signals={bad_s}")
                    else:
                        hv = sum(1 for v in eo["triggered_vetos"] if vmap[v] == "hard_veto")
                        cb = sum(1 for v in eo["triggered_vetos"] if vmap[v] == "conditional_block")
                        ded = hv * 35 + (len(eo["failed_filters"]) + cb) * 15
                        for s in eo["failed_signals"]:
                            ded += 10 if smap[s] == "critical" else (5 if smap[s] == "high" else 2)
                        cap = 49 if hv >= 1 else 100
                        expected_score = max(0, min(cap, 100 - ded))
                        expected_posture = "BLOCK" if (hv >= 1 or expected_score < 60) else ("APPROVE" if (expected_score >= 82 and cb == 0) else "REVISE")
                        if eo.get("score_cap") != cap:
                            errors.append(f"{rel}[{cid}]: score_cap={eo.get('score_cap')} != computed {cap}")
                        if eo.get("expected_score") != expected_score:
                            errors.append(f"{rel}[{cid}]: expected_score={eo.get('expected_score')} != computed {expected_score}")
                        if eo.get("posture") != expected_posture:
                            errors.append(f"{rel}[{cid}]: posture={eo.get('posture')} != computed {expected_posture}")
            else:
                if eo.get("in_universe") is not False:
                    errors.append(f"{rel}[{cid}]: out-of-universe case must set in_universe=false")
                if eo.get("posture") != "HANDOFF":
                    errors.append(f"{rel}[{cid}]: out-of-universe case must set posture='HANDOFF'")
                if eo.get("counterweight_handoff") not in ROSTER_SLUGS:
                    errors.append(f"{rel}[{cid}]: invalid counterweight_handoff '{eo.get('counterweight_handoff')}'")

    return len(errors) == 0, errors


def check_committee_contracts(repo_root: Path) -> tuple[bool, list[str]]:
    errors: list[str] = []
    director_path = repo_root / "committee" / "design-director" / "SKILL.md"
    if not director_path.is_file():
        errors.append("Missing committee/design-director/SKILL.md")
    else:
        dtext = director_path.read_text(encoding="utf-8")
        if "verdict_envelope:" not in dtext:
            errors.append("design-director/SKILL.md missing 'verdict_envelope:' block")
        for req_tok in ('envelope_version: "1.0.0"', 'suite_id: "ui-ux"', "solow_stage:", "escalation_to_suites:"):
            if req_tok not in dtext:
                errors.append(f"design-director/SKILL.md verdict_envelope missing '{req_tok}'")

    slop_path = repo_root / "committee" / "auditors" / "auditor-agentic-anti-slop" / "rules.yaml"
    if not slop_path.is_file():
        errors.append("Missing committee/auditors/auditor-agentic-anti-slop/rules.yaml")
    else:
        sdata = yaml.safe_load(slop_path.read_text(encoding="utf-8"))
        rules = sdata.get("rules", []) if isinstance(sdata, dict) else []
        dynamo = next((r for r in rules if isinstance(r, dict) and r.get("id") == "aud-slop-04"), None)
        if not dynamo:
            errors.append("auditor-agentic-anti-slop/rules.yaml missing rule id 'aud-slop-04'")
        else:
            if dynamo.get("veto_id") != "veto-central-dynamo":
                errors.append("aud-slop-04 veto_id must be 'veto-central-dynamo'")
            if dynamo.get("severity") != "hard_veto":
                errors.append("aud-slop-04 severity must be 'hard_veto'")
            preds = {p.get("predicate_id") for p in dynamo.get("deterministic_predicates", []) if isinstance(p, dict)}
            if preds != {"cd-01", "cd-02", "cd-03", "cd-04"}:
                errors.append(f"aud-slop-04 deterministic_predicates mismatch: {sorted(preds)}")
            solow = dynamo.get("solow_classification_output", {})
            if solow.get("fail_label") != "BOLT_ON_CAPITAL_K" or solow.get("pass_label") != "UNIT_DRIVE_TFP_A":
                errors.append("aud-slop-04 solow_classification_output labels invalid")

    return len(errors) == 0, errors


def check_adapters_and_limits(repo_root: Path) -> tuple[bool, list[str]]:
    errors: list[str] = []

    agents_md = repo_root / "AGENTS.md"
    if not agents_md.is_file():
        errors.append("Missing AGENTS.md")
    else:
        alen = len(agents_md.read_text(encoding="utf-8"))
        if alen >= 4000:
            errors.append(f"AGENTS.md length {alen} chars >= 4,000 hard limit")

    claude_md = repo_root / "CLAUDE.md"
    if not claude_md.is_symlink():
        errors.append("CLAUDE.md must be a symlink to AGENTS.md")
    else:
        target = os.readlink(claude_md)
        if target != "AGENTS.md":
            errors.append(f"CLAUDE.md symlink target must be relative 'AGENTS.md', got '{target}'")

    antigravity_rule = repo_root / "adapters" / "antigravity" / "uiux-bootstrap.md"
    if not antigravity_rule.is_file():
        errors.append("Missing adapters/antigravity/uiux-bootstrap.md")
    else:
        sz = antigravity_rule.stat().st_size
        if sz >= 24000:
            errors.append(f"adapters/antigravity/uiux-bootstrap.md is {sz} bytes >= 24,000 bytes limit")

    cursor_rule = repo_root / "adapters" / "cursor" / "uiux-director.mdc"
    if not cursor_rule.is_file():
        errors.append("Missing adapters/cursor/uiux-director.mdc")
    else:
        ctext = cursor_rule.read_text(encoding="utf-8")
        if "alwaysApply: false" not in ctext or "globs:" not in ctext:
            errors.append("adapters/cursor/uiux-director.mdc missing required Cursor frontmatter fields")

    windsurf_rule = repo_root / "adapters" / "windsurf-devin" / "uiux-director.md"
    if not windsurf_rule.is_file():
        errors.append("Missing adapters/windsurf-devin/uiux-director.md")
    else:
        wlen = len(windsurf_rule.read_text(encoding="utf-8"))
        if wlen >= 12000:
            errors.append(f"adapters/windsurf-devin/uiux-director.md is {wlen} chars >= 12,000 char hard limit")

    install_sh = repo_root / "adapters" / "install.sh"
    if not install_sh.is_file():
        errors.append("Missing adapters/install.sh")
    elif not os.access(install_sh, os.X_OK):
        errors.append("adapters/install.sh must be executable (chmod +x)")

    dsh_plugin = repo_root / "adapters" / "deepseek-harness" / "dsh-plugin.json"
    if not dsh_plugin.is_file():
        errors.append("Missing adapters/deepseek-harness/dsh-plugin.json")
    else:
        try:
            json.loads(dsh_plugin.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"adapters/deepseek-harness/dsh-plugin.json invalid JSON: {exc}")

    return len(errors) == 0, errors


def check_portability_and_privacy(repo_root: Path) -> tuple[bool, list[str]]:
    """Universal portability check blocking local personal paths, hidden session dirs, and personal emails."""
    errors: list[str] = []

    # Build patterns dynamically via concatenation/character classes to prevent self-matching
    mac_home_re = re.compile(r"/" + r"[U]sers" + r"/[A-Za-z0-9._-]+")
    win_home_re = re.compile(r"[A-Za-z]:\\" + r"[U]sers" + r"\\[A-Za-z0-9._-]+")
    hidden_session_re = re.compile(r"(?:^|[^A-Za-z0-9_-])" + r"\." + r"[d]sh/")
    email_re = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    allowed_email_domains = {"example.com", "example.org", "example.net", "acme.test"}

    for path in sorted(repo_root.rglob("*")):
        if ".git" in path.parts or "__pycache__" in path.parts:
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
                # Explicitly allow the ignore pattern line in .gitignore
                if not (rel == ".gitignore" and line.strip() == "." + "dsh/"):
                    errors.append(f"{rel}:{lineno}: internal hidden session directory reference detected")
            for m in email_re.finditer(line):
                addr = m.group(0)
                domain = addr.split("@", 1)[1].lower()
                if domain not in allowed_email_domains:
                    errors.append(f"{rel}:{lineno}: personal/real email address detected ({addr})")

    return len(errors) == 0, errors


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent

    results: list[tuple[str, bool, list[str]]] = []

    ok, errs = check_suite_yaml(repo_root)
    results.append(("suite.yaml manifest", ok, errs))

    ok, errs, _ = check_skill_frontmatter.run_check(repo_root)
    results.append(("17 SKILL.md frontmatter & budget", ok, errs))

    ok, errs, designs = check_design_files(repo_root)
    results.append(("12 DESIGN.md schema & refs", ok, errs))

    ok, errs = check_evals_files(repo_root, designs)
    results.append(("12 evals.json schema & math", ok, errs))

    ok, errs, _ = check_anti_cliche.run_check(repo_root)
    results.append(("Anti-cliché operational linter", ok, errs))

    ok, errs, _ = check_routing_math.run_check(repo_root)
    results.append(("Routing matrix & AI override math", ok, errs))

    ok, errs = check_committee_contracts(repo_root)
    results.append(("Verdict Envelope & Central Dynamo", ok, errs))

    ok, errs = check_adapters_and_limits(repo_root)
    results.append(("Adapters, uiux- prefix & hard limits", ok, errs))

    ok, errs = check_portability_and_privacy(repo_root)
    results.append(("Portability & privacy leak gate", ok, errs))

    print("=" * 72)
    print("  best-ui-ux-designers — Deterministic Repository Validation Suite")
    print("=" * 72)
    all_ok = True
    for label, passed, errs in results:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {label}")
        if not passed:
            all_ok = False
            for e in errs:
                print(f"         -> {e}")
    print("-" * 72)
    if all_ok:
        print("  ALL CHECKS PASSED (100%).")
        return 0
    print("  VALIDATION FAILED. Resolve every error above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
