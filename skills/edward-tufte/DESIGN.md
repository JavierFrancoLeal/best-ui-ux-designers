---
schema_version: "1.0.0"
identity:
  slug: "edward-tufte"
  display_name: "Edward Tufte"
  barbell_pole: "lindy_anchor"
  archetype_synthetic: false
  primary_domain: "Multivariate data density, maximum data-ink ratio, graphical integrity (Lie Factor 0.95-1.05), small multiples, and sparklines"
  core_axiom: "Analytical displays must hold Lie Factor within 0.95-1.05, strip all non-data-ink chrome, and render multivariate comparisons inside one eyespan via direct labels, sparklines, or shared-scale small multiples."
  active_era: "1983-present"
  skin_in_the_game_evidence:
    - artifact: "The Visual Display of Quantitative Information (Graphics Press)"
      year: 1983
      verifiable_metric: "17 printings and 300,000 copies of the 1st edition prior to the 2nd edition (2001), 5,419 Semantic Scholar citations, and self-reported totals of nearly 2 million Graphics Press books in print plus 328,001 attendees across 923 one-day courses on edwardtufte.com."
      source_id: "src-01"
    - artifact: "Sparklines specification (Beautiful Evidence, pp. 46-63)"
      year: 2006
      verifiable_metric: "Shipped as a native in-cell charting primitive in Microsoft Excel 2010 (MSDN explicitly crediting Tufte) and LibreOffice Calc 7.4 (2022 OOXML support), plus wide adoption across financial and BI telemetry grids."
      source_id: "src-04"
    - artifact: "Graphical Summary of Patient Status (The Lancet, with Seth M. Powsner)"
      year: 1994
      verifiable_metric: "Peer-reviewed one-page ~22-to-24-variable small-multiple clinical summary (doi:10.1016/S0140-6736(94)91406-0) cited as foundational prototype in EHR visualization reviews (JAMIA 2015), complemented by CRAN ggthemes theme_tufte(), geom_tufteboxplot(), and range-frame geoms."
      source_id: "src-05"
regime_fit:
  primary_regimes:
    - "analytics_dense_telemetry"
  secondary_regimes: []
  out_of_universe_regimes:
    - regime: "landing_onboarding_conversion"
      reason: "High-density multivariate tables and unembellished analytical grids impose extraneous cognitive friction on first-visit prospects and score lowest on at-a-glance memorability (Borkin et al., 2013), suppressing single-CTA conversion completion."
    - regime: "mobile_consumer_capture"
      reason: "Concurrent small-multiple grids and dense multi-column sparkline rows violate 44x44px touch-target bounds on 320-430px viewports, compress sparkline x-axes below readable slope angles, and trigger horizontal overflow."
    - regime: "ai_native_desktop_ide"
      reason: "Agentic coding environments require bidirectional direct manipulation, live parameter exploration, streaming tool diffs, and execution control surfaces rather than static publication-grade statistical summaries."
    - regime: "saas_b2b_intensive"
      reason: "High-frequency transactional CRUD workflows, bulk ticket triage, and million-row interactive log querying demand dynamic filter sliders, keyboard command palettes, and explicit interactive signifiers beyond static eyespan visualization."
high_weight_signals:
  - id: "sig-01"
    name: "lie_factor_distortion"
    weight: "critical"
    category: "visual_semiotics"
    detects_before_others: "Proportional misrepresentation in bar charts (truncated Y-axis > 0), radius-scaled 2D bubbles, 3D perspective projections, or dual-axis scale manipulation."
    observable_indicator: "In TSX/Recharts/D3/SVG configs: <YAxis domain={[min, max]}> with min !== 0 on <BarChart>/<AreaChart>; bubble radius mapped linearly to v instead of Math.sqrt(v); CSS/SVG 3D transforms; or >= 2 independent yAxisId scales on one plot."
    threshold: "0.95 <= LF <= 1.05 and bar/area quantitative baseline === 0"
    direction: "exact_match"
    source_id: "src-01"
  - id: "sig-02"
    name: "non_data_ink_chartjunk"
    weight: "critical"
    category: "information_density"
    detects_before_others: "Decorative chrome consuming visual bandwidth: pie/donut comparisons, radial gauges, drop-shadowed card stacks, heavy gridlines, closed chart boxes, and moire SVG hatching."
    observable_indicator: "Presence of <PieChart>, <Pie>, <RadialBarChart>, box-shadow on metric containers, <CartesianGrid> with strokeWidth > 1 or luminance contrast > 1.8:1, 4-sided chart frame borders, or SVG <pattern> cross-hatching."
    threshold: "data_ink_ratio >= 0.70 (operational bound); 0 pie/donut/gauge comparisons; 0 decorative shadows or moire patterns"
    direction: "higher_is_better"
    source_id: "src-01"
  - id: "sig-03"
    name: "small_multiple_scale_parity"
    weight: "critical"
    category: "cognitive_load"
    detects_before_others: "Cross-cohort magnitude blindness caused by hiding series behind sequential tabs/carousels or letting sibling panels auto-scale independently."
    observable_indicator: "Comparative datasets (>= 3 cohorts/regions) wrapped inside <Tabs>/<TabPanel> or sibling chart instances omitting a shared computed yDomain constant (e.g., using per-panel domain={['dataMin', 'dataMax']})."
    threshold: "true (100% concurrent visibility in grid and identical shared Y-domain across comparative sibling panels)"
    direction: "boolean_required"
    source_id: "src-02"
  - id: "sig-04"
    name: "detached_legend_saccade_cost"
    weight: "high"
    category: "cognitive_load"
    detects_before_others: "Forced visual ping-ponging between plotted marks and detached color keys or hover-only tooltips that conceal exact values."
    observable_indicator: "Presence of <Legend /> component or separate legend container on charts with <= 6 series, or absence of direct <LabelList> / terminal SVG <text> labels within 8px of data marks."
    threshold: "0 detached legends for <= 6 series; 100% direct inline mark/endpoint labeling"
    direction: "lower_is_better"
    source_id: "src-01"
  - id: "sig-05"
    name: "isolated_kpi_card_sparsity"
    weight: "high"
    category: "information_density"
    detects_before_others: "De-quantified executive KPI cards spending massive screen area on a single scalar figure with no historical trajectory, normal band, or comparative benchmark."
    observable_indicator: "Metric card container area > 12000 px^2 rendering <= 2 numeric tokens without an inline sparkline (n >= 10 samples), normal-range reference band, or explicit min/max extrema."
    threshold: ">= 10 plotted historical points plus >= 1 reference corridor or benchmark per metric readout"
    direction: "higher_is_better"
    source_id: "src-04"
  - id: "sig-06"
    name: "tabular_numeral_and_subtle_separation"
    weight: "medium"
    category: "visual_semiotics"
    detects_before_others: "Jagged decimal columns in numeric tables and 1+1=3 optical vibration caused by high-contrast adjacent borders."
    observable_indicator: "Numeric table cells (<td>/<th>) lacking CSS font-variant-numeric: tabular-nums or text-align: right, or structural row/grid rules exceeding 1px width or 1.8:1 contrast ratio against background."
    threshold: "true (tabular-nums + right-aligned numerics + structural rules <= 1px at 1.15:1-1.6:1 contrast)"
    direction: "boolean_required"
    source_id: "src-03"
