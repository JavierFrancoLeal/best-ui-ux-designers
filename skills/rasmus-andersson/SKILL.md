---
name: rasmus-andersson
description: Audits and refactors analytics telemetry tables, B2B SaaS views, and landing/pricing pages for Inter-grade optical typography, tabular numeral stability, glyph disambiguation, 4px spatial grids, WCAG contrast, and composable tokenized primitives. Hands off mobile capture funnels and agentic IDEs.
license: MIT
compatibility: Text-only and multimodal coding agents auditing HTML, CSS, Tailwind, design tokens, and JSX/TSX without screenshot dependencies
metadata:
  schema_version: "1.0.0"
  design_schema: "./DESIGN.md"
  barbell_pole: "convex_frontier"
  primary_regimes: "analytics_dense_telemetry,landing_onboarding_conversion"
  author: "best-ui-ux-designers"
---

## When To Use

Activate this skill when auditing, specifying, or refactoring code, tokens, or markup within these verified regimes:

- **`analytics_dense_telemetry` (Primary):** Financial ledgers, settlement dashboards, real-time monitoring tables, KPI strips, timers, pricing matrices, and identifier/hash/API-key tables where numeric stability and glyph disambiguation prevent operator errors.
- **`landing_onboarding_conversion` (Primary):** Desktop and responsive hero sections, value-proposition prose, documentation blocks, and multi-tier pricing comparisons where optical display tracking, `45ch–75ch` reading measure, and right-aligned tabular prices govern scanning precision.
- **`saas_b2b_intensive` (Secondary):** Recurring B2B billing panels, configuration tables, and multi-panel workspaces requiring finite typography tokenization, 4px/8px grid discipline, icon-type stroke parity, and composable primitives without `!important` cascade drift.

Load `./DESIGN.md` for complete OpenType tables, Dynamic Metrics calculations, and Before/After JSX/TSX + CSS reference patterns.

## Do Not Use When

Immediately issue `posture: "HANDOFF"` without computing a numeric score whenever the task falls outside this designer's universe:

- **`ai_native_desktop_ide` -> Handoff to `agentic-flow-architect` (secondary: `ben-shneiderman`):** Autonomous multi-file code editing, tool-call permission gates, speculative diff review UX, agent execution plans, and deterministic rollback workflows. Optical typography cannot substitute for agentic safety boundaries.
- **`mobile_consumer_capture` -> Handoff to `luke-wroblewski`:** One-handed smartphone onboarding, consumer checkout, receipt/camera capture, bottom thumb-zone CTA geometry, `>= 44x44px` touch ergonomics, and single-column form field reduction on `320–390px` viewports.
- **Irreversible destructive confirmation interlocks inside B2B apps -> Co-audit with `don-norman`:** When the primary task is preventing destructive action slips or mode confusion rather than typographic/spatial systems.

## Required Inputs

Request or extract the following text-verifiable artifacts before scoring (zero screenshots required):

1. **Target regime classification:** Explicit screen role (`analytics_dense_telemetry`, `landing_onboarding_conversion`, `saas_b2b_intensive`, or out-of-universe check).
2. **Markup / Component AST:** HTML, JSX, or TSX containing tables, numeric counters, identifiers/codes, hero prose, pricing cards, or inline SVG icons.
3. **Styles & Design Tokens:** CSS, SCSS, Tailwind config, `@font-face` declarations / font CDN URLs, and foreground/background hex or RGB token pairs.
4. **Font loading source:** Verification of whether Inter (or another variable sans-serif) is self-hosted (`InterVariable.woff2`), loaded from `rsms.me/inter/inter.css`, or imported from feature-stripped `fonts.googleapis.com`.

## Audit & Design Workflow

Execute these six steps in exact deterministic order:

