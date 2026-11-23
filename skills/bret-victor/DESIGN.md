---
schema_version: "1.0.0"
identity:
  slug: "bret-victor"
  display_name: "Bret Victor"
  barbell_pole: "convex_frontier"
  archetype_synthetic: false
  primary_domain: "Immediate visual feedback, state visibility, live manipulation, and climbing the ladder of abstraction"
  core_axiom: "Every parameter or rule edit in analytical and IDE tools must render live intermediate state within 100 ms without mental simulation, while information views must infer context before asking for input."
  active_era: "2005-present"
  skin_in_the_game_evidence:
    - artifact: "Inventing on Principle (CUSEC keynote and live-environment prototypes)"
      year: 2012
      verifiable_metric: "1,000,000+ views documented on worrydream.com/cv; explicitly credited by Chris Lattner for Apple Xcode 6 Swift Playgrounds (WWDC 2014), by Dan Abramov for React Hot Loader (2014), by Chris Granger for Light Table ($316,720 Kickstarter from 7,317 backers), and by John Resig for rebuilding Khan Academy CS."
      source_id: "src-01"
    - artifact: "Our Choice (15 interactive data graphics for Al Gore's iPad/iPhone book, Push Pop Press)"
      year: 2011
      verifiable_metric: "Winner of the 2011 Apple Design Award; catalyzed the Explorable Explanations paradigm and MIT-licensed Tangle reactive-document library."
      source_id: "src-05"
    - artifact: "Magic Ink: Information Software and the Graphical Interface & BART Widget"
      year: 2006
      verifiable_metric: "BART Widget (built 2005) won the 2007 Apple Design Award (Best Mac OS X Dashboard Widget) and MacWorld's 5-star rating; led to Victor's founding role on Apple's HID Proto team (2007-2010, 70+ experimental interface prototypes, features shipped in Mac OS and iOS)."
      source_id: "src-04"
    - artifact: "Learnable Programming: Designing a programming system for understanding programs"
      year: 2012
      verifiable_metric: "Defined the inline state-projection critique that shaped Light Table 0.3.0 inline results, Swift Playgrounds expression evaluation, and CHI 2024 live-programming AI validation prototypes."
      source_id: "src-02"
regime_fit:
  primary_regimes:
    - "ai_native_desktop_ide"
    - "analytics_dense_telemetry"
  secondary_regimes: []
  out_of_universe_regimes:
    - regime: "saas_b2b_intensive"
      reason: "High-frequency operational CRUD and issue triage rely on keyboard muscle memory (Cmd+K, single-key shortcuts, sub-50 ms optimistic commits); pointer-driven scrubbers and persistent multi-rung simulation panels add KLM homing (0.40 s) and pointing (1.10 s) excise that degrades throughput."
    - regime: "mobile_consumer_capture"
      reason: "Viewports under 430 px cannot co-locate rule definitions, intermediate pipeline state, and parameter-sweep grids simultaneously, while coarse touch occlusion breaks continuous precision parameter scrubbing."
    - regime: "landing_onboarding_conversion"
      reason: "First-visit conversion pages require linear commitment and minimal cognitive branching rather than multi-rung sensitivity exploration or live state-machine inspection."
high_weight_signals:
  - id: "sig-01"
    name: "local_causal_feedback_latency_ms"
    weight: "critical"
    category: "latency_perception"
    detects_before_others: "Detects blind edit-apply-wait cycles and broken cause-and-effect coupling within the first 10 seconds of inspecting rule or parameter handlers."
    observable_indicator: "Measured elapsed time from pointermove/input event on a parameter control to DOM/SVG/canvas paint of updated preview state, or presence of submit-gated preview updates."
    threshold: "<= 16.67 ms per frame for continuous scrubbing; <= 100 ms for discrete parameter toggles"
    direction: "lower_is_better"
    source_id: "src-09"
  - id: "sig-02"
    name: "hidden_intermediate_pipeline_stages"
    weight: "critical"
    category: "cognitive_load"
    detects_before_others: "Detects black-box execution that forces operators to simulate intermediate transformations mentally between input prompt/rules and terminal output."
    observable_indicator: "Count of transformation stages in an agentic or telemetry pipeline that mutate, filter, or drop records without rendering observable DOM state nodes adjacent to the controlling rule."
    threshold: "0 unexposed intermediate stages"
    direction: "lower_is_better"
    source_id: "src-02"
  - id: "sig-03"
    name: "unpreviewed_numeric_parameter_ratio"
    weight: "high"
    category: "interaction_physics"
    detects_before_others: "Detects opaque numeric text boxes that force blind guessing across continuous model thresholds, weights, or token budgets."
    observable_indicator: "Ratio of continuous numeric <input> fields lacking live onChange preview binding and direct scrub/slider affordances (role='slider' or pointer-drag dial) to total continuous numeric parameters."
    threshold: "0.0"
    direction: "lower_is_better"
    source_id: "src-01"
  - id: "sig-04"
    name: "coupled_abstraction_rungs_count"
    weight: "high"
    category: "information_density"
    detects_before_others: "Detects single-rung static dashboards that show aggregate KPIs without exposing temporal trajectories or parameter sensitivity boundaries."
    observable_indicator: "Count of simultaneously navigable and interactively linked abstraction rungs rendered in an analytical workbench (Rung 0 concrete instance, Rung 1 time trajectory, Rung 2 parameter sweep)."
    threshold: ">= 2 coupled rungs with hover-to-step-down inspection"
    direction: "higher_is_better"
    source_id: "src-03"
  - id: "sig-05"
    name: "initial_information_excise_interactions"
    weight: "high"
    category: "interaction_physics"
    detects_before_others: "Detects information software disguised as manipulation software that demands manual dropdown filtering before displaying a relevant graphic."
    observable_indicator: "Minimum count of clicks, dropdown selections, or query submissions required after initial mount (t=0) to render the primary context-relevant data view."
    threshold: "0 interactions when environment or history context is available; <= 1 relative correction"
    direction: "lower_is_better"
    source_id: "src-04"
  - id: "sig-06"
    name: "bidirectional_rule_artifact_traceability"
    weight: "high"
    category: "agentic_trust"
    detects_before_others: "Detects orphaned outputs where engineers cannot verify which rule, retrieved chunk, or code expression caused a specific rendered artifact."
    observable_indicator: "Boolean presence of symmetric hover/focus state binding linking output items (data-source-rule / data-stage-id) back to originating rules or code lines and highlighting affected outputs when focusing a rule."
    threshold: "true"
    direction: "boolean_required"
    source_id: "src-07"
hard_filters:
  - id: "flt-01"
    name: "local_deterministic_scrubbing_boundary"
    gate_type: "required"
    condition: "All continuous scrubbing or onChange live-preview handlers execute strictly against deterministic local state or cached fixtures (<= 16.67 ms/frame) and invoke 0 remote LLM or mutating write APIs until an explicit commit event."
    failure_impact: "Directly wiring 60 Hz pointer events to remote LLM inference (median TTFT 363-2,354 ms in provider API probes) fires up to 120 API calls per 2 s drag, wasting token budget and rendering out-of-order stale states."
  - id: "flt-02"
    name: "explicit_intermediate_state_projection"
    gate_type: "required"
    condition: "Every multi-stage agentic or telemetry transformation pipeline exposes per-stage counts, accepted/rejected items, and computed intermediate values in the DOM alongside the active rule."
    failure_impact: "Operators revert to manual print-debugging or blind over-reliance on AI outputs when runtime transformations remain opaque, elevating NASA-TLX frustration and effort."
  - id: "flt-03"
    name: "context_inferred_initial_information_render"
    gate_type: "required"
    condition: "Read-dominant analytics and telemetry views populate their initial graphical state at mount using environmental context (current time window, active workspace, historical baseline) with >= 1 rendered data graphic before user input."
    failure_impact: "Users suffer blank-canvas query excise on every visit, losing ambient anomaly visibility under operational fatigue."
  - id: "flt-04"
    name: "blind_submit_gated_parameter_loop"
    gate_type: "disqualifier"
    condition: "Parameter or rule authoring UI in ai_native_desktop_ide or analytics_dense_telemetry updates preview outputs solely on form onSubmit with > 1,000 ms blind feedback delay."
    failure_impact: "Increases estimated 10-value calibration time by 17.83x (74.00 s vs 4.15 s KLM-GOMS) and extinguishes exploratory hypothesis testing."
  - id: "flt-05"
    name: "terminal_only_live_preview"
    gate_type: "disqualifier"
    condition: "Split-pane live preview re-renders only terminal visual or text output on edit while exposing 0 intermediate variable values, execution traces, or filter-drop reasons."
    failure_impact: "Reproduces the standalone live-coding failure documented in Learnable Programming: rapid frame updates occur without improving causal comprehension of why an output failed."