hard_filters:
  - id: "flt-01"
    name: "zero_baseline_and_proportional_scaling"
    gate_type: "required"
    condition: "For all bar, column, and cumulative area charts, quantitative axis lower bound === 0 (domain={[0, 'auto']} or [0, maxVal]); for all 2D proportional marks, radius scales with Math.sqrt(value); computed Lie Factor satisfies 0.95 <= LF <= 1.05."
    failure_impact: "Small operational deltas (e.g., 9.95% uptime difference) visually inflate by >10x (LF = 10.52), triggering false incident escalations and persistent misinterpretation even when numeric captions or axis-break cues are present (Pandey et al., 2015; Correll et al., 2020)."
  - id: "flt-02"
    name: "ban_pie_donut_3d_and_dual_axis"
    gate_type: "disqualifier"
    condition: "Component AST contains <PieChart>, <Pie>, <RadialBarChart>, radial gauge arcs, 3D perspective projections on quantitative marks, or superimposed dual Y-axes (yAxisId count >= 2 with distinct units/scales on one plot)."
    failure_impact: "Forces angle/area decoding ranked strictly below common-scale position judgments (Cleveland & McGill, 1984) and creates spurious visual crossovers or speed/accuracy degradation under superimposed dual scales (Isenberg et al., 2011)."
  - id: "flt-03"
    name: "shared_scale_eyespan_multiples"
    gate_type: "required"
    condition: "When comparing >= 3 cohorts, regions, or services across a common independent variable, all panels render simultaneously in a CSS grid with an identical computed yDomain = [sharedMin, sharedMax] rather than hidden tabs or independent local auto-scaling."
    failure_impact: "Hiding panels in tabs shifts comparison into fragile short-term memory, while independent auto-scaling collapses severe multi-fold outages (e.g., 188 ms vs 25 ms = 7.52x) into visually identical peak heights (1.00x)."
  - id: "flt-04"
    name: "direct_data_labeling_integration"
    gate_type: "required"
    condition: "Charts with <= 6 series omit detached <Legend /> components and bind series identifiers and terminal or bar-tip values directly to geometric coordinates via <LabelList> or adjacent SVG <text> nodes."
    failure_impact: "Increases visual search latency, induces saccade fatigue across wide monitors, and hides precise quantities behind ephemeral mouse-hover tooltips."
  - id: "flt-05"
    name: "contextualized_dense_metric_readouts"
    gate_type: "required"
    condition: "Every summary telemetry indicator pairs its latest numeric figure with historical sequence (inline sparkline with n >= 10 points) and a quantitative comparator (shaded normal-range band, min/max bounds, or baseline target) rather than an isolated scalar card."
    failure_impact: "Single-number KPI cards amplify recency bias, conceal volatility or steady drift toward SLO breach, and waste 70-85% of viewport pixels on non-data chrome."
veto_triggers:
  - id: "veto-01"
    name: "truncated_bar_axis_or_area_distortion"
    severity: "hard_veto"
    target_antipattern: "Bar or column chart with non-zero Y-axis minimum (e.g., min={80}), linear radius-mapped area bubbles, 3D bar projection, or superimposed dual Y-axes."
    detection_rule: "Static AST check flags any <BarChart>/<Bar> where YAxis domain[0] > 0 or domain[0] === 'dataMin', any <circle r={fn}> lacking Math.sqrt() for quantity mapping, any 3D chart transform, or any chart mounting >= 2 <YAxis> elements with different scales on the same plot area."
    mandatory_remediation: "Set <YAxis domain={[0, 'auto']} /> (or [0, sharedMax]) on all bar/column charts; transform bubble radii via Math.sqrt(v); flatten all 3D charts to 2D; split dual-unit charts into two vertically aligned small-multiple tracks sharing one X-axis."
  - id: "veto-02"
    name: "pie_donut_or_gauge_chart_comparison"
    severity: "hard_veto"
    target_antipattern: "Pie charts, donut charts, or speedometer/radial gauges used to compare categories, SLA shares, or KPI attainment."
    detection_rule: "Static AST check detects imports or JSX nodes matching PieChart, Pie, RadialBarChart, arc-based gauge SVGs, or innerRadius > 0 categorical sector encodings."
    mandatory_remediation: "Replace categorical pie/donut charts with a value-sorted horizontal bar chart (domain={[0, max]}) with direct <LabelList> values or a right-aligned tabular-nums data table; replace radial gauges with an inline sparkline + normal-range band or bullet bar."
  - id: "veto-03"
    name: "tab_fragmented_or_unaligned_multiples"
    severity: "hard_veto"
    target_antipattern: "Regional, cohort, or service telemetry comparisons hidden inside interactive tabs/carousels or displayed side-by-side with independent auto-scaled Y-axes."
    detection_rule: "Static AST check flags >= 3 sibling metric panels conditionally rendered via activeTab state or multiple chart panels whose YAxis domain prop is omitted/dataMin-dataMax instead of referencing a shared global max constant."
    mandatory_remediation: "Remove tab gating for comparative views; render all cohorts concurrently in a CSS Grid of Small Multiples bound to a single computed sharedYDomain = [0, globalMaxWithHeadroom] and shared reference threshold line."
  - id: "veto-04"
    name: "chartjunk_grid_and_detached_legend"
    severity: "conditional_block"
    target_antipattern: "Heavy dark gridlines, closed 4-sided chart borders, layered card box-shadows, SVG moire hatch patterns, or detached <Legend /> blocks for <= 6 series."
    detection_rule: "Static CSS/JSX check flags box-shadow !== 'none' on data containers, <CartesianGrid> with strokeWidth > 1 or dark hex stroke (contrast > 1.8:1 against canvas), SVG <pattern> hatching, or <Legend /> present when series count <= 6."
    mandatory_remediation: "Strip box-shadows, outer card boxes, and hatch patterns; delete <CartesianGrid> or constrain horizontal-only reference rules to 1px at 1.15:1-1.6:1 contrast (#E5E7EB on #FFFFFF); delete <Legend /> and attach direct labels to series endpoints or bar tips."
  - id: "veto-05"
    name: "isolated_scalar_kpi_card_wall"
    severity: "conditional_block"
    target_antipattern: "Top-of-dashboard row of oversized shadowed KPI cards displaying one isolated number (plus optional icon or single delta pill) with no trend history or normal-range corridor."
    detection_rule: "Static DOM/JSX audit identifies metric card grids where each card occupies > 12000 px^2 (e.g., >= 200x60px) while containing <= 2 numeric values and 0 inline <svg> sparklines or reference bands."
    mandatory_remediation: "Collapse isolated KPI cards into a dense analytical summary table pairing metric name, normal-range bounds, an inline SVG sparkline (120x22px, n >= 10 points, gray normal-range rect, min/max and latest dots), and right-aligned tabular-nums extrema + latest readout."
