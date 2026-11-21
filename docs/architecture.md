# Architecture Blueprint — `best-ui-ux-designers` (Phase A + Solow Thesis + SDLC Map)

`best-ui-ux-designers` is **Suite #1 of 5** under `ECOSYSTEM_CONTRACT v1.0.0` (`suite_id: ui-ux`, `director_slug: design-director`, `judgment_file: DESIGN.md`). It packages falsifiable UI/UX engineering judgment into an adversarial, non-consensual multi-agent committee portable across `Google Antigravity`, `DeepSeek Harness`, `Claude Code`, `OpenAI Codex / ChatGPT`, `Cursor`, and `Windsurf / Devin Desktop`.

---

## 1. Economic Thesis: The Solow Productivity Paradox (Paul A. David, 1990)

In *"The Dynamo and the Computer: An Historical Perspective on the Modern Productivity Paradox"* (*American Economic Review*, 1990), Paul A. David demonstrated that General Purpose Technologies (GPTs) fail to lift Total Factor Productivity ($A$) during their initial adoption phase because organizations substitute the new power source directly into legacy physical layouts:

1. **Phase 1 — Central Dynamo / Direct Substitution (`BOLT_ON_CAPITAL_K`, 1880–1910):** Bolting an electric dynamo onto legacy steam shafts and belts increased capital expenditure ($K$) while preserving factory friction. In contemporary software, bolting a floating *"Ask AI"* sparkle trigger, disconnected chat sidebar, or prose-only modal onto an unmodified CRUD form, SaaS table, or IDE increases token/compute spend ($K$) while leaving Total Factor Productivity ($A$) flat—inducing chat fatigue, *Accordion Editing*, and manual copy-paste *Apple Picking* (NN/g 2024; Zamfirescu-Pereira et al., CHI 2023).
2. **Phase 2 — Unit-Drive Motors / Factory Floor Redesign (`UNIT_DRIVE_TFP_A`, 1920s):** Productivity surged only after fractional-horsepower electric motors were embedded directly into each machine tool, eliminating central shafts and reorganizing material flow. In software, voluntary adoption multiplies 2×–3× (Windsurf Cascade, Cursor Fast Apply, Linear Sync Engine, Raycast, Stripe Payment Element, and DirectGPT CHI 2024: 50% faster task completion, 50% fewer prompts, 72% shorter prompts) when AI acts as distributed unit-drive primitives bound to live workspace state: implicit context capture, sub-second inline structured diffs, direct manipulation over finite controls, and atomic `Cmd/Ctrl+Z` rollback, grounded in Lindy biological and cognitive invariants.

Every AI-bearing artifact audited by `best-ui-ux-designers` is classified into one of four `solow_stage` values (`BOLT_ON_CAPITAL_K`, `TRANSITIONAL_HYBRID`, `UNIT_DRIVE_TFP_A`, or `NOT_APPLICABLE`) and evaluated unconditionally against `aud-slop-04` (`veto-central-dynamo`).

---

## 2. Core Architectural Primitives & Epistemic Boundaries

Two epistemic rules govern the entire suite:
- **Explicit Source Attribution:** Commercial adoption figures cited in Phase A benchmarks (such as Cursor annualized revenue, Windsurf adoption milestones, or third-party Linear vs. Jira latency measurements) are explicitly attributed to vendor releases, financial press, or empirical UX studies rather than independent academic audits.
- **Deterministic Text-Only Verifiability:** Coding agents operating without visual rendering (e.g., text-only LLM harnesses) cannot reliably grade subjective pictorial aesthetics. Every signal, hard filter, veto, and heuristic in this repository is therefore defined as a falsifiable predicate verifiable over source code, AST, DOM, CSS, KLM-GOMS operator chains, or finite state machines.

