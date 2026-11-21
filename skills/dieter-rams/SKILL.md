---
name: dieter-rams
description: Audits B2B SaaS workflows and conversion landing pages for Dieter Rams's structural subtraction, functional color discipline, chrome ceilings, and honesty gates. Triggers on UI code reviews, anti-slop audits, pricing cards, or toolbar decluttering; excludes IDEs, dense analytics, and mobile capture.
license: MIT
compatibility: Text-only coding and UI review agents auditing HTML, JSX/TSX, CSS, Tailwind, or design-token repositories (agentskills.io v1.0).
metadata:
  schema_version: "1.1.0"
  judgment_schema: "./DESIGN.md"
  suite_id: "ui-ux"
  barbell_pole: "lindy_anchor"
  primary_regimes: "saas_b2b_intensive,landing_onboarding_conversion"
  author: "best-ui-ux-designers"
---

# Dieter Rams Structural Subtraction & Honesty Audit

Execute deterministic, text-verifiable UI code audits against `./DESIGN.md` to eliminate visual bloat, chromatic AI slop, and deceptive patterns in B2B SaaS workspaces and conversion surfaces without erasing perceptible interactive signifiers.

## When To Use

Proceed with full scoring only when the target artifact belongs to:
- **`saas_b2b_intensive`:** CRUD consoles, settings, billing pages, tables, operational forms, and workspace shells requiring chrome ceilings (`<= 35%`), achromatic discipline (`>= 85%` OKLCH `C <= 0.02`), and flat container depth (`<= 1`).
- **`landing_onboarding_conversion`:** Marketing heroes, pricing matrices, signup/checkout/cancellation flows requiring honesty parity, single primary CTA per fold, and zero chromatic AI slop.

## Do Not Use When

Abort and defer immediately—without emitting a numeric penalty score—if the target falls into any mandatory `out_of_universe_regimes`:
- **`analytics_dense_telemetry`** (real-time observability, trading, multi-series small multiples): state `OUT_OF_UNIVERSE` and hand off to `edward-tufte` and `ben-shneiderman`.
- **`ai_native_desktop_ide`** (multi-pane code editors, side-by-side diffs, terminal + agent verification rails): state `OUT_OF_UNIVERSE` and hand off to `agentic-flow-architect`, `jef-raskin`, and `karri-saarinen`.
- **`mobile_consumer_capture`** (one-handed thumb-zone camera/feed/quick-capture apps): state `OUT_OF_UNIVERSE` and hand off to `luke-wroblewski` and `rauno-freiberg`.

## Required Inputs

Collect or extract at least one text-verifiable UI artifact before executing the audit:
1. **Regime & surface classification:** Confirm `saas_b2b_intensive` or `landing_onboarding_conversion` (or trigger out-of-universe handoff).
2. **Markup & styling source:** HTML, JSX/TSX, CSS, Tailwind utility classes, and design-token files exposing colors, gradients, borders, blurs, chrome dimensions, and CTA hierarchy.
3. **Interactive & business-flow logic:** Countdown hooks (`useEffect`/`setInterval`), checkbox defaults (`defaultChecked`), AI inference bindings, and signup vs. cancellation flow steps.

## Execution & Audit Workflow

Read `./DESIGN.md` for exact token equations and remediation templates, then execute the following five checks in strict order using static source inspection (no computer vision required):

1. **Regime Gate:** Classify the target artifact into one of the canonical regimes before scoring; abort with `OUT_OF_UNIVERSE` + counterweight handoff if excluded.
2. **Veto Scan (`veto-01` to `veto-05`):**
   - `veto-01` (`hard_veto`): Inspect JS/TS state hooks (`useEffect`, `setInterval`, `localStorage`) and static strings for client-resetting countdown timers, hardcoded scarcity counts, or fabricated social-proof numbers.
   - `veto-02` (`hard_veto`): Check signup vs. cancellation step parity, `defaultChecked` paid add-ons, confirmshaming decline copy, and destructive handlers styled with neutral or safe primary button tokens.
   - `veto-03` (`hard_veto`): Scan CSS/Tailwind for `bg-clip-text` / `-webkit-background-clip: text`, decorative gradients across OKLCH hue `260deg–330deg` with `C > 0.18` (indigo/purple/fuchsia), and ambient colored blur glows (`> 24px`).
   - `veto-04` (`hard_veto`): Inspect text nodes and SVG badges for `"AI Powered"` / `"Smart AI"` claims or decorative sparkles lacking a bound asynchronous inference call or verifiable capability disclosure.
   - `veto-05` (`conditional_block`): Flag `backdrop-filter: blur()` on `>= 2` non-overlay structural containers or stacked persistent toolbars breaching the `35%` viewport chrome ceiling.
3. **Hard Filter Gate (`flt-01` to `flt-05`):**
   - `flt-01`: Compute persistent chrome area (`header + banners + toolbars + sidebar + sticky footer`) divided by viewport area at `1440x900` and `1280x720`; fail if `> 0.35`.
   - `flt-02`: Convert surface, canvas, border, and body-ink tokens to `oklch(L C H)`; fail if achromatic (`C <= 0.02`) surfaces occupy `< 85%` of the viewport.
   - `flt-03`: Verify `cancellation_step_count <= enrollment_step_count`, exit link contrast `>= 4.5:1`, and zero pre-checked paid add-ons.
   - `flt-04`: Traverse JSX/HTML container hierarchy; fail if ancestor-descendant bordered/shadowed card nesting reaches depth `>= 2`.
   - `flt-05`: Verify every interactive button, input, focus ring, and link preserves `>= 3.0:1` non-text boundary contrast (WCAG 2.2 SC 1.4.11) and `>= 4.5:1` label contrast (SC 1.4.3).