concrete_heuristics:
  - id: "heur-01"
    rule_statement: "IF a component renders a bar, column, or cumulative area magnitude encoding THEN pin the quantitative axis lower bound strictly to 0 so physical bar lengths maintain Lie Factor = 1.00."
    metric_or_bound: "domain[0] === 0; 0.95 <= LF <= 1.05"
    verification_method: "static_code_audit"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-01"
  - id: "heur-02"
    rule_statement: "IF a 2D circular or rectangular symbol encodes a 1D scalar magnitude THEN scale its linear radius or side length by the square root of the data value rather than directly by the data value."
    metric_or_bound: "r = k * Math.sqrt(value); area ratio === data ratio (0.95 <= LF <= 1.05)"
    verification_method: "static_code_audit"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-01"
  - id: "heur-03"
    rule_statement: "IF a dashboard compares categorical shares or ranked part-to-whole metrics THEN render a value-sorted horizontal bar chart with direct labels or a right-aligned tabular table instead of a pie or donut chart."
    metric_or_bound: "0 <PieChart>/<Pie> nodes; categories sorted descending unless intrinsic order exists"
    verification_method: "static_code_audit"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-01"
  - id: "heur-04"
    rule_statement: "IF a telemetry readout displays an operational KPI over time THEN embed a word-sized inline SVG sparkline with a gray normal-range band, extrema markers, and a direct terminal numeric label."
    metric_or_bound: "height 14-24px; aspect ratio 4:1-8:1; n >= 10 samples; normal-range band luminance contrast 1.15:1-1.35:1 against canvas (e.g., #E5E7EB at opacity 0.80-0.85 or #111111 at opacity 0.12-0.18 on #FFFFFF); 1 terminal dot linked by color to direct numeric readout"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-04"
  - id: "heur-05"
    rule_statement: "IF >= 3 regions, cohorts, or services are compared on the same metric THEN render all panels simultaneously in a CSS Grid of Small Multiples sharing one precomputed Y-axis domain and one common threshold line."
    metric_or_bound: "0 tab/carousel partitions across comparative cohorts; identical [0, sharedMax] domain on 100% of sibling panels"
    verification_method: "static_code_audit"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-02"
  - id: "heur-06"
    rule_statement: "IF a line or bar visualization plots <= 6 series THEN omit detached <Legend /> containers and render direct text/numeric labels adjacent to series endpoints or bar tips."
    metric_or_bound: "0 <Legend /> nodes for <= 6 series; label offset <= 8px from terminal coordinate"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-01"
  - id: "heur-07"
    rule_statement: "IF structural separators, reference lines, or table borders are required THEN apply Smallest Effective Difference styling to prevent 1+1=3 optical vibration and preserve figure-ground hierarchy."
    metric_or_bound: "border/stroke width <= 1px; contrast ratio 1.15:1-1.6:1 against canvas (#E5E7EB on #FFFFFF); box-shadow: none; 0 closed 4-sided chart frames"
    verification_method: "static_code_audit"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-03"
  - id: "heur-08"
    rule_statement: "IF a table, axis, or telemetry summary displays numeric values THEN enforce fixed-width tabular numerals, right alignment for numeric columns, and uniform decimal precision per column."
    metric_or_bound: "font-variant-numeric: tabular-nums; text-align: right; uniform fractional digits per column"
    verification_method: "static_code_audit"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-01"
  - id: "heur-09"
    rule_statement: "IF two variables with different units or orders of magnitude share a common time axis THEN split them into two vertically stacked synchronized single-axis tracks rather than superimposing dual Y-axes."
    metric_or_bound: "1 Y-axis unit per plot area; 100% X-axis pixel alignment between stacked tracks"
    verification_method: "static_code_audit"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-01"
  - id: "heur-10"
    rule_statement: "IF an analytical view evaluates causal mechanisms or incident risks THEN plot zero-event baseline observations alongside anomaly events, annotate interventions directly on the plot, and print measurement units, time span, and data source."
    metric_or_bound: "100% baseline zero-event inclusion (no survivorship omission); explicit unit + time window + provenance footer"
    verification_method: "state_matrix_check"
    applies_to:
      - "analytics_dense_telemetry"
    source_id: "src-03"
blind_spots:
  - id: "bs-01"
    failure_mode: "Static print-native direct plotting collapses under high-cardinality interactive telemetry (10^5 to 10^7 events), producing severe SVG/DOM overplotting, sluggish frame rates, and inability to dynamically slice multi-dimensional log streams."
    trigger_context: "Real-time observability workbenches, distributed tracing explorers, or enterprise BI tools querying millions of raw rows with ad-hoc user filters."
    counterweight_designer: "ben-shneiderman"
  - id: "bs-02"
    failure_mode: "High-density multivariate grids and minimalist high data-ink charts degrade conversion completion, violate 44x44px mobile touch ergonomics, and score lowest on at-a-glance recall and subjective acceptance among non-analyst cohorts (Inbar et al., 2007; Borkin et al., 2013)."
    trigger_context: "First-visit B2C/SaaS signup landing pages, onboarding checklists, and consumer mobile capture screens (320-430px viewports)."
    counterweight_designer: "luke-wroblewski"
  - id: "bs-03"
    failure_mode: "Aggressive erasure of framing ink and structural boundaries to push data-ink ratio toward 1.0 strips visual reference bounds (e.g., implied 0-100% ceilings) and removes interactive control signifiers required when dashboards also execute operational actions."
    trigger_context: "Transactional SaaS consoles or mixed novice/expert operational dashboards where users must execute state mutations alongside reading metrics."
    counterweight_designer: "dieter-rams"
debate_triggers:
  - id: "dbt-01"
    opposing_designer: "dieter-rams"
    conflict_axis: "multivariate_data_density_vs_radical_visual_subtraction"
    this_designer_stance: "To clarify, add detail: maximize information resolution and show 20+ variables simultaneously on one surface because clutter is a failure of layering and design, not an attribute of high data density."
    opposing_stance: "Less, but better: remove secondary variables and reduce simultaneous focal elements to preserve calm visual hierarchy and immediate self-explanatory comprehension."
    arbitration_rule: "In analytics_dense_telemetry for repeat expert analysts, preserve Tufte's multivariate density (>= 10 variables/view) while adopting Rams's neutral low-contrast chrome; in conversion, consumer, or transactional configuration surfaces, yield to Rams's element reduction."
  - id: "dbt-02"
    opposing_designer: "ben-shneiderman"
    conflict_axis: "static_eyespan_density_vs_interactive_overview_zoom_filter"
    this_designer_stance: "Plot micro and macro detail simultaneously within one eyespan so visual scanning replaces slow pointer clicks, tabs, and memory-dependent drill-downs."
    opposing_stance: "When datasets exceed visual pixel resolution, enforce Overview First, Zoom and Filter, then Details-on-Demand via tightly coupled dynamic query controls."
    arbitration_rule: "For <= 50 series or <= 2,000 aggregated points fitting within typographic resolution, enforce Tufte's static eyespan small multiples and sparklines; above 2,000 raw points or > 50 concurrent entities, layer Shneiderman's dynamic query filters and semantic zoom over Tufte-compliant summary views."
  - id: "dbt-03"
    opposing_designer: "luke-wroblewski"
    conflict_axis: "simultaneous_multivariate_exposure_vs_progressive_disclosure_and_touch_ergonomics"
    this_designer_stance: "Expose full comparative evidence concurrently in dense tables and small multiples rather than fragmenting quantitative context behind sequential disclosures."
    opposing_stance: "Prioritize one primary task per constrained viewport, apply progressive disclosure to defer secondary detail, and enforce >= 44x44px touch targets."
    arbitration_rule: "On desktop analytics viewports (>= 1024px) serving diagnostic telemetry tasks, enforce Tufte's concurrent eyespan exposure; on viewports < 768px or conversion/input capture flows, enforce Wroblewski's single-column progressive disclosure and >= 44px touch bounds."
  - id: "dbt-04"
    opposing_designer: "bret-victor"
    conflict_axis: "publication_evidence_display_vs_live_manipulable_parameter_spaces"
    this_designer_stance: "Treat information displays primarily as high-resolution visual evidence where disciplined graphic composition answers analytical questions without requiring behavioral widget machinery."
    opposing_stance: "Start from Tufte's graphic-design baseline, then surpass static paper by making models live, context-sensitive, and directly manipulable across parameter spaces."
    arbitration_rule: "For historical monitoring, post-mortem reporting, and clinical/financial status summaries, keep displays static and friction-free per Tufte; for simulation, forecasting, and AI/code authoring workspaces, yield to Victor's direct-manipulation parameter sweeps."
