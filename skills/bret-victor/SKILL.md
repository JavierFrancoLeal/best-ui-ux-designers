---
name: bret-victor
description: Audits and refactors AI-native desktop IDEs and telemetry analytics tools via Bret Victor's live-feedback, state-visibility, ladder-of-abstraction, and Magic Ink rules. Triggers for blind apply forms, hidden execution state, or filter excise; excludes B2B CRUD, mobile capture, and conversion funnels.
license: MIT
compatibility: Designed for text-only code, AST, DOM, CSS, state-machine, and runtime telemetry audit agents; no screenshot or vision capability required.
metadata:
  schema_version: "1.1.0"
  judgment_schema: "./DESIGN.md"
  suite_id: "ui-ux"
  barbell_pole: "convex_frontier"
  primary_regimes: "ai_native_desktop_ide,analytics_dense_telemetry"
  author: "best-ui-ux-designers"
---

# Bret Victor Live-Feedback & State-Visibility Skill

Evaluate, score, and refactor user interfaces in `ai_native_desktop_ide` and `analytics_dense_telemetry` using falsifiable code, DOM, CSS, and state-machine invariants derived from Bret Victor's primary works. Load `./DESIGN.md` before executing any veto check, heuristic audit, TSX refactoring, or counterweight arbitration.

## When To Use

Activate this skill when the user asks to audit, design, or refactor:
- AI-native desktop IDE panels configuring retrieval thresholds, token budgets, prompt rules, execution traces, or multi-stage agent pipelines.
- Dense telemetry, SLO alerting, simulation, or quantitative analytics workbenches where operators tune thresholds, compare time-series trajectories, or run sensitivity ("what-if") sweeps.
- Read-dominant analytical dashboards trapped behind empty filter dropdowns and manual "Run Query" buttons (*Magic Ink* excise).
- Reactive analytical narratives or parameterizable visualizations requiring inline scrubbing and model transparency.

## Do Not Use When

Decline activation and route to the specified counterweight or regime specialist when the request falls inside an out-of-universe regime:
- **`saas_b2b_intensive`** (repetitive CRUD forms, high-volume ticket triage, tabular admin queues with >=20 known-input operations/hour): route to `karri-saarinen`.
- **`mobile_consumer_capture`** (viewports <430 px, thumb-driven capture, quick mobile input flows): route to `luke-wroblewski`.
- **`landing_onboarding_conversion`** (marketing hero sections, pricing pages, signup or checkout funnels): route to `luke-wroblewski` or `dieter-rams`.
- **Static historical reporting** comparing >=12 fixed time series with zero tunable parameters: route to `edward-tufte`.
- **Linear deterministic writing or distraction-free reading** with no rule calibration: route to `dieter-rams`.

## Required Inputs

Request or extract at least one of the following text-verifiable artifacts before issuing a scored verdict:
1. Target component source code (JSX/TSX/Vue/Svelte/HTML/CSS) or state-machine definition.
2. Declared operating regime (`ai_native_desktop_ide` or `analytics_dense_telemetry`) and task frequency profile.
3. Execution boundary metadata identifying which state updates run locally versus invoke remote LLM APIs or mutating backend writes.
4. Optional runtime telemetry (event-to-paint latency in ms, mount-time data render status, KLM operator sequence).

## Execution & Audit Workflow

Follow this sequential checklist on every run:

- [ ] **Step 1 — Regime & Scope Gate:** Verify the artifact belongs to `ai_native_desktop_ide` or `analytics_dense_telemetry`. If it matches an out-of-universe regime in `Do Not Use When`, stop immediately, report `OUT_OF_UNIVERSE`, and name the target handoff designer.
- [ ] **Step 2 — Load Canonical Schema:** Read `./DESIGN.md` sections `3. Signal Detection Protocol`, `4. Hard Filters & Veto Playbook`, and `5. Executable Heuristics & Code Patterns` to anchor exact thresholds and detection predicates.
- [ ] **Step 3 — Dual-Loop Safety Inspection (`flt-01`, `veto-03`):** Inspect every `onChange`, `onInput`, and `onPointerMove` handler. Confirm zero remote LLM calls or mutating API writes execute during continuous scrubbing.
- [ ] **Step 4 — Veto & Hard-Filter Evaluation:** Run deterministic AST/DOM/state-machine checks for `veto-01` through `veto-05` and `flt-01` through `flt-05`. Record exact file, line, component, or state-transition evidence for every violation.
- [ ] **Step 5 — Signal & Heuristic Audit:** Measure `sig-01` through `sig-06` and verify applicable heuristics (`heur-01` through `heur-10`) using `static_code_audit`, `state_matrix_check`, `visual_dom_inspection`, `klm_goms_estimate`, or `runtime_telemetry`.
- [ ] **Step 6 — Counterweight & Blind-Spot Arbitration:** Check `./DESIGN.md` sections `6. Blind Spots & Counterweights` and `7. Adversarial Debate Positions` whenever continuous projections exceed 15% viewport footprint during linear work (`dieter-rams`), affect repetitive operations (`karri-saarinen`), degrade data-ink ratio (`edward-tufte`), or touch stochastic LLM execution (`agentic-flow-architect`).
- [ ] **Step 7 — Compute Verdict & Emit Refactoring:** Calculate the exact numerical score using the rubric below. If verdict is `BLOCK` or `REVISE`, output concrete compilable code fixes matching the patterns in `./DESIGN.md` Section 5.
- [ ] **Step 8 — Self-Validation Pass:** Confirm zero forbidden clichés appear in the audit report, every finding cites a falsifiable DOM/AST/latency bound, and every proposed scrubber preserves keyboard arrow stepping and explicit commit isolation.

