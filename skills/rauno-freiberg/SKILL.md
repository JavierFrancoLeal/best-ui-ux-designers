---
name: rauno-freiberg
description: Audits TSX/CSS UI code for interruptible interaction physics, compositor-only motion budgets, trigger-anchored scaling, implicit intent inference, and zero-shift local feedback. Use when reviewing SaaS, mobile capture, or AI IDE components for jank, sticky hover, layout shift, or toast spam.
license: MIT
compatibility: Designed for AgentSkills-compatible text-only and multimodal coding agents auditing HTML, CSS, Tailwind, and React/TSX codebases without runtime browser execution.
metadata:
  schema_version: "1.1.0"
  judgment_schema: "./DESIGN.md"
  suite_id: "ui-ux"
  barbell_pole: "convex_frontier"
  primary_regimes: "saas_b2b_intensive,mobile_consumer_capture"
  author: "best-ui-ux-designers"
---

# Rauno Freiberg — Interaction Physics & Web Craft Auditor

Audit HTML, CSS, Tailwind, and React/TSX UI components against deterministic interaction-physics, compositor-budget, ergonomic, and zero-shift invariants defined in `./DESIGN.md`.

## When To Use

Activate this skill when auditing or refactoring interactive web/mobile components inside:
- **`saas_b2b_intensive` (Primary):** Popovers, cascading menus, command palettes, lists, copy feedback, focus indicators, and hover/pointer ergonomics on desktop web apps.
- **`mobile_consumer_capture` (Primary):** Gesture-driven bottom sheets, drawers, rubber-banding, touch target geometry (`>=44x44 CSS px`), and iOS Safari input ergonomics (`font-size >= 16px`).
- **`ai_native_desktop_ide` (Secondary):** Run the full audit protocol with strict `0 ms` enforcement on command palettes, keyboard navigation, and streaming-adjacent controls.

## Do Not Use When

Stop full motion-physics scoring and immediately emit `posture: "HANDOFF"` with the designated counterweight slug when the surface falls outside this universe:
- **`analytics_dense_telemetry`:** Flag the regime mismatch, keep only static hygiene (`tabular-nums`, zero hover `font-weight` shift, `:focus-visible`), prohibit spring interpolation and backdrop blur on live numeric views (`>=12` series or `>=1 Hz`), and hand off primary evaluation to `edward-tufte`.
- **`landing_onboarding_conversion`:** Flag the regime mismatch, reject adding `'use client'` physics runtimes (full `motion` estimated at ~30–34 kB gzipped in third-party benchmarks vs. `0 kB` CSS) or entrance choreography that delays LCP/first-action, and hand off primary evaluation to `luke-wroblewski`.

## Required Inputs

Collect or inspect the following text-verifiable artifacts before scoring (no browser runtime or visual screenshot required):
1. **Target regime & surface context:** Confirm whether the component serves `saas_b2b_intensive`, `mobile_consumer_capture`, `ai_native_desktop_ide`, or an out-of-universe regime.
2. **Component & stylesheet source:** HTML, JSX/TSX, CSS, and Tailwind classes covering transitions, `@keyframes`, `transform-origin`, `backdrop-filter`, `:hover`, `:focus-visible`, and `prefers-reduced-motion`.
3. **Pointer & keyboard handlers:** `onClick`/`onMouseDown`, `pointermove`/`touchmove` drag logic, `toast()` invocations, submenu hover handlers, and hit-box dimensions.

## Execution & Audit Workflow

Execute these steps sequentially over the target CSS, Tailwind, and TSX files using static text/AST inspection:

1. **Scope & Regime Gate:** Classify the target surface against `When To Use` and `Do Not Use When`. If out-of-universe, halt scoring and emit `HANDOFF` naming `edward-tufte` or `luke-wroblewski`.
2. **Check Hard Vetos (`veto-01`..`veto-03`):**
   - `veto-01` (`hard_veto`): Flag `transition: all`, `transition-all`, or interactive animations targeting `height`, `width`, `top`, `left`, `right`, `bottom`, `margin`, `padding`, or `box-shadow` (exempting `visualViewport` keyboard height compensation).
   - `veto-02` (`hard_veto`): Flag `@keyframes` / `animation:` driving interactive open/close state changes on popovers, menus, drawers, or toasts; flag `scale(0)` / `scale-0` reveals; flag anchored popovers missing trigger-relative `transform-origin`.
   - `veto-03` (`hard_veto`): Flag spatial transforms/animations lacking `@media (prefers-reduced-motion: reduce)` / `useReducedMotion`, or touch-reachable `:hover` rules unwrapped from `@media (hover: hover) and (pointer: fine)`.
3. **Check Conditional Blocks (`veto-04`, `veto-05`):**
   - `veto-04` (`conditional_block`): Flag `duration > 0 ms` on `Cmd+K` launchers, keyboard list selection, or `>100/day` actions; flag `toast(` invocations inside synchronous local handlers (such as `navigator.clipboard.writeText`); flag `pointermove` / `touchmove` handlers updating React state or inherited `--*` CSS custom properties on containers with `>10` children.
   - `veto-05` (`conditional_block`): Flag animated `blur()` radii `>20 px`; flag `:hover` / `[aria-selected]` / `[data-active]` `font-weight` mutations lacking an invisible `::after { content: attr(data-text); }` bold width reservation; flag nested hover `[role="menu"]` submenus lacking safe-triangle protection (`atan2` 15-degree buffer or dynamic `clip-path: polygon`).
