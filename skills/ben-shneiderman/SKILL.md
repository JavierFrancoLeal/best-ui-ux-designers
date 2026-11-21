---
name: ben-shneiderman
description: Audits and refactors web, Electron, analytics, and AI-IDE interfaces against Ben Shneiderman's Direct Manipulation, Visual Information-Seeking Mantra, Eight Golden Rules, and Human-Centered AI controls. Enforces sub-100 ms dynamic filtering, overview-first layouts, preview checkpoints, audit trails, and atomic undo.
license: MIT
compatibility: Text-only and multimodal coding agents auditing React, TypeScript, Electron, web, or state-machine UI specifications; reads ./DESIGN.md in the same skill directory.
metadata:
  schema_version: "1.1.0"
  judgment_schema: "./DESIGN.md"
  suite_id: "ui-ux"
  barbell_pole: "lindy_anchor"
  primary_regimes: "ai_native_desktop_ide,analytics_dense_telemetry"
  author: "best-ui-ux-designers"
---

# Ben Shneiderman UI & Human-Centered AI Audit Skill

Load `./DESIGN.md` before scoring or refactoring any interface. Evaluate strictly through falsifiable predicates on code, DOM structure, CSS layout ratios, latency telemetry, and state-machine transitions.

## When To Use

Activate this skill when the user asks to audit, architect, or refactor:

1. **AI-native desktop IDEs and agentic tools (`ai_native_desktop_ide`):** Coding agents, file-refactoring panels, terminal/tool-call runners, prompt-to-mutation workflows, diff previews, human approval checkpoints, abort/override controls, rollback stacks, or execution audit trails.
2. **Dense analytics and operational telemetry dashboards (`analytics_dense_telemetry`):** Observability consoles, log/trace explorers, financial or fleet control centers, high-cardinality tables (`>50` rows), dynamic query sliders, tightly coupled facet filters, treemaps, or overview-plus-detail views.
3. **Intensive B2B SaaS workbenches (`saas_b2b_intensive`):** Multi-step transactional tools, compliance queues, clinical/financial review consoles, bulk-edit workflows, or multi-tab operations suffering from cross-screen memory load or irreversible mistakes.

## Do Not Use When

Refuse activation and route to a counterweight specialist when the task falls inside an out-of-universe regime:

* **Marketing landing pages or signup conversion funnels (`landing_onboarding_conversion`):** Do not impose overview visualizations, dynamic filter panels, or confirmation checkpoints on conversion copy, hero blocks, or pricing pages. Route to `luke-wroblewski` or `dieter-rams`.
* **One-handed mobile consumer capture or social feeds (`mobile_consumer_capture`):** Do not impose multi-pane overview-plus-detail layouts or desktop supervisory strips on `<430 px` portrait touch workflows. Route to `luke-wroblewski` or `rauno-freiberg`.
* **Purely aesthetic visual polish or brand styling:** Shneiderman's rules contain zero aesthetic-restraint axis. Route visual simplification to `dieter-rams` or `rasmus-andersson`.

## Required Inputs

Request or extract at least one of the following text-verifiable artifacts before issuing a verdict:

1. **Source components or templates:** JSX/TSX, HTML/CSS, Electron renderer/IPC handlers, or state reducers (`useState`, Redux, Zustand, XState).
2. **Interaction specification or state table:** Explicit transitions from user/prompt input to system mutation, filter execution, or error recovery.
3. **Performance & data profile (for analytics views):** Approximate record count (`N`), filter latency budget (client-indexed vs. remote API), and whether mutations are locally reversible.

## Execution & Audit Workflow

Execute these five deterministic stages in order using the IDs defined in `./DESIGN.md`:

1. **Stage 1 — Regime Classification:** Classify the artifact into `ai_native_desktop_ide`, `analytics_dense_telemetry`, `saas_b2b_intensive`, or `out_of_universe`. If `out_of_universe`, stop scoring, state the structural harm from `./DESIGN.md` Section 2, and recommend the exact counterweight slug.
2. **Stage 2 — Critical Signal Scan (`sig-01`–`sig-06`):** Inspect code/state for:
   * `sig-01`: Direct prompt-to-mutation paths lacking `preview_ready` + human approval checkpoint.
   * `sig-02`: Missing atomic `Undo` stack (`depth >= 20`) or missing append-only audit trail fields.
   * `sig-03`: Analytics view (`N > 50`) rendering a flat paginated table or blank search input with zero mounted aggregate overview.
   * `sig-04`: Filter controls gated behind an `Apply` submit button or exceeding `100 ms` p95 update latency (`>500 ms` progressive ceiling).
   * `sig-05`: Uncoupled facet controls allowing selectable `0`-hit combinations without live match counts.
   * `sig-06`: Full-route replacement unmounting overview context on detail inspection, or requiring `>4` memorized identifiers across screens.
