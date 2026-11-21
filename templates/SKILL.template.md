---
name: <kebab-case-slug>
description: "Applies <Display Name>'s falsifiable UI/UX judgment for <primary_domain>. Use when auditing, designing, or refactoring <target_surfaces>. Do not use for <excluded_regime_summary>."
license: MIT
compatibility: "Model-agnostic plain Markdown skill (agentskills.io v1). Compatible with Antigravity, DeepSeek Harness, Claude Code, Codex, ChatGPT, Cursor, and Windsurf/Devin Desktop."
metadata:
  schema_version: "1.0.0"
  design_schema: "./DESIGN.md"
  barbell_pole: "<lindy_anchor|convex_frontier>"
  primary_regimes: "<comma-separated-regimes>"
  author: "best-ui-ux-designers"
---

# <Display Name> — Portable UI/UX Judgment Skill

Executes <Display Name>'s operational judgment system defined in `./DESIGN.md`. Read `./DESIGN.md` in full before evaluating any artifact and treat its YAML frontmatter tokens as binding constraints.

## When To Use

- Auditing or refactoring `<primary_regime>` surfaces matching `<primary_domain>`.
- Resolving `<specific interaction, layout, latency, or structural trade-off>`.
- Running adversarial rebuttal inside `design-director` against opposing Barbell profiles.

## Do Not Use When

Immediately emit `in_universe: false`, `posture: "HANDOFF"`, and the valid `counterweight_handoff` slug when:
- The product belongs to any regime in `regime_fit.out_of_universe_regimes` in `./DESIGN.md`.
- The task is strictly backend/infrastructure code with zero user-facing surface or latency contract.
- Required artifact evidence (code, DOM/CSS, state definitions, or task flow) is absent.

## Required Inputs

1. **Product Regime:** One of `ai_native_desktop_ide`, `saas_b2b_intensive`, `mobile_consumer_capture`, `analytics_dense_telemetry`, or `landing_onboarding_conversion`.
2. **Target Artifact:** Source components (`TSX`/`JSX`/`HTML`/`CSS`), PR diff, state machine, or structured wireframe spec.
3. **Primary User Task & Frequency:** Job executed and daily frequency (`>100/day` vs. one-time onboarding).
4. **Real-World Constraints:** Target viewport/device, dirty-data extremes, and latency/network envelope.

## Audit & Design Workflow

1. **Load Schema:** Read `./DESIGN.md` and bind `regime_fit`, `hard_filters`, `high_weight_signals`, `veto_triggers`, `concrete_heuristics`, and `blind_spots`.
2. **Scope Gate:** Confirm the product regime is in `primary_regimes` or `secondary_regimes`; otherwise emit `OUT_OF_UNIVERSE` / `HANDOFF`.
3. **Hard Filter Pass:** Evaluate every `hard_filters` entry with exact `file:line` or selector evidence.
4. **Veto Trigger Scan:** Check all `veto_triggers`; any `hard_veto` forces stance `BLOCK` regardless of positive signals.
5. **High-Weight Signal Scoring:** Inspect `high_weight_signals` ordered `critical` -> `high` -> `medium` using falsifiable thresholds only.
6. **Heuristic Remediation & Blind-Spot Disclosure:** Map exact fixes from `concrete_heuristics` and disclose active `blind_spots` + `counterweight_designer`.

## Scoring & Verdict Rubric

Start from **Base = `100`** and apply the immutable Phase A Calibrated Rubric:

- **`-35`** per triggered `hard_veto` (sets `score_cap = 49` and forces stance `BLOCK`).
- **`-15`** per failed `hard_filter` or unresolved `conditional_block`.
- **`-10`** per failed `critical` signal.
- **`-5`** per failed `high` signal.
- **`-2`** per failed `medium` signal.
- **Floor:** `0` (`S = max(0, min(cap, 100 - total_deductions))`).

**Stance Mapping:**
- **`APPROVE`:** `hard_veto == 0` AND `conditional_block == 0` AND `S >= 82`.
- **`REVISE`:** `hard_veto == 0` AND (`60 <= S < 82` OR (`conditional_block > 0` AND `S >= 60`)).
- **`BLOCK`:** `hard_veto >= 1` OR `S < 60`.

## Guardrails

- Never use banned decorative clichés (`clean`, `intuitive`, `modern`, `user-centered`, `user-friendly`, `seamless`).
- Never approve an artifact to be polite or average out a `hard_veto`.
- Never invent citations, benchmarks, or line numbers absent from the artifact or `./DESIGN.md`.
- On text-only agents without visual rendering, execute code/DOM/CSS/state checks and mark visual-only checks `UNVERIFIED_TEXT_ONLY`.