### Four Executable Primitive Families
1. **Perceived Latency Ladder:** `<= 16.6 ms` frame budget (`<= 10 ms` JS in Google RAIL), `<= 50 ms` input dispatch / local-first optimistic write, `<= 100 ms` visual acknowledgment (Nielsen 1993 / RAIL), `<= 200 ms` INP p75 (`> 500 ms` hard failure in Core Web Vitals), `<= 400 ms` practical flow-continuity target (operationalizing Doherty & Thadhani 1982 sub-second step changes), `> 1,000 ms` thought-flow break, `> 10,000 ms` attention collapse.
2. **Context Continuity & Modelessness:** KLM-GOMS constants (`K = 0.20 s`, `B = 0.10 s`, `H = 0.40 s`, `P = 1.10 s`, `M = 1.35 s`) quantify mouse-menu penalties (`5.50 s` vs. `1.75 s` shortcut = `3.14x`). Hidden persistent modes are replaced by spring-loaded quasimodes, composable `Cmd+K` palettes, and spatially co-located inline diffs.
3. **Chat-Fatigue Prevention:** Open free-text prompts are reserved for open-ended synthesis; localized edits, filtering, sorting, and finite parameter tuning must use direct manipulation or deterministic controls.
4. **Agentic Trust Ergonomics (HCAI):** High Human Control + High Automation (Shneiderman 2020/2022) implemented via live execution trajectory visibility, risk-tiered approval checkpoints on scoped diffs, and one-step atomic rollback (`Cmd/Ctrl+Z`).

---

## 3. SDLC Post-AI Integration (6 Stages)

`best-ui-ux-designers` operates in **two calibrated execution modes** across all six essential SDLC stages to preserve high throughput without sacrificing structural vetoes:

| SDLC Stage | Execution Mode | Active Components | Escalation Trigger |
|---|---|---|---|
| **1. Plan** | **Architecture Mode** | Full `design-director` (Solow diagnosis + 4 active Barbell designers + dialectical rebuttal + 4 auditors + `verdict_envelope`) | Mandatory when defining product regime, interaction topology, or new AI surfaces |
| **2. Design** | **Architecture Mode** | Full `design-director` on wireframes, component specs, state machines, and design-token contracts | Mandatory before locking component contracts or agentic workflows |
| **3. Build** | **Fast PR Gate Mode** | 4 Via Negativa auditors on incremental TSX/JSX/CSS/Vue/Svelte PR diffs | Escalate to full `design-director` on any `hard_veto`, new AI surface, or regime shift |
| **4. Test** | **Fast PR Gate Mode** | 4 Via Negativa auditors + deterministic UI Stack / WCAG / KLM verification; escalate missing behavioral tests to `verification-eval` | Escalate to full `design-director` on `hard_veto` or regression across state matrix |
| **5. Deploy** | **Fast PR Gate Mode** | Pre-release circuit breaker checking `V_hard == 0` and clean `verdict_envelope` | Block deployment on `REJECT` (`V_hard >= 1` or `Q_total < 60`) |
| **6. Maintain** | **Fast PR Gate Mode** | Regression gate on UI refactors, latency drift, or bolt-on AI additions | Escalate to `design-director` (and `systems-harness` for backend latency/duplication) on persistent regressions |

---

## 4. Barbell Roster, Dialectical Tension Matrix & Regime Routing

The 12-designer roster enforces a strict **50/50 Barbell split** (6 `lindy_anchor` + 6 `convex_frontier`, zero bureaucratic middle). Deliberate philosophical conflicts are resolved quantitatively by regime rather than consensus averaging:

| Dialectical Axis | Pole A | Pole B | Design Director Arbitration Rule |
|---|---|---|---|
| **Multivariate Density vs. Radical Subtraction** | `edward-tufte` (small multiples, sparklines in one eyespan) | `dieter-rams` (suppress every secondary element) | In `R4` (`analytics_dense_telemetry`) Tufte leads while preserving Rams anti-junk hygiene; in `R5` (`landing_onboarding_conversion`) Rams leads and Tufte is `OUT_OF_UNIVERSE`. |
| **Keyboard-First Velocity vs. Explicit Discoverability** | `karri-saarinen` / `jef-raskin` (minimize chrome, single-key & `Cmd+K` for `>100/day`) | `don-norman` / `susan-kare` (visible signifiers & labeled icons without memorization) | In `R2` (`saas_b2b_intensive`) Saarinen & Raskin prevail (with inline `<kbd>` hints); in `R3` and `R5` Norman & Kare prevail. |
| **Agentic Flow Autonomy vs. Strict Human Control** | `agentic-flow-architect` (multi-file diffs, terminal & test chaining) | `ben-shneiderman` / `jef-raskin` (continuous visibility, approval checkpoints, instant Undo) | Coupled in `R1` (`0.35` vs. `0.25`): multi-step autonomy is permitted only with pre-turn checkpoints, visible trajectory, and atomic rollback. |
| **Live Simulation & Physics vs. Zero Motor Distraction** | `bret-victor` / `rauno-freiberg` (interruptible physics & live state projections) | `dieter-rams` / `karri-saarinen` (`0 ms` motion on `>100/day` actions, neutral surfaces) | Daily frequency arbitrates: actions `>100x/day` (`Cmd+K`, list navigation) = `0 ms`; parameter exploration or touch gestures = continuous `<= 200 ms` response. |
| **Linear Mobile Funnel vs. High-Ceiling Systematization** | `luke-wroblewski` (`<=14` form elements, thumb-zone single-column funnel) | `rasmus-andersson` (high-precision composable typographic/grid primitives) | `R3` and `R5` prioritize Wroblewski (`<=12–14` critical form elements); `R4` prioritizes Andersson for optical typography and `tabular-nums`. |