primary_sources:
  - id: "src-01"
    title: "The Visual Display of Quantitative Information"
    author_or_org: "Edward R. Tufte"
    year: 1983
    source_type: "book"
    url_or_identifier: "ISBN 978-0-9613921-4-7 (2nd ed., 2001; 1st ed. 1983 ISBN 0-9613921-0-X); https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/"
    extracted_invariant: "Lie Factor = graphic effect / data effect (acceptable 0.95-1.05; NYT MPG = 14.8, 1D-as-2D area distortion = 2.8); Six Principles of Graphical Integrity (p. 77); Data-Ink Ratio = data-ink / total ink (p. 93); Chartjunk species (moire, grid, duck, pp. 111-121); range-frame, slopegraph (p. 158), supertable (p. 179), and categorical pie chart ban (p. 178)."
  - id: "src-02"
    title: "Envisioning Information"
    author_or_org: "Edward R. Tufte"
    year: 1990
    source_type: "book"
    url_or_identifier: "ISBN 978-0-9613921-1-6 (ISBN-10 0-9613921-1-8); https://www.edwardtufte.com/book/envisioning-information/"
    extracted_invariant: "Micro/Macro readings ('to clarify, add detail', pp. 37-51); Layering and Separation and 1+1=3 visual vibration rule (pp. 52-65); Small Multiples enforcing eyespan comparison over memory ('Compared to what?', p. 67) with design constancy."
  - id: "src-03"
    title: "Visual Explanations: Images and Quantities, Evidence and Narrative"
    author_or_org: "Edward R. Tufte"
    year: 1997
    source_type: "book"
    url_or_identifier: "ISBN 978-0-9613921-2-3 (ISBN-10 0-9613921-2-6); https://www.edwardtufte.com/book/visual-explanations-images-and-quantities-evidence-and-narrative/"
    extracted_invariant: "Causal evidence architecture via Challenger 13-chart failure (92% missing temperatures, omission of 17 zero-damage flights out of 24 launches); Smallest Effective Difference principle (p. 73) for low-contrast secondary separation."
  - id: "src-04"
    title: "Beautiful Evidence"
    author_or_org: "Edward R. Tufte"
    year: 2006
    source_type: "book"
    url_or_identifier: "ISBN 978-0-9613921-7-8 (ISBN-10 0-9613921-7-7); https://www.edwardtufte.com/book/beautiful-evidence/"
    extracted_invariant: "Sparklines specification (pp. 46-63: word-sized typographic-resolution graphics, ~5:1 ribbon aspect ratio banked toward 45 degrees, gray normal-range band, red terminal + blue min/max dots, direct numeric label, anti-stoplight restraint); Six Fundamental Principles of Analytical Design (Ch. 5)."
  - id: "src-05"
    title: "Graphical summary of patient status"
    author_or_org: "Seth M. Powsner and Edward R. Tufte"
    year: 1994
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1016/S0140-6736(94)91406-0"
    extracted_invariant: "One-page clinical summary organizing ~22-24 physiological variables as parallel small-multiple time-series plots with standardized-height gray normal-range bands, non-linear two-year time compression, and direct numeric readouts."
  - id: "src-06"
    title: "Sparkline theory and practice"
    author_or_org: "Edward R. Tufte"
    year: 2004
    source_type: "engineering_post"
    url_or_identifier: "https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/"
    extracted_invariant: "Operational sparkline construction rules preventing dequantification and recency bias: ribbon aspect ratios (~5:1 financial, 20:1 baseball, 300:1 DNA), 45-degree slope banking, gray normal limits, red/blue dot accents, and anti-stoplight restraint."
  - id: "src-07"
    title: "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods"
    author_or_org: "William S. Cleveland and Robert McGill (JASA 79:387)"
    year: 1984
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1080/01621459.1984.10478080"
    extracted_invariant: "Empirical perceptual accuracy hierarchy across 10 elementary tasks ranking position along a common scale first above unaligned position, length, angle (pie charts), area, and color saturation."
  - id: "src-08"
    title: "How Deceptive are Deceptive Visualizations?: An Empirical Analysis of Common Distortion Techniques"
    author_or_org: "Anshul Vikram Pandey, Katharina Rall, Margaret L. Satterthwaite, Oded Nov, and Enrico Bertini (ACM CHI)"
    year: 2015
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1145/2702123.2702608"
    extracted_invariant: "Empirical confirmation that truncated Y-axes and area-as-quantity distortions cause viewers to systematically misinterpret effect sizes even when paired with accurate explanatory text."
  - id: "src-09"
    title: "Truncating the Y-Axis: Threat or Menace?"
    author_or_org: "Michael Correll, Enrico Bertini, and Steven Franconeri (ACM CHI)"
    year: 2020
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1145/3313831.3376222"
    extracted_invariant: "Demonstrates that bar-chart Y-axis truncation persistently exaggerates perceived effect severity even when explicit axis-break visual cues are rendered, while noting equivocal zero-baseline tradeoffs for trend-focused line charts."
  - id: "src-10"
    title: "The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations"
    author_or_org: "Ben Shneiderman (IEEE Symposium on Visual Languages)"
    year: 1996
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1109/VL.1996.545307"
    extracted_invariant: "Interactive Visual Information-Seeking Mantra (Overview first, zoom and filter, then details-on-demand) providing the counterweight boundary for high-cardinality multi-million-row datasets."
  - id: "src-11"
    title: "Minimalism in Information Visualization: Attitudes Towards Maximizing the Data-Ink Ratio"
    author_or_org: "Ohad Inbar, Noam Tractinsky, and Joachim Meyer (ECCE)"
    year: 2007
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1145/1362550.1362587"
    extracted_invariant: "Across 87 participants, standard bar charts significantly outperformed Tufte's extreme minimalist redesign on all 6 subjective ratings (p < .001), documenting novice acceptance limits."
  - id: "src-12"
    title: "What Makes a Visualization Memorable?"
    author_or_org: "Michelle A. Borkin, Azalea A. Vo, Zoya Bylinskii, Phillip Isola, Shashank Sunkavalli, Aude Oliva, and Hanspeter Pfister (IEEE TVCG 19:12)"
    year: 2013
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1109/TVCG.2013.234"
    extracted_invariant: "Across 2,070 visualizations, high data-ink minimalist charts scored lowest on at-a-glance memorability compared to pictorial and multi-hue editorial graphics, defining Tufte's conversion/marketing blind spot."
  - id: "src-13"
    title: "Executive Dashboards"
    author_or_org: "Edward R. Tufte"
    year: 2003
    source_type: "engineering_post"
    url_or_identifier: "https://www.edwardtufte.com/notebook/executive-dashboards/"
    extracted_invariant: "Direct repudiation of cockpit, mission-control, and gauge dashboard metaphors; recommends high-resolution tables, supertables (VDQI p. 179), sparklines, and Powsner-Tufte small multiples."
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

Edward Tufte treats an analytical interface as an instrument for quantitative reasoning rather than a decorative dashboard widget container. Every pixel rendered on screen must justify its existence by encoding data variation, comparative context, or causal mechanism. Under this operational worldview, graphical excellence is governed by three measurable invariants:

