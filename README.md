# `best-ui-ux-designers`

[![Validate Repository](https://github.com/JavierFrancoLeal/best-ui-ux-designers/actions/workflows/validate.yml/badge.svg)](https://github.com/JavierFrancoLeal/best-ui-ux-designers/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Ecosystem Contract](https://img.shields.io/badge/ECOSYSTEM__CONTRACT-v1.2.0-black.svg)](suite.yaml)

**Stop AI coding agents from shipping generic UI slop, broken focus states, non-compositor animation jank, and unguarded async mutations.**

`best-ui-ux-designers` is a portable, CPU-first UI/UX pre-merge audit suite for `agentskills.io`-compatible coding agents (`Google Antigravity`, `DeepSeek Harness`, `Claude Code`, `OpenAI Codex / ChatGPT`, `Cursor`, and `Windsurf / Devin Desktop`):

1. **Deterministic CPU Pre-Scanner First (`tools/uiux_cpu_scanner.py`, zero-dep Python 3.9+, JSON + SARIF 2.1.0):** Scans `.html`, `.css`, `.js`, `.jsx`, `.ts`, `.tsx`, `.vue`, and `.svelte` files in `<0.2 s` for undefined JS calls, unguarded async mutations (`POST`/`PUT`/`PATCH`/`DELETE` without double-submit lock or `try/catch`), `prefers-reduced-motion` omissions (checking both local files and project-wide `globals.css`), non-compositor animations (`transition: all`, `box-shadow`/`width`/`height`/`top`/`left`), missing `:focus-visible` rings, `<16px` mobile inputs, `<44px` touch targets, and unlabeled icon buttons.
2. **4 *Via Negativa* Circuit-Breaker Checklists (`committee/auditors/*/rules.yaml`):** Constrains LLM review to falsifiable veto rules (`PASS` | `CONDITIONAL_BLOCK` | `HARD_VETO` with `file:line` evidence) grounded in human-factors laws (Cowan 4-chunk working memory limit, Hick-Hyman choice entropy, Baymard `<= 14` form-field ceiling, KLM-GOMS motor tax, WCAG 2.2 AA).
3. **12 Compact Designer Briefs (`skills/*/BRIEF.md`, `<= 25 KB` active panel budget):** Loads 4–5 regime-matched design briefs (`~2 KB` each, 18× smaller than full `DESIGN.md` dossiers) so the agent gets concrete heuristics without blowing up the context window.

---

## 30-Second Quickstart

```bash
git clone https://github.com/JavierFrancoLeal/best-ui-ux-designers.git
cd best-ui-ux-designers

# 1. Run the zero-dependency CPU pre-scanner on any frontend file or directory
python3 tools/uiux_cpu_scanner.py --format markdown path/to/your/src

# 2. Or output SARIF 2.1.0 / fail CI on BLOCKER findings
python3 tools/uiux_cpu_scanner.py --format sarif --fail-on-blocker path/to/your/src

# 3. Install into your project workspace for Claude Code, Cursor, Antigravity, Codex, Windsurf, or DSH
./adapters/install.sh --target all --mode director-only --scope workspace --dest /path/to/your-project
```

---

## Economic Thesis: The Solow Productivity Paradox in Post-AI Software

In *"The Dynamo and the Computer: An Historical Perspective on the Modern Productivity Paradox"* (1990), economic historian **Paul A. David** explained why factories failed to achieve measurable Total Factor Productivity ($A$) gains during the first three decades of electrification (**Phase 1 — Central Dynamo / Direct Substitution, 1880–1910**): factory owners simply bolted a single electric dynamo onto legacy steam-era central drive shafts and leather belts. Capital expenditure ($K$) rose while workflow topology remained unchanged.

Sustained productivity leaps materialized only in **Phase 2 — Unit-Drive Motors / Factory Floor Redesign (1920s)**, when engineers demolished central shafts and embedded small fractional-horsepower electric motors directly into individual workstations—redesigning material flow around the machine's true physics.

Software teams repeat the exact same failure mode today when they bolt a floating *"Ask AI"* sparkle button or disconnected sidebar chat drawer onto an unmodified legacy form, CRUD table, or IDE:
- **Phase 1 (`BOLT_ON_CAPITAL_K`):** Token spend ($K$) increases while Total Factor Productivity ($A$) stalls. Users suffer chat fatigue, *Accordion Editing* (iterative repair prompts), and *Apple Picking* (manual copy-paste loops), documented empirically by Nielsen Norman Group (2024) and Zamfirescu-Pereira et al. (CHI 2023).
- **Phase 2 (`UNIT_DRIVE_TFP_A`):** Voluntary adoption multiplies 2×–3× (evidenced by Windsurf Cascade, Cursor Fast Apply, Linear, Raycast, Stripe Payment Element, and the DirectGPT CHI 2024 controlled study showing 50% faster task completion, 50% fewer prompts, and 72% shorter prompts) only when AI primitives are distributed as **unit-drive motors coupled to live workspace state**: implicit context capture, sub-second inline diffs, direct manipulation, and atomic `Cmd/Ctrl+Z` rollback—anchored by Lindy biological and cognitive invariants.

To enforce this thesis deterministically on every AI-bearing artifact, `auditor-agentic-anti-slop` executes the mandatory **`aud-slop-04` (`veto-central-dynamo`)** circuit breaker.

---

## Architecture Overview

```text
Target Artifact (TSX/JSX/CSS/DOM/State/PR Diff)
                    │
                    ▼
        ┌───────────────────────┐
        │    design-director    │  Step 1: Regime (R1–R5) + Solow Stage + 15% AI Override
        │  routing-matrix.yaml  │          Silences 8 OUT_OF_UNIVERSE profiles (0 averaging)
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │ 4 Active Barbell      │  Step 2: Isolated parallel scoring (S_i in 0..100)
        │ Designers (5 w/ AI)   │  Step 3: Adversarial Rebuttal via debate_triggers
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │ 4 Via Negativa        │  Step 4: Unconditional circuit breakers
        │ Auditors (V_hard)     │          Cognitive · Latency · Physics/WCAG · Anti-Slop
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │ Weighted Synthesis    │  Step 5: Q_total = sum(w_{r,i} * S_i)
        │ SHIP | ITERATE | REJECT          + Patch Plan + verdict_envelope v1.0.0
        └───────────────────────┘
```

### Dual SDLC Execution Modes
- **Architecture Mode (`plan`, `design`):** Invoke full `design-director` (Solow diagnosis + 4 active Barbell designers + dialectical rebuttal + 4 auditors + `verdict_envelope`).
- **Fast PR Gate Mode (`build`, `test`, `deploy`, `maintain`):** Run the 4 Via Negativa auditors on UI diffs; escalate to full `design-director` on any `hard_veto`, new AI surface, or regime shift.

See [docs/architecture.md](docs/architecture.md) for the complete specification.

---

## The 12-Designer Barbell Roster

Admitted strictly via 4 binary filters (Lindy survival / invariant anchor, measurable voluntary adoption, forced competitor imitation, and resilience under dirty data, latency, and fatigue — see [docs/selection-rubric.md](docs/selection-rubric.md)). Zero industry awards or vanity criteria.

### Pole 1 — Lindy Anchors (6 Profiles, 50%)
| Slug | Primary Domain | Primary Regimes |
|---|---|---|
| `dieter-rams` | Structural subtraction, achromatic discipline, anti-dark-pattern honesty | `saas_b2b_intensive`, `landing_onboarding_conversion` |
| `don-norman` | Perceptible signifiers, natural mapping, gulf-bridging feedback, error recovery | `mobile_consumer_capture`, `landing_onboarding_conversion` |
| `edward-tufte` | Data-ink ratio, Lie Factor (`0.95–1.05`), sparklines, shared-scale small multiples | `analytics_dense_telemetry` |
| `jef-raskin` | Modelessness, quasimodes, sacred user work, KLM-GOMS efficiency | `ai_native_desktop_ide`, `saas_b2b_intensive` |
| `ben-shneiderman` | Direct manipulation, Visual Information-Seeking Mantra, Human-Centered AI (HCAI) | `ai_native_desktop_ide`, `analytics_dense_telemetry` |
| `susan-kare` | 1-bit road-sign icon semiotics, pixel-grid clarity, non-text contrast & labeling | `mobile_consumer_capture` |

### Pole 2 — Convex Frontier (6 Profiles, 50%)
| Slug | Primary Domain | Primary Regimes |
|---|---|---|
| `bret-victor` | Live deterministic feedback, intermediate state visibility, Ladder of Abstraction | `ai_native_desktop_ide`, `analytics_dense_telemetry` |
| `karri-saarinen` | Local-first `<=50 ms` sync, keyboard-first workflows, opinionated defaults, LCH craft | `saas_b2b_intensive` |
| `luke-wroblewski` | Mobile-first thumb ergonomics, `<=14`-element single-column forms, gradual engagement | `mobile_consumer_capture`, `landing_onboarding_conversion` |
| `rasmus-andersson` | Optical typography (Inter), `tabular-nums`, homoglyph disambiguation, 4px grids | `analytics_dense_telemetry`, `landing_onboarding_conversion` |
| `rauno-freiberg` | Interruptible interaction physics, compositor-only motion, trigger-anchored geometry | `saas_b2b_intensive`, `mobile_consumer_capture` |
| `agentic-flow-architect` | Synthetic archetype: Flow Awareness, sub-400 ms inline diffs, checkpoints, atomic undo | `ai_native_desktop_ide` (+15% cross-cutting AI override) |

---

## Product Regime Routing (`routing-matrix.yaml`)

Each base regime activates **exactly 4 designers** (40%–60% Lindy balance, max weight `<= 0.35`, exact sum `1.00`) and silences 8 (`OUT_OF_UNIVERSE`):

| Regime | Active Panel & Exact Weights | Barbell Split |
|---|---|---|
| `ai_native_desktop_ide` (R1) | `agentic-flow-architect` 0.35 · `ben-shneiderman` 0.25 · `jef-raskin` 0.20 · `bret-victor` 0.20 | 45% Lindy / 55% Convex |
| `saas_b2b_intensive` (R2) | `karri-saarinen` 0.35 · `rauno-freiberg` 0.25 · `jef-raskin` 0.20 · `dieter-rams` 0.20 | 40% Lindy / 60% Convex |
| `mobile_consumer_capture` (R3) | `luke-wroblewski` 0.35 · `don-norman` 0.25 · `susan-kare` 0.20 · `rauno-freiberg` 0.20 | 45% Lindy / 55% Convex |
| `analytics_dense_telemetry` (R4) | `edward-tufte` 0.35 · `ben-shneiderman` 0.25 · `rasmus-andersson` 0.25 · `bret-victor` 0.15 | 60% Lindy / 40% Convex |
| `landing_onboarding_conversion` (R5) | `luke-wroblewski` 0.35 · `dieter-rams` 0.30 · `don-norman` 0.20 · `rasmus-andersson` 0.15 | 50% Lindy / 50% Convex |

**Embedded AI Override (`R2`–`R5`):** When an artifact outside `R1` includes any generative or agentic surface, `design-director` injects `agentic-flow-architect: 0.15` and scales base weights by `0.85` (exact sum `1.00`).

---

## The 4 Via Negativa Circuit Breakers

| Auditor | Core Failure Modes Vetoed |
|---|---|
| `auditor-cognitive-fatigue` | `>4` ungrouped Cowan chunks, Hick-Hyman choice bloat, `>14` form elements (Baymard), hidden modes, `>3x` KLM tax |
| `auditor-latency-broken-states` | Missing UI Stack states (Ideal/Blank/Loading/Partial/Error), `>50 ms` input / `>100 ms` ack / `>200 ms` INP (>500 ms fail), missing rollback or double-submit guard |
| `auditor-physics-accessibility` | WCAG 2.2 AA failures (`4.5:1`/`3:1`, SC 1.4.1/2.4.11/2.5.7/2.5.8), Fitts penalty, `transition-all` / layout animation, `blur >20 px`, `>300 ms`, missing `prefers-reduced-motion` |
| `auditor-agentic-anti-slop` | Unjustified free-text chat over direct controls, opaque agents without trajectory/diff/undo, stacked visual AI slop (`>=3` signals), **`aud-slop-04` (`veto-central-dynamo`)** |

---

## Quickstart & Multi-Harness Installation

Use `adapters/install.sh` to mount the suite into any supported workspace or global harness directory without colliding with sibling SDLC suites:

```bash
git clone https://github.com/JavierFrancoLeal/best-ui-ux-designers.git
cd best-ui-ux-designers

# Default safe multi-suite installation (registers strictly 1 SKILL.md entry + bundled CPU scanner;
# lazy references renamed to PROFILE.md / AUDITOR.md to defeat recursive **/SKILL.md discovery)
./adapters/install.sh --target all --mode director-only --scope workspace --dest /path/to/your-project

# Run the zero-dependency CPU pre-scanner directly
python3 tools/uiux_cpu_scanner.py --format markdown path/to/component.html

# Preview actions safely without writing files
./adapters/install.sh --target antigravity --mode director-only --scope workspace --dest /path/to/your-project --dry-run
```

Supported `--target` values: `antigravity`, `deepseek`, `claude`, `codex`, `cursor`, `windsurf`, `all`. All rule files use the exact `<suite_id>-` prefix (`ui-ux-bootstrap.md`, `ui-ux-director.mdc`, `ui-ux-director.md`), `AGENTS.md` (and any pre-existing regular `CLAUDE.md`) is updated idempotently via fenced markers (`<!-- BEGIN best-ui-ux-designers -->` ... `<!-- END best-ui-ux-designers -->`), and `install_deepseek` installs `dsh-plugin.json`.

---

## Local Verification (CI / Deterministic Checks)

```bash
pip install -r requirements-dev.txt
python3 validators/validate_repo.py
bash -n adapters/install.sh
bash adapters/install.sh --target all --mode full --scope workspace --dest /tmp/test-uiux-full --dry-run
bash adapters/install.sh --target all --mode director-only --scope workspace --dest /tmp/test-uiux-director --dry-run
```

## Documentation Index

- [docs/architecture.md](docs/architecture.md) — Phase A Blueprint, Solow Paradox Thesis, 6-Stage SDLC Map, 5-Step Deliberation Protocol
- [docs/design-md-spec.md](docs/design-md-spec.md) — Normative `DESIGN.md` v1.0.0 Schema & Illustrative Code Snippet Contract
- [docs/selection-rubric.md](docs/selection-rubric.md) — 4 Binary Admission Filters (Wittgenstein/Lindy) & Via Negativa Blacklist
- [docs/primary-sources-index.md](docs/primary-sources-index.md) — Consolidated Verifiable Primary Sources Index (`00`–`12` + Solow)

## Related Agent Governance & Companion Suites

| Repository | Role | Status |
| :--- | :--- | :--- |
| **[`casebook`](https://github.com/JavierFrancoLeal/casebook)** | Bounded-entropy 4-tier constitutional memory, Open Symptoms Radar & 5-to-1 compaction oracle | **`v1.0.1` Live** |
| **[`dual-brain-guard`](https://github.com/JavierFrancoLeal/dual-brain-guard)** | Harness-agnostic mechanical Proposer != Verifier cross-model guard (`CLI + MCP + hooks`) | **`v1.1.1` Live** |
| **[`autonomy-ladder`](https://github.com/JavierFrancoLeal/autonomy-ladder)** | Evidence-based Traffic-Light autonomy grader (`🟢 / ⚑ / 🟡 / 🔴` & `A/B/C/D` trust scores) | **`v1.0.2` Live** |
| **[`governed-browser`](https://github.com/JavierFrancoLeal/governed-browser)** | Constitutional commit-click brake (`🛑 RED` on Send/Pay/Delete) & SHA-256 hash-chained audit trail | **`v1.0.1` Live** |
| **[`forensic-contracts`](https://github.com/JavierFrancoLeal/forensic-contracts)** | 5-line `@forensic-contract` linter, `@blast-radius` cage enforcer & literal `sourcePin` verifier | **`v1.0.1` Live** |
| **[`agent-governance`](https://github.com/JavierFrancoLeal/agent-governance)** | Complete 26-plugin DeepSeek Harness governance suite (mother repository) | **`v1.0.0` Live** |
| **[`best-security-governance-architects`](https://github.com/JavierFrancoLeal/best-security-governance-architects)** | CPU-first pre-merge security & governance suite (`ECOSYSTEM_CONTRACT v1.2.0`) | **`v1.2.0` Live** |

## License

Released under the [MIT License](LICENSE).
