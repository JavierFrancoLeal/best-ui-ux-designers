---
name: susan-kare
description: "Audits and refactors icon systems, SVG grids, visual metaphors, non-text contrast, and ARIA labeling using Susan Kare's 1-bit road-sign semiotics. Triggers on mobile consumer capture and landing onboarding UIs; hands off dense analytics, B2B SaaS, and desktop IDEs."
license: MIT
compatibility: "Text-only and multimodal coding agents (Claude Code, DeepSeek V4, Codex) auditing JSX/TSX, HTML, SVG, and CSS artifacts"
metadata:
  schema_version: "1.0.0"
  design_schema: "./DESIGN.md"
  barbell_pole: "lindy_anchor"
  primary_regimes: "mobile_consumer_capture"
  author: "best-ui-ux-designers"
---

## When To Use

Activate this skill when auditing, specifying, or refactoring iconography, action toolbars, navigation bars, status/category badges, or SVG component libraries inside:
- **`mobile_consumer_capture`** (primary regime): camera, voice, note, receipt, or field-entry mobile capture bars, bottom navigation, and offline/sync status queues.
- **`landing_onboarding_conversion`** (secondary regime): first-run onboarding flows, step checklists, feature cards, and consumer conversion CTAs relying on visual symbols.

Load `./DESIGN.md` before scoring to access the exact signal thresholds (`sig-01`..`sig-06`), gate filters (`flt-01`..`flt-04`), veto triggers (`veto-01`..`veto-05`), and TSX/SVG/CSS reference patterns.

## Do Not Use When

Do not apply this skill—and immediately return `in_universe: false`, `posture: "HANDOFF"`, and the matching `counterweight_handoff` slug—when the target UI belongs to an out-of-universe regime:
- **`analytics_dense_telemetry`** (real-time observability consoles, P99 latency dashboards, financial matrices, multi-series charts) -> hand off to **`edward-tufte`**.
- **`saas_b2b_intensive`** (dense enterprise CRUD workspaces, >25-50 workflow mutations, triage tables, keyboard-first command menus) -> hand off to **`karri-saarinen`**.
- **`ai_native_desktop_ide`** (desktop code editors, diff viewers, terminal-centric agentic workbenches optimized for hardware-keyboard habituation) -> hand off to **`jef-raskin`**.

## Required Inputs

Request or extract the following verifiable artifacts before scoring (if any required token is missing, declare the gap explicitly rather than guessing):
1. **Target regime & viewport class:** confirm whether the surface is `mobile_consumer_capture` or `landing_onboarding_conversion` (and whether touch `>= 44x44 CSS px` or desktop `>= 24x24 CSS px` bounds apply).
2. **Markup / Component source:** JSX/TSX/HTML containing interactive icon controls (`<button>`, `<a>`, `[role="button"]`), status/category badges, and inline or imported `<svg>` definitions.
3. **SVG geometry & styling tokens:** `viewBox`, `width`, `height`, `stroke-width` / `strokeWidth`, child primitive nodes, and resolved foreground/background CSS color values (hex/RGB/HSL) for every icon and badge state.
4. **Action semantics:** handler names, visible text children, tooltips (`title`), and ARIA attributes (`aria-label`, `aria-labelledby`, `aria-hidden`, `aria-pressed`).

## Audit & Design Workflow

Execute these 5 steps sequentially and deterministically:

1. **Step 1 — Regime Gate:** Match the UI scope against `When To Use` and `Do Not Use When`. If out-of-universe, halt scoring immediately and emit `posture: "HANDOFF"` with the designated `counterweight_handoff` slug (`edward-tufte`, `karri-saarinen`, or `jef-raskin`).
2. **Step 2 — Static SVG & Grid Audit (`sig-03`, `sig-06`, `flt-02`, `veto-02`, `veto-05`):**
   - Inspect all peer `<svg>` elements on the surface for a single shared integer square `viewBox` (`0 0 24 24`, `0 0 20 20`, or `0 0 16 16`).
   - Verify uniform `stroke-width` in `[1.5, 2.0]` px (`<= 0.25 px` variance across siblings) and zero hairline strokes `< 1.0 px`.
   - Flag any `<= 32px` UI icon with `> 6` geometric primitives, `<filter>`, `<linearGradient>`, or `<radialGradient>`, or legacy hardware symbols (e.g., floppy disk) mapped to cloud auto-sync, download, or export actions.