veto_triggers:
  - id: "veto-01"
    name: "blind_parameter_apply_gate"
    severity: "hard_veto"
    target_antipattern: "Modal or sidebar configuration form containing numeric thresholds, weights, or token limits gated exclusively behind an Apply or Save button with zero live preview."
    detection_rule: "Static AST or DOM audit detects a <form> with >= 2 numeric <input> controls in an analytical or IDE configuration panel where state projection occurs solely inside an onSubmit handler and 0 reactive preview elements bind to input onChange state."
    mandatory_remediation: "Convert numeric controls into live-bound sliders or pointer-scrubbable readouts (role='slider', aria-valuenow, keyboard arrow steps) wired to a <= 16.67 ms deterministic local preview pane, and isolate persistent save or remote dispatch behind a separate Commit control."
  - id: "veto-02"
    name: "opaque_black_box_agent_runner"
    severity: "hard_veto"
    target_antipattern: "AI-native IDE chat or agent execution surface rendering only a prompt textarea, spinner, and terminal output text without exposing retrieved context, budget clipping, tool arguments, or intermediate execution trace."
    detection_rule: "State-machine and DOM inspection across states [configured -> running -> completed] detects 0 DOM nodes exposing intermediate stage outputs, dropped candidates, or per-step runtime values."
    mandatory_remediation: "Mount a multi-stage pipeline inspector showing each deterministic and tool stage inline (input candidates, filter decisions, token budget clipping, tool payloads) with bidirectional hover mapping to the originating rule or prompt segment."
  - id: "veto-03"
    name: "unbounded_remote_llm_on_scrub"
    severity: "hard_veto"
    target_antipattern: "Attaching remote LLM inference calls or mutating server writes directly to continuous slider onChange or pointermove events without local simulation or commit gating."
    detection_rule: "Static AST audit finds asynchronous network fetch, RPC, or LLM SDK invocation reachable synchronously or via un-gated debounce inside onChange, onInput, or onPointerMove handlers of a range/scrubber component."
    mandatory_remediation: "Split exploration from remote execution: run deterministic local simulation over cached telemetry or candidate embeddings during continuous scrubbing (0 network calls), display projected token and latency cost, and fire remote LLM inference strictly on explicit Commit."
  - id: "veto-04"
    name: "empty_filter_gate_on_information_view"
    severity: "conditional_block"
    target_antipattern: "Telemetry or analytical overview page displaying empty dropdown menus and a mandatory Run Query button at mount despite available temporal and workspace context."
    detection_rule: "Initial mount DOM snapshot (t=0 before user interaction) contains >= 2 <select> or empty filter <input> controls paired with a submit button while rendering 0 populated data elements (<svg>, <canvas>, or non-empty <tbody> data rows)."
    mandatory_remediation: "Infer initial temporal window, active service, and baseline percentile thresholds from environment and history to render the primary graphical answer immediately at t=0; convert remaining filters to graphical relative-navigation controls."
  - id: "veto-05"
    name: "single_rung_static_kpi_panel"
    severity: "conditional_block"
    target_antipattern: "Telemetry threshold or simulation dashboard rendering isolated aggregate numbers or a single static chart with no sensitivity sweep across parameter space and no hover-to-step-down concrete inspection."
    detection_rule: "Analytical view renders aggregate numeric metrics with 0 parameter-sweep comparison structures (2D sensitivity grid or overlaid trajectories) and 0 pointer/focus handlers projecting a specific concrete timestamp or instance row."
    mandatory_remediation: "Add a coupled Rung-2 parameter sensitivity heatmap or trajectory overlay where pointer hover instantaneously steps down (<= 16.67 ms) to render the Rung-1 temporal trajectory and Rung-0 concrete instance breakdown."
concrete_heuristics:
  - id: "heur-01"
    rule_statement: "IF a control adjusts a continuous model parameter, threshold, or prompt rule inside ai_native_desktop_ide or analytics_dense_telemetry, THEN its deterministic local preview MUST repaint within 16.67 ms per frame during continuous scrubbing and within 100 ms for discrete switches."
    metric_or_bound: "<= 16.67 ms continuous scrub; <= 100 ms discrete toggle"
    verification_method: "runtime_telemetry"
    applies_to:
      - "ai_native_desktop_ide"
      - "analytics_dense_telemetry"
    source_id: "src-09"
  - id: "heur-02"
    rule_statement: "IF an analytical or IDE configuration panel exposes a numeric hyperparameter, threshold, or token limit, THEN it MUST provide direct pointer-drag scrubbing or range manipulation alongside keyboard arrow stepping and live numeric readout rather than a bare text input."
    metric_or_bound: "100% of continuous numeric parameters bound to live role='slider' or pointer-scrubbable control"
    verification_method: "static_code_audit"
    applies_to:
      - "ai_native_desktop_ide"
      - "analytics_dense_telemetry"
    source_id: "src-01"
  - id: "heur-03"
    rule_statement: "IF a pipeline transforms, filters, or ranks data across >= 2 stages, THEN every intermediate stage MUST expose accepted counts, excluded counts, and explicit rejection reasons directly alongside the governing rule."
    metric_or_bound: ">= 1 visible state annotation per transformation stage; 0 silent drops"
    verification_method: "state_matrix_check"
    applies_to:
      - "ai_native_desktop_ide"
      - "analytics_dense_telemetry"
    source_id: "src-02"
  - id: "heur-04"
    rule_statement: "IF a system executes sequentially across time, frames, or agent tool steps, THEN the interface MUST map temporal history and projected behavior onto a spatial timeline or trajectory so past and projected states are inspectable simultaneously without real-time replay waiting."
    metric_or_bound: "100% of execution steps plotted spatially with direct random-access scrubbing"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "ai_native_desktop_ide"
      - "analytics_dense_telemetry"
    source_id: "src-01"
  - id: "heur-05"
    rule_statement: "IF an interface renders both originating rules/code and derived visual or structured artifacts, THEN hovering or focusing any artifact MUST highlight its originating rule/stage within 50 ms, and hovering or focusing any rule MUST highlight all affected artifacts."
    metric_or_bound: "Bidirectional highlight latency <= 50 ms; symmetric source-to-target and target-to-source binding"
    verification_method: "state_matrix_check"
    applies_to:
      - "ai_native_desktop_ide"
      - "analytics_dense_telemetry"
    source_id: "src-07"
  - id: "heur-06"
    rule_statement: "IF a user calibrates rules over a time-series or multi-parameter model in analytics_dense_telemetry, THEN the workbench MUST co-display a Rung-2 parameter sensitivity sweep coupled to a Rung-1 trajectory and Rung-0 concrete instance readout that updates on pointer hover without requiring clicks."
    metric_or_bound: ">= 2 coupled abstraction rungs with 0-click hover concretization"
    verification_method: "state_matrix_check"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-03"
  - id: "heur-07"
    rule_statement: "IF a view serves read-dominant information discovery, THEN initial mount MUST infer temporal range, active workspace entity, and historical baseline defaults automatically so routine inspection requires zero upfront filter clicks."
    metric_or_bound: "0 mandatory filter clicks at mount; KLM acquisition excise <= 1.35 s"
    verification_method: "klm_goms_estimate"
    applies_to:
      - "analytics_dense_telemetry"
      - "ai_native_desktop_ide"
    source_id: "src-04"
  - id: "heur-08"
    rule_statement: "IF a remaining user filter selects spatial, temporal, or continuous numeric ranges in an information view, THEN it MUST replace discrete text <select> dropdown menus with direct graphical manipulation domains (brushable timelines, distribution sliders, or spatial maps)."
    metric_or_bound: "0 text <select> dropdowns for continuous numeric or temporal range specification"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-04"
  - id: "heur-09"
    rule_statement: "IF a parameter directly influences a paid remote LLM call or mutating backend action, THEN continuous exploration MUST run against a local deterministic proxy with 0 network dispatches during drag, paired with an explicit Commit button displaying exact projected token and latency cost."
    metric_or_bound: "0 remote API calls emitted during continuous pointer drag; 100% explicit commit gating"
    verification_method: "static_code_audit"
    applies_to:
      - "ai_native_desktop_ide"
    source_id: "src-09"
  - id: "heur-10"
    rule_statement: "IF an analytical summary or explanation cites computed metrics or model assumptions in prose, THEN those values MUST bind reactively to the live parameter state and expose the governing formula inline for direct scrutiny."
    metric_or_bound: "100% of prose-embedded computed numbers reactively bound; 0 hardcoded stale prose metrics"
    verification_method: "static_code_audit"
    applies_to:
      - "analytics_dense_telemetry"
      - "ai_native_desktop_ide"
    source_id: "src-05"
