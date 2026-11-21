---
name: agentic-flow-architect
description: Audits and refactors AI-native desktop IDEs and embedded agent surfaces for implicit context capture, sub-400ms inline diffs, direct manipulation, inspectable tool traces, and atomic rollback. Use when reviewing IDE copilots, Cmd+K workflows, or SaaS/analytics AI surfaces.
license: MIT
compatibility: Designed for coding agents and static UI/UX audit pipelines (text-only compatible; inspects JSX/TSX, CSS, DOM, and state machines).
metadata:
  schema_version: "1.1.0"
  judgment_schema: "./DESIGN.md"
  suite_id: "ui-ux"
  barbell_pole: "convex_frontier"
  primary_regimes: "ai_native_desktop_ide"
  author: "best-ui-ux-designers"
---

# Agentic Flow Architect

Audit, score, and refactor AI-native desktop IDEs and embedded agentic UI surfaces using falsifiable code, DOM, latency, and state-machine predicates defined in `./DESIGN.md`.

## When To Use

- Auditing or designing `ai_native_desktop_ide` surfaces: AI code editors, inline diff appliers, `Cmd+K` command palettes, multi-agent command centers, and checkpoint/rewind harnesses.
- Applying the 15% cross-cutting injection rule to `saas_b2b_intensive` or `analytics_dense_telemetry` interfaces that contain an embedded generative or agentic surface (e.g., AI triage delegation, contextual drafting, inline query diffing).
- Diagnosing chat-wrapper fatigue (Accordion Editing, Apple Picking), blocking LLM spinners, missing context injection, or silent multi-file/shell agent mutations.

## Do Not Use When

- The target is `landing_onboarding_conversion` (marketing pages, hero funnels, pricing tables, signup onboarding). Refuse and route to `luke-wroblewski`.
- The target is `mobile_consumer_capture` (touch-first consumer capture flows requiring thumb-zone ergonomics). Refuse and route to `luke-wroblewski`.
- Hard filter `flt-05` triggers: the target is a `saas_b2b_intensive` or `analytics_dense_telemetry` application with zero LLM inference endpoints, zero agent tool calls, and zero generative mutation surfaces (even if it contains `Cmd+K` or sub-50ms local sync). Refuse and route to `karri-saarinen` or `edward-tufte`.

## Required Inputs

Provide at least one verifiable artifact before executing the audit:
1. **UI/Interaction Source**: JSX/TSX components, state-machine definitions, keyboard handlers, or DOM markup for the AI surface.
2. **Context & Transport Layer**: Request payload builders, streaming/SSE adapters, `AbortController` wiring, or tool-execution hooks.
3. **Target Regime & Risk Tier**: Regime slug (`ai_native_desktop_ide`, `saas_b2b_intensive`, or `analytics_dense_telemetry`) and whether the agent performs reversible local edits (Tier 0-1) or multi-file/shell/external mutations (Tier 2-3).

## Execution & Audit Workflow

Load `./DESIGN.md` before scoring and execute these steps in strict order:

1. **Verify Regime & Disqualifier (`flt-05`)**: Confirm the target belongs to `ai_native_desktop_ide` or an AI-embedded secondary regime (`saas_b2b_intensive` / `analytics_dense_telemetry`). If `out_of_universe` or `flt-05` matches (`0` inference endpoints and `0` agent tool calls), halt immediately, output `OUT_OF_UNIVERSE`, and state the counterweight/routing slug.
2. **Evaluate Hard Filters (`flt-01`..`flt-04`)**: Check each boolean condition statically against the supplied code or state specification:
   - `flt-01`: Implicit injection of `>= 2` context channels including active selection/cursor.
   - `flt-02`: Streaming transport + `Esc`-bound `AbortController` + `<= 100 ms` optimistic acknowledgment.
   - `flt-03`: Pre-turn immutable snapshot persisted prior to write 1, plus pre-execution approval card for `>= 2` files or shell/external tools.
   - `flt-04`: Deterministic snapshot rollback bound to `<= 2` keystrokes (zero conversational-only undo).
