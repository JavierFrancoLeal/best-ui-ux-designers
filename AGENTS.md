# AGENTS.md — `best-ui-ux-designers` Routing & Guardrails

This repository provides a portable, multi-harness adversarial UI/UX judgment suite (`suite_id: ui-ux`, `ECOSYSTEM_CONTRACT v1.0.0`). Every judgment rule is expressed as a falsifiable code, DOM, CSS, latency, or state-machine predicate verifiable by both multimodal and text-only coding agents.

## Dual-Mode SDLC Routing

Select the execution mode based on the SDLC stage and change scope:

1. **Architecture Mode (`plan` / `design` — new surfaces, redesigns, AI workflows, regime shifts):**
   - Load `committee/design-director/SKILL.md` and `committee/design-director/routing-matrix.yaml`.
   - Execute the full 5-step adversarial deliberation protocol:
     1. Ingest observables, classify regime (`R1`–`R5`), check `embedded_ai_override` (+15% `agentic-flow-architect`), silence all `OUT_OF_UNIVERSE` designers, and assign `solow_stage`.
     2. Run the 4 active Barbell designers (5 with AI override) in isolation (`skills/<slug>/SKILL.md` + `skills/<slug>/DESIGN.md`).
     3. Arbitrate active `debate_triggers` without consensus averaging.
     4. Run all 4 Via Negativa auditors unconditionally (`committee/auditors/*/SKILL.md` + `rules.yaml`).
     5. Compute weighted `Q_total`, issue deterministic verdict (`SHIP` | `ITERATE` | `REJECT`), and emit the `verdict_envelope` v1.0.0 block.

2. **Fast PR Gate Mode (`build` / `test` / `deploy` / `maintain` — incremental TSX/JSX/CSS/Vue/Svelte diffs):**
   - Run the 4 Via Negativa auditors directly as a regression circuit breaker:
     - `committee/auditors/auditor-cognitive-fatigue/SKILL.md`
     - `committee/auditors/auditor-latency-broken-states/SKILL.md`
     - `committee/auditors/auditor-physics-accessibility/SKILL.md`
     - `committee/auditors/auditor-agentic-anti-slop/SKILL.md` (includes `aud-slop-04` / `veto-central-dynamo`)
   - Escalate to full `committee/design-director/SKILL.md` immediately if any auditor fires a `hard_veto`, introduces a new AI/LLM surface, or changes the product regime.

## Mandatory Invariants

- **Zero Consensus Averaging:** Never load all 12 designers simultaneously. Load strictly the active regime panel from `routing-matrix.yaml` and declare excluded designers `OUT_OF_UNIVERSE`.
- **Unconditional Via Negativa:** Any `hard_veto` (`V_hard >= 1`) from an active designer or auditor forces `REJECT` regardless of high panel scores.
- **Central Dynamo Veto (Solow Test):** Reject bolt-on AI chat sidebars or floating sparkle wrappers (`aud-slop-04` / `veto-central-dynamo`) that increase token capital (`K`) without eliminating workflow steps or lifting Total Factor Productivity (`A`).
- **Zero Decorative Clichés:** Never justify findings with vague terms (`clean`, `intuitive`, `modern`, `user-centered`, `user-friendly`, `seamless`). Cite exact file/line evidence, numeric thresholds, DOM/CSS selectors, or state transitions.
- **Immutable Phase A Scoring:** Base `100`; `-35` per `hard_veto` (`cap = 49`, `BLOCK`); `-15` per failed `hard_filter` or unresolved `conditional_block`; `-10` critical, `-5` high, `-2` medium signal; floor `0`; `APPROVE >= 82`, `REVISE 60..81`, `BLOCK < 60`.
- **Text-Only Compatibility:** When visual rendering tools are unavailable, evaluate static code/DOM/CSS/state predicates deterministically and mark visual-only checks `UNVERIFIED_TEXT_ONLY`.
- **Cross-Suite Escalation:** Populate `verdict_envelope.escalation_to_suites` per `suite.yaml` (`verification-eval`, `systems-harness`, `security-governance`, `spec-context`) whenever defects cross outside UI/UX boundaries.
