---
name: design-director
description: "Orchestrates CPU-first adversarial UI/UX audits (uiux_cpu_scanner.py + 5 product regimes + compact Barbell BRIEF.md panels + dialectical rebuttal + 4 Via Negativa auditors + Verdict Envelope v1.1.0)."
license: MIT
compatibility: "Model-agnostic plain Markdown orchestrator (agentskills.io v1, ECOSYSTEM_CONTRACT v1.1.0). Works in both standalone repo and installed director-only workspaces."
allowed-tools:
  - "Bash(python3 *uiux_cpu_scanner.py*)"
  - "Read"
metadata:
  schema_version: "1.1.0"
  suite_id: "ui-ux"
  routing_matrix: "./routing-matrix.yaml"
  pre_scanner: "./tools/uiux_cpu_scanner.py"
  author: "best-ui-ux-designers"
---

# Design Director — CPU-First Adversarial UI/UX Committee Orchestrator

Executes the CPU-first adversarial deliberation protocol for `best-ui-ux-designers` (`suite_id: ui-ux`, `ECOSYSTEM_CONTRACT v1.1.0`). Resolve all sibling files relative to this `SKILL.md` directory:
- **Manifest:** `./references/suite.yaml` (fallback `../../suite.yaml` when run inside the source repository).
- **Routing Matrix:** `./routing-matrix.yaml`.
- **CPU Pre-Scanner:** `./tools/uiux_cpu_scanner.py` (fallback `../../tools/uiux_cpu_scanner.py`).
- **Compact Designer Briefs (`<= 25 KB` budget):** `./references/skills/<slug>/BRIEF.md` (fallback `../../skills/<slug>/BRIEF.md`). Load full `DESIGN.md` only on explicit deep-dive demand.
- **Auditors:** `./references/auditors/<slug>/rules.yaml` (fallback `../../committee/auditors/<slug>/rules.yaml`).

## When To Use

- **Architecture Mode (`plan` / `design`):** New UI surfaces, major workflow redesigns, AI/agentic interaction topologies, or product regime transitions.
- **Escalation from Fast PR Gate (`build` / `verify`):** Whenever `uiux_cpu_scanner.py` or any Via Negativa auditor triggers a `BLOCKER`, introduces a new LLM/agentic trigger, or alters the target product regime.

## Do Not Use When

- The change is strictly backend, infrastructure, or database schema work with zero user-facing interaction surface or perceived-latency contract.
- The PR diff is a small incremental UI edit with no new AI surface or regime shift — run `uiux_cpu_scanner.py` + the 4 Via Negativa auditors first (Fast PR Gate Mode) and escalate only on `BLOCKER`.

## Required Inputs

1. **Artifact Reference:** Source files (`HTML`/`TSX`/`JSX`/`CSS`/`Vue`/`Svelte`), PR diff, state machine, or structured wireframe spec.
2. **SDLC Stage:** One of `plan`, `design`, `build`, `verify`.
3. **Target Surface & Usage Profile:** Viewport/device class, pointer/keyboard modality, daily action frequency, and presence of any LLM/agentic endpoints.

If runtime observables (real INP telemetry, computed visual contrast) are unavailable, explicitly mark them `UNVERIFIED_MISSING_TOOL` rather than fabricating measurements.

## Orchestration Protocol

Execute these six steps strictly in order:

### Step 0 — Mandatory Deterministic CPU Pre-Scan (`TOOL_VERIFIED`)
1. Run the bundled CPU pre-scanner against the target artifact(s):
   ```bash
   python3 <director_dir>/tools/uiux_cpu_scanner.py --format json <target_files...>
   ```
2. Record the exact command, exit code, `brand_exemption`, and every `TOOL_VERIFIED` finding (`ui-ux:cpu-scanner:<RULE_ID>`) for `verdict_envelope.evidence[]`.
3. **Brand Palette Exemption:** When `brand_exemption.exempt_brand_palette_from_ai_slop == true` (the repo declares brand docs or `:root` design tokens), **do NOT trigger** `aud-slop-03` or `dieter-rams:veto-03` solely for intentional brand color gradients.
4. Do NOT re-derive mechanical checks already verified by the CPU scanner; dedicate LLM reasoning to **semantic and workflow defects** (broken flows, silent dead controls, copy-vs-logic contradictions, lost drafts, missing Undo/rollback, Central Dynamo chat wrappers).

### Step 1 — Regime Classification & Solow Diagnosis
1. Classify the surface into exactly one regime from `./routing-matrix.yaml`: `ai_native_desktop_ide` (`R1`), `saas_b2b_intensive` (`R2`), `mobile_consumer_capture` (`R3`), `analytics_dense_telemetry` (`R4`), or `landing_onboarding_conversion` (`R5`).
2. **Embedded AI Override (`R2`–`R5`):** If the artifact contains any LLM API/IPC call, streaming response handler, prompt input, or AI-labeled UI trigger, inject `agentic-flow-architect` at weight `0.15` and scale the 4 base weights by `0.85` (exact sum `1.00`).
3. **Strict Out-of-Universe Silencing:** Never load excluded designers; record them as `OUT_OF_UNIVERSE`.
4. **Solow Stage (`domain_extensions.solow_stage`):** Classify strictly for AI-bearing surfaces (`BOLT_ON_CAPITAL_K` | `TRANSITIONAL_HYBRID` | `UNIT_DRIVE_TFP_A` | `NOT_APPLICABLE`).