4. **High-Weight Signal Evaluation (`sig-01` to `sig-07`):**
   - Evaluate `sig-01` (`critical`: achromatic ratio `>= 85%`), `sig-02` (`critical`: chrome ratio `<= 35%`), `sig-03` (`critical`: exactly `1` primary high-chroma CTA per fold), `sig-04` (`critical`: `0` unbacked AI claims), `sig-05` (`high`: nested bordered depth `<= 1`), `sig-06` (`high`: `0` ephemeral ornament/idle-motion nodes), and `sig-07` (`medium`: interactive signifier contrast floor).
5. **Blind-Spot Guardrail Verification (`don-norman` Check):**
   - Before recommending deletion of any border, label, icon, or button, confirm the remediation does not turn interactive controls into low-contrast plain text or hide Undo/Back/Cancel actions. If recommending Braun signal yellow (`#E5A800`) on a light canvas, mandate a `1px` dark structural border (`#141413` or `#7D5600`) so non-text boundary contrast exceeds `3.0:1`.

## Verdict & Severity Criteria

Compute score `S` deterministically from base `100` using the immutable Phase A Calibrated Rubric:

- **Base score**: `100`
- **Hard Veto (`hard_veto`)**: `-35` per triggered veto. Any triggered `hard_veto` caps final `S` at `49` (`S = min(S, 49)`) and forces stance `BLOCK`.
- **Hard Filter / Conditional Block**: `-15` per failed `hard_filter` (`flt-01`..`flt-05`) or triggered `conditional_block` (`veto-05`).
- **Critical Signal (`sig-01`..`sig-04`)**: `-10` per failed `critical` signal.
- **High Signal (`sig-05`, `sig-06`)**: `-5` per failed `high` signal.
- **Medium Signal (`sig-07`)**: `-2` per failed `medium` signal.
- **Score Floor**: `0` (`S = max(0, S)`).

### Stance Mapping
- **`APPROVE`**: `hard_veto == 0` AND `conditional_block == 0` AND `S >= 82`.
- **`REVISE`**: `hard_veto == 0` AND (`60 <= S < 82` OR (`conditional_block >= 1` AND `S >= 60`)).
- **`BLOCK`**: `hard_veto >= 1` OR `S < 60`.

### Worked Scoring Reference
- 0 vetos, 0 filters, 1 `medium` signal (`sig-07`) -> `100 - 2 = 98` -> `APPROVE`.
- 0 `hard_veto`, 1 `conditional_block` (`veto-05`) only -> `100 - 15 = 85` -> `REVISE` (unresolved conditional block prevents `APPROVE`).
- 0 `hard_veto`, 1 `conditional_block` (`veto-05`) + 1 `hard_filter` (`flt-04`) + 1 `high` signal (`sig-05`) -> `100 - 15 - 15 - 5 = 65` -> `REVISE`.
- 1 `hard_veto` (`veto-03`) only -> raw `100 - 35 = 65`, capped at `49` -> `BLOCK`.
- 2 `hard_veto` + 2 `hard_filter` + 2 `critical` + 1 `high` -> raw `100 - 70 - 30 - 20 - 5 = -25`, floored at `0` -> `BLOCK`.

### Required Output Contract

Emit every audit report in this exact structure:

```markdown
### Verdict: <APPROVE | REVISE | BLOCK | OUT_OF_UNIVERSE>
- **Regime**: `<detected_regime>`
- **Final Score**: `<0..100> / 100` (or `N/A — deferred to <counterweight_slugs>`)

#### Penalty Breakdown

| Rule ID | Type | Penalty | Observed Evidence (File/Selector/Predicate) |
| :--- | :--- | :---: | :--- |
| `<id>` | `<hard_veto|conditional_block|hard_filter|critical|high|medium>` | `-N` | `<exact token, DOM node, or state violation>` |

#### Mandatory Remediations
1. `<Exact code/CSS/token diff required to resolve each veto, filter, and signal>`

#### Signifier Preservation Check (`don-norman` Guardrail)
- Confirm interactive control boundary contrast (`>= 3.0:1`), label contrast (`>= 4.5:1`), and explicit recovery/exit affordances remain intact after subtraction.
```

## Guardrails

- **Zero subjective clichés**: Ban vague design adjectives in findings and remediations; cite only falsifiable predicates (`OKLCH C`, viewport percentage, nesting depth, WCAG luminance contrast ratio, and state-graph step count).
- **Reproducible attribution**: Record each distinct schema ID triggered by observable evidence with its exact CSS selector, token, or AST line so penalty math is deterministic.
- **Legitimate deadlines and real AI features**: Do not veto a countdown timer backed by an immutable server-enforced timestamp, nor an AI action bound to a real inference handler with honest loading/error states.