1. **Regime Gate Check:** Verify whether the prompt targets `ai_native_desktop_ide` or `mobile_consumer_capture`. If yes, abort scoring and emit `in_universe: false`, `posture: "HANDOFF"`, and the valid `counterweight_handoff` slug.
2. **Numeral & Homoglyph Verification (`sig-01`, `sig-02`, `flt-01`, `flt-02`, `veto-01`, `veto-02`):** Inspect every numeric table cell, header, KPI counter, timer, and price for `font-variant-numeric: tabular-nums` (plus `"tnum"` fallback) and `text-align: right` (or `end`) on tabular columns; inspect every account code, transaction ID, UUID, hash, and API key for OpenType disambiguation (`"ss02" 1` or `"cv05" 1, "cv08" 1, "zero" 1`, optional `"cv11" 1`) or a disambiguated monospace token; flag any `fonts.googleapis.com` Inter stylesheet whenever OpenType `ssXX`/`cvXX`/`zero` features are relied upon (`veto-02`); verify `"case" 1` on uppercase badges, keycaps, and punctuated numeric ranges (`heur-03`).
3. **Optical Metrics & Reading Measure Audit (`sig-03`, `sig-04`, `sig-05`, `flt-04`, `veto-03`):** Check `font-optical-sizing: auto` on `opsz`-capable variable fonts; validate `letter-spacing` against Inter Dynamic Metrics `tracking(z) = -0.0223 + 0.185 * exp(-0.1745 * z)` (headings `>= 24px` in `-0.030em` to `-0.015em`, body `14–16px` in `-0.006em` to `-0.011em`, micro-labels `<= 12px` at `>= 0.000em` or `+0.04em` when uppercase); check single-column prose blocks for `45ch <= max-width <= 75ch` (`> 80ch` triggers `veto-03`) and `text-align != justify`; count unique font sizes (`<= 6`) and weights (`<= 3`, favoring `400/500/600` in dense telemetry) per view.
4. **Contrast, Reflow & Icon Parity Audit (`sig-07`, `flt-03`, `veto-04`):** Compute WCAG 2.2 sRGB relative luminance contrast ratios (unrounded): normal text `>= 4.5:1`, large text (`>= 24px` regular or `>= 18.5px` bold) `>= 3.0:1`, interactive borders/icons `>= 3.0:1`; flag fixed `px` height paired with `overflow: hidden` on text boxes that clip under WCAG SC 1.4.12 (`1.5x` line-height, `0.12em` tracking); verify icons snap to discrete bounding classes (`16px`, `20px`, `24px`, `32px`) with uniform stroke weight (`1.5px` at `16–20px`, `2px` at `>= 24px`).
5. **Spatial Grid & Cascade Integrity Audit (`sig-06`, `flt-05`, `veto-05`):** Check `px % 4 === 0` across all `padding`, `margin`, and `gap` declarations (excluding `1px`/`2px` borders); check role-bound `line-height` (`1.10–1.25` display, `1.20–1.35` dense table, `1.45–1.60` readable body); flag any `!important` in component CSS, `> 2` inline typography/spacing overrides per view, or child `font-feature-settings` rules that overwrite inherited parent OpenType tags.
6. **Score & Remediate:** Compute final score and posture per the rubric below, then emit exact CSS/TSX patches resolving every triggered veto and failed filter.

## Scoring & Verdict Rubric

Start from **Base `100`** and apply exact deductions (floor `0`):

- **`-35`** per triggered `hard_veto` (`veto-01`, `veto-02`, `veto-03`) — **also imposes a hard score cap of `49` and forces posture `BLOCK`**.
- **`-15`** per failed `hard_filter` (`flt-01`..`flt-05`) OR triggered `conditional_block` (`veto-04`, `veto-05`).
- **`-10`** per failed `critical` signal (`sig-01`, `sig-02`, `sig-07`).
- **`-5`** per failed `high` signal (`sig-03`, `sig-04`, `sig-05`).
- **`-2`** per failed `medium` signal (`sig-06`).

**Score Formula:**
- `raw = 100 - 35*(hard_vetos) - 15*(failed_filters + conditional_blocks) - 10*(failed_critical_signals) - 5*(failed_high_signals) - 2*(failed_medium_signals)`
- `capped = min(raw, 49)` if `hard_vetos >= 1`, else `raw`
- `S = max(0, capped)`

**Verdict Postures:**
- **`APPROVE`**: `0` `hard_veto`, `0` `conditional_block`, and `S >= 82`.
- **`REVISE`**: `0` `hard_veto`, and (`60 <= S < 82` OR (`>= 1` `conditional_block` with `S >= 60`)).
- **`BLOCK`**: `>= 1` `hard_veto` OR `S < 60`.
- **`HANDOFF`**: Out-of-universe regime detected; omit score and route to counterweight slug.

**Worked Numeric Example:**
A telemetry view triggers `1` `hard_veto` (`veto-01`: `-35`), fails `1` `hard_filter` (`flt-01`: `-15`), and fails `1` `critical` signal (`sig-01`: `-10`):
- `raw = 100 - 35 - 15 - 10 = 40`
- `capped = min(40, 49) = 40`; `S = max(0, 40) = 40` -> **`BLOCK`** (note: even if `raw` had been `65` from a single `hard_veto` alone, the `49` cap forces `S = 49` and `BLOCK`).

## Guardrails

- **Zero subjective adjectives:** Never evaluate or justify fixes using vague terms; cite exact CSS properties, OpenType feature tags, `ch` bounds, `4px` modulo checks, or WCAG 2.2 contrast ratios.
- **Prevent OpenType cascade clobbering:** Never emit a child `font-feature-settings: "tnum" 1;` rule that wipes out a parent's `"cv05" 1, "cv08" 1, "case" 1` settings; use `font-variant-numeric: tabular-nums;` alongside composed CSS custom-property feature tokens.
- **Verify font binary provenance:** Never recommend `fonts.googleapis.com` for Inter when `ss02`, `cv05`, `cv08`, `cv11`, or `zero` are required; specify self-hosted `InterVariable.woff2` / `InterVariable-Italic.woff2` from `github.com/rsms/inter/releases` or `https://rsms.me/inter/inter.css`.
- **Respect counterweight boundaries:** Never override `luke-wroblewski` on `< 600px` mobile capture touch targets (`>= 44x44px`), `don-norman` on irreversible destructive confirmation interlocks, or `agentic-flow-architect` / `ben-shneiderman` on agentic IDE execution safety.
