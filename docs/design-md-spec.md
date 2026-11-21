# Normative Specification — `DESIGN.md` v1.0.0

Every designer package under `skills/<slug>/` consists of three deterministic files:
1. `SKILL.md` — `agentskills.io` v1 operational entry point (`<= 500` lines, `description <= 320` chars, exact 6 literal `##` headings, immutable Phase A Calibrated Rubric).
2. `DESIGN.md` — Hybrid YAML frontmatter + structured 8-section Markdown judgment specification validated against `validators/schema_design.json` (JSON Schema Draft 2020-12).
3. `evals/evals.json` — Minimum 5 deterministic test cases (`>= 3` `expected_trigger: true`, `>= 2` `expected_trigger: false` / `HANDOFF`) with structured `expected_output` objects.

---

## 1. YAML Frontmatter Contract (`schema_version: "1.0.0"`)

All 12 `skills/<slug>/DESIGN.md` files MUST declare valid YAML frontmatter (strict 2-space indentation) conforming to `validators/schema_design.json`:

| Root Key | Cardinality | Key Constraints & Strict Enums |
|---|---|---|
| `schema_version` | Required (`"1.0.0"`) | Exact SemVer string `"1.0.0"` |
| `identity` | Required (object) | `slug` (`^[a-z0-9]+(-[a-z0-9]+)*$`, `<= 64` chars, matching parent folder), `display_name`, `barbell_pole` (`lindy_anchor \| convex_frontier`), `archetype_synthetic` (bool), `primary_domain`, `core_axiom` (1 falsifiable sentence, `<= 220` chars, zero banned clichés), `active_era`, `skin_in_the_game_evidence` (`>= 2` items with `artifact`, integer `year`, `verifiable_metric`, valid `source_id`) |
| `regime_fit` | Required (object) | Strict regime enum: `ai_native_desktop_ide`, `saas_b2b_intensive`, `mobile_consumer_capture`, `analytics_dense_telemetry`, `landing_onboarding_conversion`. Keys: `primary_regimes` (`>= 1`), `secondary_regimes` (`>= 0`), `out_of_universe_regimes` (`>= 1` objects `{regime, reason}`) |
| `high_weight_signals` | Required (`>= 4` items) | `id` (`^sig-[0-9]{2}$`), `name` (`snake_case`), `weight` (`critical \| high \| medium`), `category` (`latency_perception \| cognitive_load \| information_density \| interaction_physics \| visual_semiotics \| agentic_trust \| conversion_ergonomics`), `detects_before_others`, `observable_indicator`, `threshold`, `direction` (`lower_is_better \| higher_is_better \| exact_match \| boolean_required`), valid `source_id` |
| `hard_filters` | Required (`>= 3` items) | `id` (`^flt-[0-9]{2}$`), `name`, `gate_type` (`required \| disqualifier`), `condition`, `failure_impact` |
| `veto_triggers` | Required (`>= 3` items) | `id` (`^veto-[0-9]{2}$`), `name`, `severity` (`hard_veto \| conditional_block`), `target_antipattern`, `detection_rule`, `mandatory_remediation` |
| `concrete_heuristics` | Required (`>= 5` items) | `id` (`^heur-[0-9]{2}$`), `rule_statement` (IF/THEN, zero banned clichés), `metric_or_bound`, `verification_method` (`static_code_audit \| runtime_telemetry \| klm_goms_estimate \| visual_dom_inspection \| state_matrix_check`), `applies_to` (subset of valid regimes), valid `source_id` |
| `blind_spots` | Required (`>= 2` items) | `id` (`^bs-[0-9]{2}$`), `failure_mode`, `trigger_context`, `counterweight_designer` (must exist in the official 12-slug roster) |
| `debate_triggers` | Required (`>= 2` items) | `id` (`^dbt-[0-9]{2}$`), `opposing_designer` (must exist in the official 12-slug roster), `conflict_axis` (`snake_case`), `this_designer_stance`, `opposing_stance`, `arbitration_rule` |
| `primary_sources` | Required (`>= 3` items) | `id` (`^src-[0-9]{2}$`), `title`, `author_or_org`, integer `year`, `source_type` (`book \| peer_reviewed_paper \| engineering_post \| shipped_oss_repo \| primary_talk \| official_standard \| empirical_benchmark`), `url_or_identifier`, `extracted_invariant` |
| `markdown_contract` | Required (object) | `required_sections_order`: exact 8 literal `##` headings listed in Section 2 below |

### Referential & Anti-Cliché Integrity
- Every `source_id` in `skin_in_the_game_evidence`, `high_weight_signals`, and `concrete_heuristics` MUST resolve to an `id` declared in `primary_sources`.
- Every `counterweight_designer` and `opposing_designer` MUST belong to the canonical 12-slug roster.
- Operational YAML fields (`identity.core_axiom`, `high_weight_signals`, `hard_filters`, `veto_triggers`, `concrete_heuristics`) MUST contain zero banned decorative clichés (`clean`, `intuitive`, `modern`, `user-centered`, `user-friendly`, `seamless`, and Spanish equivalents), enforced by `validators/check_anti_cliche.py`.

---

## 2. Mandatory Markdown Body Structure (8 Fixed Sections)

Immediately following the closing `---` frontmatter fence (separated by a blank line), every `DESIGN.md` MUST contain these exact eight `##` headings in strict order:

1. `## 1. Operational Worldview`
2. `## 2. Regime Boundaries & Out-of-Universe Rationale`
3. `## 3. Signal Detection Protocol`
4. `## 4. Hard Filters & Veto Playbook`
5. `## 5. Executable Heuristics & Code Patterns`
6. `## 6. Blind Spots & Counterweights`
7. `## 7. Adversarial Debate Positions`
8. `## 8. Primary Source Notes`

---

## 3. Section 5 TSX/CSS Code Patterns Contract (Illustrative Snippets)

The TSX, TypeScript, JSX, HTML, SVG, and CSS blocks embedded inside **Section 5 (`## 5. Executable Heuristics & Code Patterns`)** of each `DESIGN.md` are **normative illustrative reference snippets in Markdown**, not a standalone compiled Node/TypeScript workspace package.

- **Purpose:** Demonstrate concrete *Before (Vetoed)* vs. *After (Compliant)* structural, DOM, ARIA, state-machine, and CSS token transformations that coding agents adapt to the target repository's real framework and build system.
- **Validation Scope:** Repository CI (`validators/validate_repo.py`) validates YAML schema compliance, referential integrity, Markdown section contracts, and balanced syntax hygiene (including repairing line-split logical operators such as `||` and balanced code fences), without requiring a local `node`/`tsc` toolchain to type-check illustrative documentation snippets.
- **Adaptation Rule:** When applying a Section 5 pattern to a production codebase, the executing coding agent MUST adapt imports, types, and state bindings to the target project's actual compiler and test suite.
