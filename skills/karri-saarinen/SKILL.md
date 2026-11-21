---
name: karri-saarinen
description: Audits and refactors desktop B2B SaaS and AI-native IDE interfaces using Karri Saarinen's local-first sub-100ms velocity, keyboard-first KLM efficiency, opinionated defaults, and LCH tonal craft rubric. Applies to code reviews, state models, and UI specs; excludes mobile capture, telemetry, and landing pages.
license: MIT
compatibility: Requires read access to frontend source code (React/TSX/CSS), state/sync modules, or UI specifications; fully compatible with text-only coding agents without visual rendering tools.
metadata:
  schema_version: "1.0.0"
  design_schema: "./DESIGN.md"
  barbell_pole: "convex_frontier"
  primary_regimes: "saas_b2b_intensive"
  author: "best-ui-ux-designers"
---

# Karri Saarinen Audit & Refactoring Skill

This skill executes deterministic code, DOM, CSS, and state-machine audits modeled on Karri Saarinen's engineering and visual craft invariants (Linear, Airbnb DLS, Coinbase). It optimizes for `<= 50 ms` local-first daily mutations, keyboard-first Keystroke-Level Model (KLM) velocity, opinionated Via Negativa defaults, programmatic LCH/OKLCH tonal layering, and `0 ms` motion on high-frequency surfaces.

For full canonical definitions, verified primary sources, adversarial debate arbitration rules, and full TSX reference implementations, read `./DESIGN.md` before issuing a `BLOCK` or proposing multi-file architectural refactors.

## When To Use

Invoke this skill when auditing or refactoring:
- High-frequency desktop B2B SaaS workspaces (`saas_b2b_intensive`): issue trackers, CRMs, sprint/cycle planners, triage inboxes, code-review queues, collaborative editors, internal operational consoles.
- AI-native desktop workspaces and IDEs (`ai_native_desktop_ide`): agent orchestration boards, diff review surfaces, coding session managers, and command-palette-driven developer tools.

## Do Not Use When

Do NOT invoke this skill (refuse and route out-of-universe) for:
- `mobile_consumer_capture`: Smartphones or coarse-pointer touch apps (`viewport < 768px`, one-handed thumb ergonomics, camera/receipt capture). Route to `luke-wroblewski`.
- `analytics_dense_telemetry`: Real-time APM/Kubernetes observability dashboards, BI charts, multivariate small-multiples, or OLAP slicing interfaces. Route to `edward-tufte`.
- `landing_onboarding_conversion`: Public marketing landing pages, pricing tables, checkout funnels, or one-time consumer onboarding flows. Route to `luke-wroblewski` or `don-norman`.
- **Cold-start / regulated enterprise exceptions:** If the target cohort uses the app `< 3` times/month or regulatory law mandates `>= 3` audit-verified custom fields with multi-party sign-off interlocks, invoke `don-norman` or `ben-shneiderman` alongside `./DESIGN.md` Section 7 arbitration rules.

## Required Inputs

Collect or inspect the following text-verifiable artifacts before scoring:
1. **Frontend source code:** React/TSX/JSX components, entity creation modals, command palettes (`Cmd+K`), and contextual menus.
2. **State & sync layer:** Client store mutations, IndexedDB/SQLite persistence hooks, optimistic rollback handlers, and global `keydown` listeners.
3. **Styles & tokens:** CSS/Tailwind/StyleX declarations, border widths, dark-mode elevation tokens, and transition/animation durations.
4. **Regime & task frequency profile:** Target viewport, pointer modality (`fine` vs. `coarse`), daily action frequency (`>= 100x/day` vs. infrequent), and regulatory field requirements.

## Audit & Design Workflow

Execute all five phases sequentially without relying on screenshots or subjective aesthetic adjectives:

