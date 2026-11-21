#!/usr/bin/env python3
"""Validate committee/design-director/routing-matrix.yaml mathematical invariants."""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import yaml

EXPECTED_REGIMES = {
    "ai_native_desktop_ide",
    "saas_b2b_intensive",
    "mobile_consumer_capture",
    "analytics_dense_telemetry",
    "landing_onboarding_conversion",
}
EXPECTED_LINDY = {
    "dieter-rams",
    "don-norman",
    "edward-tufte",
    "jef-raskin",
    "ben-shneiderman",
    "susan-kare",
}
EXPECTED_CONVEX = {
    "bret-victor",
    "karri-saarinen",
    "luke-wroblewski",
    "rasmus-andersson",
    "rauno-freiberg",
    "agentic-flow-architect",
}
FULL_ROSTER = EXPECTED_LINDY | EXPECTED_CONVEX
TOL = 1e-9


def run_check(repo_root: Path) -> tuple[bool, list[str], dict[str, Any]]:
    errors: list[str] = []
    matrix_path = repo_root / "committee" / "design-director" / "routing-matrix.yaml"
    if not matrix_path.is_file():
        return False, ["Missing committee/design-director/routing-matrix.yaml"], {}

    try:
        data = yaml.safe_load(matrix_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return False, [f"Invalid YAML in routing-matrix.yaml: {exc}"], {}

    roster_cfg = data.get("barbell_roster", {})
    lindy = set(roster_cfg.get("lindy_anchor", []))
    convex = set(roster_cfg.get("convex_frontier", []))
    if lindy != EXPECTED_LINDY:
        errors.append(f"barbell_roster.lindy_anchor mismatch: {sorted(lindy)}")
    if convex != EXPECTED_CONVEX:
        errors.append(f"barbell_roster.convex_frontier mismatch: {sorted(convex)}")

    regimes = data.get("regimes", {})
    if set(regimes.keys()) != EXPECTED_REGIMES:
        errors.append(
            f"Expected exact 5 regimes {sorted(EXPECTED_REGIMES)}, got {sorted(regimes.keys())}"
        )

    override = data.get("embedded_ai_override", {})
    inj_designer = override.get("injected_designer")
    inj_weight = float(override.get("injected_weight", 0.0))
    scale_factor = float(override.get("base_weight_scale_factor", 0.0))
    override_regimes = set(override.get("applies_to_regimes", []))

    if inj_designer != "agentic-flow-architect":
        errors.append(f"embedded_ai_override.injected_designer must be 'agentic-flow-architect', got '{inj_designer}'")
    if not math.isclose(inj_weight, 0.15, abs_tol=TOL):
        errors.append(f"embedded_ai_override.injected_weight must be 0.15, got {inj_weight}")
    if not math.isclose(scale_factor, 0.85, abs_tol=TOL):
        errors.append(f"embedded_ai_override.base_weight_scale_factor must be 0.85, got {scale_factor}")
    if override_regimes != (EXPECTED_REGIMES - {"ai_native_desktop_ide"}):
        errors.append(f"embedded_ai_override.applies_to_regimes must be R2-R5, got {sorted(override_regimes)}")

    activated_anywhere: set[str] = set()

    for rname, rcfg in regimes.items():
        weights = rcfg.get("active_weights", {})
        oou = rcfg.get("out_of_universe", [])
        if not isinstance(weights, dict) or not isinstance(oou, list):
            errors.append(f"Regime {rname}: active_weights must be dict and out_of_universe must be list")
            continue

        active_set = set(weights.keys())
        oou_set = set(oou)
        if len(active_set) != 4:
            errors.append(f"Regime {rname}: expected 4 active designers, got {len(active_set)}")
        if len(oou) != 8 or len(oou_set) != 8:
            errors.append(f"Regime {rname}: expected 8 unique OUT_OF_UNIVERSE designers, got {len(oou)}")
        if active_set & oou_set:
            errors.append(f"Regime {rname}: overlap between active and OUT_OF_UNIVERSE: {active_set & oou_set}")
        if (active_set | oou_set) != FULL_ROSTER:
            errors.append(f"Regime {rname}: active U OUT_OF_UNIVERSE != 12-slug roster")

        total = sum(float(v) for v in weights.values())
        if not math.isclose(total, 1.0, abs_tol=TOL):
            errors.append(f"Regime {rname}: base weights sum to {total}, expected 1.0")

        for slug, w in weights.items():
            wf = float(w)
            if wf <= 0 or wf > 0.35 + TOL:
                errors.append(f"Regime {rname}: designer {slug} weight {wf} violates (0, 0.35]")
            activated_anywhere.add(slug)

        lindy_sum = sum(float(w) for s, w in weights.items() if s in EXPECTED_LINDY)
        convex_sum = sum(float(w) for s, w in weights.items() if s in EXPECTED_CONVEX)
        if not (0.40 - TOL <= lindy_sum <= 0.60 + TOL):
            errors.append(f"Regime {rname}: Lindy balance {lindy_sum:.4f} outside [0.40, 0.60]")
        if not math.isclose(lindy_sum, float(rcfg.get("lindy_ratio", -1)), abs_tol=TOL):
            errors.append(f"Regime {rname}: declared lindy_ratio mismatch ({rcfg.get('lindy_ratio')} vs {lindy_sum})")
        if not math.isclose(convex_sum, float(rcfg.get("convex_ratio", -1)), abs_tol=TOL):
            errors.append(f"Regime {rname}: declared convex_ratio mismatch ({rcfg.get('convex_ratio')} vs {convex_sum})")

        if rname in override_regimes:
            if inj_designer in active_set:
                errors.append(f"Regime {rname}: {inj_designer} should not already be in base active_weights")
            override_total = sum(float(w) * scale_factor for w in weights.values()) + inj_weight
            if not math.isclose(override_total, 1.0, abs_tol=TOL):
                errors.append(f"Regime {rname}: AI override weights sum to {override_total}, expected 1.0")

    orphans = FULL_ROSTER - activated_anywhere
    if orphans:
        errors.append(f"Orphan designers never activated in any regime: {sorted(orphans)}")

    stats = {
        "regimes": len(regimes),
        "roster_covered": len(activated_anywhere),
        "orphans": len(orphans),
    }
    return len(errors) == 0, errors, stats


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    ok, errors, stats = run_check(repo_root)
    if ok:
        print(
            f"[PASS] check_routing_math: {stats['regimes']} regimes exact sum=1.00, "
            f"Barbell 40-60%, {stats['roster_covered']}/12 roster covered ({stats['orphans']} orphans), "
            f"15% AI override exact sum=1.00"
        )
        return 0
    print(f"[FAIL] check_routing_math: {len(errors)} error(s)")
    for e in errors:
        print(f"  - {e}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
