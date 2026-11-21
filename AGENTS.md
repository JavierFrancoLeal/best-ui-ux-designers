# AGENTS.md — `best-ui-ux-designers` Routing & Guardrails

Portable, CPU-first adversarial UI/UX judgment suite (`suite_id: ui-ux`, `ECOSYSTEM_CONTRACT v1.1.0`). Mechanical HTML/CSS/JS/accessibility checks execute deterministically via `tools/uiux_cpu_scanner.py` before semantic LLM review.

## Dual-Mode Pre-Merge Routing

1. **Fast PR Gate Mode (`build` / `verify` — incremental UI diffs):**
   - Run `python3 tools/uiux_cpu_scanner.py --format json <files...>` first (`TOOL_VERIFIED`).
   - Run the 4 Via Negativa auditors (`committee/auditors/*/rules.yaml` or `design-director/references/auditors/*/rules.yaml`) for semantic delta checks (`auditor-cognitive-fatigue`, `auditor-latency-broken-states`, `auditor-physics-accessibility`, `auditor-agentic-anti-slop`).
   - Escalate to `design-director` on any `BLOCKER`, new AI/LLM surface, or regime shift.

2. **Architecture Mode (`plan` / `design` — new surfaces, redesigns, AI workflows):**
   - Load `committee/design-director/SKILL.md` and `./routing-matrix.yaml`.
   - Execute the 6-step protocol: Step 0 CPU pre-scan → Step 1 Regime (`R1`–`R5`) + 15% AI override + `solow_stage` → Step 2 Compact `BRIEF.md` panel (`<= 25 KB` total; never load `OUT_OF_UNIVERSE` profiles) → Step 3 Dialectical rebuttal → Step 4 Via Negativa semantic delta → Step 5 Anti-dilution verdict (`SHIP` | `ITERATE` | `REJECT`) + `Verdict Envelope v1.1.0`.

## Mandatory Invariants

- **CPU Before LLM:** Never guess syntax, undefined JS calls, `prefers-reduced-motion`, or DOM attributes by eye when `tools/uiux_cpu_scanner.py` can verify them deterministically.
- **Single-Root-Cause Deduplication:** Count each `file:line` defect at most once at its highest severity (`BLOCKER` `-30`, `MAJOR` `-12`, `MINOR` `-4`; heuristic score only).
- **Zero Dilution:** Any `BLOCKER >= 1` forces `REJECT`; any unresolved `MAJOR >= 1` prohibits `SHIP` (forces `ITERATE`).
- **Brand Palette Exemption:** Exempt declared project brand tokens (`brand_exemption.exempt_brand_palette_from_ai_slop == true`) from visual AI slop rules.
- **Terminable Handoffs:** Populate `verdict_envelope.escalations[]` strictly from `suite.yaml -> handoff_targets`, never escalating to any suite already in `visited_suites`.
