---
name: jef-raskin
description: "Audits and refactors AI-native desktop IDEs and intensive B2B SaaS interfaces using Jef Raskin's cognetics: eliminating hidden modes, blocking confirmations, manual save data loss, and KLM-GOMS homing overhead. Triggers on desktop/SaaS workflow audits, state machines, shortcuts, and draft persistence."
license: MIT
compatibility: Text-only engineering agents auditing React, TypeScript, Electron, DOM, CSS, or finite state machines; requires reading ./DESIGN.md in the same directory.
metadata:
  schema_version: "1.1.0"
  judgment_schema: "./DESIGN.md"
  suite_id: "ui-ux"
  barbell_pole: "lindy_anchor"
  primary_regimes: "ai_native_desktop_ide,saas_b2b_intensive"
  author: "best-ui-ux-designers"
---

# Jef Raskin — Cognetics, Modelessness & KLM-GOMS Audit Skill

Operationalizes Jef Raskin's engineering invariants from `./DESIGN.md` for text-only code, DOM, CSS, and state-machine audits. Read `./DESIGN.md` before scoring or refactoring any interface artifact.

## When To Use

Activate this skill when the user requests UI/UX code review, interaction architecture, state-machine auditing, or JSX/TSX refactoring for:

* **`ai_native_desktop_ide`:** Code editors, IDE extensions, Electron desktop apps, AI coding composers (`Plan`/`Ask`/`Edit`/`Agent` dispatch), command palettes, diff checkpoints, or keyboard-driven navigation loops.
* **`saas_b2b_intensive`:** High-frequency operational desktop web apps (ticketing, CRM, ERP, claims/triage editors, data tables) where keyboard operators process repetitive daily workflows (`>=20` unit tasks/day).
* **Targeted Raskin defects:** Hidden persistent modes, blocking `"Are you sure?"` modals on reversible operations, manual `"Save"` buttons with draft loss on reload/network failure, excessive mouse-keyboard shuttling (`H` and `P` operators), nested submenus, or unlabeled domain icons.

## Do Not Use When

Decline activation and route to the appropriate counterweight skill in the following out-of-universe regimes:

* **`mobile_consumer_capture`:** Touch-first smartphones, `<768px` viewports, `pointer: coarse` input, or one-handed thumb flows -> route to `luke-wroblewski`.
* **`analytics_dense_telemetry`:** Read-heavy SRE monitoring walls, multi-series visual anomaly scanning, or high-density static/interactive data graphics (`read:write > 10:1`) -> route to `edward-tufte` and `ben-shneiderman`.
* **`landing_onboarding_conversion`:** First-time marketing pages, checkout funnels, or novice walk-up conversion flows lacking prior motor habituation -> route to `don-norman` and `luke-wroblewski`.
* **Irreversible external safety boundaries:** Production database drops, financial transfers, or permanent repository destruction -> apply `don-norman` hard forcing functions (interlocks/lockouts) instead of zero-friction Undo.
* **Long-running async multi-agent orchestration:** Background agent tool loops lasting `>10s` -> combine Raskin quasimodal dispatch with `agentic-flow-architect`.

## Required Inputs

Collect at least one text-verifiable engineering artifact before executing the audit:

1. **Source artifact:** React/TSX/Electron component code, DOM markup, CSS, keyboard shortcut registry, or state-machine specification.
2. **Regime & hardware context:** Target product regime (`ai_native_desktop_ide` or `saas_b2b_intensive`), primary input modality (confirm physical keyboard + fine pointer), and daily task frequency.
3. **Mutation reversibility classification:** Whether target delete/edit/dispatch actions are locally reversible (soft-delete, undo stack, git checkpoint) or externally irreversible.

If hardware modality or reversibility is unspecified, state the assumption explicitly before calculating scores.

## Execution & Audit Workflow

Execute these six deterministic steps in exact order, cross-referencing IDs in `./DESIGN.md`:

1. **Verify Regime Gate:** Confirm the artifact belongs to `ai_native_desktop_ide` or `saas_b2b_intensive` with physical keyboard input. If it falls into an out-of-universe regime, stop scoring, emit `OUT_OF_UNIVERSE`, and specify the exact counterweight slug(s).
2. **Run Hard Filter & Mode-Matrix Check (`flt-01..flt-05`, `sig-01`):**
   * Enumerate all primary keyboard/pointer gestures (`Enter`, `Backspace`, `Delete`, `Tab`, primary click) against persistent component states.
   * Flag `veto-01` if any persistent off-locus mode flag alters `Enter` between read-only analysis and file/data mutation without a spring-loaded quasimode or spatial separation.
   * Flag `veto-04` if a B2B editor locks fields behind an explicit `Edit` toggle + manual `Save` button without pessimistic concurrent locking.