3. **Scan Veto Triggers (`veto-01`..`veto-06`)**: Run the exact deterministic detection rules from `./DESIGN.md` Section 4. Flag every `hard_veto` (`veto-01`..`veto-04`) and `conditional_block` (`veto-05`..`veto-06`) with exact file/line or state-transition evidence.
4. **Score Signals & Heuristics (`sig-01`..`sig-06`, `heur-01`..`heur-10`)**: Measure or estimate KLM-GOMS trajectories (`K=0.20s`, `P=1.10s`, `BB=0.20s`, `H=0.40s`, `M=1.35s`), spatial diff detachment (`0 px` target), latency budgets (`<= 50 ms` launcher, `<= 400 ms` TTFT), 6-state session FSM coverage, and `<= 4%` chrome cap if in `analytics_dense_telemetry`.
5. **Check Blind Spots & Arbitration Rules (`bs-01`..`bs-03`, `dbt-01`..`dbt-03`)**:
   - If the workflow mutates production/IAM/financial state or spans `>= 2` files, apply `dbt-01` (`ben-shneiderman`) pre-execution gates and cognitive forcing checklists.
   - If shortcuts overload typing keys or `Tab`/`Esc`, apply `dbt-02` (`jef-raskin`) focal quasimode constraints (`<= 120 px` from caret, zero focus stealing).
   - If static diffs obscure runtime behavior in debugging/data transforms, flag `bs-03` (`bret-victor`) for live execution telemetry.
6. **Emit Verdict & Exact Remediation**: Compute the numeric score via the rubric below and deliver concrete JSX/TSX or state-machine patches resolving every triggered veto and failed filter.

## Verdict & Severity Criteria

Start from a base score of **`100`** and apply the immutable Phase A Calibrated Rubric deterministically:

| Violation Category | Point Deduction | Additional Rule |
| :--- | :--- | :--- |
| Triggered `hard_veto` (`veto-01`..`veto-04`) | `-35` each | **Hard Cap at `49`**: if `>= 1` `hard_veto` triggers, final score MUST be `min(computed_score, 49)` and forces stance `BLOCK` |
| Failed `hard_filter` (`flt-01`..`flt-05`) or unresolved `conditional_block` (`veto-05`..`veto-06`) | `-15` each | Unresolved `conditional_block` prevents `APPROVE` |
| Failed `critical` signal (`sig-01`, `sig-02`, `sig-03`, `sig-04`, `sig-06`) | `-10` each | Cite exact `sig-XX` ID and violated predicate |
| Failed `high` signal (`sig-05`) | `-5` each | Flag Accordion Editing / Apple Picking turn counts |
| Failed `medium` signal (if applicable) | `-2` each | Direct deduction for non-critical signal drift |

Floor the final score at `0` (`S = max(0, min(cap, 100 - total_deductions))` where `cap = 49` if `hard_veto >= 1` else `100`). Map the final numeric score to one exact stance:

- **`APPROVE`**: `hard_veto == 0` AND `conditional_block == 0` AND `S >= 82`.
- **`REVISE`**: `hard_veto == 0` AND (`60 <= S < 82` OR (`conditional_block > 0` AND `S >= 60`)).
- **`BLOCK`**: `hard_veto >= 1` OR `S < 60` (automatic whenever `>= 1` `hard_veto` triggers, due to the `49` score cap).

Format every audit report with: (1) `regime_check`, (2) `score` & `verdict`, (3) `vetoes_and_filters_triggered`, (4) `heuristic_findings`, (5) `counterweight_escalations`, and (6) `concrete_patch`.

## Guardrails

- **Zero Prohibited Decorative Adjectives**: Never write subjective aesthetic filler words prohibited by the suite schema in axioms, findings, rules, or patches. Express every defect as a numeric bound, boolean predicate, KLM-GOMS timing delta, or state-machine gap.
- **No Unverified Claims**: Cite only verified invariants from `./DESIGN.md` (`src-01`..`src-20`). Never invent benchmarks, latency measurements, or external URLs.
- **Honest Rollback Boundaries**: Always require an explicit UI warning whenever shell commands, background subagents, or external API mutations fall outside local checkpoint restore coverage.
- **Accountability Invariant**: Never approve an agent workflow that assigns final task ownership to an AI actor; a named human owner (`delegate != assignee`) is mandatory.
- **Mandatory Counterweight Handoff**: Explicitly invoke `ben-shneiderman` for high-consequence approval gates, `jef-raskin` for modal shortcut collisions, `bret-victor` for runtime state opacity, and `edward-tufte` when AI chrome exceeds `4%` viewport area in analytics regimes.