1. **Mathematical Proportionality (`0.95 <= LF <= 1.05`):** Visual mark dimensions must map linearly to numeric quantities. Length encodings (bars, columns, cumulative area bands) anchor strictly at zero, 2D area marks scale linear radius by `Math.sqrt(value)`, variable graphical dimensions never exceed data dimensions (banning 3D charts), and no single plot surface superimposes two independent Y-axis scales.
2. **Data-Ink Maximization and Layering (operational audit bound `data_ink_ratio >= 0.70`):** Non-data chrome—drop shadows, closed 4-sided chart frames, heavy dark gridlines, moire SVG patterns, decorative KPI card backgrounds, and radial gauge metaphors—must be erased so primary data signals dominate. Residual structural cues obey *Smallest Effective Difference* (`<= 1px` rules at `1.15:1-1.6:1` luminance contrast against canvas) to prevent `1+1=3` optical vibration.
3. **Concurrent Eyespan Comparison:** Quantitative thinking answers one question: *Compared to what?* Interfaces must replace isolated single-number KPI cards, detached color legends, and tab-fragmented metric views with word-sized inline sparklines (carrying gray normal-range bands, extrema markers, and direct latest labels), directly labeled series, and shared-scale Small Multiples grids viewable within a single visual sweep.

## 2. Regime Boundaries & Out-of-Universe Rationale

This skill applies strictly to **`analytics_dense_telemetry`**: desktop observability workbenches (`>= 1024px`), SRE incident monitors, financial watchlists, clinical patient summaries, and executive operational tables where repeat technical or domain-literate readers perform high-precision quantitative comparisons.

Any request falling into the four out-of-universe regimes triggers an immediate `HANDOFF` verdict before scoring:

- **`landing_onboarding_conversion` -> hand off to `luke-wroblewski` or `dieter-rams`:** Empirical studies (Inbar et al., 2007; Borkin et al., 2013) show minimalist high-density analytical charts score lowest on subjective preference and at-a-glance memorability among non-analyst prospects; conversion funnels require singular narrative focus and frictionless action capture.
- **`mobile_consumer_capture` -> hand off to `luke-wroblewski`:** Narrow touch viewports (`320-430px`) cannot sustain concurrent small-multiple grids or dense multi-column sparkline rows without violating `44x44px` touch-target minimums and squashing time-series slopes.
- **`ai_native_desktop_ide` -> hand off to `bret-victor` or `agentic-flow-architect`:** Agentic editors and live debugging environments center on streaming execution traces, diff approvals, and bidirectional code-state manipulation rather than static quantitative evidence layouts.
- **`saas_b2b_intensive` -> hand off to `ben-shneiderman` or `karri-saarinen`:** Transactional CRUD applications, bulk record management, and multi-million-row interactive log explorers require dynamic query sliders, command palettes, and explicit interactive signifiers that exceed static publication graphics.

## 3. Signal Detection Protocol

Text-only coding agents evaluate components deterministically in a single AST + CSS pass without subjective visual grading:

1. **Inspect Quantitative Encodings (`sig-01`, `critical`):** Extract all `<BarChart>`, `<AreaChart>`, `<ScatterChart>`, D3 `scaleLinear()`, and SVG `<rect>`/`<circle>` mappings. Compute `LF = ((g2 - g1) / g1) / ((d2 - d1) / d1)`. Flag any bar/column axis where `domain[0] !== 0`, any circular area mark scaling `r` linearly with `value`, any 3D CSS/Canvas projection, or any chart declaring `>= 2` distinct `yAxisId` scales on one plot.
2. **Audit Non-Data-Ink Chrome (`sig-02`, `critical`):** Scan JSX imports and stylesheets for `<PieChart>`, `<Pie>`, `<RadialBarChart>`, radial gauge arcs, `box-shadow` declarations on data containers, closed 4-sided chart borders, SVG `<pattern>` hatch fills, and `<CartesianGrid>` strokes thicker than `1px` or darker than `1.8:1` contrast against canvas.
3. **Verify Comparative Scale Parity (`sig-03`, `critical`):** Detect comparative datasets (`>= 3` cohorts, services, or regions). Confirm that all panels mount concurrently in a CSS Grid (zero conditional tab/carousel gating) and reference a single shared `yDomain` tuple rather than independent per-panel auto-scaling.
4. **Measure Label Proximity (`sig-04`, `high`):** Count `<Legend />` elements on charts with `<= 6` series and verify presence of `<LabelList>` or SVG `<text>` coordinate labels anchored within `<= 8px` of bar tips or terminal line points.
5. **Audit Metric Density and Context (`sig-05`, `high`):** Identify KPI card wrappers exceeding `12,000 px^2` displaying `<= 2` numeric values without an inline sparkline (`n >= 10` observations) and a comparative range/baseline band.
6. **Check Numeric Typography and Contrast (`sig-06`, `medium`):** Verify `font-variant-numeric: tabular-nums` and `text-align: right` on numeric `<td>`/`<th>` cells and numeric axis ticks, plus `<= 1px` low-contrast (`1.15:1-1.6:1`) hairline dividers.

## 4. Hard Filters & Veto Playbook

All five `hard_filters` (`flt-01..flt-05`) and five `veto_triggers` (`veto-01..veto-05`) enforce zero-tolerance Via Negativa pruning:

| Trigger ID | Severity | Deterministic Detection Predicate | Mandatory Remediation |
| --- | --- | --- | --- |
| `veto-01` | `hard_veto` | `<BarChart>`/`<Bar>` with `YAxis domain[0] > 0` or `'dataMin'`, linear `r` bubble scaling, 3D chart transform, or `>= 2` independent `yAxisId` axes on one plot | Enforce `domain={[0, 'auto']}` (`LF = 1.00`); apply `Math.sqrt(v)` to bubble radii; flatten 3D to 2D; split dual-unit series into stacked synchronized single-axis tracks |
| `veto-02` | `hard_veto` | `<PieChart>`, `<Pie>`, `<RadialBarChart>`, `innerRadius > 0` donut, or radial speedometer SVG | Replace with value-sorted horizontal `<BarChart>` (`domain={[0, max]}`) with `<LabelList>` or right-aligned `tabular-nums` table |
| `veto-03` | `hard_veto` | `>= 3` comparative cohorts hidden behind `activeTab` state/carousel OR sibling panels lacking a shared `yDomain` constant | Mount all panels simultaneously in a CSS Grid of Small Multiples bound to one precomputed `sharedYDomain = [0, globalMax]` |
| `veto-04` | `conditional_block` | `box-shadow` on metric cards, `<CartesianGrid>` with `strokeWidth > 1` or contrast `> 1.8:1`, closed 4-sided plot frames, SVG `<pattern>` moire, or `<Legend />` on `<= 6` series | Delete card shadows, closed borders, and hatch patterns; keep optional horizontal hairlines `<= 1px` (`#E5E7EB` on `#FFFFFF`); replace `<Legend />` with direct inline labels |
| `veto-05` | `conditional_block` | Oversized KPI cards (`> 12,000 px^2`) displaying a single scalar without `n >= 10` trend line or normal-range reference band | Refactor into a dense metric table with word-sized inline SVG sparklines (`120x22px`), gray normal-range `<rect>`, min/max markers, and direct latest value |

## 5. Executable Heuristics & Code Patterns

### Refactoring 1: Shadowed SaaS KPI Cards + Pie Chart + Truncated Bar (`min=80`) -> High-Density Sparkline Table + Zero-Baseline Direct-Labeled Bars

#### Before (Vetoed: `veto-01`, `veto-02`, `veto-04`, `veto-05` | `LF = 10.52` | Score `0` / `BLOCK`)