### Phase 1: Regime & Boundary Check
1. Identify the target interface's primary viewport, pointer modality (`fine` vs. `coarse`), daily user action frequency, and regulatory schema constraints.
2. If the artifact matches any `out_of_universe_regimes` entry (`mobile_consumer_capture`, `analytics_dense_telemetry`, `landing_onboarding_conversion`), stop scoring immediately, output `OUT_OF_UNIVERSE`, state the falsifiable structural mismatch, and name the counterweight slug (`luke-wroblewski`, `edward-tufte`, `don-norman`, or `ben-shneiderman`).

### Phase 2: Hard Filters & Veto Triggers Evaluation
Inspect the submitted TSX/JSX, state store, sync layer, and CSS/tokens against every gate and veto defined in `./DESIGN.md`:

- **Hard Filters (`-15` pts each if failed):**
  - `flt-01` (`required`): Optimistic mutations capture prior snapshots, persist durably (IndexedDB/SQLite) with idempotency or monotonic sync IDs, and execute deterministic rollback on server rejection.
  - `flt-02` (`required`): Cached view navigation paints in `<= 100 ms` with `0` blocking spinners or full-page skeleton loaders.
  - `flt-03` (`required`): Single-key global listeners abort when `document.activeElement` is `INPUT`, `TEXTAREA`, `SELECT`, `[contenteditable="true"]`, or when `event.isComposing === true`.
  - `flt-04` (`required`): Zero dynamic component `<style>` rule injection during dense list navigation (build-time atomic CSS or static tokenized CSS).
  - `flt-05` (`disqualifier`): Fails if primary creation or status paths dynamically enforce `> 3` admin-configured custom mandatory fields before local commit.

- **Veto Triggers:**
  - `veto-01` (`hard_veto`, `-35` pts, caps score `<= 49`, forces `BLOCK`): Daily CRUD handler awaits network I/O (`await fetch/mutateAsync`) before updating local store or locks controls with a spinner.
  - `veto-02` (`hard_veto`, `-35` pts, caps score `<= 49`, forces `BLOCK`): Primary entity creation modal requires `> 1` un-defaulted mandatory field, `> 1` step, lacks title `autoFocus`, or lacks single-key trigger (`C`) + `Cmd/Ctrl+Enter` commit.
  - `veto-03` (`hard_veto`, `-35` pts, caps score `<= 49`, forces `BLOCK`): `transition-duration > 0ms`, `animation-duration > 0ms`, or spring wrappers applied to `Cmd/Ctrl+K` command palettes, hotkey pickers, or high-frequency (`>= 100x/day`) list row hover/selection highlights.
  - `veto-04` (`conditional_block`, `-15` pts, prevents `APPROVE`): `>= 3` primary entity actions trapped in mouse-only toolbars without keyboard shortcuts, `< 90%` `<kbd>` hints in `[role="menuitem"]`, or nested hover submenus lacking a CSS `clip-path` triangular safe zone.
  - `veto-05` (`conditional_block`, `-15` pts, prevents `APPROVE`): Hardcoded hex/rgb/hsl literals in components, structural container `border-width > 1px`, or dark-mode elevation modeled via drop shadows instead of LCH/OKLCH lightness steps.

### Phase 3: Weighted Signal Scoring
Audit all 7 signals from `./DESIGN.md` and deduct once per failed signal:
- **Critical (`-10` pts each):** `sig-01` (`local_mutation_paint_latency`), `sig-02` (`daily_action_keyboard_coverage`), `sig-03` (`entity_creation_required_field_bloat`).
- **High (`-5` pts each):** `sig-04` (`high_frequency_motion_tax`), `sig-05` (`inline_shortcut_signifier_parity`), `sig-06` (`programmatic_lch_tonal_layering`).
- **Medium (`-2` pts each):** `sig-07` (`deterministic_agent_workbench_framing`).

### Phase 4: Mandatory Remediation Output
For every triggered veto, failed filter, or failed signal, provide:
1. Exact line/symbol/CSS selector evidence from the audited artifact.
2. KLM-GOMS or latency delta estimate (using `K=0.20s`, `P=1.10s`, `H=0.40s`, `M=1.35s`, `R=wait`).
3. Ready-to-compile TSX/CSS patch following `./DESIGN.md` Section 5 patterns (never emit abstract prose advice when a concrete code diff is possible).

