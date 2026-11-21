#!/usr/bin/env python3
"""Validate all 17 SKILL.md files (12 designers + design-director + 4 auditors)."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

ALLOWED_KEYS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
DESIGNER_REQUIRED_ROOT_KEYS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
}
DESIGNER_REQUIRED_METADATA = {
    "schema_version",
    "judgment_schema",
    "suite_id",
    "barbell_pole",
    "primary_regimes",
    "author",
}
REQUIRED_DESIGNER_H2 = [
    "When To Use",
    "Do Not Use When",
    "Required Inputs",
    "Execution & Audit Workflow",
    "Verdict & Severity Criteria",
    "Guardrails",
]
PHASE_A_RUBRIC_TOKENS = ["-35", "49", "-15", "-10", "-5", "-2", "82", "60"]
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DESIGNER_OPTIONAL_ROOT_KEYS = {"allowed-tools"}
DISCOVERY_BUDGET_LIMIT = 8000
DIRECTOR_DISCOVERY_BUDGET_LIMIT = 384


def parse_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str, str | None]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, "", f"{path}: missing or malformed YAML frontmatter delimiters"
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as exc:
        return None, "", f"{path}: invalid YAML frontmatter: {exc}"
    if not isinstance(data, dict):
        return None, "", f"{path}: frontmatter must parse as a YAML mapping"
    return data, m.group(2), None


def extract_h2_headings(body: str) -> list[str]:
    headings: list[str] = []
    in_code = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code and line.startswith("## "):
            headings.append(line[3:].strip())
    return headings


def run_check(repo_root: Path) -> tuple[bool, list[str], dict[str, Any]]:
    errors: list[str] = []
    skill_paths: list[tuple[str, Path]] = []

    skills_dir = repo_root / "skills"
    if skills_dir.is_dir():
        for p in sorted(skills_dir.glob("*/SKILL.md")):
            skill_paths.append(("designer", p))

    director_skill = repo_root / "committee" / "design-director" / "SKILL.md"
    if director_skill.is_file():
        skill_paths.append(("director", director_skill))
    else:
        errors.append("Missing committee/design-director/SKILL.md")

    auditors_dir = repo_root / "committee" / "auditors"
    if auditors_dir.is_dir():
        for p in sorted(auditors_dir.glob("*/SKILL.md")):
            skill_paths.append(("auditor", p))

    designer_count = sum(1 for kind, _ in skill_paths if kind == "designer")
    auditor_count = sum(1 for kind, _ in skill_paths if kind == "auditor")
    if designer_count != 12:
        errors.append(f"Expected 12 designer SKILL.md files, found {designer_count}")
    if auditor_count != 4:
        errors.append(f"Expected 4 auditor SKILL.md files, found {auditor_count}")
    if len(skill_paths) != 17:
        errors.append(f"Expected 17 total SKILL.md files, found {len(skill_paths)}")

    total_discovery_chars = 0
    seen_names: set[str] = set()

    for kind, path in skill_paths:
        rel = path.relative_to(repo_root)
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) > 500:
            errors.append(f"{rel}: {len(lines)} lines exceeds 500-line ceiling")

        fm, body, err = parse_frontmatter(path)
        if err:
            errors.append(err)
            continue
        assert fm is not None

        extra_keys = set(fm.keys()) - ALLOWED_KEYS
        if extra_keys:
            errors.append(f"{rel}: disallowed root keys {sorted(extra_keys)}")

        name = fm.get("name")
        desc = fm.get("description")
        folder_name = path.parent.name

        if not isinstance(name, str) or not SLUG_RE.match(name) or len(name) > 64:
            errors.append(f"{rel}: invalid name '{name}'")
        elif name != folder_name:
            errors.append(f"{rel}: name '{name}' != folder '{folder_name}'")
        elif name in seen_names:
            errors.append(f"{rel}: duplicate skill name '{name}'")
        else:
            seen_names.add(name)

        if not isinstance(desc, str) or not desc.strip():
            errors.append(f"{rel}: missing or empty description")
        elif len(desc) > 320:
            errors.append(f"{rel}: description length {len(desc)} > 320 chars")
        else:
            total_discovery_chars += len(str(name or "")) + len(desc)

        if kind == "designer":
            missing_root = DESIGNER_REQUIRED_ROOT_KEYS - set(fm.keys())
            extra_root = set(fm.keys()) - (DESIGNER_REQUIRED_ROOT_KEYS | DESIGNER_OPTIONAL_ROOT_KEYS)
            if missing_root or extra_root:
                errors.append(
                    f"{rel}: designer root keys invalid (missing={sorted(missing_root)}, extra={sorted(extra_root)})"
                )
            if fm.get("license") != "MIT":
                errors.append(f"{rel}: license must be 'MIT'")
            meta = fm.get("metadata")
            if not isinstance(meta, dict):
                errors.append(f"{rel}: metadata must be a mapping")
            else:
                missing_meta = DESIGNER_REQUIRED_METADATA - set(meta.keys())
                if missing_meta:
                    errors.append(f"{rel}: metadata missing {sorted(missing_meta)}")
                if meta.get("schema_version") != "1.1.0":
                    errors.append(f"{rel}: metadata.schema_version must be '1.1.0'")
                if meta.get("judgment_schema") != "./DESIGN.md":
                    errors.append(f"{rel}: metadata.judgment_schema must be './DESIGN.md'")
                if meta.get("suite_id") != "ui-ux":
                    errors.append(f"{rel}: metadata.suite_id must be 'ui-ux'")
                if meta.get("author") != "best-ui-ux-designers":
                    errors.append(f"{rel}: metadata.author must be 'best-ui-ux-designers'")

            h2s = extract_h2_headings(body)
            if h2s != REQUIRED_DESIGNER_H2:
                errors.append(f"{rel}: H2 headings mismatch: expected {REQUIRED_DESIGNER_H2}, got {h2s}")

            for token in PHASE_A_RUBRIC_TOKENS:
                if token not in body:
                    errors.append(f"{rel}: missing calibrated Phase A rubric token '{token}'")

    if total_discovery_chars >= DISCOVERY_BUDGET_LIMIT:
        errors.append(
            f"Discovery budget exceeded: {total_discovery_chars} chars >= {DISCOVERY_BUDGET_LIMIT}"
        )

    stats = {
        "total_skills": len(skill_paths),
        "discovery_chars": total_discovery_chars,
        "discovery_limit": DISCOVERY_BUDGET_LIMIT,
    }
    return len(errors) == 0, errors, stats


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    ok, errors, stats = run_check(repo_root)
    if ok:
        print(
            f"[PASS] check_skill_frontmatter: {stats['total_skills']} skills validated "
            f"(discovery budget {stats['discovery_chars']}/{stats['discovery_limit']} chars)"
        )
        return 0
    print(f"[FAIL] check_skill_frontmatter: {len(errors)} error(s)")
    for e in errors:
        print(f"  - {e}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
