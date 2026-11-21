#!/usr/bin/env python3
"""Scan operational YAML fields in DESIGN.md and auditor rules.yaml for banned decorative cliches."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

BANNED_CLICHE_RE = re.compile(
    r"\b(clean\s+(?:ui|ux|design|interface|look|aesthetic)|intuitive|modern\s+(?:ui|ux|design|look|aesthetic)|"
    r"user-centered|user-friendly|seamless|limpio|intuitivo|moderno|centrado en el usuario)\b",
    re.IGNORECASE,
)

OPERATIONAL_DESIGN_KEYS = (
    "high_weight_signals",
    "hard_filters",
    "veto_triggers",
    "concrete_heuristics",
)


def _scan_value(value: Any, path_str: str, skip_keys: set[str], hits: list[str]) -> None:
    if isinstance(value, str):
        for m in BANNED_CLICHE_RE.finditer(value):
            snippet = value[max(0, m.start() - 25) : min(len(value), m.end() + 25)].replace("\n", " ")
            hits.append(f"{path_str}: banned cliché '{m.group(0)}' in '...{snippet}...'")
    elif isinstance(value, list):
        for idx, item in enumerate(value):
            _scan_value(item, f"{path_str}[{idx}]", skip_keys, hits)
    elif isinstance(value, dict):
        for k, v in value.items():
            if k in skip_keys:
                continue
            _scan_value(v, f"{path_str}.{k}", skip_keys, hits)


def _parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: missing YAML frontmatter")
    data = yaml.safe_load(m.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter is not a YAML mapping")
    return data


def run_check(repo_root: Path) -> tuple[bool, list[str], dict[str, int]]:
    errors: list[str] = []
    design_files = sorted((repo_root / "skills").glob("*/DESIGN.md"))
    rule_files = sorted((repo_root / "committee" / "auditors").glob("*/rules.yaml"))

    if len(design_files) != 12:
        errors.append(f"Expected 12 skills/*/DESIGN.md files, found {len(design_files)}")
    if len(rule_files) != 4:
        errors.append(f"Expected 4 committee/auditors/*/rules.yaml files, found {len(rule_files)}")

    for path in design_files:
        rel = str(path.relative_to(repo_root))
        try:
            fm = _parse_frontmatter(path)
        except Exception as exc:
            errors.append(f"{rel}: {exc}")
            continue
        axiom = fm.get("identity", {}).get("core_axiom")
        if axiom is not None:
            _scan_value(axiom, f"{rel}:identity.core_axiom", set(), errors)
        for key in OPERATIONAL_DESIGN_KEYS:
            if key in fm:
                _scan_value(fm[key], f"{rel}:{key}", {"primary_sources"}, errors)

    for path in rule_files:
        rel = str(path.relative_to(repo_root))
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{rel}: YAML error: {exc}")
            continue
        # Exclude primary_sources titles/quotes to prevent false positives on verbatim citations
        _scan_value(data, rel, {"primary_sources"}, errors)

    stats = {"design_files": len(design_files), "rule_files": len(rule_files)}
    return len(errors) == 0, errors, stats


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    ok, errors, stats = run_check(repo_root)
    if ok:
        print(
            f"[PASS] check_anti_cliche: 0 banned clichés across "
            f"{stats['design_files']} DESIGN.md + {stats['rule_files']} auditor rules.yaml"
        )
        return 0
    print(f"[FAIL] check_anti_cliche: {len(errors)} violation(s)")
    for e in errors:
        print(f"  - {e}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
