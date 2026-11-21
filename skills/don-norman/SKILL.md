---
name: don-norman
description: "Audits mobile capture, onboarding, and SaaS UI code (TSX/DOM/CSS/ARIA) via Don Norman's cognitive engineering rules: perceptible signifiers, natural mapping, gulf-bridging feedback, preventive constraints, and input-preserving error recovery. Use for signifier, form, or flat-UI audits."
license: MIT
compatibility: "Text-only and multimodal coding agents inspecting HTML, JSX/TSX, CSS, ARIA, and client state machines (no browser or vision required)."
metadata:
  schema_version: "1.0.0"
  design_schema: "./DESIGN.md"
  barbell_pole: "lindy_anchor"
  primary_regimes: "mobile_consumer_capture,landing_onboarding_conversion"
  author: "best-ui-ux-designers"
---

# Don Norman UI/UX Cognitive Engineering Auditor

Execute deterministic, code-verifiable interface audits grounded in `./DESIGN.md` (`schema_version: "1.0.0"`). Every finding must cite a concrete DOM node, CSS declaration, ARIA attribute, or state transition—never subjective visual adjectives.

## When To Use

Activate this skill when auditing or refactoring UI code (TSX/DOM/CSS/ARIA) inside:
- **`mobile_consumer_capture` (Primary):** Enforce all 7 signals, 5 hard filters, 5 veto triggers, perceptible clickability signifiers, single-pointer gesture parity, and `>=44x44px` mobile touch floors (`48x48px` target).
- **`landing_onboarding_conversion` (Primary):** Enforce all 7 signals, 5 hard filters, 5 veto triggers, visible navigation (`heur-09`), forgiving input constraints, input-preserving error recovery, and zero false affordances.
- **`saas_b2b_intensive` (Secondary):** Enforce full rubric on forms, onboarding, and settings; apply `heur-10` KLM handoff if reviewing daily keyboard-first power-user views (`>=50` ops/session -> consult `karri-saarinen`).

## Do Not Use When

Decline scoring and immediately emit `OUT_OF_UNIVERSE` / `HANDOFF` without a Norman score when the target falls into:
- **`ai_native_desktop_ide`:** Explain KLM-GOMS overhead (`2.23x–3.94x` mouse+chrome penalty) and viewport consumption from visible mouse buttons in daily keyboard-first IDEs; hand off to `karri-saarinen` and `jef-raskin`.
- **`analytics_dense_telemetry`:** Explain data-ink displacement on `>=10`-series monitoring walls from enforcing `>=44–48px` touch targets and elevated button chrome; hand off to `edward-tufte`.

## Required Inputs

Collect or inspect the following text-verifiable artifacts before scoring (no browser or vision required):
1. **Target regime classification:** Confirm `mobile_consumer_capture`, `landing_onboarding_conversion`, `saas_b2b_intensive`, or out-of-universe scope.
2. **Component markup & styling:** HTML, JSX/TSX, CSS/Tailwind rules covering buttons, links, switches, touch targets, color contrast, and visual signifiers.
3. **Interaction & error state machine:** Touch/drag handlers, `onBlur`/`onChange`/`onSubmit` validation handlers, form reset logic, disabled buttons, ARIA bindings (`aria-invalid`, `aria-errormessage`, `aria-describedby`, `role="status"`), and Undo/confirmation flows.

## Audit & Design Workflow

Inspect the provided HTML, JSX/TSX, CSS, and client state code in four ordered passes:

### Pass 0 — Scope & Regime Gate
Confirm the target belongs to `mobile_consumer_capture`, `landing_onboarding_conversion`, or `saas_b2b_intensive`. If it targets `ai_native_desktop_ide` or `analytics_dense_telemetry`, halt immediately and hand off to `karri-saarinen`/`jef-raskin` or `edward-tufte`.

### Pass 1 — Veto Triggers (`veto-01`..`veto-05`)
Check exact static/state detection rules:
1. **`veto-01` (`hard_veto` — `flat_indiscernible_control`):** `<button>`, `<a href>`, or `[role="button"]` shares static body text styling (`background: transparent`, `border: none/0`, `box-shadow: none`, `text-decoration: none`, same color) or fails `>=3:1` WCAG 1.4.11 boundary contrast.
2. **`veto-02` (`hard_veto` — `hidden_gesture_only_action`):** `onTouchStart`/`onTouchEnd`/`onPointerMove`/drag handler mutates or deletes data with zero equivalent visible `<button>` in the component tree.
3. **`veto-03` (`hard_veto` — `destructive_validation_reset`):** Validation error or 4xx API catch branch invokes `form.reset()`, `setState(empty)`, or clears user-entered controlled inputs.
4. **`veto-04` (`hard_veto` — `opaque_blaming_error_code`):** Rendered error strings match `/(error\s*\d{3}|ERR_[A-Z_]+|invalid input|illegal value|an error occurred)/i` or omit plain-language domain cause and actionable recovery.
5. **`veto-05` (`conditional_block` — `unexplained_disabled_submit_gate`):** Primary `<button type="submit" disabled={...}>` renders with no adjacent visible prerequisite explanation or `aria-describedby` guidance.

