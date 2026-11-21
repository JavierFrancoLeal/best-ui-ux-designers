#!/usr/bin/env python3
"""Generate compact operational BRIEF.md files (<= 3 KB each) from skills/*/DESIGN.md.

Keeps active director context load under the ECOSYSTEM_CONTRACT v1.1.0 25 KB budget
while leaving full essays, TSX recipes, and bibliographies in DESIGN.md for lazy lookup.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


def _parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: missing YAML frontmatter")
    data = yaml.safe_load(m.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter is not a mapping")
    return data


def _clip(text: str, limit: int = 165) -> str:
    clean = " ".join(str(text or "").split())
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1].rstrip() + "…"


def build_brief(fm: dict[str, Any]) -> str:
    ident = fm.get("identity", {})
    slug = ident.get("slug", "")
    name = ident.get("display_name", slug)
    pole = ident.get("barbell_pole", "")
    axiom = _clip(ident.get("core_axiom", ""), 260)
    rfit = fm.get("regime_fit", {})
    prim = ", ".join(rfit.get("primary_regimes", []))
    oou = ", ".join(x.get("regime", "") for x in rfit.get("out_of_universe_regimes", []) if isinstance(x, dict))

    lines: list[str] = [
        f"# {name} (`{slug}`) — Compact Operational Brief",
        f"- **Pole:** `{pole}` · **Primary Regimes:** `{prim}` · **OOU:** `{oou}`",
        f"- **Core Axiom:** {axiom}",
        "- **Deduplication & CPU-First Rule:** Consume `tools/uiux_cpu_scanner.py` output first (`TOOL_VERIFIED`). Count each root-cause defect **at most once** at its highest severity (`BLOCKER` | `MAJOR` | `MINOR`). Do NOT re-flag declared project brand tokens as slop when `brand_exemption.exempt_brand_palette_from_ai_slop == true`.",
        "",
        "## Veto Triggers (Semantic & Structural)",
    ]
    for v in fm.get("veto_triggers", []):
        sev = "BLOCKER" if v.get("severity") == "hard_veto" else "MAJOR"
        cond = _clip(v.get("detection_rule", v.get("target_antipattern", v.get("name", ""))), 140)
        lines.append(f"- `{v.get('id')}` (`{sev}` · `{v.get('name')}`): {cond}")

    lines.append("")
    lines.append("## Hard Filters & Critical Signals (Semantic Focus)")
    for flt in fm.get("hard_filters", []):
        cond = _clip(flt.get("condition", ""), 120)
        lines.append(f"- `{flt.get('id')}` (`MAJOR` · `{flt.get('name')}`): {cond}")
    for sig in fm.get("high_weight_signals", []):
        if sig.get("weight") == "critical":
            thr = _clip(sig.get("threshold", sig.get("detects_before_others", "")), 115)
            lines.append(f"- `{sig.get('id')}` (`MAJOR` · `{sig.get('name')}`): {thr}")

    debates = fm.get("debate_triggers", [])
    if debates:
        lines.append("")
        lines.append("## Debate Triggers")
        for d in debates:
            axis = _clip(d.get("conflict_axis", ""), 70)
            arb = _clip(d.get("arbitration_rule", ""), 100)
            lines.append(f"- `{d.get('id')}` vs `{d.get('opposing_designer')}` ({axis}): {arb}")

    lines.append("")
    lines.append("> Deep bibliography, primary sources, and reference code patterns live in `./DESIGN.md` (load only on explicit demand).")
    return "\n".join(lines) + "\n"


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    design_files = sorted((repo_root / "skills").glob("*/DESIGN.md"))
    if not design_files:
        print("ERROR: No skills/*/DESIGN.md found", file=sys.stderr)
        return 1
    sizes: list[tuple[str, int]] = []
    for dp in design_files:
        fm = _parse_frontmatter(dp)
        content = build_brief(fm)
        out_path = dp.parent / "BRIEF.md"
        out_path.write_text(content, encoding="utf-8")
        sizes.append((dp.parent.name, len(content.encode("utf-8"))))
    max_sz = max(s for _, s in sizes)
    avg_sz = sum(s for _, s in sizes) // len(sizes)
    print(f"[OK] Generated {len(sizes)} BRIEF.md files (avg={avg_sz} B, max={max_sz} B; 5-designer panel ~{avg_sz*5:,} B / ~{(avg_sz*5)//4:,} tokens)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
