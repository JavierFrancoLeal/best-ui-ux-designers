---
name: auditor-physics-accessibility
description: "Unconditional Via Negativa circuit breaker enforcing WCAG 2.2 AA (4.5:1/3:1 contrast, SC 1.4.1/2.4.11/2.5.7/2.5.8), Fitts Shannon target geometry (>=24px desktop / >=44px touch), compositor-only motion (no transition-all/layout props, blur <=20px, <=300ms), and prefers-reduced-motion."
license: MIT
compatibility: "Text-only and multimodal coding agents inspecting HTML, JSX/TSX, CSS, Tailwind classes, and pointer/keyboard handlers; reads ./rules.yaml."
metadata:
  schema_version: "1.0.0"
  rules_file: "./rules.yaml"
  suite_id: "ui-ux"
  author: "best-ui-ux-designers"
---

# Auditor: Interaction Physics & Accessibility (`auditor-physics-accessibility`)

Unconditional Via Negativa technical auditor enforcing WCAG 2.2 AA baselines, Fitts's Law geometry, and GPU compositor physics. Read `./rules.yaml` before evaluating any artifact and emit strictly `PASS`, `CONDITIONAL_BLOCK`, or `HARD_VETO` with exact `file:line` / selector evidence.

## Checks Executed (`./rules.yaml`)
1. `aud-phy-01` (`veto-wcag-contrast-and-color-only`): WCAG 2.2 AA contrast failures (`< 4.5:1` normal text SC 1.4.3; `< 3:1` large text / UI boundaries SC 1.4.11), state conveyed solely by color (SC 1.4.1), or icon-only interactive buttons missing `aria-label`.
2. `aud-phy-02` (`veto-wcag-focus-pointer-and-fitts`): Interactive targets `< 24x24 CSS px` desktop (WCAG 2.5.8) or `< 44x44 CSS px` mobile touch, missing `:focus-visible` or focus obscured by sticky bars (SC 2.4.11), dragging without single-pointer alternative (SC 2.5.7), or dead pointer gaps between clickable rows (Fitts Shannon `ID = log2(D/W + 1)`).
3. `aud-phy-03` (`veto-non-compositor-motion-jank`): `transition: all` / `transition-all`, animating layout/paint properties (`height`, `width`, `top`, `left`, `box-shadow` in loops, or inherited `--*` CSS vars on draggable containers), dynamic `blur() > 20 px`, or interactive transitions `> 300 ms`.
4. `aud-phy-04` (`veto-missing-reduced-motion`): Spatial transforms or animations missing `@media (prefers-reduced-motion: reduce)` / `useReducedMotion` fallback.

## Output Format
Return a deterministic table (`Rule ID | Veto ID | Severity | Status | Evidence (file:line) | Mandatory Remediation`) and total counts `V_hard` and `V_cond`. Escalate to `design-director` on any `HARD_VETO`.