3. **Audit Work Preservation (`sig-02`, `veto-02`):**
   * Inspect every editable buffer (`>16` chars). Verify durable write-through (`localStorage`, `IndexedDB`, or disk journal within `<=500 ms`), mount hydration, and text survival across simulated reload and `401`/`5xx` failure.
4. **Audit Blocking Confirmations & Reversibility (`sig-03`, `veto-03`):**
   * Inspect all `window.confirm`, `alert`, `<dialog>`, and `role="alertdialog"` triggers.
   * For every locally reversible mutation, flag `veto-03` and require immediate execution + universal `Cmd/Ctrl+Z` Undo + non-blocking `role="status"` Undo toast (`>=8s`).
   * For externally irreversible actions, verify a Norman forcing function (e.g., typing resource identifier) rather than a habituated generic `"Confirm"` click.
5. **Compute KLM-GOMS, Hick & Label Diagnostics (`sig-04..sig-06`, `veto-05`, `heur-04..heur-10`):**
   * Write the exact KLM-GOMS operator sequence for each frequent unit task using `K=0.20s`, `P=1.10s`, `H=0.40s`, `M=1.35s`, and `R(t)` (applying Card-Moran-Newell M-placement Rules 0–2).
   * Flag `H > 0` round-trips in daily keyboard loops, submenu depth `>=2` without incremental search (`<=250 ms`), adaptive menu reordering, duplicate competing shortcuts, sticky verb-noun tool modes, beginner/expert mode splits, and unlabeled domain-specific icons.
6. **Produce Deterministic Output & Refactored Code:**
   * Emit the structured audit scorecard (triggered IDs, KLM Before/After operator equations and exact seconds saved, final numeric score, and verdict).
   * Provide compilable TSX/code remediation eliminating every triggered veto and conditional block.

## Verdict & Severity Criteria

Start every in-universe audit at **`100` points** and apply the immutable Phase A Calibrated Rubric deterministically:

| Finding Class | Penalty | Cap / Constraint |
| :--- | :--- | :--- |
| **`hard_veto`** (`veto-01`, `veto-02`, `veto-03`) | **`-35`** each | If `>= 1` `hard_veto` triggers, final score is **capped at `49`** (`cap = 49`) and forces stance `BLOCK`. |
| **Failed `hard_filter` (`flt-01`..`flt-05`) or unresolved `conditional_block` (`veto-04`, `veto-05`)** | **`-15`** each | Any unresolved `conditional_block` prevents `APPROVE` (forces `REVISE` when `S >= 60`). |
| **Failed `critical` signal (`sig-01`..`sig-03`)** | **`-10`** each | Direct deduction per failed critical signal. |
| **Failed `high` signal (`sig-04`, `sig-05`)** | **`-5`** each | Direct deduction per failed high signal. |
| **Failed `medium` signal (`sig-06`)** | **`-2`** each | Applied for unlabeled domain icons or non-monotonic shortcut drift. |

* **Floor & Cap:** `S = max(0, min(cap, 100 - total_deductions))` where `cap = 49` if `hard_veto >= 1` else `100`.
* **Verdict Thresholds:**
  * **`APPROVE`:** `hard_veto == 0` AND `conditional_block == 0` AND `S >= 82`.
  * **`REVISE`:** `hard_veto == 0` AND (`60 <= S < 82` OR (`conditional_block > 0` AND `S >= 60`)).
  * **`BLOCK`:** `hard_veto >= 1` OR `S < 60`.

## Guardrails

* **Zero subjective clichés:** Never justify a finding using banned vague adjectives (`clean`, `intuitive`, `modern`, `user-centered`). Every finding must cite an exact AST/DOM/CSS predicate, state transition, or KLM-GOMS/Fitts/Hick bound from `./DESIGN.md`.
* **No fabricated benchmarks:** Never invent telemetry numbers, patents, or user-study statistics. Use strictly the verified KLM-GOMS constants (`K=0.20s`, `P=1.10s`, `H=0.40s`, `M=1.35s`), Fitts (`50 + 150 log2(D/S + 1) ms`), and verified sources in `./DESIGN.md`.
* **No silent scope creep:** Respect all three mandatory out-of-universe boundaries and escalate blind spots (`bs-01..bs-04`) to their designated roster counterweights rather than forcing keyboard purism where it harms operators.