## Verdict & Severity Criteria

Start from a base score of **100** and apply the immutable Phase A Calibrated Rubric deterministically:

| Finding Category | Penalty | Cap / Constraint |
| --- | --- | --- |
| `hard_veto` (`veto-01`, `veto-02`, `veto-03`) | `-35` each | If count >= 1, final score is **capped at `49`** and forces posture `BLOCK`. |
| Failed `hard_filter` (`flt-01`..`flt-05`) or unresolved `conditional_block` (`veto-04`, `veto-05`) | `-15` each | Unresolved `conditional_block` prevents `APPROVE`. |
| Failed `critical` signal (`sig-01`, `sig-02`) | `-10` each | Direct deduction per failed critical signal. |
| Failed `high` signal (`sig-03`..`sig-06`) | `-5` each | Direct deduction per failed high signal. |
| Failed `medium` signal (when applicable) | `-2` each | Direct deduction; floor final score at `0` (`S = max(0, min(cap, 100 - total_deductions))`). |

Assign the verdict strictly by band:
- **`APPROVE`:** `hard_veto == 0` AND `conditional_block == 0` AND `S >= 82`.
- **`REVISE`:** `hard_veto == 0` AND (`60 <= S < 82` OR (`conditional_block > 0` AND `S >= 60`)).
- **`BLOCK`:** `hard_veto >= 1` (capped at `<= 49`) OR `S < 60`.

### Required Audit Output Format

```markdown
### Verdict: <APPROVE | REVISE | BLOCK> (Score: <0-100>/100)
- **Regime:** <ai_native_desktop_ide | analytics_dense_telemetry>
- **Hard Vetoes Triggered:** <IDs or None>
- **Failed Filters / Conditional Blocks:** <IDs or None>
- **Failed Signals / Heuristics:** <IDs or None>
- **Counterweight Arbitration Applied:** <slug + rule or None>

#### Deterministic Findings
1. [<ID>] <Exact AST/DOM/state evidence> -> <Exact bound violated> -> <Required code change>

#### Refactored Implementation
<Compilable code patch resolving all triggered vetoes and blocks>
```

## Guardrails

1. **Zero Clichés:** Never use `"clean"`, `"intuitive"`, `"modern"`, or `"user-centered"` in verdicts, findings, or remediation rules. Express every criterion as a falsifiable DOM, AST, CSS, latency, or state-machine predicate.
2. **Mandatory Dual-Loop Isolation:** Never recommend firing remote LLM requests, paid embeddings, or mutating database writes on continuous slider `onChange` or `onPointerMove` events. Always enforce a local deterministic proxy (`<= 16.67 ms`) plus an explicit Commit control displaying projected token/latency cost.
3. **No Standalone Live-Preview Theater:** Never approve a split-pane live preview (`flt-05`) that updates terminal output without exposing intermediate pipeline stages, variable values, or filter-drop reasons.
4. **Keyboard & Accessibility Parity:** Every pointer-scrubbable parameter must expose semantic `role="slider"`, `aria-valuenow`, focusability, and deterministic keyboard arrow stepping so expert keyboard workflows and assistive technologies remain unblocked.
5. **Respect Algorithmic & Scale Ceilings:** Do not force raw per-iteration runtime expansion on pure algorithmic loops or >12-series static read-only views; summarize distributions or hand off to `edward-tufte`, `dieter-rams`, or `karri-saarinen` per `./DESIGN.md` Section 7.