4. **Evaluate Hard Filters (`flt-01`..`flt-05`):**
   - `flt-01` (`compositor_only_and_zero_layout_thrash`): Pass only if interactive animations ban `transition: all`, exclude layout/paint properties (`height`, `width`, `top`, `left`, `right`, `bottom`, `margin`, `padding`, `box-shadow`), and avoid inherited `--*` drag writes.
   - `flt-02` (`reduced_motion_accessibility_parity`): Pass only if every spatial motion rule has a reduced-motion fallback preserving functional state transitions.
   - `flt-03` (`interruptibility_on_rapid_retrigger`): Pass only if transitions use cancelable CSS transitions (`@starting-style`) or velocity-preserving springs without input locking.
   - `flt-04` (`zero_motion_high_frequency_disqualifier`): Fail if `duration > 0 ms` appears on `>100/day` actions, keyboard navigation, command palettes, or subsequent peer tooltips.
   - `flt-05` (`focus_visible_and_target_geometry_gate`): Pass only if focus indicators use `:focus-visible` (`>=3:1` contrast, respecting border-radius), hit targets meet `>=24×24 CSS px` desktop / `>=44×44 CSS px` mobile, and mobile `<input>` font sizes are `>=16 px`.
5. **Evaluate Weighted Signals (`sig-01`..`sig-07`):**
   - `critical`: `sig-01` (`non_composited_transition_count`), `sig-02` (`blocking_keyframe_interactive_triggers`), `sig-03` (`high_frequency_action_motion_ms`).
   - `high`: `sig-04` (`popover_origin_and_scale_floor`), `sig-05` (`dynamic_blur_radius_px`), `sig-06` (`state_change_layout_shift_triggers`).
   - `medium`: `sig-07` (`touch_pointer_ergonomic_guards`).
6. **Compute Calibrated Score & Emit Exact Remediations:** Apply the Phase A Calibrated Rubric below and output `file:line`, rule ID, deterministic cause, and exact CSS/TSX replacement patches following `./DESIGN.md` Section 5.

## Verdict & Severity Criteria

Start every in-universe audit at base score `100` and apply deductions cumulatively (Phase A Calibrated Rubric — Immutable):

| Category | Penalty | Additional Constraint |
| :--- | :--- | :--- |
| Base Score | `100` | Starting value |
| Triggered `hard_veto` (`veto-01`..`veto-03`) | `-35` each | Caps maximum score `S` at `49` and forces posture `BLOCK` |
| Failed `hard_filter` (`flt-01`..`flt-05`) or unresolved `conditional_block` (`veto-04`, `veto-05`) | `-15` each | Unresolved `conditional_block` prevents `APPROVE` |
| Failed `critical` signal (`sig-01`..`sig-03`) | `-10` each | Direct deduction |
| Failed `high` signal (`sig-04`..`sig-06`) | `-5` each | Direct deduction |
| Failed `medium` signal (`sig-07`) | `-2` each | Direct deduction |
| Minimum Score Floor | `0` | `S = max(0, min(cap, 100 - total_deductions))` where `cap = 49` if `hard_veto_count > 0` else `100` |

### Posture Mapping

- **`APPROVE`:** `hard_veto_count == 0` AND `conditional_block_count == 0` AND `S >= 82`.
- **`REVISE`:** `hard_veto_count == 0` AND (`60 <= S < 82` OR (`conditional_block_count > 0` AND `S >= 60`)).
- **`BLOCK`:** `hard_veto_count > 0` OR `S < 60`.

### Required Output Format & Worked Example

Return a compact structured report containing:
1. **Verdict Header:** `regime`, `in_universe` (`true` | `false`), `score` (`0–100` or `N/A` if out-of-universe), `posture` (`APPROVE` | `REVISE` | `BLOCK` | `HANDOFF`), and `counterweight_handoff` (when applicable).
2. **Score Calculation Trace:** Explicit arithmetic showing base `100`, every triggered ID with its exact deduction, cap applied (`49` if any `hard_veto`), and final `S`.
3. **Findings Table (`file:line`):** Ordered by severity (`hard_veto` -> `conditional_block` -> `hard_filter` -> `critical` -> `high` -> `medium`), each with the exact deterministic detection evidence and minimal code remediation.

*Worked Scoring Example:* An AI IDE context menu uses compositor transitions, `@starting-style`, trigger-bound `transform-origin`, `scale(0.96)`, `:focus-visible`, `@media (hover: hover) and (pointer: fine)`, and `prefers-reduced-motion`, **except** it animates `backdrop-filter: blur(28px)` and omits a safe-triangle prediction cone on its nested hover submenu: `veto-05` (`-15`) + `sig-05` (`-5`) -> `100 - 15 - 5 = 80` -> **`REVISE`**.

## Guardrails

- **Bundle Budget Escalation (`dieter-rams`):** If fixing an animation proposes importing full `motion` (estimated at `~30–34 kB` gzipped) or adding `'use client'` to a Server Component shell where CSS `@starting-style` (`0 kB`) or initial `LazyMotion` (`~5 kB`) works, block the heavy dependency and prefer pure CSS.
- **Daily Keyboard Velocity Escalation (`karri-saarinen`):** If a prompt asks to "add subtle spring animations to `Cmd+K` search results," reject the request under `flt-04` and enforce `0 ms` transitions.
- **Virtual Keyboard Height Exception (`Vaul`):** Dynamic `height`/`bottom` adjustment driven strictly by `window.visualViewport` resize events (`>60 px` delta) when a mobile software keyboard opens inside a drawer is exempt from `veto-01`; continuous pointer dragging must still use `translate3d`.
- **Zero Subjective Clichés:** Never justify interaction verdicts with banned filler adjectives (`clean`, `intuitive`, `modern`, `user-centered`); state exact CSS properties, compositor budgets, pixel/ms thresholds, and DOM/ARIA predicates from `./DESIGN.md`.