3. **Step 3 — Road-Sign Labeling & Metaphor Audit (`sig-01`, `sig-02`, `flt-01`, `veto-01`):**
   - Check every interactive icon control against the closed 6-symbol universal allowlist: `{close, search, back, home, trash, menu}`.
   - Flag any non-allowlisted icon (especially any AI sparkle, magic wand, or domain action) lacking a persistent visible sibling text label, or relying on hover-only `title`/tooltips.
   - Flag any view where `>= 2` distinct action handlers reuse the same icon stem or colliding outer silhouette.
4. **Step 4 — Contrast, State Redundancy, ARIA & Touch Envelope Audit (`sig-04`, `sig-05`, `flt-03`, `flt-04`, `veto-03`, `veto-04`):**
   - Compute WCAG 2.2 relative luminance contrast between icon foreground/stroke and background (`>= 3.0:1` required per SC 1.4.11; `>= 4.5:1` recommended to match SC 1.4.3).
   - Verify every status/category indicator combines a unique 1-bit geometric shape plus explicit visible text (zero color-only dots per SC 1.4.1).
   - Verify `aria-hidden="true"` and `focusable="false"` on all SVGs paired with visible text, descriptive action-verb `aria-label` on icon-only universal controls, and hit-box dimensions `>= 44x44 CSS px` on mobile (`>= 24x24 CSS px` on desktop, `>= 8px` gap).
5. **Step 5 — Score, Verdict & Concrete Code Remediation:**
   - Compute the numeric score and posture strictly via `## Scoring & Verdict Rubric`.
   - When posture is `BLOCK` or `REVISE`, output exact TSX/SVG/CSS diffs resolving every triggered veto, failed filter, and failed signal, referencing `./DESIGN.md` Section 5 patterns.

## Scoring & Verdict Rubric

Start from **Base Score = `100`** and apply deductions deterministically:
- **`-35`** for each triggered **`hard_veto`** (imposes hard **`score_cap = 49`** and forces **`posture = BLOCK`**).
- **`-15`** for each failed **`hard_filter`** (`flt-01`..`flt-04`) OR each active **`conditional_block`** (`veto-05`).
- **`-10`** for each failed **`critical`** signal (`sig-01`, `sig-02`, `sig-04`).
- **`-5`** for each failed **`high`** signal (`sig-03`, `sig-05`).
- **`-2`** for each failed **`medium`** signal (`sig-06`).
- **Floor = `0`** (`raw = max(0, 100 - total_deductions)`; if `hard_veto >= 1`, `final_score = min(raw, 49)` else `final_score = raw`).

**Verdict Postures (Immutable):**
- **`APPROVE`**: `0` `hard_veto`, `0` `conditional_block`, and `S >= 82`.
- **`REVISE`**: `0` `hard_veto` AND (`60 <= S < 82` OR (`>= 1` active `conditional_block` with `S >= 60`)).
- **`BLOCK`**: `>= 1` `hard_veto` OR `S < 60`.

**Worked Numeric Examples:**
- *Example A (`BLOCK`):* Mobile toolbar ships 1 unlabeled AI sparkle button (`veto-01` hard_veto `-35`, `flt-01` `-15`, `sig-01` critical `-10`) and omits `aria-hidden="true"` on a labeled button (`sig-05` high `-5`). Calculation: `100 - 35 - 15 - 10 - 5 = 35`. Since `hard_veto = 1`, `score_cap = 49`; `min(35, 49) = 35` -> **`BLOCK` (Score `35`, Cap `49`)**.
- *Example B (`REVISE`):* Onboarding bar passes all hard filters and labels, but renders a 12-path gradient floppy-disk SVG for "Cloud Auto-Sync" (`veto-05` conditional_block `-15`, `sig-06` medium `-2`). Calculation: `100 - 15 - 2 = 83`. Because `conditional_block = 1` with `S >= 60` -> **`REVISE` (Score `83`, Cap `100`)**.

## Guardrails

- **Zero subjective adjectives:** Never justify findings with vague terms or stylistic praise; every finding must cite an exact predicate (`viewBox`, `stroke-width`, primitive count, contrast ratio, pixel dimension, ARIA attribute, or allowlist violation).
- **No fabricated compliance:** Never assume contrast passes without computing luminance from actual hex/RGB tokens; if background tokens are absent, flag missing input before approving.
- **No hover-only compromises:** Never accept `title`, CSS `:hover`, or `Tooltip`-only labels as remediation for `veto-01` or `flt-01` on mobile capture or onboarding surfaces.
- **Strict regime discipline:** Never force labeled icon toolbars onto `ai_native_desktop_ide`, `saas_b2b_intensive`, or `analytics_dense_telemetry` prompts—always emit `HANDOFF` to the registered counterweight slug.
