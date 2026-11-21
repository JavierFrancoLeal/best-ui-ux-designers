---
name: luke-wroblewski
description: Audits and refactors mobile capture flows, checkouts, and onboarding funnels using Luke Wroblewski's DOM, CSS, and state-machine predicates for <=14-element single-column forms, persistent top labels, native input semantics, inline validation, gradual engagement, and thumb-zone ergonomics.
license: MIT
compatibility: Text-only LLM coding agents (DeepSeek V4, Claude, GPT) auditing HTML, JSX/TSX, CSS, and client-side form state machines without computer vision.
metadata:
  schema_version: "1.0.0"
  design_schema: "./DESIGN.md"
  barbell_pole: "convex_frontier"
  primary_regimes: "mobile_consumer_capture,landing_onboarding_conversion"
  author: "best-ui-ux-designers"
---

## When To Use

- Auditing or refactoring mobile consumer capture flows at viewports `<430 CSS px` (quick bookings, polling/feedback widgets, mobile lead capture, express checkout, touch-first forms).
- Auditing or refactoring web checkout pipelines, landing conversion funnels, and first-time user onboarding flows (`landing_onboarding_conversion`).
- Diagnosing form abandonment caused by multi-column field scattering, `>14` visible form elements, upfront mandatory registration walls, placeholder-only labels, generic `type="text"` inputs, premature or submit-only validation, `<select>` wheel bloat for 2–5 choices, or top-left primary actions/hamburger drawers hiding `<=5` core routes.

## Do Not Use When

- **`ai_native_desktop_ide`** (`pointer: fine`, viewport `>=1024 px`, multi-pane authoring canvases, layer trees, inline code diffs, or `>20` concurrent property inspector controls) -> emit `posture: "HANDOFF"` and delegate to `rasmus-andersson`.
- **`saas_b2b_intensive`** (authenticated desktop B2B operational workbenches with `>15` repetitive CRUD/triage mutations per session, `Cmd+K` command palettes, keyboard-first workflows, and `<100 ms` latency targets) -> emit `posture: "HANDOFF"` and delegate to `karri-saarinen`.
- **`analytics_dense_telemetry`** (observability consoles, financial terminals, or diagnostic dashboards requiring simultaneous synoptic comparison across `>=4` quantitative time-series or dense multi-column metric matrices) -> emit `posture: "HANDOFF"` and delegate to `edward-tufte`.

## Required Inputs

1. **Target regime & viewport context**: Confirm whether the screen serves `mobile_consumer_capture` (`<430 px` / `pointer: coarse`) or `landing_onboarding_conversion`, or belongs to an out-of-universe desktop regime.
2. **Markup / Component source**: HTML, JSX/TSX, or template markup covering all form controls, `<label>` bindings, navigation elements, and entry-gate logic.
3. **Stylesheet / Layout definitions**: CSS, Tailwind classes, or layout tokens exposing grid/flex column counts, computed input `font-size`, touch target dimensions (`min-width`/`min-height`), spacing gaps, and bottom/top positioning.
4. **Validation & Auth state machine**: Event handlers (`onFocus`, `onChange`, `onBlur`, `onSubmit`), error-clearing transitions, value-preservation behavior on submit failure, and authentication gating rules.

## Audit & Design Workflow

1. **Gate 0 — Regime Classification**: Check viewport, pointer modality, and primary user task against `DESIGN.md` Section 2. If the request targets `ai_native_desktop_ide`, `saas_b2b_intensive`, or `analytics_dense_telemetry`, immediately terminate scoring and return `in_universe: false`, `posture: "HANDOFF"`, and the matching `counterweight_handoff` slug.
2. **Gate 1 — Hard Veto Scan (`veto-01`..`veto-05`)**:
   - Inspect auth/entry transitions for `veto-01` (mandatory account wall before guest checkout or core value delivery).
   - Inspect every rendered `<input>`, `<select>`, and `<textarea>` for `veto-02` (placeholder-only or hidden `<label>`).
   - Count visible form elements and inspect layout CSS + action buttons for `veto-03` (`>14` visible elements in multi-column layout OR `<button type="reset">`/`Clear` with visual parity to Submit).
   - Trace validation handlers for `veto-04` (`onSubmit`-only blind validation OR premature `onFocus`/first-character errors).
   - Inspect `<430 px` navigation and small-cardinality `<select>` controls for `veto-05` (`conditional_block`: top-left hamburger hiding `<=5` core routes OR native `<select>` for `2–5` options / `1–8` integer counts).