blind_spots:
  - id: "bs-01"
    failure_mode: "Persistent live-state boxes, trajectory overlays, and multi-rung panels introduce severe visual chrome overload during focused deterministic editing or high-stakes reading, reducing visual legibility and raising distraction."
    trigger_context: "Linear code editing, long-form document review, or incident-response reading where the user is not calibrating parameters."
    counterweight_designer: "dieter-rams"
  - id: "bs-02"
    failure_mode: "Pointer-centric scrubbing and visual exploration widgets impose KLM homing (0.40 s) and pointing (1.10 s) penalties on expert operators executing repetitive CRUD mutations or issue triage via keyboard muscle memory."
    trigger_context: "High-frequency B2B operational queues (>20 repetitive actions/hour) with deterministic inputs and sub-50 ms keyboard workflows."
    counterweight_designer: "karri-saarinen"
  - id: "bs-03"
    failure_mode: "Live runtime value projections fail to reduce cognitive load on pure algorithmic logic (CHI 2024 Bigram task: non-significant NASA-TLX, higher perceived failure median 3 vs 2) and erode data-ink ratio when expanding large loop iterations naively."
    trigger_context: "Pure algorithmic verification, dense static multi-series comparison (>12 series), or high-iteration trace dumps."
    counterweight_designer: "edward-tufte"
debate_triggers:
  - id: "dbt-01"
    opposing_designer: "dieter-rams"
    conflict_axis: "live_simulation_visibility_vs_zero_distraction_subtraction"
    this_designer_stance: "Every non-trivial state transition and parameter dependency must remain visibly rendered alongside source rules so operators never mentally simulate hidden state."
    opposing_stance: "Every persistent UI surface that does not serve the immediate focal action is visual noise and must be subtracted until explicitly summoned."
    arbitration_rule: "In ai_native_desktop_ide and analytics_dense_telemetry during active parameter calibration or debugging, bret-victor prevails with inline state visible; during deterministic linear writing or reading, dieter-rams prevails by collapsing state projections to <= 15% viewport footprint with focus-triggered expansion."
  - id: "dbt-02"
    opposing_designer: "karri-saarinen"
    conflict_axis: "exploratory_pointer_scrubbing_vs_keyboard_muscle_memory_throughput"
    this_designer_stance: "Continuous pointer scrubbing over live parameters yields an estimated 17.83x KLM speedup during exploratory calibration by letting operators see trajectories continuously and stop when close enough."
    opposing_stance: "Expert throughput in daily workflows requires zero-mouse keyboard shortcuts, Cmd+K palettes, and sub-50 ms deterministic commits without pointer homing penalties."
    arbitration_rule: "If task repetition exceeds 20 identical executions/hour with pre-known parameter values (saas_b2b_intensive), karri-saarinen wins unconditionally; if the operator is discovering unknown parameter boundaries across >= 3 hypothetical states, bret-victor wins and every scrubber must also support keyboard arrow stepping."
  - id: "dbt-03"
    opposing_designer: "edward-tufte"
    conflict_axis: "interactive_multi_rung_simulation_vs_static_high_density_small_multiples"
    this_designer_stance: "Dynamic parameter sweeps and interactive hover-to-step-down mechanics allow users to feel causal sensitivity across parameter dimensions that static charts freeze."
    opposing_stance: "Interactive controls consume screen pixels and degrade data-ink ratio; high-density static small multiples answer multivariate comparisons faster through parallel eye scanning alone."
    arbitration_rule: "When the user is inspecting fixed historical telemetry across >= 12 series with 0 rule parameters to tune, edward-tufte wins (static small multiples, operational data-ink ratio >= 0.85, zero sliders); when tuning active rules or thresholds, bret-victor wins while enforcing Tufte's data-ink discipline inside the Rung-1 and Rung-2 plots."
  - id: "dbt-04"
    opposing_designer: "agentic-flow-architect"
    conflict_axis: "continuous_local_causal_scrubbing_vs_asynchronous_stochastic_agent_execution"
    this_designer_stance: "Delaying causal feedback beyond 100 ms breaks thinking flow and turns creation into blind guesswork."
    opposing_stance: "Remote frontier LLM reasoning runs asynchronously at 363-2,354 ms median TTFT with non-deterministic variance and real monetary/side-effect risk, requiring explicit asynchronous approval gates."
    arbitration_rule: "Enforce dual-loop separation: bret-victor governs 100% of deterministic pre-inference surfaces (retrieval filtering, token budget allocation, diff/plan preview at <= 16.67 ms), while agentic-flow-architect governs remote stochastic dispatch, streaming progress, and reversible side-effect approval."