## Scoring & Verdict Rubric

Compute final score `S` deterministically using the exact Phase A Calibrated Rubric (do not alter):

1. Start at **Base = `100`**.
2. Subtract **`-35`** for each triggered `hard_veto`.
3. Subtract **`-15`** for each failed `hard_filter` OR triggered `conditional_block`.
4. Subtract **`-10`** for each failed `critical` signal.
5. Subtract **`-5`** for each failed `high` signal.
6. Subtract **`-2`** for each failed `medium` signal.
7. If `count(hard_veto) > 0`, **cap `S = min(S, 49)`** and force stance **`BLOCK`**.
8. Enforce minimum floor **`S = max(0, S)`**.

**Stance Mapping:**
- **`APPROVE`**: `count(hard_veto) == 0` AND `count(conditional_block) == 0` AND `S >= 82`.
- **`REVISE`**: `count(hard_veto) == 0` AND (`60 <= S < 82` OR (`count(conditional_block) > 0` AND `S >= 60`)).
- **`BLOCK`**: `count(hard_veto) > 0` OR `S < 60`.

*Calibration sanity checks:*
- `1 hard_veto` alone -> `100 - 35 = 65` -> capped at **`49`** -> **`BLOCK`**.
- `1 conditional_block` alone -> `100 - 15 = 85` -> unresolved conditional block -> **`REVISE`**.
- `1 failed hard_filter` + `1 conditional_block` + `1 failed high signal` -> `100 - 15 - 15 - 5 = 65` -> **`REVISE`**.
- `0 vetoes`, `0 filter failures`, `1 failed high` + `1 failed medium` -> `100 - 5 - 2 = 93` -> **`APPROVE`**.

### Required Audit Output Format

Return every in-universe review using this exact structure:

```markdown
### Audit Verdict: [APPROVE | REVISE | BLOCK] (Score: XX / 100)

- **Regime Fit:** `saas_b2b_intensive` | `ai_native_desktop_ide`
- **Score Math:** `100 - [veto deductions] - [filter/cond_block deductions] - [signal deductions] = XX` (cap/floor applied if triggered)
- **Hard Vetoes Triggered:** `[list IDs or None]`
- **Conditional Blocks Triggered:** `[list IDs or None]`
- **Hard Filters Failed:** `[list IDs or None]`
- **Signals Failed:** `[list IDs with weights or None]`

#### Findings & Deterministic Evidence

| ID | Category | Evidence in Code/DOM/CSS | Exact Threshold Violated |
| :--- | :--- | :--- | :--- |

#### KLM-GOMS & Latency Impact
- **Current Estimated Cost:** `[seconds + blocking R(t)]`
- **Post-Refactor Cost:** `[seconds + <=50ms local write]`

#### Mandatory Code Remediation
[Exact compilable JSX/TSX/CSS patch]
```

## Guardrails

- **Never use vague aesthetic clichés** (`clean`, `intuitive`, `modern`, `user-centered`) anywhere in audit findings or remediation criteria; express every defect as a numeric threshold, boolean invariant, or AST/DOM/CSS predicate.
- **Apply rubric penalties faithfully and transparently:** A single architectural flaw can legitimately violate a veto (e.g., `veto-01` blocking spinner) and its corresponding measured signal (`sig-01` latency > 50 ms) — list each triggered ID transparently in the `Score Math` line so human reviewers and automated evaluators can verify exact arithmetic.
- **Check IME and editable targets explicitly:** Never approve a single-key shortcut patch (`C`, `A`, `L`, `S`, `P`, `X`) unless `flt-03` (`INPUT`/`TEXTAREA`/`SELECT`/`contenteditable`/`isComposing`) is explicitly guarded in code.
