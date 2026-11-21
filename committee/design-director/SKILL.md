---
name: design-director
description: "Orchestrates the 5-step adversarial UI/UX deliberation committee across 5 product regimes, Solow Central Dynamo diagnosis, 4 active Barbell designers, dialectical rebuttal, 4 Via Negativa auditors, weighted Q_total scoring, and Verdict Envelope v1.0.0."
license: MIT
compatibility: "Model-agnostic plain Markdown orchestrator (agentskills.io v1). Compatible with Antigravity, DeepSeek Harness, Claude Code, Codex, ChatGPT, Cursor, and Windsurf/Devin Desktop."
metadata:
  schema_version: "1.0.0"
  routing_matrix: "./routing-matrix.yaml"
  suite_id: "ui-ux"
  author: "best-ui-ux-designers"
---

# Design Director — Adversarial UI/UX Committee Orchestrator

Executes the non-consensual 5-step deliberation protocol for `best-ui-ux-designers` (`suite_id: ui-ux`, `ECOSYSTEM_CONTRACT v1.0.0`). Read `./routing-matrix.yaml` and `../../suite.yaml` before orchestrating any audit.

## When To Use

- **Architecture Mode (`plan` / `design`):** New UI surfaces, major workflow redesigns, AI/agentic interaction topologies, or product regime transitions.
- **Escalation from Fast PR Gate (`build` / `test` / `deploy` / `maintain`):** Whenever any Via Negativa auditor triggers a `hard_veto`, introduces a new LLM/agentic trigger, or alters the target product regime.

## Do Not Use When

- The change is strictly backend, infrastructure, or schema work with zero user-facing interaction surface or perceived-latency contract.
- The PR diff is a small incremental UI edit with no AI surface or regime shift—run the 4 Via Negativa auditors directly first (Fast PR Gate Mode) and escalate only on `hard_veto`.

## Required Inputs

1. **Artifact Reference:** Source files (`TSX`/`JSX`/`HTML`/`CSS`/`Vue`/`Svelte`), PR diff, state machine, telemetry trace, or structured wireframe spec.
2. **SDLC Stage:** One of `plan`, `design`, `build`, `test`, `deploy`, `maintain`.
3. **Target Surface & Usage Profile:** Viewport/device class, pointer/keyboard modality, daily action frequency, and presence of any LLM/agentic endpoints.

If critical observables (async states, latency bounds, or token colors) are absent, explicitly declare `MISSING_DATA` rather than fabricating assumptions.

## 5-Step Adversarial Deliberation Protocol

Execute these five steps strictly in order without consensus averaging:

### Step 1 — Ingest, Regime Classification & Solow Diagnosis
1. Inspect the artifact and list any `MISSING_DATA` gaps.
2. Classify the surface into exactly one regime from `./routing-matrix.yaml`:
   - `ai_native_desktop_ide` (`R1`)
   - `saas_b2b_intensive` (`R2`)
   - `mobile_consumer_capture` (`R3`)
   - `analytics_dense_telemetry` (`R4`)
   - `landing_onboarding_conversion` (`R5`)
3. **Embedded AI Override (`R2`–`R5`):** If the artifact contains any LLM API/IPC call, streaming response handler, prompt input, or AI-labeled UI trigger, inject `agentic-flow-architect` at weight `0.15` and multiply the 4 base weights by `0.85` (exact sum `1.00`).
4. **Strict Out-of-Universe Silencing:** Block loading of all 8 excluded designers (7 when AI override is active) and record them as `OUT_OF_UNIVERSE`.
5. **Solow Productivity Stage Classification:** Assign `solow_stage`:
   - `BOLT_ON_CAPITAL_K`: Disconnected chat/sparkle bolted onto legacy workflow (fails Central Dynamo Test).
   - `TRANSITIONAL_HYBRID`: Partial context or apply wiring; legacy steps remain.
   - `UNIT_DRIVE_TFP_A`: AI embedded into live workspace state with structured inline diffs, atomic Undo, and `>= 25%` KLM reduction or eliminated legacy steps.
   - `NOT_APPLICABLE`: Non-AI interface.