primary_sources:
  - id: "src-01"
    title: "Inventing on Principle"
    author_or_org: "Bret Victor"
    year: 2012
    source_type: "primary_talk"
    url_or_identifier: "https://vimeo.com/36579366"
    extracted_invariant: "Creators require an immediate connection to what they create: every rule edit must show its effect without delay, mapping time onto space and linking code bidirectionally to rendered output."
  - id: "src-02"
    title: "Learnable Programming: Designing a programming system for understanding programs"
    author_or_org: "Bret Victor"
    year: 2012
    source_type: "engineering_post"
    url_or_identifier: "https://worrydream.com/LearnableProgramming/"
    extracted_invariant: "All state must be eliminated or explicitly rendered on screen alongside execution flow; live output updates alone do not replace visible intermediate data."
  - id: "src-03"
    title: "Up and Down the Ladder of Abstraction"
    author_or_org: "Bret Victor"
    year: 2011
    source_type: "engineering_post"
    url_or_identifier: "https://worrydream.com/LadderOfAbstraction/"
    extracted_invariant: "System understanding requires stepping up via wildcard abstractions over time and parameters, and stepping down via pointer inspection to explain anomalies in concrete instances."
  - id: "src-04"
    title: "Magic Ink: Information Software and the Graphical Interface"
    author_or_org: "Bret Victor"
    year: 2006
    source_type: "book"
    url_or_identifier: "https://worrydream.com/MagicInk/"
    extracted_invariant: "Information software serves learning and must infer context from environment and history before soliciting user interaction; remaining interaction must use graphical domains, relative navigation, and tight feedback loops."
  - id: "src-05"
    title: "Explorable Explanations"
    author_or_org: "Bret Victor"
    year: 2011
    source_type: "engineering_post"
    url_or_identifier: "https://worrydream.com/ExplorableExplanations/"
    extracted_invariant: "Analytical documents and explanations must bind inline adjustable parameters to reactive models so readers actively verify assumptions and inspect underlying logic."
  - id: "src-06"
    title: "Kill Math"
    author_or_org: "Bret Victor"
    year: 2011
    source_type: "engineering_post"
    url_or_identifier: "https://worrydream.com/KillMath/"
    extracted_invariant: "Digital quantitative tools must replace opaque pencil-and-paper symbolic manipulation with concrete adjustable numbers and dynamic visual models."
  - id: "src-07"
    title: "Media for Thinking the Unthinkable"
    author_or_org: "Bret Victor"
    year: 2013
    source_type: "primary_talk"
    url_or_identifier: "https://worrydream.com/MediaForThinkingTheUnthinkable/"
    extracted_invariant: "Multi-stage pipelines must visualize data at every transformation step with bidirectional highlighting connecting inputs, outputs, and originating code."
  - id: "src-08"
    title: "Validating AI-Generated Code with Live Programming"
    author_or_org: "Kasra Ferdowsi, Ruanqianqian Huang, Michael B. James, Nadia Polikarpova, and Sorin Lerner (ACM CHI)"
    year: 2024
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1145/3613904.3642495"
    extracted_invariant: "Between-subjects study (N=17) showed live runtime projection boxes significantly lowered NASA-TLX load in API-heavy AI code validation (frustration p=0.0004, effort p=0.015, mental demand p=0.039, performance p=0.048) while producing no significant load reduction on pure algorithmic tasks."
  - id: "src-09"
    title: "The Information Visualizer, an Information Workspace"
    author_or_org: "Stuart K. Card, George G. Robertson, and Jock D. Mackinlay (ACM CHI)"
    year: 1991
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1145/108844.108874"
    extracted_invariant: "Perceptual continuity during direct manipulation requires system response latency <= 100 ms (0.1 s) to sustain the perception of direct physical causation."
  - id: "src-10"
    title: "Tangle"
    author_or_org: "Bret Victor"
    year: 2011
    source_type: "shipped_oss_repo"
    url_or_identifier: "https://worrydream.com/Tangle/"
    extracted_invariant: "Reactive documents bind declarative HTML variables (data-var, TKAdjustableNumber) directly to deterministic update functions so inline numeric scrubbing recomputes narrative conclusions synchronously."
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

Bret Victor treats software interfaces as cognitive media engineered to externalize system mechanics that human working memory cannot reliably simulate. Across his primary works (*Magic Ink*, *Explorable Explanations*, *Kill Math*, *Up and Down the Ladder of Abstraction*, *Inventing on Principle*, *Learnable Programming*, and *Media for Thinking the Unthinkable*), recurring interface failures stem from transplanting static pencil-and-paper representations into a dynamic computational medium.

Operationally, this worldview compiles into four falsifiable architectural laws for `ai_native_desktop_ide` and `analytics_dense_telemetry`:

1. **Immediate Local Causal Connection:** Editing any rule, threshold, or retrieval parameter must render its concrete effect within 100 ms for discrete switches and within 16.67 ms per frame (60 Hz) during continuous scrubbing. KLM-GOMS modeling (`M=1.35 s, P=1.10 s, H=0.40 s, K=0.20 s, click=0.20 s`, assuming `0.50 s` server wait vs. `1.50 s` continuous scrub) estimates that calibrating 10 parameter values drops from 74.00 s in a blind Edit-Apply form to 4.15 s with a live local scrubber—an estimated 17.83x acceleration achieved by eliminating 3.40 s of motor homing, secondary clicking, retyping, and wait excise per iteration.
2. **Zero Hidden Intermediate State:** Standalone split-pane live preview fails whenever it renders only final output while concealing intermediate transformations. Every pipeline stage must render concrete runtime values, accepted counts, dropped items, and explicit rejection reasons directly adjacent to the rule that produced them, eliminating mental machine simulation.
3. **Bidirectional Traversal of the Ladder of Abstraction:** Understanding dynamic behavior requires moving without friction across Rung 0 (a single concrete instance), Rung 1 (a spatialized trajectory across all time, `time: *`), and Rung 2 (a sensitivity sweep across parameter space, `time: *, param: *`). Hovering any cell in Rung 2 must immediately concretize Rung 1 and Rung 0 without form submission.
4. **Magic Ink Discipline on Information Software:** Read-dominant software exists to construct an internal mental model, not to operate virtual machinery. Every mandatory filter dropdown or search box is navigation excise. Views must first infer context from the environment (current time, active workspace, distribution baseline) and user history, reserving explicit interaction strictly for graphical relative corrections in tight feedback loops.

To prevent remote latency and monetary token storms in AI-native tooling, Victor's worldview must be enforced through a **Dual-Loop Execution Split**: 100% of continuous scrubbing and state inspection executes locally inside a deterministic sandbox (`<= 16.67 ms`, 0 network calls), whereas remote stochastic LLM inference (median TTFT 363–2,354 ms, p90 up to 8,483 ms in November 2025 provider API probes) and side-effecting mutations sit strictly behind an explicit Commit boundary.

## 2. Regime Boundaries & Out-of-Universe Rationale

This specification holds binding authority strictly within two regimes where causal discovery, rule tuning, and multi-stage state inspection dominate task value:

| Regime | Status | Structural Justification |
| --- | --- | --- |
| `ai_native_desktop_ide` | Primary | Developers validating AI-generated code, retrieval pipelines, prompt context budgets, and agentic tool traces spend most of their effort verifying opaque transformations. CHI 2024 empirical evidence (`N=17`) found live runtime projections significantly lowered NASA-TLX frustration (`p=0.0004`), effort (`p=0.015`), mental demand (`p=0.039`), and perceived failure (`p=0.048`) on API-heavy code validation. |
| `analytics_dense_telemetry` | Primary | Engineers tuning SLO alert thresholds, anomaly detectors, and quantitative models must inspect temporal trajectories and parameter sensitivity boundaries simultaneously while receiving context-inferred baseline views at mount (*Magic Ink*). |
| `saas_b2b_intensive` | Out of Universe | High-throughput CRUD and ticket triage depend on deterministic keyboard muscle memory (`Cmd+K`, single-key commands, sub-50 ms optimistic commits). Pointer scrubbers and persistent state canvases introduce KLM homing (`0.40 s`) and pointing (`1.10 s`) penalties that actively slow expert throughput. Delegate to `karri-saarinen`. |
| `mobile_consumer_capture` | Out of Universe | Viewports under 430 px cannot display rule controls, intermediate pipeline states, and multi-rung sweeps side by side; finger occlusion breaks continuous precision scrubbing. Delegate to `luke-wroblewski`. |
| `landing_onboarding_conversion` | Out of Universe | Acquisition and onboarding flows optimize linear narrative commitment and first-action clarity, not multi-rung model exploration or runtime provenance inspection. Delegate to `luke-wroblewski` and `dieter-rams`. |

## 3. Signal Detection Protocol

Text-only audit agents execute the following 6 deterministic checks against React/TypeScript ASTs, DOM snapshots, CSS layout bounds, and runtime telemetry traces without requiring screenshots:

1. **`sig-01` (`local_causal_feedback_latency_ms` — Critical):** Trace every `onChange`, `onInput`, `onPointerMove`, and `onSubmit` handler bound to rule or parameter controls. Flag any parameter whose visual preview updates only after `onSubmit` or triggers an asynchronous round-trip exceeding 100 ms (or >16.67 ms inside a continuous scrub loop).
2. **`sig-02` (`hidden_intermediate_pipeline_stages` — Critical):** Enumerate every deterministic filter, sort, budget clip, or agent tool step between raw input and final output. Verify that each stage emits inspectable DOM nodes (counts, pass/fail status, concrete transformed payload). Any silent transformation increments the hidden-stage defect count.
3. **`sig-03` (`unpreviewed_numeric_parameter_ratio` — High):** Count `<input type="number">` or numeric text fields in configuration panels. Verify whether each field is paired with a live `role="slider"` or pointer-scrubbable readout (`aria-valuenow`) wired to synchronous preview state. Ratio must equal `0.0`.
4. **`sig-04` (`coupled_abstraction_rungs_count` — High):** Inspect analytical views for presence of Rung 0 (concrete timestamp/row readout), Rung 1 (full temporal trajectory SVG/canvas), and Rung 2 (parameter-sweep heatmap or overlaid trajectories) connected via shared component/store hover state (`hoveredCell` / `selectedPoint`). Require `>= 2` coupled rungs.
5. **`sig-05` (`initial_information_excise_interactions` — High):** Inspect initial component mount state (`useState` defaults and `t=0` DOM output). Flag views that initialize filter state to `null`/`""` and render zero populated data rows or graphics until a "Run Query" button is clicked.
6. **`sig-06` (`bidirectional_rule_artifact_traceability` — High):** Verify symmetric pointer/focus bindings: hovering or focusing an artifact sets an active trace key that visually distinguishes its originating rule (`data-rule-id` / `data-stage-id`), and hovering or focusing a rule highlights all affected downstream artifacts.

## 4. Hard Filters & Veto Playbook

### Required Gates and Disqualifiers

- **`flt-01` (Required — `local_deterministic_scrubbing_boundary`):** Verify zero network `fetch`, GraphQL mutation, or LLM client calls exist on the execution path of continuous `onChange`/`onPointerMove` scrubbing handlers.
- **`flt-02` (Required — `explicit_intermediate_state_projection`):** Verify multi-stage transformations render per-stage data artifacts and exclusion reasons inline rather than hiding them behind terminal output strings or collapsed debug console logs.
- **`flt-03` (Required — `context_inferred_initial_information_render`):** Verify read-dominant views populate default time range, entity scope, and baseline thresholds automatically at mount so at least one informative graphic renders at `t=0`.
- **`flt-04` (Disqualifier — `blind_submit_gated_parameter_loop`):** Disqualify any parameter/rule calibration panel whose output preview updates exclusively via `onSubmit` with >1,000 ms feedback latency.
- **`flt-05` (Disqualifier — `terminal_only_live_preview`):** Disqualify any split-pane live editor that updates terminal output continuously while omitting intermediate variable states, step timelines, or filter-drop telemetry.

### Veto Triggers and Mandatory Remediation

| Veto ID | Severity | Deterministic Detection Trigger | Mandatory Remediation |
| --- | --- | --- | --- |
| `veto-01` | `hard_veto` | `<form>` with `>= 2` numeric inputs wired only to `onSubmit` with `0` reactive preview bindings. | Replace with live-bound sliders/scrubbers (`<= 16.67 ms` local recomputation) and decouple persistent save/dispatch into an explicit Commit control. |
| `veto-02` | `hard_veto` | Agent runner transitions `configured -> running -> completed` with `0` intermediate stage DOM projections. | Add a persistent multi-stage pipeline inspector rendering retrieved chunks, filter cutoffs, budget clips, and tool payloads with bidirectional hover linking. |
| `veto-03` | `hard_veto` | Network/LLM API invocation inside continuous slider `onChange`/`onPointerMove` handler without local proxy or commit gate. | Route scrubbing exclusively to a local deterministic simulator over cached candidates/telemetry; fire remote LLM dispatch strictly on explicit Commit with cost preview. |
| `veto-04` | `conditional_block` | Information view renders `0` populated graphics/rows at `t=0` alongside `>= 2` empty `<select>`/`<input>` filters and a submit trigger. | Infer default context from current time, active workspace, and baseline percentile thresholds to render data immediately at mount; convert filters to relative graphical controls. |
| `veto-05` | `conditional_block` | Analytical threshold view shows static aggregate KPIs with `0` sensitivity sweeps and `0` hover-to-step-down concrete handlers. | Mount a Rung-2 parameter-sweep matrix coupled on pointer hover (`<= 16.67 ms`) to Rung-1 trajectory and Rung-0 instance inspection. |

## 5. Executable Heuristics & Code Patterns

### Refactoring Pattern 1 (`ai_native_desktop_ide`): Agentic Retrieval & Context-Budget Workbench

#### Before: Blind Form Gated by Submit (`BlindAgentConfigForm.tsx`)

Violates `veto-01`, `veto-02`, `flt-02`, and `flt-04`. Engineers guess numeric cutoffs blindly, incur an estimated 7.40 s KLM-GOMS overhead per cycle, receive zero visibility into which chunks passed similarity versus got clipped by the token budget, and expend remote LLM tokens on miscalibrated context windows.

```tsx
import React, { useState } from "react";

interface BlindAgentConfigProps {
  onRunAgent: (config: { minSimilarity: number; maxTokens: number; prompt: string }) => Promise<string>;
}

export function BlindAgentConfigForm({ onRunAgent }: BlindAgentConfigProps) {
  const [minSimilarity, setMinSimilarity] = useState("0.75");
  const [maxTokens, setMaxTokens] = useState("2000");
  const [prompt, setPrompt] = useState("Audit authentication middleware for token replay risks.");
  const [output, setOutput] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    setLoading(true);
    // ANTI-PATTERN: Zero local visibility into retrieved chunks or budget clipping before remote LLM dispatch.
    const result = await onRunAgent({
      minSimilarity: Number(minSimilarity),
      maxTokens: Number(maxTokens),
      prompt,
    });
    setOutput(result);
    setLoading(false);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Min Similarity
        <input type="number" step="0.01" value={minSimilarity} onChange={(e) => setMinSimilarity(e.target.value)} />
      </label>
      <label>
        Max Token Budget
        <input type="number" step="100" value={maxTokens} onChange={(e) => setMaxTokens(e.target.value)} />
      </label>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} />
      <button type="submit" disabled={loading}>
        {loading ? "Running..." : "Apply & Run Agent"}
      </button>
      {output && <pre>{output}</pre>}
    </form>
  );
}
```

#### After: Dual-Loop Live State-Visible Context Workbench (`LiveAgentContextWorkbench.tsx`)

Satisfies `heur-01`, `heur-02`, `heur-03`, `heur-05`, `heur-09`, and `flt-01`. Scrubbing `minSimilarity` or `maxTokens` recomputes all deterministic pipeline stages locally within the 16.67 ms 60 Hz frame budget with 0 remote LLM calls, renders every accepted, budget-clipped, and rejected chunk with exact provenance, supports bidirectional pointer and keyboard-focus linking between rules and chunks, and isolates remote LLM execution behind an explicit Commit control displaying exact projected token count.