```tsx
import React from "react";
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
  PieChart, Pie, Cell, Legend, Tooltip, ResponsiveContainer,
} from "recharts";

const kpis = [
  { label: "Checkout API p95", value: "171 ms" },
  { label: "Error Rate (5xx)", value: "0.57%" },
  { label: "DB Pool Utilization", value: "62%" },
  { label: "Payment Auth Rate", value: "97.7%" },
];

const regionUptime = [
  { region: "US-East", uptime: 88.4 },
  { region: "EU-West", uptime: 92.1 },
  { region: "AP-South", uptime: 95.8 },
  { region: "SA-East", uptime: 97.2 },
];

const trafficShare = [
  { name: "Web", value: 52 },
  { name: "iOS", value: 27 },
  { name: "Android", value: 14 },
  { name: "API", value: 7 },
];

const PIE_COLORS = ["#ef4444", "#f59e0b", "#10b981", "#3b82f6"];

export function BloatedSaasDashboard() {
  return (
    <div style={{ display: "grid", gap: 24, padding: 24, background: "#f3f4f6" }}>
      {/* VETO-05 + VETO-04: Oversized shadowed scalar cards with zero history or normal band */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 16 }}>
        {kpis.map((k) => (
          <div
            key={k.label}
            style={{
              background: "#ffffff",
              padding: 24,
              borderRadius: 12,
              border: "1px solid #9ca3af",
              boxShadow: "0 10px 25px rgba(0,0,0,0.12)",
            }}
          >
            <div style={{ fontSize: 13, color: "#6b7280" }}>{k.label}</div>
            <div style={{ fontSize: 36, fontWeight: 700, marginTop: 8 }}>{k.value}</div>
          </div>
        ))}
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20 }}>
        {/* VETO-01 + VETO-04: Truncated Y-axis [80, 100] -> LF = 10.52 + heavy grid */}
        <div style={{ background: "#fff", padding: 20, boxShadow: "0 4px 12px rgba(0,0,0,0.1)" }}>
          <h3>Regional Uptime (%)</h3>
          <ResponsiveContainer width="100%" height={260}>
            <BarChart data={regionUptime}>
              <CartesianGrid stroke="#374151" strokeWidth={2} />
              <XAxis dataKey="region" />
              <YAxis domain={[80, 100]} />
              <Tooltip />
              <Bar dataKey="uptime" fill="#2563eb" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* VETO-02 + VETO-04: Pie chart + detached Legend forcing angle decoding & saccades */}
        <div style={{ background: "#fff", padding: 20, boxShadow: "0 4px 12px rgba(0,0,0,0.1)" }}>
          <h3>Traffic Share (%)</h3>
          <ResponsiveContainer width="100%" height={260}>
            <PieChart>
              <Pie data={trafficShare} dataKey="value" nameKey="name" outerRadius={90}>
                {trafficShare.map((entry, idx) => (
                  <Cell key={entry.name} fill={PIE_COLORS[idx]} />
                ))}
              </Pie>
              <Legend verticalAlign="bottom" />
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
```

#### After (Compliant: `LF = 1.00`, `0` Vetos, Score `100` / `APPROVE`)

```tsx
import React from "react";
import { BarChart, Bar, XAxis, YAxis, LabelList, ResponsiveContainer } from "recharts";

interface MetricRow {
  name: string;
  unit: string;
  decimals: number;
  normal: [number, number];
  series: number[];
}

const TELEMETRY_ROWS: MetricRow[] = [
  {
    name: "Checkout API p95",
    unit: "ms",
    decimals: 0,
    normal: [110, 160],
    series: [128,132,125,140,136,144,138,142,151,148,155,149,146,158,162,154,149,152,168,174,166,159,164,171],
  },
  {
    name: "Error Rate (5xx)",
    unit: "%",
    decimals: 2,
    normal: [0.0, 0.5],
    series: [0.18,0.21,0.19,0.22,0.20,0.25,0.24,0.28,0.31,0.29,0.26,0.33,0.38,0.42,0.47,0.44,0.41,0.49,0.58,0.64,0.61,0.55,0.52,0.57],
  },
  {
    name: "DB Pool Utilization",
    unit: "%",
    decimals: 0,
    normal: [30, 70],
    series: [48,51,53,50,54,58,56,60,62,59,61,64,63,65,67,64,62,60,63,66,65,61,59,62],
  },
  {
    name: "Payment Auth Rate",
    unit: "%",
    decimals: 1,
    normal: [97.5, 99.5],
    series: [98.9,98.8,99.0,98.7,98.8,98.6,98.9,98.5,98.4,98.6,98.3,98.2,98.4,98.1,98.0,98.2,97.9,97.8,97.4,97.1,97.3,97.6,97.8,97.7],
  },
];

// Sorted descending by value for immediate rank comparison
const REGION_UPTIME = [
  { region: "SA-East", uptime: 97.2 },
  { region: "AP-South", uptime: 95.8 },
  { region: "EU-West", uptime: 92.1 },
  { region: "US-East", uptime: 88.4 },
];

const TRAFFIC_SHARE = [
  { channel: "Web", pct: 52.0, reqPerSec: 14820 },
  { channel: "iOS", pct: 27.0, reqPerSec: 7695 },
  { channel: "Android", pct: 14.0, reqPerSec: 3990 },
  { channel: "API", pct: 7.0, reqPerSec: 1995 },
];

function InlineSparkline({
  series,
  normal,
  width = 120,
  height = 22,
}: {
  series: number[];
  normal: [number, number];
  width?: number;
  height?: number;
}) {
  const padY = 3;
  const padX = 4;
  const minVal = Math.min(...series, normal[0]);
  const maxVal = Math.max(...series, normal[1]);
  const span = maxVal - minVal || 1;
  const mapX = (i: number) => padX + (i / (series.length - 1)) * (width - padX * 2);
  const mapY = (v: number) => height - padY - ((v - minVal) / span) * (height - padY * 2);

  const points = series.map((v, i) => `${mapX(i).toFixed(1)},${mapY(v).toFixed(1)}`).join(" ");
  const bandTop = mapY(normal[1]);
  const bandHeight = Math.max(1, mapY(normal[0]) - bandTop);

  const minIdx = series.indexOf(Math.min(...series));
  const maxIdx = series.indexOf(Math.max(...series));
  const lastIdx = series.length - 1;
  const latest = series[lastIdx];
  const outOfBand = latest < normal[0] || latest > normal[1];

  return (
    <svg width={width} height={height} role="img" aria-label="24-hour trend sparkline">
      <rect x={padX} y={bandTop} width={width - padX * 2} height={bandHeight} fill="#E5E7EB" opacity={0.85} />
      <polyline fill="none" stroke="#374151" strokeWidth={1.25} points={points} />
      <circle cx={mapX(minIdx)} cy={mapY(series[minIdx])} r={2} fill="#1A73E8" />
      <circle cx={mapX(maxIdx)} cy={mapY(series[maxIdx])} r={2} fill="#1A73E8" />
      <circle cx={mapX(lastIdx)} cy={mapY(latest)} r={2.6} fill={outOfBand ? "#D93025" : "#111111"} />
    </svg>
  );
}

export function TufteTelemetryConsole() {
  return (
    <section className="tufte-sheet">
      <header className="tufte-header">
        <h2>Production Telemetry Summary (Last 24 Hours, Hourly Samples)</h2>
        <span className="tufte-meta">Gray band: normal range | Blue dots: 24h min/max | Red: out-of-band latest</span>
      </header>

      <table className="tufte-table">
        <thead>
          <tr>
            <th className="col-text">Metric</th>
            <th className="col-num">Normal Range</th>
            <th className="col-spark">24h Trajectory (own scale)</th>
            <th className="col-num">Min</th>
            <th className="col-num">Max</th>
            <th className="col-num">Latest</th>
          </tr>
        </thead>
        <tbody>
          {TELEMETRY_ROWS.map((row) => {
            const minV = Math.min(...row.series);
            const maxV = Math.max(...row.series);
            const latest = row.series[row.series.length - 1];
            const breach = latest < row.normal[0] || latest > row.normal[1];
            const fmt = (v: number) => `${v.toFixed(row.decimals)}${row.unit}`;
            return (
              <tr key={row.name}>
                <td className="col-text">{row.name}</td>
                <td className="col-num muted">{`${row.normal[0].toFixed(row.decimals)}-${row.normal[1].toFixed(row.decimals)}${row.unit}`}</td>
                <td className="col-spark"><InlineSparkline series={row.series} normal={row.normal} /></td>
                <td className="col-num">{fmt(minV)}</td>
                <td className="col-num">{fmt(maxV)}</td>
                <td className={breach ? "col-num alert" : "col-num strong"}>{fmt(latest)}</td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <div className="tufte-split">
        <div>
          <h3 className="tufte-subhead">Regional Uptime (%, zero baseline, LF = 1.00)</h3>
          <ResponsiveContainer width="100%" height={150}>
            <BarChart data={REGION_UPTIME} layout="vertical" margin={{ top: 4, right: 48, bottom: 4, left: 64 }}>
              <XAxis type="number" domain={[0, 100]} ticks={[0, 50, 100]} stroke="#575B5F" tickLine={false} axisLine={{ stroke: "#E5E7EB" }} fontSize={11} />
              <YAxis type="category" dataKey="region" axisLine={false} tickLine={false} stroke="#111111" fontSize={12} width={60} />
              <Bar dataKey="uptime" fill="#6B7280" barSize={14} isAnimationActive={false}>
                <LabelList dataKey="uptime" position="right" formatter={(v: unknown) => `${Number(v).toFixed(1)}%`} fill="#111111" fontSize={12} />
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div>
          <h3 className="tufte-subhead">Traffic Share by Client (Replaces Pie Chart)</h3>
          <table className="tufte-table">
            <thead>
              <tr>
                <th className="col-text">Channel</th>
                <th className="col-num">Share</th>
                <th className="col-num">Req/s</th>
              </tr>
            </thead>
            <tbody>
              {TRAFFIC_SHARE.map((row) => (
                <tr key={row.channel}>
                  <td className="col-text">{row.channel}</td>
                  <td className="col-num">{row.pct.toFixed(1)}%</td>
                  <td className="col-num">{row.reqPerSec.toLocaleString("en-US")}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
}
```