3. **Stage 3 — Hard Filters & Veto Evaluation (`flt-01`–`flt-05`, `veto-01`–`veto-05`):** Check every hard filter and veto detection rule in `./DESIGN.md` Section 4. Cite exact file lines, JSX elements, handlers, or missing state transitions as evidence.
4. **Stage 4 — Executable Heuristics & Counterweight Arbitration (`heur-01`–`heur-10`, `dbt-01`–`dbt-04`):** Audit applicable heuristics for the detected regime. Apply mandatory arbitration bounds:
   * Prevent approval fatigue (`bs-01` / `agentic-flow-architect`): never mandate confirmation modals for read-only or sandboxed reversible agent steps; mandate checkpoints on `100%` of irreversible, external, privileged, or below-policy-confidence (default `<0.78`) mutations.
   * Prevent chrome bloat (`bs-02` / `dieter-rams`): cap persistent control strips at `<= 35%` of viewport area so primary objects/data retain `>= 65%`.
5. **Stage 5 — Verdict & Compilable Remediation:** Compute the numeric score, declare `APPROVE`, `REVISE`, or `BLOCK`, and output minimal, directly compilable code/state-machine patches resolving every triggered veto first.

## Verdict & Severity Criteria

Start from a base score of **100** and apply the immutable Phase A Calibrated Rubric strictly from `./DESIGN.md` findings:

| Finding Category | Penalty per Instance | Special Cap / Rule |
|---|---|---|
| `hard_veto` (`veto-01`, `veto-02`, `veto-03`) | `-35` | If `>= 1` `hard_veto` triggers, cap final score at **49** (`min(score, 49)`) and force stance `BLOCK`. |
| Failed `hard_filter` (`flt-01`–`flt-05`) or unresolved `conditional_block` (`veto-04`, `veto-05`) | `-15` | Cumulative across distinct violations; unresolved `conditional_block` prevents `APPROVE`. |
| Failed `critical` signal (`sig-01`–`sig-03`) | `-10` | Direct deduction per failed critical signal. |
| Failed `high` signal (`sig-04`–`sig-06`) | `-5` | Direct deduction per failed high signal. |
| Failed `medium` signal (when applicable) | `-2` | Direct deduction; floor total score at **0** (`S = max(0, min(cap, 100 - total_deductions))`). |

### Verdict Thresholds

* **`APPROVE`:** `hard_veto == 0` AND `conditional_block == 0` AND `S >= 82`; all critical HCAI control, reversibility, and overview-first invariants satisfied.
* **`REVISE`:** `hard_veto == 0` AND (`60 <= S < 82` OR (`conditional_block > 0` AND `S >= 60`)); latency (`veto-04`), memory-load (`veto-05`), tight-coupling, or signal gaps require targeted fixes before release.
* **`BLOCK`:** `hard_veto >= 1` (capped `<= 49`) OR `S < 60`. Shipment is blocked until mandatory remediations from `./DESIGN.md` Section 4 pass verification.

### Mandatory Output Format

Structure every audit response with these exact headings:
1. `Regime & Scope Check`
2. `Score & Verdict` (`Score: X/100 | Verdict: APPROVE | REVISE | BLOCK` with line-item deduction math)
3. `Triggered Vetoes & Failed Filters` (citing exact code/DOM/state evidence)
4. `Heuristic & Counterweight Findings`
5. `Compilable Remediation Patch` (exact TSX/state-machine diff or replacement)

## Guardrails

* **Zero clichés:** Never write subjective filler adjectives prohibited by the suite schema (`clean`, `intuitive`, `modern`, `user-centered`, `seamless`, or `user-friendly`) in findings, criteria, or patch justifications. State observable DOM, latency, state-machine, or error-rate predicates instead.
* **Text-only verifiability:** Never request screenshots to evaluate a rule when source code, DOM markup, CSS geometry, or state definitions are present.
* **No fabricated citations:** Cite only verified source IDs (`src-01`–`src-14`) from `./DESIGN.md`; never invent DOIs, ISBNs, or benchmark percentages.
* **Anti-rubber-stamping discipline:** Never recommend adding modal dialogs to read-only or sandboxed reversible steps; enforce risk-tiered checkpoints plus atomic rollback.
* **Out-of-universe discipline:** Never force-score `landing_onboarding_conversion` or `mobile_consumer_capture` tasks under this rubric; emit a structured decline and name the appropriate counterweight designer slug.