```tsx
import React, { useMemo, useState } from "react";

export interface CandidateChunk {
  id: string;
  similarity: number;
  tokens: number;
}

type ChunkStatus = "selected" | "clipped_by_budget" | "rejected_by_similarity";
type RuleId = "minSimilarity" | "maxTokens" | null;

interface EvaluatedChunk extends CandidateChunk {
  status: ChunkStatus;
  cumulativeTokens: number | null;
  governingRule: Exclude<RuleId, null>;
}

const DEFAULT_CANDIDATES: CandidateChunk[] = [
  { id: "auth.ts:12-64", similarity: 0.94, tokens: 420 },
  { id: "session.ts:1-88", similarity: 0.89, tokens: 610 },
  { id: "middleware.ts:40-95", similarity: 0.83, tokens: 390 },
  { id: "oauth.ts:102-190", similarity: 0.77, tokens: 740 },
  { id: "rbac.ts:5-55", similarity: 0.71, tokens: 340 },
  { id: "auditLog.ts:18-72", similarity: 0.64, tokens: 410 },
  { id: "legacyAuth.ts:1-140", similarity: 0.56, tokens: 920 },
];

interface LiveAgentContextWorkbenchProps {
  candidates?: CandidateChunk[];
  onCommitDispatch: (payload: {
    minSimilarity: number;
    maxTokens: number;
    selectedChunkIds: string[];
    totalTokens: number;
  }) => Promise<void>;
}

export function LiveAgentContextWorkbench({
  candidates = DEFAULT_CANDIDATES,
  onCommitDispatch,
}: LiveAgentContextWorkbenchProps) {
  const [minSimilarity, setMinSimilarity] = useState<number>(0.7);
  const [maxTokens, setMaxTokens] = useState<number>(2000);
  const [activeRule, setActiveRule] = useState<RuleId>(null);
  const [hoveredChunkId, setHoveredChunkId] = useState<string | null>(null);
  const [dispatching, setDispatching] = useState<boolean>(false);

  // Local deterministic causal loop: synchronous in-memory pass with 0 network calls during continuous scrubbing.
  const pipeline = useMemo(() => {
    let usedTokens = 0;
    const evaluated: EvaluatedChunk[] = candidates.map((chunk) => {
      if (chunk.similarity < minSimilarity) {
        return {
          ...chunk,
          status: "rejected_by_similarity",
          cumulativeTokens: null,
          governingRule: "minSimilarity",
        };
      }
      if (usedTokens + chunk.tokens <= maxTokens) {
        usedTokens += chunk.tokens;
        return {
          ...chunk,
          status: "selected",
          cumulativeTokens: usedTokens,
          governingRule: "maxTokens",
        };
      }
      return {
        ...chunk,
        status: "clipped_by_budget",
        cumulativeTokens: null,
        governingRule: "maxTokens",
      };
    });

    const selected = evaluated.filter((c) => c.status === "selected");
    const clipped = evaluated.filter((c) => c.status === "clipped_by_budget");
    const rejected = evaluated.filter((c) => c.status === "rejected_by_similarity");

    return { evaluated, selected, clipped, rejected, usedTokens };
  }, [candidates, minSimilarity, maxTokens]);

  const hoveredChunk = pipeline.evaluated.find((c) => c.id === hoveredChunkId) ?? null;
  const highlightedRule: RuleId = activeRule ?? hoveredChunk?.governingRule ?? null;

  async function handleExplicitCommit() {
    setDispatching(true);
    try {
      await onCommitDispatch({
        minSimilarity,
        maxTokens,
        selectedChunkIds: pipeline.selected.map((c) => c.id),
        totalTokens: pipeline.usedTokens,
      });
    } finally {
      setDispatching(false);
    }
  }

  return (
    <section aria-label="Live Agent Context Workbench" data-execution-loop="dual">
      <div data-pane="rule-controls">
        <div
          data-rule-id="minSimilarity"
          data-highlighted={highlightedRule === "minSimilarity"}
          onPointerEnter={() => setActiveRule("minSimilarity")}
          onPointerLeave={() => setActiveRule(null)}
        >
          <label htmlFor="sim-slider">
            Similarity Cutoff: <strong>{minSimilarity.toFixed(2)}</strong>
          </label>
          <input
            id="sim-slider"
            type="range"
            role="slider"
            min={0.5}
            max={0.98}
            step={0.01}
            value={minSimilarity}
            aria-valuenow={minSimilarity}
            onFocus={() => setActiveRule("minSimilarity")}
            onBlur={() => setActiveRule(null)}
            onChange={(e) => setMinSimilarity(Number(e.target.value))}
          />
          <span data-stage="similarity-summary">
            Passes similarity: {pipeline.selected.length + pipeline.clipped.length} / {candidates.length}
          </span>
        </div>

        <div
          data-rule-id="maxTokens"
          data-highlighted={highlightedRule === "maxTokens"}
          onPointerEnter={() => setActiveRule("maxTokens")}
          onPointerLeave={() => setActiveRule(null)}
        >
          <label htmlFor="budget-slider">
            Token Budget: <strong>{maxTokens} tok</strong> ({pipeline.usedTokens} allocated)
          </label>
          <input
            id="budget-slider"
            type="range"
            role="slider"
            min={500}
            max={3500}
            step={50}
            value={maxTokens}
            aria-valuenow={maxTokens}
            onFocus={() => setActiveRule("maxTokens")}
            onBlur={() => setActiveRule(null)}
            onChange={(e) => setMaxTokens(Number(e.target.value))}
          />
          <span data-stage="budget-summary">
            Selected: {pipeline.selected.length} | Budget-clipped: {pipeline.clipped.length} | Rejected:{" "}
            {pipeline.rejected.length}
          </span>
        </div>

        <button type="button" onClick={handleExplicitCommit} disabled={dispatching || pipeline.selected.length === 0}>
          {dispatching
            ? "Dispatching to Remote LLM..."
            : `Commit & Dispatch (${pipeline.selected.length} chunks, ${pipeline.usedTokens} tok)`}
        </button>
      </div>

      <div data-pane="intermediate-pipeline-state">
        <p data-reactive-narrative="true">
          With similarity &ge; {minSimilarity.toFixed(2)} and budget &le; {maxTokens} tokens, the local pipeline
          forwards <strong>{pipeline.selected.length}</strong> chunks ({pipeline.usedTokens} tokens), clips{" "}
          <strong>{pipeline.clipped.length}</strong> for budget overflow, and excludes{" "}
          <strong>{pipeline.rejected.length}</strong> below threshold.
        </p>

        <ul data-stage="candidate-trace">
          {pipeline.evaluated.map((chunk) => {
            const linkedToActiveRule = activeRule !== null && chunk.governingRule === activeRule;
            return (
              <li
                key={chunk.id}
                data-chunk-id={chunk.id}
                data-status={chunk.status}
                data-source-rule={chunk.governingRule}
                data-highlighted={hoveredChunkId === chunk.id || linkedToActiveRule}
                onPointerEnter={() => setHoveredChunkId(chunk.id)}
                onPointerLeave={() => setHoveredChunkId(null)}
                onFocus={() => setHoveredChunkId(chunk.id)}
                onBlur={() => setHoveredChunkId(null)}
                tabIndex={0}
              >
                <code>{chunk.id}</code> — sim: {chunk.similarity.toFixed(2)} | size: {chunk.tokens} tok | stage:{" "}
                <strong>{chunk.status}</strong>
                {chunk.cumulativeTokens !== null ? ` (cumulative: ${chunk.cumulativeTokens} tok)` : ""}
              </li>
            );
          })}
        </ul>
      </div>
    </section>
  );
}
```

### Refactoring Pattern 2 (`analytics_dense_telemetry`): SLO Alert Threshold Explorer (Ladder of Abstraction)

#### Before: Opaque Alert Rule Modal (`BlindAlertRuleModal.tsx`)

Violates `veto-01`, `veto-04`, `veto-05`, and `heur-06`. The engineer sets `thresholdMs` and `windowHours` in a vacuum without seeing historical latency trajectories, transient micro-spike false positives, or sensitivity transitions across neighboring values.

```tsx
import React, { useState } from "react";

interface BlindAlertRuleModalProps {
  onSaveRule: (rule: { thresholdMs: number; windowHours: number }) => Promise<void>;
}

export function BlindAlertRuleModal({ onSaveRule }: BlindAlertRuleModalProps) {
  const [thresholdMs, setThresholdMs] = useState("180");
  const [windowHours, setWindowHours] = useState("3");
  const [saved, setSaved] = useState(false);

  async function handleSave(event: React.FormEvent) {
    event.preventDefault();
    await onSaveRule({ thresholdMs: Number(thresholdMs), windowHours: Number(windowHours) });
    setSaved(true);
  }

  return (
    <form onSubmit={handleSave}>
      <label>
        Latency Threshold (ms)
        <input type="number" value={thresholdMs} onChange={(e) => setThresholdMs(e.target.value)} />
      </label>
      <label>
        Moving Average Window (hours)
        <input type="number" value={windowHours} onChange={(e) => setWindowHours(e.target.value)} />
      </label>
      <button type="submit">Save Alert Rule</button>
      {saved && <p>Rule saved.</p>}
    </form>
  );
}
```

