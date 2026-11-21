---
trigger: model_decision
description: "Activates best-ui-ux-designers (suite_id: ui-ux, v1.1.0) for CPU-first UI/UX architecture reviews, component audits, AI surface design, and frontend PR diffs."
---

# UI/UX Adversarial Judgment Bootstrap (`ui-ux-bootstrap`)

Invoke this rule when planning, designing, implementing, or reviewing user-facing interfaces (`*.html`, `*.tsx`, `*.jsx`, `*.css`, `*.vue`, `*.svelte`), design tokens, state machines, or AI interaction flows.

## Skill & Tool Lookup Paths
- Workspace director: `.agents/skills/design-director/SKILL.md` (global: `~/.gemini/config/skills/design-director/SKILL.md`)
- Bundled CPU pre-scanner: `.agents/skills/design-director/tools/uiux_cpu_scanner.py`
- Lazy references (`--mode director-only`): `.agents/skills/design-director/references/skills/<slug>/BRIEF.md` (and `PROFILE.md`) and `.agents/skills/design-director/references/auditors/<slug>/rules.yaml` (and `AUDITOR.md`).

## Dual-Mode Dispatch
1. **Fast PR Gate (`build` / `verify`):**
   - Run `python3 .agents/skills/design-director/tools/uiux_cpu_scanner.py --format json <files...>`.
   - Apply semantic delta checks from the 4 Via Negativa auditors in `.agents/skills/design-director/references/auditors/*/rules.yaml`.
   - Escalate to `design-director` on any `BLOCKER`, new AI trigger, or regime shift.
2. **Architecture Mode (`plan` / `design`):**
   - Run `design-director/SKILL.md` (Step 0 CPU pre-scan + Regime `R1`–`R5` + compact `BRIEF.md` active panel `<= 25 KB` + rebuttal + 4 auditors + `Verdict Envelope v1.1.0`).

## Non-Negotiable Invariants
- Any `BLOCKER >= 1` forces `REJECT`; any unresolved `MAJOR >= 1` prohibits `SHIP`.
- Count each root-cause `file:line` defect at most once (no triple counting); label numeric panel scores `score_heuristic`.
- Respect `brand_exemption.exempt_brand_palette_from_ai_slop` for declared project brand palettes.
- Never escalate to a suite already in `visited_suites`.