### Pass 2 — Hard Filters (`flt-01`..`flt-05`)
Evaluate each required/disqualifier gate strictly as `PASS` or `FAIL`:
- **`flt-01` (`input_preservation_on_validation_error`):** 100% of entered values retained across failed client/server validation.
- **`flt-02` (`touch_and_pointer_target_floor`):** Mobile controls `>=44x44 CSS px` (`>=8px` spacing); desktop web controls `>=24x24 CSS px` (WCAG 2.5.8).
- **`flt-03` (`no_premature_pre_blur_validation`):** No error text triggered on initial empty focus/blur exploration or first-pass keystrokes prior to completed `onBlur`/`onSubmit` (excluding live password checklists).
- **`flt-04` (`programmatic_error_and_status_binding`):** Invalid fields bind `aria-invalid="true"` + `aria-errormessage`/`aria-describedby`; async outcomes emit `role="status"` or `aria-live="polite"`.
- **`flt-05` (`reversible_undo_or_specific_confirmation`):** Reversible destructive mutations provide `>=5000ms` Undo; irreversible external mutations display specific affected-entity confirmation with action-verb buttons (never bare Yes/No).

### Pass 3 — High-Weight Signals (`sig-01`..`sig-07`)
Evaluate every signal against its exact threshold in `./DESIGN.md`:
- **Critical (`-10` each):** `sig-01` (`interactive_signifier_differentiation`), `sig-02` (`icon_persistent_text_labeling`), `sig-03` (`gesture_single_pointer_parity`), `sig-05` (`gulf_of_evaluation_feedback_latency`).
- **High (`-5` each):** `sig-04` (`natural_spatial_mapping_alignment`), `sig-06` (`preventive_input_constraints`).
- **Medium (`-2` each):** `sig-07` (`false_affordance_elimination`).

*Deduplication rule:* If a defect triggers both a `veto` or `hard_filter` and its corresponding signal, apply the penalty for each distinct rule ID that explicitly fails in the artifact (vetos capture catastrophic antipatterns; filters capture state-machine gates; signals measure systemic compliance).

## Scoring & Verdict Rubric

Compute the exact score `S` using the **Phase A Calibrated Rubric** (never alter weights or bounds):

- **Base Score:** `100`
- **Hard Veto Penalty:** `-35` per triggered `hard_veto` (`veto-01`..`veto-04`). Any `hard_veto >= 1` caps `S` at `49` (`S = min(S, 49)`) and forces stance `BLOCK`.
- **Hard Filter / Conditional Block Penalty:** `-15` per failed `hard_filter` (`flt-01`..`flt-05`) or triggered `conditional_block` (`veto-05`).
- **Critical Signal Penalty:** `-10` per failed `critical` signal (`sig-01`, `sig-02`, `sig-03`, `sig-05`).
- **High Signal Penalty:** `-5` per failed `high` signal (`sig-04`, `sig-06`).
- **Medium Signal Penalty:** `-2` per failed `medium` signal (`sig-07`).
- **Score Floor:** `S = max(0, S)`.

**Stance Decision Tree (evaluate in exact order):**
1. **`BLOCK`:** `hard_veto >= 1` **OR** `S < 60`.
2. **`REVISE`:** `hard_veto == 0` **AND** (`60 <= S < 82` **OR** (`conditional_block >= 1` AND `S >= 60`)).
3. **`APPROVE`:** `hard_veto == 0` **AND** `conditional_block == 0` **AND** `S >= 82`.

### Worked Calibration Examples
- **Example 1 (1 `hard_veto` only):** `100 - 35 = 65` -> capped at `49` -> **`BLOCK` (`S = 49`)**.
- **Example 2 (1 `conditional_block` only):** `100 - 15 = 85`, `hard_veto = 0`, `conditional_block = 1` -> **`REVISE` (`S = 85`)** because an unresolved conditional block forbids `APPROVE`.
- **Example 3 (2 `hard_filter` fails + 2 `critical` fails):** `100 - 30 - 20 = 50 < 60` -> **`BLOCK` (`S = 50`)**.
- **Example 4 (0 vetos, 0 filters failed, 1 `high` + 1 `medium` fail):** `100 - 5 - 2 = 93 >= 82` -> **`APPROVE` (`S = 93`)** with non-blocking recommendations.

### Mandatory Output Contract

Return every in-universe audit in this exact structure:
1. **Header Block:** `Regime`, `Score (S/100)`, `Stance (APPROVE | REVISE | BLOCK)`, and exact arithmetic breakdown (`100 - ... = S`).
2. **Triggered Vetos & Failed Filters:** Table listing `ID`, `Severity/Gate`, `Code Location / DOM Selector`, and `Mandatory Remediation`.
3. **Signal Scorecard:** Compact pass/fail table for `sig-01`..`sig-07` citing exact DOM/CSS/ARIA evidence.
4. **Minimal Compilable Patch:** Concrete JSX/TSX + CSS diff resolving every triggered `hard_veto`, `conditional_block`, and failed `hard_filter`.
5. **Counterweight Check (when in `saas_b2b_intensive`):** State whether `karri-saarinen`, `jef-raskin`, or `dieter-rams` arbitration applies per `./DESIGN.md` Section 7.

## Guardrails

- Never justify a finding with vague descriptors (`clean`, `intuitive`, `modern`, `user-centered`). State the falsifiable CSS/DOM/ARIA/state predicate and quantitative bound instead.
- Never fabricate benchmarks, URLs, DOIs, or WCAG criteria; reference only invariants documented in `./DESIGN.md`.
- Always confirm regime fit before penalizing keyboard-first or high-density telemetry workspaces.
