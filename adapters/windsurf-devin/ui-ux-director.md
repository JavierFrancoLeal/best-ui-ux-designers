---
trigger: model_decision
description: "Routes UI/UX reviews, frontend diffs, and AI workflow audits through best-ui-ux-designers (suite_id: ui-ux, v1.1.0) with CPU pre-scanning and Via Negativa circuit breakers."
---

# UI/UX Adversarial Judgment Director (`ui-ux-director`)

Use this rule for UI architecture, frontend diffs (`*.html`, `*.tsx`, `*.jsx`, `*.css`, `*.vue`, `*.svelte`), state machines, and AI user flows. Director and bundled scanner live under `.windsurf/skills/design-director/` (lazy briefs and auditors in `./references/`).

## Dual-Mode Execution
1. **Fast PR Gate (`build` / `verify`):** Run `python3 .windsurf/skills/design-director/tools/uiux_cpu_scanner.py --format json <files...>`, then apply semantic delta checks from `.windsurf/skills/design-director/references/auditors/*/rules.yaml`. Escalate to `design-director` on `BLOCKER` or new AI surface.
2. **Architecture Mode (`plan` / `design`):** Execute `.windsurf/skills/design-director/SKILL.md` (CPU pre-scan + Regime `R1`–`R5` + compact `BRIEF.md` active panel + rebuttal + 4 auditors + `Verdict Envelope v1.1.0`).

## Mandatory Guardrails
- `BLOCKER >= 1` forces `REJECT`; unresolved `MAJOR >= 1` prohibits `SHIP`.
- Deduplicate each `file:line` defect once; respect `brand_exemption`; never escalate to suites already in `visited_suites`.