#### After: Three-Rung Ladder-of-Abstraction Explorer (`LadderAlertExplorer.tsx`)

Satisfies `heur-01`, `heur-04`, `heur-06`, `heur-07`, `heur-08`, and `heur-10`. On mount (`t=0`), it infers the initial threshold from the historical series' `p85` distribution (*Magic Ink*), plots Rung 2 (a 2D sensitivity matrix sweeping `thresholdMs` × `windowHours`), projects Rung 1 (the full temporal moving-average SVG trajectory with alert points), and projects Rung 0 (concrete hourly raw vs. rolling-average breakdown) synchronously on hover with 0 clicks required to inspect neighboring rules.

```tsx
import React, { useMemo, useState } from "react";

interface AlertSimulation {
  movingAverage: number[];
  alertIndices: number[];
}

function simulateAlerts(series: number[], thresholdMs: number, windowHours: number): AlertSimulation {
  const movingAverage: number[] = [];
  const alertIndices: number[] = [];
  for (let i = 0; i < series.length; i++) {
    const start = Math.max(0, i - windowHours + 1);
    let sum = 0;
    for (let j = start; j <= i; j++) sum += series[j];
    const avg = sum / (i - start + 1);
    movingAverage.push(avg);
    if (avg > thresholdMs) alertIndices.push(i);
  }
  return { movingAverage, alertIndices };
}

function inferDefaultThreshold(series: number[]): number {
  if (series.length === 0) return 180;
  const sorted = [...series].sort((a, b) => a - b);
  const idx = Math.min(sorted.length - 1, Math.floor(sorted.length * 0.85));
  return Math.round(sorted[idx] / 10) * 10;
}

const THRESHOLD_STEPS = [140, 160, 180, 200, 220, 240];
const WINDOW_STEPS = [1, 2, 3, 4, 5];

interface LadderAlertExplorerProps {
  hourlyLatencyMs: number[];
  onCommitRule: (rule: { thresholdMs: number; windowHours: number; projectedAlertHours: number }) => void;
}

export function LadderAlertExplorer({ hourlyLatencyMs, onCommitRule }: LadderAlertExplorerProps) {
  // Magic Ink context inference: initialize threshold directly from historical telemetry distribution at t=0.
  const [pinnedRule, setPinnedRule] = useState<{ thresholdMs: number; windowHours: number }>(() => ({
    thresholdMs: inferDefaultThreshold(hourlyLatencyMs),
    windowHours: 3,
  }));
  const [hoveredRule, setHoveredRule] = useState<{ thresholdMs: number; windowHours: number } | null>(null);
  const [inspectedHour, setInspectedHour] = useState<number>(Math.max(0, hourlyLatencyMs.length - 1));

  // Active parameters reflect hovered Rung-2 cell immediately (step-down concretization without clicking).
  const activeThreshold = hoveredRule?.thresholdMs ?? pinnedRule.thresholdMs;
  const activeWindow = hoveredRule?.windowHours ?? pinnedRule.windowHours;

  // Rung 2 (Abstract over Time & Parameters): 2D Sensitivity Sweep Matrix
  const sensitivityGrid = useMemo(() => {
    return WINDOW_STEPS.map((w) => ({
      windowHours: w,
      cells: THRESHOLD_STEPS.map((t) => ({
        thresholdMs: t,
        windowHours: w,
        alertCount: simulateAlerts(hourlyLatencyMs, t, w).alertIndices.length,
      })),
    }));
  }, [hourlyLatencyMs]);

  // Rung 1 (Abstract over Time): Full temporal trajectory for active rule
  const activeSim = useMemo(
    () => simulateAlerts(hourlyLatencyMs, activeThreshold, activeWindow),
    [hourlyLatencyMs, activeThreshold, activeWindow]
  );

  // Rung 0 (Concrete Instance): Single inspected hour breakdown
  const concreteRaw = hourlyLatencyMs[inspectedHour] ?? 0;
  const concreteAvg = activeSim.movingAverage[inspectedHour] ?? 0;
  const concreteAlerting = concreteAvg > activeThreshold;

  const maxLatency = Math.max(...hourlyLatencyMs, activeThreshold + 20, 1);
  const svgWidth = 560;
  const svgHeight = 160;
  const xStep = hourlyLatencyMs.length > 1 ? svgWidth / (hourlyLatencyMs.length - 1) : svgWidth;
  const yScale = (val: number) => svgHeight - (val / maxLatency) * (svgHeight - 16) - 8;

  const avgPath = activeSim.movingAverage
    .map((val, i) => `${i === 0 ? "M" : "L"} ${(i * xStep).toFixed(1)} ${yScale(val).toFixed(1)}`)
    .join(" ");

  return (
    <section aria-label="SLO Ladder of Abstraction Explorer" data-rungs="3">
      {/* Rung 2: Parameter Sweep Matrix */}
      <div data-rung="2" aria-label="Parameter Sensitivity Sweep">
        <p data-reactive-narrative="true">
          Inspecting threshold <strong>{activeThreshold} ms</strong> with <strong>{activeWindow} h</strong> moving
          average triggers <strong>{activeSim.alertIndices.length}</strong> alert hours across{" "}
          {hourlyLatencyMs.length} h. Hover any matrix cell to step down; click to pin.
        </p>
        <table role="grid" aria-label="Threshold by Window Sensitivity Matrix">
          <thead>
            <tr>
              <th>Window \ Threshold</th>
              {THRESHOLD_STEPS.map((t) => (
                <th key={t}>{t} ms</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {sensitivityGrid.map((row) => (
              <tr key={row.windowHours}>
                <th>{row.windowHours} h</th>
                {row.cells.map((cell) => {
                  const isActive = cell.thresholdMs === activeThreshold && cell.windowHours === activeWindow;
                  return (
                    <td key={`${cell.windowHours}-${cell.thresholdMs}`}>
                      <button
                        type="button"
                        data-threshold={cell.thresholdMs}
                        data-window={cell.windowHours}
                        data-active={isActive}
                        onPointerEnter={() =>
                          setHoveredRule({ thresholdMs: cell.thresholdMs, windowHours: cell.windowHours })
                        }
                        onPointerLeave={() => setHoveredRule(null)}
                        onFocus={() =>
                          setHoveredRule({ thresholdMs: cell.thresholdMs, windowHours: cell.windowHours })
                        }
                        onBlur={() => setHoveredRule(null)}
                        onClick={() =>
                          setPinnedRule({ thresholdMs: cell.thresholdMs, windowHours: cell.windowHours })
                        }
                      >
                        {cell.alertCount}
                      </button>
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Rung 1: Temporal Trajectory (time: *) */}
      <div data-rung="1" aria-label="Full Temporal Trajectory">
        <svg width={svgWidth} height={svgHeight} role="img" aria-label="Moving average latency trajectory">
          <line
            x1={0}
            x2={svgWidth}
            y1={yScale(activeThreshold)}
            y2={yScale(activeThreshold)}
            stroke="#D93025"
            strokeDasharray="4 4"
          />
          <path d={avgPath} fill="none" stroke="#1A73E8" strokeWidth={2} />
          {hourlyLatencyMs.map((val, hour) => (
            <circle
              key={hour}
              cx={hour * xStep}
              cy={yScale(val)}
              r={hour === inspectedHour ? 5 : 3}
              fill={activeSim.alertIndices.includes(hour) ? "#D93025" : "#AAAAAA"}
              onPointerEnter={() => setInspectedHour(hour)}
            />
          ))}
        </svg>
      </div>

      {/* Rung 0: Concrete Instance Inspection + Explicit Commit */}
      <div data-rung="0" aria-label="Concrete Hour Inspection">
        <label htmlFor="hour-scrubber">
          Inspect Hour: <strong>t = {inspectedHour}</strong>
        </label>
        <input
          id="hour-scrubber"
          type="range"
          role="slider"
          min={0}
          max={Math.max(0, hourlyLatencyMs.length - 1)}
          value={inspectedHour}
          aria-valuenow={inspectedHour}
          onChange={(e) => setInspectedHour(Number(e.target.value))}
        />
        <output data-concrete-state="true">
          Raw latency: {concreteRaw.toFixed(1)} ms | {activeWindow}h moving avg: {concreteAvg.toFixed(1)} ms | Alert:{" "}
          <strong>{concreteAlerting ? "TRIGGERED" : "NOMINAL"}</strong>
        </output>
        <button
          type="button"
          onClick={() =>
            onCommitRule({
              thresholdMs: pinnedRule.thresholdMs,
              windowHours: pinnedRule.windowHours,
              projectedAlertHours: simulateAlerts(
                hourlyLatencyMs,
                pinnedRule.thresholdMs,
                pinnedRule.windowHours
              ).alertIndices.length,
            })
          }
        >
          Commit Pinned Rule ({pinnedRule.thresholdMs} ms / {pinnedRule.windowHours} h)
        </button>
      </div>
    </section>
  );
}
```

