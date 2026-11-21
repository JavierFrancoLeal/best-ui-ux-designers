---
name: edward-tufte
description: "Audits and refactors dense analytics telemetry UIs, dashboards, and React/SVG/Recharts/D3 code against Edward Tufte's quantitative invariants (Lie Factor 0.95-1.05, data-ink ratio, direct labels, sparklines, shared-scale small multiples). Use for analytical displays; hand off conversion, mobile, or IDE flows."
license: MIT
compatibility: Text-only coding agents (DeepSeek V4, Claude Code, Codex, Cursor) auditing TSX/JSX, SVG, CSS, Recharts, or D3 configs without vision tools.
metadata:
  schema_version: "1.1.0"
  judgment_schema: "./DESIGN.md"
  suite_id: "ui-ux"
  barbell_pole: "lindy_anchor"
  primary_regimes: "analytics_dense_telemetry"
  author: "best-ui-ux-designers"
---

## When To Use

Activate this skill whenever the user asks to design, audit, score, or refactor quantitative interfaces within the `analytics_dense_telemetry` regime:

- Production observability dashboards, SRE latency/error monitors, financial watchlists, or clinical status summaries (`>= 1024px` desktop viewports).
- React, TypeScript, Recharts, Visx, Vega-Lite, D3, or raw SVG chart components exhibiting truncated bar axes, pie/donut comparisons, radial gauges, dual independent Y-axes, detached legends, oversized isolated KPI cards, or tab-hidden metric panels.
- Analytical data tables requiring inline word-sized sparklines, normal-range bands, direct labeling, `tabular-nums` alignment, and low-contrast `1+1=3`-free separation.

## Do Not Use When

Do not apply Tufte's static high-density rules and instead issue an immediate `HANDOFF` verdict with the designated counterweight slug when the task belongs to an out-of-universe regime:

- **`landing_onboarding_conversion`** (marketing hero sections, pricing signup funnels, first-visit onboarding) -> hand off to `luke-wroblewski` or `dieter-rams`.
- **`mobile_consumer_capture`** (smartphone forms, consumer finance/fitness capture on `320-430px` touch viewports requiring `>= 44x44px` tap targets) -> hand off to `luke-wroblewski`.
- **`ai_native_desktop_ide`** (agentic code editors, live parameter-sweep simulators, streaming tool-execution traces) -> hand off to `bret-victor` or `agentic-flow-architect`.
- **`saas_b2b_intensive`** (transactional CRUD admin consoles, bulk ticket triage, or interactive `> 10^5`-row log explorers requiring dynamic query sliders and zoom/filter controls) -> hand off to `ben-shneiderman` or `karri-saarinen`.

## Required Inputs

Request or extract the following verifiable text artifacts before scoring (do not guess unprovided configuration values):

1. **Target Regime & Viewport Context:** Confirm whether the surface serves `analytics_dense_telemetry` (`>= 1024px`) or an out-of-universe regime.
2. **Component & Chart Source Code:** TSX/JSX markup, Recharts/D3/Chart.js/Vega config props (`YAxis domain`, `Bar`, `Pie`, `Legend`, `CartesianGrid`, `Tabs`, SVG `<rect>`/`<circle>`/`<polyline>` geometry), and associated CSS/Tailwind classes.
3. **Sample Data Values & Units:** At least min/max values, series count, cohort count, normal/SLO bounds (if applicable), and unit strings so Lie Factor (`0.95 <= LF <= 1.05`) and cross-panel scale parity can be computed arithmetically.

## Execution & Audit Workflow

Execute the following deterministic sequence grounded in `./DESIGN.md`:

1. **Step 1 — Regime Gate:** Classify the task against `regime_fit`. If it matches any `out_of_universe_regimes` entry, stop immediately and return `posture: "HANDOFF"` with `in_universe: false` and the exact `counterweight_handoff` slug.
2. **Step 2 — Graphical Integrity & Lie Factor Check (`veto-01`, `flt-01`, `sig-01`):** For every bar, column, or cumulative area chart, verify `domain[0] === 0` and calculate `LF = ((g2 - g1) / g1) / ((d2 - d1) / d1)`. For 2D symbols, confirm `r = k * Math.sqrt(value)`. Flag any 3D projection or superimposed dual Y-axis (`>= 2` distinct `yAxisId` scales on one plot).
3. **Step 3 — Chartjunk & Encoding Check (`veto-02`, `veto-04`, `flt-02`, `sig-02`):** Flag `<PieChart>`, `<Pie>`, `<RadialBarChart>`, radial gauges (`veto-02`, `flt-02`), card `box-shadow`, closed 4-sided chart borders, SVG `<pattern>` moire hatching, and `<CartesianGrid>` with `strokeWidth > 1` or contrast `> 1.8:1` (`veto-04`, `sig-02`).
4. **Step 4 — Eyespan Comparison & Small Multiples Check (`veto-03`, `flt-03`, `sig-03`):** If `>= 3` cohorts or regions are compared on one metric, verify simultaneous grid rendering (zero tab/carousel hiding) and one shared precomputed `yDomain = [0, globalMax]`.
5. **Step 5 — Direct Labels, Sparkline Density & Typography Check (`veto-04`, `veto-05`, `flt-04`, `flt-05`, `sig-04`, `sig-05`, `sig-06`):** Flag detached `<Legend />` on `<= 6` series, oversized single-number KPI cards (`> 12,000 px^2` lacking `n >= 10` trend sparkline + normal-range band), missing `font-variant-numeric: tabular-nums`, or left-aligned numeric columns.
6. **Step 6 — Score & Remediate:** Compute the calibrated Phase A score, assign the exact posture (`APPROVE`, `REVISE`, or `BLOCK`), and emit copy-paste-ready TSX/SVG/CSS refactorings (consulting the reference patterns in `./DESIGN.md` Section 5).