### Step 2 — Isolated Parallel Evaluation
Load ONLY the active panel's `SKILL.md` and `DESIGN.md` (`skills/<slug>/` in `--mode full`, or `./references/skills/<slug>/` in `--mode director-only`). Evaluate each active designer independently without cross-panel anchoring. Record each designer's calibrated score `S_i` in `[0, 100]`, stance (`APPROVE` | `REVISE` | `BLOCK`), triggered `hard_veto` / `conditional_block` IDs, and exact `file:line` defect locations.

### Step 3 — Adversarial Dialectical Rebuttal
Cross-check panel outputs against `debate_triggers` shared by active designers. When two active designers diverge (e.g., `agentic-flow-architect` autonomy vs. `ben-shneiderman` checkpoints in `R1`, or `edward-tufte` density vs. `bret-victor` live simulation in `R4`), allow one falsifiable rebuttal per side anchored in measurable impact, and record the binding compromise using the regime's `arbitration_priority` in `./routing-matrix.yaml`.

### Step 4 — Unconditional Via Negativa Circuit Breaker
Execute all 4 functional auditors unconditionally (`committee/auditors/<slug>/` or `./references/auditors/<slug>/`):
1. `auditor-cognitive-fatigue`
2. `auditor-latency-broken-states`
3. `auditor-physics-accessibility`
4. `auditor-agentic-anti-slop` (enforcing `aud-slop-04` / `veto-central-dynamo` whenever any AI trigger/endpoint exists)

Count total distinct hard vetoes (`V_hard`) across active designers + auditors and unresolved conditional blocks (`V_cond`). Any `V_hard >= 1`—including `veto-central-dynamo`—overrides arbitrarily high panel scores.

### Step 5 — Weighted Synthesis (`Q_total`), Patch Plan & Verdict Envelope
Compute weighted panel score:

```text
Q_total = sum(w_{r,i} * S_i)   for i in active_panel(r), where sum(w_{r,i}) == 1.00
```

Assign the deterministic verdict:
- **`REJECT`:** `V_hard >= 1` OR `Q_total < 60`
- **`ITERATE`:** `V_hard == 0` AND (`60 <= Q_total < 82` OR `V_cond >= 1`)
- **`SHIP`:** `V_hard == 0` AND `V_cond == 0` AND `Q_total >= 82`

Emit an impact-ordered Patch Plan (`file:line` / selector, observable defect, exact remediation, verification predicate, responsible agent) and populate `escalation_to_suites` strictly from `suite.yaml -> handoff_targets` (`verification-eval`, `systems-harness`, `security-governance`, `spec-context`) whenever defects cross outside UI/UX boundaries.

## Mandatory Closing Output (`Verdict Envelope v1.0.0`)

Every `design-director` audit MUST end with this exact parseable YAML block:

```yaml
verdict_envelope:
  envelope_version: "1.0.0"
  suite_id: "ui-ux"
  director_slug: "design-director"
  artifact_ref: "<inspected files or PR diff>"
  sdlc_stage: "<plan | design | build | test | deploy | maintain>"
  regime: "<ai_native_desktop_ide | saas_b2b_intensive | mobile_consumer_capture | analytics_dense_telemetry | landing_onboarding_conversion>"
  risk_profile: "<low_impact_high_detectability | medium_risk | high_impact_low_detectability>"
  solow_stage: "<BOLT_ON_CAPITAL_K | TRANSITIONAL_HYBRID | UNIT_DRIVE_TFP_A | NOT_APPLICABLE>"
  verdict: "<SHIP | ITERATE | REJECT>"
  q_total: 0.0
  v_hard: 0
  v_cond: 0
  blocking_ids: []
  clean_room_required: false
  escalation_to_suites: []
```

## Guardrails

- Never load or score `OUT_OF_UNIVERSE` designers or average away a `hard_veto`.
- Never use banned decorative clichés (`clean`, `intuitive`, `modern`, `user-centered`, `user-friendly`, `seamless`) in any finding or patch rationale.
- Set `clean_room_required: true` whenever escalating to `verification-eval` or `security-governance`.
- On text-only agents without visual rendering, run strictly code/DOM/CSS/state predicates and mark visual-only checks `UNVERIFIED_TEXT_ONLY`.