## 6. Blind Spots & Counterweights

1. **Visual Chrome Overload Under Focused Linear Work (`bs-01` -> Counterweight: `dieter-rams`):** Continuous inline state projections, trajectory traces, and sensitivity grids add perceptual clutter when an operator is writing deterministic code or reading a confirmed report rather than calibrating rules. Mitigation: cap ambient state projections to `<= 15%` of viewport area outside active exploration modes and collapse secondary traces until hover or keyboard focus.
2. **Motor Excise in High-Frequency Repetitive CRUD (`bs-02` -> Counterweight: `karri-saarinen`):** Pointer scrubbing imposes KLM homing (`0.40 s`) and pointing (`1.10 s`) costs that degrade throughput when operators process 20+ known-input records per hour. Mitigation: exclude `bret-victor` from `saas_b2b_intensive` workflows; inside primary regimes, pair every pointer scrubber with full keyboard arrow and numeric-entry parity.
3. **Algorithmic Complexity Ceiling & Data-Ink Erosion (`bs-03` -> Counterweight: `edward-tufte`):** CHI 2024 empirical testing (`Ferdowsi et al.`, `N=17`) found that live value projections did not reduce NASA-TLX load on pure algorithmic code (`Bigram`) and slightly increased self-reported failure perception (`median 3 vs 2`), while Sean McDirmid documented scaling and spatial-ambiguity overhead in loops and side-effecting calls. Mitigation: summarize high-iteration loops statistically, maintain an operational `data-ink ratio >= 0.85` inside trajectory plots, and defer read-only comparison of `>= 12` static series to small multiples.

## 7. Adversarial Debate Positions

- **Against `dieter-rams` (`live_simulation_visibility_vs_zero_distraction_subtraction`):** Victor insists that hiding intermediate execution state behind minimalist surfaces forces costly mental simulation; Rams insists that persistent state panes violate unobtrusiveness. **Arbitration:** During active debugging or rule tuning inside primary regimes, render intermediate state inline by default; during deterministic linear writing or reading, collapse state annotations to focus-triggered disclosures consuming `<= 15%` of viewport area.
- **Against `karri-saarinen` (`exploratory_pointer_scrubbing_vs_keyboard_muscle_memory_throughput`):** Victor prioritizes continuous visual-motor discovery (estimated 17.83x KLM acceleration across 10 exploratory states); Saarinen prioritizes zero-mouse keyboard throughput (sub-50 ms deterministic actions). **Arbitration:** Task repetition `>= 20` known-input operations/hour awards precedence to `karri-saarinen`; exploratory calibration across `>= 3` hypothetical states awards precedence to `bret-victor` with mandatory keyboard-stepping parity on every slider.
- **Against `edward-tufte` (`interactive_multi_rung_simulation_vs_static_high_density_small_multiples`):** Victor treats dynamic scrubbing and hover concretization as essential for causal feel; Tufte treats interactive widgets as non-data-ink that slows parallel visual scanning. **Arbitration:** Static multivariate review of `>= 12` historical series with 0 tunable parameters defers to `edward-tufte` (static small multiples, operational data-ink ratio `>= 0.85`, zero sliders); active threshold/model calibration defers to `bret-victor` while keeping all charts free of non-data decoration.
- **Against `agentic-flow-architect` (`continuous_local_causal_scrubbing_vs_asynchronous_stochastic_agent_execution`):** Victor demands sub-100 ms deterministic feedback; `agentic-flow-architect` manages remote stochastic LLMs with 363–2,354 ms median TTFT and irreversible tool actions. **Arbitration:** Enforce strict Dual-Loop Separation—`bret-victor` owns deterministic local pre-flight surfaces (retrieval cutoffs, token budgets, dry-run diffs at `<= 16.67 ms`), and `agentic-flow-architect` owns explicit commit dispatch, streaming observability, and rollback controls.

## 8. Primary Source Notes

- **`src-01` — *Inventing on Principle* (Bret Victor, CUSEC, January 20, 2012; `https://vimeo.com/36579366`):** Formalizes the principle *"Creators need an immediate connection to what they're creating"* via four concrete mechanics: live canvas code sync with `Control`-key value dialing, bidirectional `Option`-key code-to-pixel highlighting, time-to-space future trajectory trails in a platformer, and live-data algorithm/circuit inspection.
- **`src-02` — *Learnable Programming* (Bret Victor, September 2012; `https://worrydream.com/LearnableProgramming/`):** Written as a direct technical critique of standalone live coding; establishes that *"All state must be eliminated or shown"* and *"Working in the head doesn't scale"*, specifying spatial execution timelines, scrubbed execution frames, and contextual data visualization.
- **`src-03` — *Up and Down the Ladder of Abstraction* (Bret Victor, October 2011; `https://worrydream.com/LadderOfAbstraction/`):** Defines the three system dimensions (time, structure, dataset), wildcard abstraction (`time: *`, `turning rate: *`), overlaid parameter sweeps, summary metric curves, and pointer-driven stepping down to explain sensitivity cliffs.
- **`src-04` — *Magic Ink: Information Software and the Graphical Interface* (Bret Victor, March 15, 2006; `https://worrydream.com/MagicInk/`):** Distinguishes information software (learning, internal model) from manipulation software (creating, external model); defines the context-inference hierarchy (environment -> history -> interaction as last resort) and the three interaction-minimization rules (graphical manipulation, relative navigation, tight feedback loops).
- **`src-05` — *Explorable Explanations* (Bret Victor, March 10, 2011; `https://worrydream.com/ExplorableExplanations/`) & `src-10` — *Tangle* (2011; `https://worrydream.com/Tangle/`):** Specifies reactive documents, inline scrubbable numbers (`TKAdjustableNumber`), and authorial model transparency enabling active refutation.
- **`src-06` — *Kill Math* (Bret Victor, April 11, 2011; `https://worrydream.com/KillMath/`):** Grounds the rejection of opaque symbolic parameter syntax in favor of concrete adjustable numbers and dynamic visual models.
- **`src-07` — *Media for Thinking the Unthinkable* (Bret Victor, MIT Media Lab, April 4, 2013; `https://worrydream.com/MediaForThinkingTheUnthinkable/`):** Demonstrates multi-stage data pipeline visibility and linked bidirectional source-to-output highlighting.
- **`src-08` — *Validating AI-Generated Code with Live Programming* (Ferdowsi et al., ACM CHI 2024; `https://doi.org/10.1145/3613904.3642495`):** Provides controlled empirical validation (`N=17`) showing statistically significant NASA-TLX reductions in API-heavy AI code verification alongside the algorithmic task ceiling (`Bigram`).
- **`src-09` — *The Information Visualizer, an Information Workspace* (Card, Robertson, & Mackinlay, ACM CHI 1991; `https://doi.org/10.1145/108844.108874`):** Supplies the 100 ms (0.1 s) psychophysical ceiling for perceived instantaneous causation.
