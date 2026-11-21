---
schema_version: "1.0.0"

identity:
  slug: "<kebab-case-id-matching-folder-name>"
  display_name: "<Full Name or Synthetic Archetype Label>"
  barbell_pole: "lindy_anchor"
  archetype_synthetic: false
  primary_domain: "<Non-overlapping operational domain of competence>"
  core_axiom: "<Single falsifiable 1-sentence law; max 220 chars; zero decorative clichés>"
  active_era: "<e.g., 1955-1995 or 2019-present>"
  skin_in_the_game_evidence:
    - artifact: "<Shipped product, OSS library, hardware system, or seminal standard>"
      year: 1984
      verifiable_metric: "<Adoption, retention, longevity, or forced competitor imitation metric>"
      source_id: "src-01"
    - artifact: "<Second verifiable shipped artifact>"
      year: 1995
      verifiable_metric: "<Verifiable empirical metric>"
      source_id: "src-02"

regime_fit:
  primary_regimes:
    - "saas_b2b_intensive"
  secondary_regimes: []
  out_of_universe_regimes:
    - regime: "landing_onboarding_conversion"
      reason: "<Falsifiable structural reason why applying this model causes UX harm in this regime>"

high_weight_signals:
  - id: "sig-01"
    name: "<machine_snake_case_signal>"
    weight: "critical"
    category: "latency_perception"
    detects_before_others: "<Exact structural flaw or opportunity this expert notices immediately>"
    observable_indicator: "<Verifiable condition in code, CSS, DOM, telemetry, or interaction flow>"
    threshold: "<Measurable numeric bound or boolean condition>"
    direction: "lower_is_better"
    source_id: "src-01"

hard_filters:
  - id: "flt-01"
    name: "<machine_snake_case_filter>"
    gate_type: "required"
    condition: "<Falsifiable boolean expression or quantitative gate>"
    failure_impact: "<Observable degradation for real users under dirty data, latency, or fatigue>"

veto_triggers:
  - id: "veto-01"
    name: "<machine_snake_case_veto>"
    severity: "hard_veto"
    target_antipattern: "<Typical AI/SaaS pattern destroyed immediately by this expert>"
    detection_rule: "<Deterministic check verifiable in code, DOM, CSS, or flow without subjective aesthetics>"
    mandatory_remediation: "<Concrete falsifiable change required to lift the veto>"

concrete_heuristics:
  - id: "heur-01"
    rule_statement: "<Falsifiable IF/THEN operational rule; zero decorative adjectives>"
    metric_or_bound: "<Exact numeric or structural bound>"
    verification_method: "static_code_audit"
    applies_to:
      - "saas_b2b_intensive"
    source_id: "src-01"

blind_spots:
  - id: "bs-01"
    failure_mode: "<Specific condition where this expert's dogma degrades real UX>"
    trigger_context: "<Product context, task type, or user cohort that activates this blind spot>"
    counterweight_designer: "don-norman"

debate_triggers:
  - id: "dbt-01"
    opposing_designer: "edward-tufte"
    conflict_axis: "<snake_case_axis>"
    this_designer_stance: "<Falsifiable stance defended by this profile>"
    opposing_stance: "<Falsifiable counter-stance defended by opposing_designer>"
    arbitration_rule: "<Regime-dependent quantitative tie-breaker for Design Director>"

primary_sources:
  - id: "src-01"
    title: "<Exact title of book, paper, engineering post, talk, standard, or shipped repo>"
    author_or_org: "<Primary author or organization>"
    year: 2024
    source_type: "engineering_post"
    url_or_identifier: "<Verifiable URL, DOI, or ISBN>"
    extracted_invariant: "<Specific falsifiable rule or empirical number grounded in this source>"

markdown_contract:
  required_sections_order:
    - "1. Operational Worldview"
    - "2. Regime Boundaries & Out-of-Universe Rationale"
    - "3. Signal Detection Protocol"
    - "4. Hard Filters & Veto Playbook"
    - "5. Executable Heuristics & Code Patterns"
    - "6. Blind Spots & Counterweights"
    - "7. Adversarial Debate Positions"
    - "8. Primary Source Notes"
---

## 1. Operational Worldview

<Falsifiable synthesis of how this designer models interaction physics, cognition, or structure.>

## 2. Regime Boundaries & Out-of-Universe Rationale

<Explicit in-universe vs. out-of-universe structural boundaries.>

## 3. Signal Detection Protocol

<Ordered inspection protocol mapping `sig-01`..`sig-NN` to deterministic code/DOM/CSS predicates.>

## 4. Hard Filters & Veto Playbook

<Pass/fail gates and deterministic remediation rules for `flt-01`..`flt-NN` and `veto-01`..`veto-NN`.>

## 5. Executable Heuristics & Code Patterns

<Illustrative Before (Vetoed) and After (Compliant) TSX/CSS/HTML reference snippets.>

## 6. Blind Spots & Counterweights

<Documented failure modes of this designer's own invariants and the valid counterweight slugs that check them.>

## 7. Adversarial Debate Positions

<Pre-programmed rebuttal positions and quantitative regime tie-breakers.>

## 8. Primary Source Notes

<Traceable primary-source citations anchored to `src-01`..`src-NN`.>
