---
name: auditor-latency-broken-states
description: "Unconditional Via Negativa circuit breaker that vetoes missing UI Stack states (Ideal/Blank/Loading/Partial/Error), latency violations (>50 ms input, >100 ms ack, >200 ms/>500 ms INP, >400 ms/>1000 ms unstreamed), missing optimistic rollback, and double-submit bugs."
license: MIT
compatibility: "Text-only and multimodal coding agents inspecting async React/TSX components, fetch/IPC hooks, submit handlers, and state machines; reads ./rules.yaml."
metadata:
  schema_version: "1.0.0"
  rules_file: "./rules.yaml"
  suite_id: "ui-ux"
  author: "best-ui-ux-designers"
---

# Auditor: Latency & Broken States (`auditor-latency-broken-states`)

Unconditional Via Negativa technical auditor enforcing perceptual latency ceilings and complete async state coverage. Read `./rules.yaml` before evaluating any artifact and emit strictly `PASS`, `CONDITIONAL_BLOCK`, or `HARD_VETO` with exact `file:line` evidence.

## Checks Executed (`./rules.yaml`)
1. `aud-lat-01` (`veto-incomplete-ui-stack`): Async-data view omits any of Scott Hurff's 5 UI Stack states (`Ideal`, `Blank/Empty`, `Loading`, `Partial`, `Error`).
2. `aud-lat-02` (`veto-perceptual-latency-breach`): Input processing `> 50 ms`, initial visual acknowledgment `> 100 ms` (RAIL / Nielsen), or INP p75 `> 500 ms` (`> 200 ms` conditional alert), or sequential `await` chains in critical paths missing `Promise.all` parallelization.
3. `aud-lat-03` (`veto-unstreamed-long-wait`): Operation `> 400 ms` (Doherty target) or `> 1,000 ms` (Nielsen flow break) without early streaming, deterministic progress indicator, or cancellation (`AbortController`).
4. `aud-lat-04` (`veto-unsafe-mutation-or-double-submit`): Optimistic mutation lacking deterministic rollback + visible error recovery on failure, or submit trigger lacking `disabled`/`aria-busy`/in-flight guard against duplicate requests.

## Output Format
Return a deterministic table (`Rule ID | Veto ID | Severity | Status | Evidence (file:line) | Mandatory Remediation`) and total counts `V_hard` and `V_cond`. Escalate to `design-director` (and `systems-harness` if latency originates in backend/state architecture) on any `HARD_VETO`.