### Regime Weight Matrix (`committee/design-director/routing-matrix.yaml`)
- **R1 `ai_native_desktop_ide`:** `agentic-flow-architect` (`0.35`), `ben-shneiderman` (`0.25`), `jef-raskin` (`0.20`), `bret-victor` (`0.20`) — 45% Lindy / 55% Convex.
- **R2 `saas_b2b_intensive`:** `karri-saarinen` (`0.35`), `rauno-freiberg` (`0.25`), `jef-raskin` (`0.20`), `dieter-rams` (`0.20`) — 40% Lindy / 60% Convex.
- **R3 `mobile_consumer_capture`:** `luke-wroblewski` (`0.35`), `don-norman` (`0.25`), `susan-kare` (`0.20`), `rauno-freiberg` (`0.20`) — 45% Lindy / 55% Convex.
- **R4 `analytics_dense_telemetry`:** `edward-tufte` (`0.35`), `ben-shneiderman` (`0.25`), `rasmus-andersson` (`0.25`), `bret-victor` (`0.15`) — 60% Lindy / 40% Convex.
- **R5 `landing_onboarding_conversion`:** `luke-wroblewski` (`0.35`), `dieter-rams` (`0.30`), `don-norman` (`0.20`), `rasmus-andersson` (`0.15`) — 50% Lindy / 50% Convex.
- **Embedded AI Cross-Cutting Override (`R2`–`R5`):** Injects `agentic-flow-architect: 0.15` and multiplies base weights by `0.85` (exact sum `1.00`).

---

## 5. Five-Step Adversarial Deliberation Protocol

1. **Step 1 — Ingest, Regime Classification & Solow Diagnosis:** Validate minimum observables (declare `MISSING_DATA` if absent), classify `R1`–`R5`, evaluate the 15% embedded AI override, silence all `OUT_OF_UNIVERSE` profiles, and assign `solow_stage`.
2. **Step 2 — Isolated Parallel Evaluation:** Each active designer scores the artifact independently (`S_i` in `[0, 100]`) using the immutable Phase A Calibrated Rubric (`Base 100`, `-35` per `hard_veto` with `cap = 49`, `-15` per failed `hard_filter` or unresolved `conditional_block`, `-10` critical, `-5` high, `-2` medium, floor `0`).
3. **Step 3 — Dialectical Rebuttal:** Evaluate active `debate_triggers` between panel members and record quantitative regime arbitration.
4. **Step 4 — Unconditional Via Negativa Circuit Breaker:** Run all 4 functional auditors (`auditor-cognitive-fatigue`, `auditor-latency-broken-states`, `auditor-physics-accessibility`, `auditor-agentic-anti-slop`). Any `hard_veto` (`V_hard >= 1`) overrides high designer scores.
5. **Step 5 — Weighted Synthesis, Patch Plan & Verdict Envelope:** Compute `Q_total = sum(w_{r,i} * S_i)` and emit:
   - **`REJECT`:** `V_hard >= 1` OR `Q_total < 60`
   - **`ITERATE`:** `V_hard == 0` AND (`60 <= Q_total < 82` OR `V_cond >= 1`)
   - **`SHIP`:** `V_hard == 0` AND `V_cond == 0` AND `Q_total >= 82`
   Terminate with the parseable `verdict_envelope` v1.0.0 YAML block and populate `escalation_to_suites` per `suite.yaml` when defects cross into `verification-eval`, `systems-harness`, `security-governance`, or `spec-context`.
