#!/usr/bin/env python3
"""Master deterministic CI validation suite for best-ui-ux-designers (ECOSYSTEM_CONTRACT v1.2.0)."""

from __future__ import annotations

import json
import re
import subprocess
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
import ecosystem_core_validator as core  # noqa: E402

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
MAX_PANEL_BRIEF_BYTES = 25600  # ECOSYSTEM_CONTRACT v1.1.0 <= 25 KB operational budget


def _native_schema_validate(instance: Any, schema: dict[str, Any], root: dict[str, Any], path: str = "$") -> list[str]:
    errs: list[str] = []
    if "$ref" in schema:
        parts = schema["$ref"].lstrip("#/").split("/")
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
        type_ok = any(
            (t == "object" and isinstance(instance, dict))
            or (t == "array" and isinstance(instance, list))
            or (t == "string" and isinstance(instance, str))
            or (t == "integer" and isinstance(instance, int) and not isinstance(instance, bool))
            or (t == "number" and isinstance(instance, (int, float)) and not isinstance(instance, bool))
            or (t == "boolean" and isinstance(instance, bool))
            for t in types
        )
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


def check_design_files(repo_root: Path) -> tuple[bool, list[str], dict[str, dict[str, Any]]]:
    errors: list[str] = []
    parsed_designs: dict[str, dict[str, Any]] = {}
    schema = json.loads((repo_root / "validators" / "schema_design.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema) if jsonschema is not None else None

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
            errors.append(f"{rel}: malformed YAML frontmatter")
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
        if fm.get("identity", {}).get("slug") != folder_slug:
            errors.append(f"{rel}: identity.slug != folder '{folder_slug}'")
        src_ids = {s.get("id") for s in fm.get("primary_sources", []) if isinstance(s, dict)}
        for ev in fm.get("identity", {}).get("skin_in_the_game_evidence", []):
            if ev.get("source_id") not in src_ids:
                errors.append(f"{rel}: unknown source_id '{ev.get('source_id')}'")
        for sig in fm.get("high_weight_signals", []):
            if sig.get("source_id") not in src_ids:
                errors.append(f"{rel}: signal {sig.get('id')} unknown source_id '{sig.get('source_id')}'")
        for heur in fm.get("concrete_heuristics", []):
            if heur.get("source_id") not in src_ids:
                errors.append(f"{rel}: heuristic {heur.get('id')} unknown source_id '{heur.get('source_id')}'")
        for bs in fm.get("blind_spots", []):
            if bs.get("counterweight_designer") not in ROSTER_SLUGS:
                errors.append(f"{rel}: invalid counterweight_designer '{bs.get('counterweight_designer')}'")
        for dbt in fm.get("debate_triggers", []):
            if dbt.get("opposing_designer") not in ROSTER_SLUGS:
                errors.append(f"{rel}: invalid opposing_designer '{dbt.get('opposing_designer')}'")

        h2s: list[str] = []
        in_code = False
        for lineno, line in enumerate(body.splitlines(), start=1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                if re.search(r"[^|]\|\s*$", line) or line.strip() == "|":
                    errors.append(f"{rel}: broken split '|' near body line {lineno}")
            elif line.startswith("## "):
                h2s.append(line[3:].strip())
        if in_code:
            errors.append(f"{rel}: unbalanced markdown code fence")
        if h2s != REQUIRED_DESIGN_SECTIONS:
            errors.append(f"{rel}: H2 section order mismatch (actual={h2s})")

    if found_slugs != ROSTER_SLUGS:
        errors.append(f"skills/ directory slugs mismatch roster: missing={sorted(ROSTER_SLUGS - found_slugs)}")
    return len(errors) == 0, errors, parsed_designs


def check_briefs_budget(repo_root: Path) -> tuple[bool, list[str]]:
    """Verify all 12 compact BRIEF.md files exist and any 5-designer panel stays <= 25 KB."""
    errors: list[str] = []
    briefs = sorted((repo_root / "skills").glob("*/BRIEF.md"))
    if len(briefs) != 12:
        return False, [f"Expected 12 skills/*/BRIEF.md files, found {len(briefs)}"]
    sizes = sorted((p.stat().st_size, p.parent.name) for p in briefs)
    worst_5 = sum(sz for sz, _ in sizes[-5:])
    if worst_5 > MAX_PANEL_BRIEF_BYTES:
        errors.append(f"Worst-case 5-designer BRIEF.md panel is {worst_5} bytes > {MAX_PANEL_BRIEF_BYTES} budget")
    return len(errors) == 0, errors


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
            if not c.get("prompt") or not isinstance(c.get("assertions"), list) or not c["assertions"]:
                errors.append(f"{rel}[{cid}]: missing prompt or assertions")
            if c.get("expected_scope") not in VALID_REGIMES:
                errors.append(f"{rel}[{cid}]: invalid expected_scope '{c.get('expected_scope')}'")
            eo = c.get("expected_output")
            if not isinstance(eo, dict):
                errors.append(f"{rel}[{cid}]: expected_output must be a JSON object")
                continue
            if c.get("expected_trigger") is True and design:
                bad_v = [v for v in eo.get("triggered_vetos", []) if v not in vmap]
                bad_f = [f for f in eo.get("failed_filters", []) if f not in fset]
                bad_s = [s for s in eo.get("failed_signals", []) if s not in smap]
                if bad_v or bad_f or bad_s:
                    errors.append(f"{rel}[{cid}]: unknown IDs vetos={bad_v} filters={bad_f} signals={bad_s}")
    return len(errors) == 0, errors


def check_central_dynamo_rule(repo_root: Path) -> tuple[bool, list[str]]:
    errors: list[str] = []
    slop_path = repo_root / "committee" / "auditors" / "auditor-agentic-anti-slop" / "rules.yaml"
    if not slop_path.is_file():
        return False, ["Missing auditor-agentic-anti-slop/rules.yaml"]
    sdata = yaml.safe_load(slop_path.read_text(encoding="utf-8"))
    rules = sdata.get("rules", []) if isinstance(sdata, dict) else []
    dynamo = next((r for r in rules if isinstance(r, dict) and r.get("id") == "aud-slop-04"), None)
    if not dynamo:
        errors.append("auditor-agentic-anti-slop/rules.yaml missing rule id 'aud-slop-04'")
    else:
        if dynamo.get("veto_id") != "veto-central-dynamo" or dynamo.get("severity") != "hard_veto":
            errors.append("aud-slop-04 must keep veto_id='veto-central-dynamo' and severity='hard_veto'")
        preds = {p.get("predicate_id") for p in dynamo.get("deterministic_predicates", []) if isinstance(p, dict)}
        if preds != {"cd-01", "cd-02", "cd-03", "cd-04"}:
            errors.append(f"aud-slop-04 deterministic_predicates mismatch: {sorted(preds)}")
    return len(errors) == 0, errors


def _uiux_scanner_smoke(installed_scanner: Path, dest: Path) -> list[str]:
    """Domain-specific synthetic buggy HTML smoke test for uiux_cpu_scanner.py."""
    errs: list[str] = []
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
        return [f"UI-UX scanner smoke FAIL: exited {sproc.returncode}: {sproc.stderr}"]
    sdata = json.loads(sproc.stdout)
    rule_ids = {f["rule_id"] for f in sdata["results"][0]["findings"]}
    for exp in ("CPU-JS-UNDEF", "CPU-MOTION-REDUCED", "CPU-A11Y-ICON-BTN"):
        if exp not in rule_ids:
            errs.append(f"UI-UX scanner smoke FAIL: missed expected defect '{exp}' (got {sorted(rule_ids)})")
    return errs


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    results: list[tuple[str, bool, list[str]]] = []

    ok, errs, suite_data = core.check_suite_manifest(repo_root)
    results.append((f"[Core v{core.CORE_VALIDATOR_VERSION}] suite.yaml manifest", ok, errs))

    ok, errs = core.check_director_contract(repo_root, suite_data)
    results.append((f"[Core v{core.CORE_VALIDATOR_VERSION}] Director SKILL.md & Verdict Envelope", ok, errs))

    ok, errs = core.check_adapters_and_namespacing(repo_root, suite_data)
    results.append((f"[Core v{core.CORE_VALIDATOR_VERSION}] Adapters, exact <suite_id>- prefix & limits", ok, errs))

    ok, errs = core.check_portability_and_privacy(repo_root)
    results.append((f"[Core v{core.CORE_VALIDATOR_VERSION}] Portability & privacy leak gate", ok, errs))

    ok, errs = core.check_auditor_rules_and_citations(repo_root, suite_data)
    results.append((f"[Core v{core.CORE_VALIDATOR_VERSION}] Clean-Room rules.yaml schema & citation hygiene", ok, errs))

    ok, errs = core.check_anti_self_auditing_integrity(repo_root, suite_data)
    results.append((f"[Core v{core.CORE_VALIDATOR_VERSION}] Anti-self-auditing & validator SHA-256 pin", ok, errs))

    ok, errs = core.check_multisuite_coexistence(repo_root, suite_data, scanner_smoke_fn=_uiux_scanner_smoke)
    results.append((f"[Core v{core.CORE_VALIDATOR_VERSION}] Live multi-suite coexistence + UI-UX CPU scanner", ok, errs))

    ok, errs, _ = check_skill_frontmatter.run_check(repo_root)
    results.append(("[UI-UX] 17 SKILL.md frontmatter & budget", ok, errs))

    ok, errs, designs = check_design_files(repo_root)
    results.append(("[UI-UX] 12 DESIGN.md schema & refs", ok, errs))

    ok, errs = check_briefs_budget(repo_root)
    results.append(("[UI-UX] 12 compact BRIEF.md (<= 25 KB/panel)", ok, errs))

    ok, errs = check_evals_files(repo_root, designs)
    results.append(("[UI-UX] 12 evals.json schema & refs", ok, errs))

    ok, errs, _ = check_anti_cliche.run_check(repo_root)
    results.append(("[UI-UX] Anti-cliché operational linter", ok, errs))

    ok, errs, _ = check_routing_math.run_check(repo_root)
    results.append(("[UI-UX] Routing matrix & AI override math", ok, errs))

    ok, errs = check_central_dynamo_rule(repo_root)
    results.append(("[UI-UX] Central Dynamo rule contract", ok, errs))

    print("=" * 72)
    print("  best-ui-ux-designers (ECOSYSTEM_CONTRACT v1.2.0) — Ecosystem + Domain Validation Suite")
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
