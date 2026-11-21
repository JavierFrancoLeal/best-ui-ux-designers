---
trigger: model_decision
description: "Activates best-ui-ux-designers (suite_id: ui-ux) for UI/UX architecture reviews, component audits, AI surface design, and TSX/JSX/CSS/Vue/Svelte PR diffs."
---

# UI/UX Adversarial Judgment Bootstrap (`uiux-bootstrap`)

Invoke this rule whenever planning, designing, implementing, or reviewing user-facing interfaces, frontend diffs (`*.tsx`, `*.jsx`, `*.css`, `*.vue`, `*.svelte`), design tokens, state machines, or AI interaction flows.

## Skill Lookup Paths
- Workspace skills: `.agents/skills/` (or `.agent/skills/` fallback)
- Global skills: `~/.gemini/config/skills/`
- In `--mode director-only` installations, load `design-director/SKILL.md` first and resolve individual designers/auditors lazily from `design-director/references/skills/<slug>/` and `design-director/references/auditors/<slug>/`.

## Dual-Mode SDLC Dispatch
1. **Architecture Mode (`plan` / `design`):**
   - Load `design-director` (`SKILL.md` + `routing-matrix.yaml`).
   - Run the 5-step adversarial deliberation protocol: Regime Classification (`R1`–`R5`) + Solow Stage (`BOLT_ON_CAPITAL_K` | `TRANSITIONAL_HYBRID` | `UNIT_DRIVE_TFP_A` | `NOT_APPLICABLE`) + 4 active Barbell designers (5 with 15% embedded AI override) + Dialectical Rebuttal + 4 Via Negativa auditors + weighted `Q_total` + `verdict_envelope` v1.0.0.
   - Never load `OUT_OF_UNIVERSE` designers.
2. **Fast PR Gate Mode (`build` / `test` / `deploy` / `maintain`):**
   - Run all 4 Via Negativa auditors on UI diffs: `auditor-cognitive-fatigue`, `auditor-latency-broken-states`, `auditor-physics-accessibility`, `auditor-agentic-anti-slop` (enforcing `aud-slop-04` / `veto-central-dynamo` on any AI trigger).
   - Escalate immediately to full `design-director` on any `hard_veto`, new AI surface, or regime change.

## Non-Negotiable Invariants
- Any `hard_veto` (`V_hard >= 1`) forces `REJECT` regardless of panel score.
- Enforce the immutable Phase A Calibrated Rubric (`Base 100`, `-35` `hard_veto` cap `49`, `-15` `hard_filter`/`conditional_block`, `-10` critical, `-5` high, `-2` medium, floor `0`, `APPROVE >= 82`, `REVISE 60..81`, `BLOCK < 60`).
- Zero banned decorative clichés (`clean`, `intuitive`, `modern`, `user-centered`, `user-friendly`, `seamless`); cite exact `file:line`, DOM/CSS selectors, or state predicates.
- Populate `verdict_envelope.escalation_to_suites` per `suite.yaml` when defects cross into `verification-eval`, `systems-harness`, `security-governance`, or `spec-context`.