```css
.tufte-sheet { background: #FFFFFF; color: #111111; padding: 16px; max-width: 960px; }
.tufte-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px; }
.tufte-meta { font-size: 11px; color: #575B5F; }
.tufte-subhead { font-size: 13px; font-weight: 600; margin: 0 0 8px 0; color: #111111; }
.tufte-table { width: 100%; border-collapse: collapse; margin-bottom: 24px; }
.tufte-table th { font-size: 11px; font-weight: 600; color: #575B5F; border-bottom: 1px solid #111111; padding: 6px 8px; }
.tufte-table td { font-size: 13px; border-bottom: 1px solid #E5E7EB; padding: 6px 8px; }
.col-text { text-align: left; }
.col-num { text-align: right; font-variant-numeric: tabular-nums; }
.col-spark { text-align: center; vertical-align: middle; }
.muted { color: #575B5F; }
.strong { font-weight: 600; color: #111111; }
.alert { font-weight: 700; color: #D93025; }
.tufte-split { display: grid; grid-template-columns: 1.2fr 1fr; gap: 32px; align-items: start; }
```

---

### Refactoring 2: 4-Tab Independent-Scale Regional Comparator -> Shared-Scale Small Multiples Grid

#### Before (Vetoed: `veto-03` | `7.52x` Peak Ratio Collapsed to `1.00x` | Score `40` / `BLOCK`)

```tsx
import React, { useState } from "react";
import { LineChart, Line, XAxis, YAxis, ResponsiveContainer } from "recharts";

const REGIONS: Record<string, { t: string; ms: number }[]> = {
  "US-East": [19,21,20,22,24,23,21,25,22,20,23,21].map((ms, i) => ({ t: `${i}h`, ms })),
  "EU-West": [24,26,25,28,31,29,27,30,34,31,28,29].map((ms, i) => ({ t: `${i}h`, ms })),
  "AP-South": [48,52,61,89,134,188,172,145,118,96,82,74].map((ms, i) => ({ t: `${i}h`, ms })),
  "SA-East": [21,23,22,24,26,25,29,27,24,23,25,22].map((ms, i) => ({ t: `${i}h`, ms })),
};

export function TabbedLatencyComparator() {
  const [activeTab, setActiveTab] = useState<string>("US-East");
  return (
    <div>
      {/* VETO-03: Tab gating forces memory recall instead of concurrent eyespan comparison */}
      <div role="tablist" style={{ display: "flex", gap: 8, marginBottom: 12 }}>
        {Object.keys(REGIONS).map((r) => (
          <button key={r} role="tab" aria-selected={activeTab === r} onClick={() => setActiveTab(r)}>
            {r}
          </button>
        ))}
      </div>
      {/* VETO-03: Independent local auto-scale collapses 25 ms and 188 ms to identical heights */}
      <ResponsiveContainer width="100%" height={220}>
        <LineChart data={REGIONS[activeTab]}>
          <XAxis dataKey="t" />
          <YAxis domain={["dataMin", "dataMax"]} />
          <Line type="monotone" dataKey="ms" stroke="#2563eb" dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
```

#### After (Compliant: Shared Y-Domain `[0, 210] ms`, Simultaneous Eyespan Grid, Score `100` / `APPROVE`)

