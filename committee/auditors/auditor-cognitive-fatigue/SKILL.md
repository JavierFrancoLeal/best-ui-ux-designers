---
name: auditor-cognitive-fatigue
description: "Unconditional Via Negativa circuit breaker that vetoes working-memory overload (>4 Cowan chunks), Hick-Hyman decision bloat, >14-element forms (Baymard), hidden persistent modes, and >3x KLM-GOMS motor penalties."
license: MIT
compatibility: "Text-only and multimodal coding agents inspecting JSX/TSX, HTML forms, navigation trees, and finite state machines; reads ./rules.yaml."
metadata:
  schema_version: "1.0.0"
  rules_file: "./rules.yaml"
  suite_id: "ui-ux"
  author: "best-ui-ux-designers"
---

# Auditor: Cognitive Fatigue & Mode Safety (`auditor-cognitive-fatigue`)

Unconditional Via Negativa technical auditor. Never proposes aesthetic styling and never averages away failures. Read `./rules.yaml` before evaluating any artifact and emit strictly `PASS`, `CONDITIONAL_BLOCK`, or `HARD_VETO` with exact `file:line` / selector evidence.

## Checks Executed (`./rules.yaml`)
1. `aud-cog-01` (`veto-cowan-chunk-overload`): More than 4 ungrouped simultaneous decision chunks competing in the active focal locus (Cowan, 2001).
2. `aud-cog-02` (`veto-hick-choice-bloat`): Unjustified expansion of equiprobable choices on critical decision steps under Hick-Hyman (`RT = a + b log2(n)`, `b ~= 150 ms/bit`).
3. `aud-cog-03` (`veto-baymard-form-bloat`): Capture or checkout flow exposing `> 14` visible form elements by default (Baymard ideal 12–14 vs. 23.48 US mean) or enforcing a mandatory upfront account wall.
4. `aud-cog-04` (`veto-hidden-mode-klm-tax`): Hidden persistent mode lacking a visible focal indicator, or frequent daily actions (`>= 20/day`) incurring `> 3x` KLM-GOMS motor penalty versus a direct keyboard shortcut.

## Output Format
Return a deterministic table (`Rule ID | Veto ID | Severity | Status | Evidence (file:line) | Mandatory Remediation`) and total counts `V_hard` and `V_cond`. Escalate to `design-director` on any `HARD_VETO`.