3. **Gate 2 — Hard Filter Evaluation (`flt-01`..`flt-05`)**: Verify each boolean filter against the source code: single-column flow & `<=14` element cap (`flt-01`), persistent top `<label>` & `>=16px` input font (`flt-02`), WHATWG `autocomplete`/`type`/`inputmode`/`enterkeyhint` (`flt-03`), `>=44x44px` hit areas & lower thumb-band primary action at `<430 px` (`flt-04`), and non-premature/non-data-wiping validation (`flt-05`).
4. **Gate 3 — Signal Scoring (`sig-01`..`sig-07`)**: Score all seven signals (`sig-01`..`sig-03` `critical`; `sig-04`..`sig-06` `high`; `sig-07` `medium`) deterministically from DOM, CSS, and state-machine evidence.
5. **Gate 4 — Minimal Deterministic Remediation**: Compute the final score and verdict using the rubric below, then emit exact JSX/TSX + CSS patches resolving every triggered veto first, followed by failed filters and signals.

## Scoring & Verdict Rubric

Start from a base score of `100` and apply every applicable deduction:

- **`hard_veto` (`veto-01`..`veto-04`)**: `-35` each; sets maximum score ceiling (`score_cap`) to `49` and forces posture `BLOCK`.
- **Failed `hard_filter` (`flt-01`..`flt-05`) or active `conditional_block` (`veto-05`)**: `-15` each.
- **Failed `critical` signal (`sig-01`..`sig-03`)**: `-10` each.
- **Failed `high` signal (`sig-04`..`sig-06`)**: `-5` each.
- **Failed `medium` signal (`sig-07`)**: `-2` each.
- **Floor**: Minimum score `S` is `0` (`S = max(0, min(score_cap, raw_score))`).

Posture thresholds:

- **`APPROVE`**: `0` `hard_veto`, `0` `conditional_block`, and `S >= 82`.
- **`REVISE`**: `0` `hard_veto`, and (`60 <= S < 82` OR (`>= 1` `conditional_block` with `S >= 60`)).
- **`BLOCK`**: `>= 1` `hard_veto` OR `S < 60`.

**Worked Numerical Example**:
A mobile checkout triggers `veto-02` (`hard_veto`: `-35`, `score_cap = 49`), fails `flt-02` (`-15`), fails `sig-03` (`critical`: `-10`), and fails `sig-04` (`high`: `-5`).
`raw_score = 100 - 35 - 15 - 10 - 5 = 35`.
Applying cap and floor: `S = max(0, min(49, 35)) = 35`.
Verdict: **`BLOCK`** (`expected_score: 35`, `score_cap: 49`).

## Guardrails

- Never emit subjective aesthetic labels (`clean`, `intuitive`, `modern`, `user-centered`); every finding must cite an exact signal/filter/veto ID and a verifiable DOM, CSS, HTML attribute, or state-machine predicate.
- Never use `<input type="number">` for credit cards, CVVs, postal codes, phone numbers, or OTPs; enforce `type="text"` with `inputmode="numeric"` and valid WHATWG `autocomplete` tokens.
- Never suppress browser pinch-zoom (`user-scalable=no` or `maximum-scale=1`) to prevent iOS Safari focus zoom; enforce computed `font-size >= 16px` on form controls instead.
- Never preserve `<button type="reset">` or wipe user-entered form fields after validation errors; retain 100% of entered values and shift focus to the first invalid control.
- Never force this skill onto `ai_native_desktop_ide`, `saas_b2b_intensive`, or `analytics_dense_telemetry`; always execute `HANDOFF` to the designated roster counterweight.