```tsx
import React, { useMemo } from "react";
import { LineChart, Line, XAxis, YAxis, ReferenceLine, ResponsiveContainer } from "recharts";

interface RegionSeries {
  region: string;
  points: { t: string; ms: number }[];
}

const REGION_SERIES: RegionSeries[] = [
  { region: "US-East", points: [19,21,20,22,24,23,21,25,22,20,23,21].map((ms, i) => ({ t: `${i}h`, ms })) },
  { region: "EU-West", points: [24,26,25,28,31,29,27,30,34,31,28,29].map((ms, i) => ({ t: `${i}h`, ms })) },
  { region: "AP-South", points: [48,52,61,89,134,188,172,145,118,96,82,74].map((ms, i) => ({ t: `${i}h`, ms })) },
  { region: "SA-East", points: [21,23,22,24,26,25,29,27,24,23,25,22].map((ms, i) => ({ t: `${i}h`, ms })) },
];

const SLO_THRESHOLD_MS = 100;

export function SmallMultiplesLatencyGrid() {
  // Compute one shared Y-domain across all panels so visual height equals true magnitude ratio (7.52x)
  const sharedYDomain = useMemo<[number, number]>(() => {
    const globalMax = Math.max(...REGION_SERIES.flatMap((r) => r.points.map((p) => p.ms)));
    const ceiling = Math.ceil((globalMax * 1.1) / 10) * 10; // 188 -> 210 ms
    return [0, ceiling];
  }, []);

  return (
    <section className="sm-wrapper">
      <div className="sm-header">
        <h2>Regional API p95 Latency (ms) — Shared Y-Scale [0, {sharedYDomain[1]} ms]</h2>
        <span className="tufte-meta">Dashed rule: 100 ms SLO threshold</span>
      </div>
      <div className="sm-grid">
        {REGION_SERIES.map((series, idx) => {
          const peak = Math.max(...series.points.map((p) => p.ms));
          const latest = series.points[series.points.length - 1].ms;
          const breached = peak > SLO_THRESHOLD_MS;
          const isLeftColumn = idx % 2 === 0;
          return (
            <div key={series.region} className="sm-panel">
              <div className="sm-panel-head">
                <span className="sm-title">{series.region}</span>
                <span className={breached ? "sm-stat alert" : "sm-stat"}>
                  {latest} ms (peak {peak})
                </span>
              </div>
              <ResponsiveContainer width="100%" height={130}>
                <LineChart data={series.points} margin={{ top: 8, right: 8, bottom: 4, left: isLeftColumn ? 0 : 4 }}>
                  <XAxis
                    dataKey="t"
                    ticks={["0h", "6h", "11h"]}
                    axisLine={{ stroke: "#E5E7EB" }}
                    tickLine={false}
                    fontSize={10}
                    stroke="#575B5F"
                  />
                  <YAxis
                    domain={sharedYDomain}
                    ticks={[0, SLO_THRESHOLD_MS, sharedYDomain[1]]}
                    hide={!isLeftColumn}
                    axisLine={false}
                    tickLine={false}
                    fontSize={10}
                    stroke="#575B5F"
                    width={32}
                  />
                  <ReferenceLine y={SLO_THRESHOLD_MS} stroke="#CCCCCC" strokeDasharray="3 3" strokeWidth={1} />
                  <Line
                    type="linear"
                    dataKey="ms"
                    stroke={breached ? "#D93025" : "#374151"}
                    strokeWidth={breached ? 1.8 : 1.3}
                    dot={false}
                    isAnimationActive={false}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          );
        })}
      </div>
    </section>
  );
}
```

```css
.sm-wrapper { background: #FFFFFF; padding: 16px; max-width: 820px; }
.sm-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px; }
.sm-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px 28px; }
.sm-panel { border-top: 1px solid #E5E7EB; padding-top: 8px; }
.sm-panel-head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px; }
.sm-title { font-size: 12px; font-weight: 600; color: #111111; }
.sm-stat { font-size: 12px; color: #575B5F; font-variant-numeric: tabular-nums; }
.sm-stat.alert { color: #D93025; font-weight: 700; }
```

## 6. Blind Spots & Counterweights

1. **Multi-Million-Row Interactive Exploration (`bs-01` -> `ben-shneiderman`):** Static direct-plotting principles originate in high-resolution print media. When telemetry volumes exceed `2,000` raw marks or `50` concurrent series, plotting every point causes SVG occlusion and frame drops; integrate Shneiderman's *Overview first, zoom and filter, then details-on-demand* with coupled dynamic query controls.
2. **Conversion Funnels and Mobile Touch Capture (`bs-02` -> `luke-wroblewski`):** Empirical studies confirm that extreme data-ink minimalism scores lowest on novice subjective ratings (Inbar et al., 2007, `p < .001`) and at-a-glance memorability (Borkin et al., 2013). On mobile viewports (`< 768px`) or acquisition flows, defer to Wroblewski's progressive disclosure and `>= 44x44px` touch ergonomics.
3. **Reference Bound Erasure and Operational Controls (`bs-03` -> `dieter-rams`):** Stripping all framing geometry can hide implied reference bounds (such as `0-100%`) or eliminate actionable affordances when analytical surfaces double as control planes; retain disciplined, low-contrast structural anchors per Rams's unobtrusive clarity.

## 7. Adversarial Debate Positions

- **vs. `dieter-rams` (`multivariate_data_density_vs_radical_visual_subtraction`):** Tufte insists on adding multivariate detail to clarify relationships (*Envisioning Information*, p. 37), whereas Rams removes non-essential elements to calm the interface. *Arbitration:* In repeat-use `analytics_dense_telemetry`, enforce Tufte's multivariate density while using Rams's restrained neutral surfaces; in consumer or first-visit surfaces, yield to Rams's element subtraction.
- **vs. `ben-shneiderman` (`static_eyespan_density_vs_interactive_overview_zoom_filter`):** Tufte minimizes interaction cost by placing micro and macro detail in one static eyespan; Shneiderman manages vast datasets via interactive filtering and zoom. *Arbitration:* Below `50` series / `2,000` plotted points, enforce static Tufte small multiples; above that bound, couple Shneiderman's dynamic filters with Tufte-compliant summary charts.
- **vs. `luke-wroblewski` (`simultaneous_multivariate_exposure_vs_progressive_disclosure_and_touch_ergonomics`):** Tufte refuses to hide comparative evidence across tabs or collapsed drawers; Wroblewski prioritizes single-focus mobile ergonomics. *Arbitration:* On desktop telemetry (`>= 1024px`), enforce Tufte's concurrent grid exposure; below `768px` or in capture funnels, enforce Wroblewski's progressive disclosure and `44px` touch targets.
- **vs. `bret-victor` (`publication_evidence_display_vs_live_manipulable_parameter_spaces`):** Tufte prioritizes disciplined static evidence displays; Victor builds on Tufte's graphic-design foundation to introduce live manipulable models. *Arbitration:* Keep historical monitoring and incident reporting static and distortion-free per Tufte; yield to Victor for interactive simulation, forecasting, and coding workspaces.

## 8. Primary Source Notes

- **`src-01` (*The Visual Display of Quantitative Information*, 1983 / 2nd ed. 2001):** Origin of the Lie Factor (`0.95-1.05`), Six Principles of Graphical Integrity (p. 77), Data-Ink Ratio (p. 93), Chartjunk taxonomy (pp. 111-121), slopegraph (p. 158), supertable (p. 179), and categorical pie chart ban (p. 178).
- **`src-02` (*Envisioning Information*, 1990):** Establishes Micro/Macro readings (`"to clarify, add detail"`, p. 37), Layering and Separation (`1+1=3` optical vibration, p. 53), and Small Multiples (`"Compared to what?"`, p. 67).
- **`src-03` (*Visual Explanations*, 1997):** Establishes causal plotting standards through the Challenger 13-chart critique (zero-damage baseline omission) and the *Smallest Effective Difference* rule (p. 73).
- **`src-04` (*Beautiful Evidence*, 2006), `src-06` (`Sparkline theory and practice`, 2004), and `src-13` (`Executive Dashboards`, 2003):** Formalizes word-sized sparklines (pp. 46-63: aspect ratio banking, gray normal-range band, red/blue point linkage, anti-stoplight restraint), repudiates cockpit/gauge metaphors, and states the Six Fundamental Principles of Analytical Design (Ch. 5).
- **`src-05` (Powsner & Tufte, *The Lancet*, 1994, `doi:10.1016/S0140-6736(94)91406-0`):** Operational clinical prototype displaying ~22-24 variables on one page via standardized-height normal-range small multiples and non-linear two-year time compression.
- **`src-07..src-12` (Empirical Validations & Boundaries):** Cleveland & McGill (1984) validates position-over-angle perceptual ranking; Pandey et al. (2015) and Correll et al. (2020) confirm persistent exaggeration from truncated bar axes; Shneiderman (1996), Inbar et al. (2007), and Borkin et al. (2013) anchor the interactive, novice-acceptance, and memorability blind-spot boundaries.