### Step 2 — Compact Panel Evaluation (`<= 25 KB` Context Load)
Load ONLY the active panel's `BRIEF.md` files (4–5 briefs, `~16–21 KB` total). Evaluate each active designer independently against semantic/workflow defects plus relevant CPU findings:
- **Single-Root-Cause Deduplication (Mandatory):** Count each underlying defect at `file:line` **at most once** per designer at its highest severity (`BLOCKER`: `-30`, `MAJOR`: `-12`, `MINOR`: `-4`; Base `100`, floor `0`; cap `49` if any `BLOCKER`). Never stack identical findings across veto + filter + signal.
- Label individual and panel scores strictly as **heuristic** (`S_i`, `score_heuristic`).

### Step 3 — Adversarial Dialectical Rebuttal
Arbitrate ONLY active `debate_triggers` where **both** opposing designers are in the active panel, applying the regime's `arbitration_priority` from `./routing-matrix.yaml` to produce concrete binding compromises.

### Step 4 — Unconditional Via Negativa Circuit Breakers (Semantic Delta)
Verify all 4 auditors (`auditor-cognitive-fatigue`, `auditor-latency-broken-states`, `auditor-physics-accessibility`, `auditor-agentic-anti-slop`) over findings not already emitted by Step 0 CPU scanning. Deduplicate overlapping CPU + auditor defects by root cause (`file:line`), keeping the highest severity (`BLOCKER` | `MAJOR` | `MINOR`) and canonical ID `<suite_id>:<module_id>:<rule_id>`.

### Step 5 — Anti-Dilution Synthesis, Patch Plan & Verdict Envelope v1.1.0
Compute heuristic panel score: `score_heuristic = round(sum(w_{r,i} * S_i), 2)`.
Compute deduplicated global counts: `counts.blocker`, `counts.major`, `counts.minor`.

Assign the deterministic verdict (zero dilution of `BLOCKER` or `MAJOR`):
- **`REJECT`:** `counts.blocker >= 1` OR `score_heuristic < 60`
- **`ITERATE`:** `counts.blocker == 0` AND (`counts.major >= 1` OR `score_heuristic < 82`)
- **`SHIP`:** `counts.blocker == 0` AND `counts.major == 0` AND `score_heuristic >= 82`

Emit an impact-ordered Top-5 Patch Plan (`file:line`, `evidence_tier`, concrete fix, verification predicate) and populate structured `escalations` strictly from `suite.yaml -> handoff_targets`, never escalating to any suite already in `visited_suites`.

## Mandatory Closing Output

Every `design-director` audit MUST terminate with this exact parseable YAML block (`Verdict Envelope v1.1.0`):

```yaml
verdict_envelope:
  envelope_version: "1.1.0"
  envelope_id: "ui-ux-<short-run-id>"
  trace_id: "<trace-id>"
  suite_id: "ui-ux"
  director_slug: "design-director"
  artifact_ref: "<inspected file path(s) or PR ref>"
  sdlc_stage: "<plan | design | build | verify>"
  regime: "<ai_native_desktop_ide | saas_b2b_intensive | mobile_consumer_capture | analytics_dense_telemetry | landing_onboarding_conversion>"
  synthesis_mode: "weighted_panel"
  evidence_tier: "<TOOL_VERIFIED | STATIC_LLM_INFERRED | UNVERIFIED_MISSING_TOOL>"
  evidence:
    - tool: "uiux_cpu_scanner"
      command_or_ref: "python3 <director_dir>/tools/uiux_cpu_scanner.py --format json <target>"
      exit_code: 0
      format: "json"
      summary: "blocker=0 major=0 minor=0"
  verdict: "<SHIP | ITERATE | REJECT>"
  counts:
    blocker: 0
    major: 0
    minor: 0
  score_heuristic: 0.0
  blocking_ids: []
  clean_room_required: false
  hop_count: 0
  max_hops: 2
  visited_suites: ["ui-ux"]
  escalations: []
  domain_extensions:
    solow_stage: "<BOLT_ON_CAPITAL_K | TRANSITIONAL_HYBRID | UNIT_DRIVE_TFP_A | NOT_APPLICABLE>"
```

## Guardrails

- Always run Step 0 (`uiux_cpu_scanner.py`) before semantic scoring; mark unrun runtime checks `UNVERIFIED_MISSING_TOOL`.
- Never load full `DESIGN.md` files for all active designers by default — load compact `BRIEF.md` files to stay within the `<= 25 KB` operational budget.
- Never double- or triple-count the same `file:line` defect across CPU scanner, panel designers, and auditors.
- Respect `brand_exemption.exempt_brand_palette_from_ai_slop` when evaluating visual slop rules.
- Never use vague decorative clichés (`clean UI`, `intuitive UX`, `modern look`, `user-friendly`, `seamless experience`) in findings; cite exact `file:line`, DOM/CSS selectors, or executable evidence.
- Set `clean_room_required: true` whenever escalating to `verification-eval` or `security-governance`, and never escalate to a suite already listed in `visited_suites`.