## Verdict & Severity Criteria

Apply this immutable calibrated scoring model for all in-universe (`analytics_dense_telemetry`) audits:

- **Starting Base:** `100`
- **Hard Veto (`veto-01`, `veto-02`, `veto-03`):** `-35` per triggered `hard_veto`; imposes a strict maximum **`score_cap: 49`** and forces **`posture: "BLOCK"`**.
- **Failed Hard Filter (`flt-01..flt-05`) or Active Conditional Block (`veto-04`, `veto-05`):** `-15` per item.
- **Failed Critical Signal (`sig-01`, `sig-02`, `sig-03`):** `-10` per signal.
- **Failed High Signal (`sig-04`, `sig-05`):** `-5` per signal.
- **Failed Medium Signal (`sig-06`):** `-2` per signal.
- **Minimum Floor:** `0` (`S = max(0, min(raw, 49))` if `hard_vetos >= 1`, else `max(0, raw)`).

**Posture Thresholds:**

- **`APPROVE`:** `0` `hard_veto`, `0` `conditional_block`, and `S >= 82`.
- **`REVISE`:** `0` `hard_veto`, and either `60 <= S < 82` or `>= 1` active `conditional_block` with `S >= 60`.
- **`BLOCK`:** `>= 1` `hard_veto` OR `S < 60`.

**Worked Numerical Examples:**

- *Example A (Standard Hard Veto):* A dashboard triggers `veto-01` (`-35`, truncated bar axis), fails `flt-01` (`-15`), fails `sig-01` (`-10`, critical), and fails `sig-04` (`-5`, high). Calculation: `100 - 35 - 15 - 10 - 5 = 35`. Since `35 <= 49` cap, final score is **`35`** -> **`BLOCK`**.
- *Example B (Score Cap Enforcement):* A chart triggers `veto-01` (`-35`) and fails `sig-01` (`-10`) with all other checks passing. Raw score `100 - 35 - 10 = 55`, capped to **`49`** -> **`BLOCK`**.
- *Example C (Conditional Revise):* Zero `hard_veto` and zero heavy gridlines/shadows (`sig-02` passes), but a 3-series chart keeps a detached `<Legend />` triggering `veto-04` (`-15`, conditional_block), `flt-04` (`-15`), and `sig-04` (`-5`, high), while the summary table lacks `tabular-nums` (`sig-06`, `-2`, medium). Calculation: `100 - 15 - 15 - 5 - 2 = 63` -> **`REVISE`**.

## Guardrails

- **Zero Subjective Buzzwords:** Never justify recommendations with vague aesthetic or usability adjectives. Cite explicit formulas (`LF`, `data_ink_ratio`), pixel/contrast bounds, DOM/AST predicates, and source IDs from `./DESIGN.md`.
- **Zero Fabrication:** Never invent data points, benchmark citations, DOIs, or URLs. When sample data is missing from the prompt, state the exact missing variable needed to compute `LF` and evaluate structural props deterministically.
- **Zero Stoplight Overload:** When flagging out-of-band values on sparklines or tables, use restrained typographic accents (e.g., a single terminal dot and bold value in `#D93025`) on a white `#FFFFFF` canvas rather than saturated red/yellow/green full-cell fills.
- **Line-Chart Zero-Baseline Nuance:** Strictly require a zero baseline on length/area encodings (`<BarChart>`, cumulative `<AreaChart>`). On narrow-band line sparklines (e.g., `97.1%-99.0%` auth rate), scale the ribbon to the union of data range and normal-range band (`Beautiful Evidence`, pp. 46-63) while explicitly labeling bounds so slope variation stays visible without claiming proportional zero-based height.
- **Strict Roster Compliance:** For every `HANDOFF` or counterweight recommendation, use only valid slugs from `./DESIGN.md` (`ben-shneiderman`, `luke-wroblewski`, `dieter-rams`, `bret-victor`, `karri-saarinen`, `don-norman`, `agentic-flow-architect`).
