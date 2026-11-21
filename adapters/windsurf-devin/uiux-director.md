---
trigger: model_decision
description: "Routes UI/UX design reviews, frontend diffs, and AI workflow audits through best-ui-ux-designers (suite_id: ui-ux) with Solow Central Dynamo and Via Negativa circuit breakers."
---

# UI/UX Adversarial Judgment Director (`uiux-director`)

Use this rule for UI architecture, frontend component changes (`*.tsx`, `*.jsx`, `*.css`, `*.vue`, `*.svelte`), state machines, and AI/agentic user flows. Deep rubrics live in `.windsurf/skills/design-director/` (with lazy references in `.windsurf/skills/design-director/references/` under `--mode director-only`).

## Dual-Mode Execution
1. **Architecture Mode (`plan` / `design`):** Load `design-director/SKILL.md` + `routing-matrix.yaml`. Classify regime (`R1`–`R5`), evaluate the 15% embedded AI override, silence `OUT_OF_UNIVERSE` profiles, assign `solow_stage`, run 4 active Barbell designers + dialectical rebuttal + 4 Via Negativa auditors, compute `Q_total`, and emit `verdict_envelope` v1.0.0.
2. **Fast PR Gate Mode (`build` / `test` / `deploy` / `maintain`):** Run the 4 Via Negativa auditors (`auditor-cognitive-fatigue`, `auditor-latency-broken-states`, `auditor-physics-accessibility`, `auditor-agentic-anti-slop` with `aud-slop-04` / `veto-central-dynamo`). Escalate to `design-director` on any `hard_veto`, new AI trigger, or regime shift.

## Mandatory Guardrails
- Any `hard_veto` (`V_hard >= 1`) forces `REJECT`.
- Immutable Phase A Rubric: Base `100`; `-35` `hard_veto` (cap `49`); `-15` `hard_filter`/`conditional_block`; `-10` critical, `-5` high, `-2` medium; floor `0`; `APPROVE >= 82`, `REVISE 60..81`, `BLOCK < 60`.
- Zero decorative clichés (`clean`, `intuitive`, `modern`, `user-centered`, `user-friendly`, `seamless`). Cite exact `file:line`, DOM/CSS predicates, and numeric bounds.
