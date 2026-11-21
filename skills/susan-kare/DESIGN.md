---
schema_version: "1.0.0"
identity:
  slug: "susan-kare"
  display_name: "Susan Kare"
  barbell_pole: "lindy_anchor"
  archetype_synthetic: false
  primary_domain: "High-legibility iconic semiotics, minimal pixel-grid visual metaphors, hardware-decoupled symbols, and unambiguous recognition"
  core_axiom: "Every UI icon must pass a 32x32 1-bit silhouette test on a uniform integer grid, function as a distinct road sign rather than illustration, and pair any non-universal or AI action with a visible persistent text label."
  active_era: "1983-present"
  skin_in_the_game_evidence:
    - artifact: "Apple Macintosh 1984 1-bit iconography and Command key symbol (U+2318)"
      year: 1984
      verifiable_metric: "16x16 Bowen-knot bitmap shipped continuously on Apple keyboards for 42+ years (1984-2026) and standardized in Unicode 1.1 (1993) as U+2318 PLACE OF INTEREST SIGN; original 1982-1983 icon sketchbooks acquired jointly by MoMA and SFMOMA (2015, Obj. 112.2015)"
      source_id: "src-01"
    - artifact: "Apple Macintosh MacPaint 32x32 1-bit toolset (Lasso, Paint Bucket, Brush) and Trash/Document/Application icon system"
      year: 1984
      verifiable_metric: "32x32 1-bit monochrome silhouettes established cross-platform GUI vocabulary (folded-corner document, pouring paint bucket, slip-knot lasso, trash can, bomb, watch) persisted across desktop and mobile software for 4+ decades"
      source_id: "src-02"
    - artifact: "Chicago (Elefont), Geneva, and Monaco Macintosh bitmap typefaces"
      year: 1984
      verifiable_metric: "Chicago served as default Mac OS UI font across 13 years (System 1 through 7.6, 1984-1997) and first 4 generations of monochrome iPod; Monaco shipped continuously from 1984 through macOS Sequoia 15.2 (40+ years) alongside Geneva, serving as default Mac OS X Terminal/Xcode monospace until 2009"
      source_id: "src-03"
    - artifact: "Microsoft Windows 3.0 Solitaire 16-color VGA card deck (cards.dll) and Control Panel icons"
      year: 1990
      verifiable_metric: "71x96 pixel 16-color VGA card faces shipped unchanged in cards.dll from Windows 3.0 (1990) through Windows XP (16+ years), onboarding first-time PC users to mouse drag-and-drop; inducted into World Video Game Hall of Fame (2019) with 35 million monthly active players reported by 2020"
      source_id: "src-12"
regime_fit:
  primary_regimes:
    - "mobile_consumer_capture"
  secondary_regimes:
    - "landing_onboarding_conversion"
  out_of_universe_regimes:
    - regime: "ai_native_desktop_ide"
      reason: "Persistent labeled icon chrome consumes code-editor viewport real estate and imposes KLM-GOMS pointer homing penalties (H=0.4s + P=1.1s) on developers executing hundreds of nested commands per hour via keyboard shortcuts and command palettes."
    - regime: "saas_b2b_intensive"
      reason: "Multi-entity B2B workspaces exceeding 25-50 domain-specific CRUD mutations exhaust the finite set of distinguishable 1-bit silhouettes, degrading scannability compared to neutral chrome reduction, keyboard shortcuts, and searchable Cmd+K command menus."
    - regime: "analytics_dense_telemetry"
      reason: "Quantitative observability dashboards require maximizing the data-ink ratio via tabular numerals, range frames, small multiples, and sparklines; categorical pictograms add non-data ink (chartjunk) and cannot encode continuous multivariate distributions."
high_weight_signals:
  - id: "sig-01"
    name: "unlabeled_non_universal_action_icons"
    weight: "critical"
    category: "visual_semiotics"
    detects_before_others: "Within 10s, flags interactive controls displaying domain-specific, abstract, or AI icons without persistent visible text labels or hiding labels behind hover-only tooltips that fail on touch."
    observable_indicator: "Count of interactive controls (<button>, <a>, [role='button']) whose icon is outside the 6-item universal allowlist {close, search, back, home, trash, menu} and lacks a persistent visible sibling text node (non-sr-only, opacity > 0, not hover-gated)."
    threshold: "0 unlabeled non-universal action controls"
    direction: "lower_is_better"
    source_id: "src-05"
  - id: "sig-02"
    name: "ambiguous_duplicate_metaphor_collision"
    weight: "critical"
    category: "agentic_trust"
    detects_before_others: "Within 10s, catches distinct actions sharing an identical glyph stem (especially multiple AI sparkles, star, or wand variants) or sibling icons with near-identical outer silhouettes."
    observable_indicator: "Count of distinct action handlers within a single view sharing the same SVG path signature, icon stem (e.g., Sparkles/Wand/Star), or colliding outer contour without disambiguating visible text."
    threshold: "0 duplicate or colliding icon metaphors per view"
    direction: "lower_is_better"
    source_id: "src-06"
  - id: "sig-03"
    name: "icon_grid_and_stroke_inconsistency"
    weight: "high"
    category: "visual_semiotics"
    detects_before_others: "Within 10s, detects mismatched SVG viewBox dimensions (e.g., 16x16 beside 24x24 and 32x32) or heterogeneous/hairline stroke weights (<1.0px or >0.25px spread) within the same toolbar."
    observable_indicator: "Distinct count of SVG integer viewBox grids across peer icons on one surface AND stroke-width range/minimum across those peer SVGs."
    threshold: "1 uniform integer viewBox per surface AND uniform stroke-width in [1.5, 2.0] px (0 strokes < 1.0 px)"
    direction: "exact_match"
    source_id: "src-08"
  - id: "sig-04"
    name: "non_text_contrast_or_color_only_state"
    weight: "critical"
    category: "cognitive_load"
    detects_before_others: "Within 10s, identifies pale low-contrast icons (<3.0:1 luminance ratio) or status/category badges differentiated solely by color dots without distinct geometric shapes and visible text."
    observable_indicator: "Minimum WCAG 2.2 relative luminance contrast ratio of functional icon foreground/stroke against background AND count of semantic status indicators lacking both unique geometry and visible text."
    threshold: "contrast_ratio >= 3.0:1 (target >= 4.5:1) AND 0 color-only status indicators"
    direction: "higher_is_better"
    source_id: "src-07"
  - id: "sig-05"
    name: "missing_accessible_icon_semantics"
    weight: "high"
    category: "interaction_physics"
    detects_before_others: "Within 10s, catches icon-only buttons missing aria-label, decorative SVGs beside text missing aria-hidden='true', standalone semantic SVGs lacking accessible text, or touch targets smaller than 44x44 CSS px on mobile."
    observable_indicator: "Boolean compliance across all icon elements: (icon-only control => non-empty action-verb aria-label) AND (icon+text => svg[aria-hidden='true'][focusable='false']) AND (mobile interactive box >= 44x44 CSS px; desktop >= 24x24 CSS px)."
    threshold: "true (100% control compliance)"
    direction: "boolean_required"
    source_id: "src-07"
  - id: "sig-06"
    name: "svg_primitive_bloat_or_non_binary_effects"
    weight: "medium"
    category: "visual_semiotics"
    detects_before_others: "Within 10s, detects illustrative SVG bloat (>6 primitives, gradients, drop-shadow filters) inside <=32px UI icons or legacy hardware metaphors bound to mismatched cloud/auto-sync behaviors."
    observable_indicator: "Count of <=32px UI action SVGs with >6 geometric primitives, any <linearGradient>/<radialGradient>/<filter> child, or legacy hardware icons (e.g., floppy disk) mapped to cloud-sync, auto-save, or export actions."
    threshold: "<= 6 SVG primitives per icon, 0 filter/gradient tags, 0 behavior-mismatched legacy hardware metaphors"
    direction: "lower_is_better"
    source_id: "src-09"
hard_filters:
  - id: "flt-01"
    name: "mandatory_visible_label_for_non_universal_actions"
    gate_type: "required"
    condition: "Every interactive control outside {close, search, back, home, trash, menu} renders a persistent visible text label (not hover-only or sr-only) adjacent to its icon."
    failure_impact: "Under mobile touch interaction (no hover) and first-exposure fatigue, unlabeled non-universal icons drop to 0% task invocation (NN/g clock-for-history study) or fragmented misinterpretation (0% AI attribution for isolated sparkles, n=107)."
  - id: "flt-02"
    name: "uniform_integer_svg_grid_and_minimum_stroke"
    gate_type: "required"
    condition: "All sibling UI icons on a surface share one integer square viewBox (e.g., '0 0 24 24', '0 0 20 20', or '0 0 16 16'), uniform stroke-width in [1.5, 2.0] px (or 1-bit solid fill), and zero strokes < 1.0 px."
    failure_impact: "Subpixel hairlines (<1.0 px) and mixed coordinate grids blur via anti-aliasing on 1x displays and outdoor mobile glare, nearly doubling visual search time (15.4s ultra-flat vs 8.0s traditional icons in INTERACT 2015)."
  - id: "flt-03"
    name: "non_text_contrast_and_non_color_state_encoding"
    gate_type: "required"
    condition: "Every functional icon and state glyph achieves >= 3.0:1 relative luminance contrast (WCAG 2.1/2.2 SC 1.4.11) AND every status/category badge pairs a distinct geometric silhouette with explicit visible text rather than color alone (SC 1.4.1)."
    failure_impact: "Low-vision cohorts, color-vision-deficient users, and mobile operators in daylight fail to distinguish capture sync/error states, causing silent upload loss and repeated retries."
  - id: "flt-04"
    name: "accessible_name_and_touch_target_envelope"
    gate_type: "required"
    condition: "Every icon-only button carries a descriptive action-verb aria-label, every SVG paired with visible text carries aria-hidden='true' and focusable='false', and hit regions measure >= 44x44 CSS px on mobile (>= 24x24 CSS px on desktop)."
    failure_impact: "Assistive technologies announce unlabelled icon controls generically as 'button' or read path noise, while sub-44px mobile icon buttons generate adjacent-target mis-taps during one-handed capture."
veto_triggers:
  - id: "veto-01"
    name: "unlabeled_ai_sparkle_or_duplicate_symbol_toolbar"
    severity: "hard_veto"
    target_antipattern: "Toolbar or action bar shipping unlabeled domain/AI icons or reusing generic AI sparkle/wand/star variants for multiple distinct actions on one screen."
    detection_rule: "Static JSX/DOM audit finds >= 1 interactive control with a non-universal icon (including any AI sparkle/wand glyph) lacking a persistent visible text label, OR >= 2 distinct action handlers in one view using the same icon symbol stem."
    mandatory_remediation: "Replace duplicate sparkles with distinct functional silhouettes matching each concrete verb/noun and attach a concise persistent visible text label (1-2 words) to every non-universal control."
  - id: "veto-02"
    name: "subpixel_hairline_or_mixed_svg_grid_system"
    severity: "hard_veto"
    target_antipattern: "Inconsistent icon set mixing viewBox scales (16x16, 24x24, 32x32) or hairline strokes (<1.0px) alongside thick strokes (>2.25px) on the same bar."
    detection_rule: "Static SVG/JSX audit detects >1 distinct viewBox value among sibling toolbar icons, non-integer viewBox dimensions, any stroke-width < 1.0, or >0.25px stroke-width variance across siblings."
    mandatory_remediation: "Normalize all sibling SVGs to one integer square viewBox (e.g., viewBox='0 0 24 24'), enforce one uniform strokeWidth in [1.5, 2.0] px with stroke='currentColor' and fill='none', and preserve a >=1px safe zone."
  - id: "veto-03"
    name: "color_only_state_or_sub_3_to_1_icon_contrast"
    severity: "hard_veto"
    target_antipattern: "Status/category indicators built purely from colored circles/dots or functional icons rendered below 3.0:1 relative luminance contrast."
    detection_rule: "CSS/JSX audit computes relative luminance contrast < 3.0:1 for any functional icon stroke/fill against its background, OR detects >= 2 semantic states distinguished exclusively via color CSS tokens without unique geometric silhouettes and visible text."
    mandatory_remediation: "Increase foreground/background luminance contrast to >= 3.0:1 (target >= 4.5:1) and encode every state with a distinct 1-bit geometric silhouette (e.g., check-circle, sync-arrows, alert-triangle, dashed-square) plus an explicit visible text label."
  - id: "veto-04"
    name: "undersized_touch_target_or_missing_aria_contract"
    severity: "hard_veto"
    target_antipattern: "Mobile icon buttons clipped to glyph dimensions (e.g., 20x20px) or omitting aria-label on icon-only buttons / aria-hidden='true' on decorative paired SVGs."
    detection_rule: "CSS/JSX audit detects mobile interactive icon controls with min-width < 44px or min-height < 44px (desktop < 24x24px), OR any icon-only control missing a non-empty aria-label/aria-labelledby, OR any paired decorative SVG missing aria-hidden='true'."
    mandatory_remediation: "Set min-width: 44px; min-height: 44px on mobile controls (>= 24x24px desktop) via hit-area padding around the 20-24px icon, add explicit action-verb aria-label to icon-only universal buttons, and add aria-hidden='true' focusable='false' to SVGs beside visible text."
  - id: "veto-05"
    name: "bloated_svg_or_mismatched_legacy_hardware_metaphor"
    severity: "conditional_block"
    target_antipattern: "Illustrative multi-path SVG with gradients/shadows used as a <=32px UI icon, or legacy physical hardware symbols (e.g., floppy disk) mapped to incongruent cloud auto-sync or export behaviors."
    detection_rule: "Static SVG/JSX audit detects >6 path/shape primitives in a <=32px UI icon, any <linearGradient>/<radialGradient>/<filter> element inside an action SVG, OR a floppy-disk glyph mapped to handlers/labels specifying 'sync', 'auto-save', 'cloud', or 'export'."
    mandatory_remediation: "Remove all SVG filters, shadows, and gradients; simplify geometry to <=6 primitives that pass a 1-bit monochrome silhouette test; and swap workflow-mismatched hardware icons for behavior-accurate symbols (e.g., circular arrows for Sync, arrow-into-tray for Download) paired with visible labels."
concrete_heuristics:
  - id: "heur-01"
    rule_statement: "IF an SVG acts as a UI action or status icon rendered at <= 32px, THEN it MUST pass 1-bit monochrome reduction using <= 6 geometric primitives, 0 <filter>/<linearGradient>/<radialGradient> elements, and currentColor inheritance."
    metric_or_bound: "<= 6 primitives; 0 gradients/filters"
    verification_method: "static_code_audit"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-02"
  - id: "heur-02"
    rule_statement: "IF multiple icons occupy the same toolbar, tab bar, or onboarding step list, THEN every SVG MUST share one integer square viewBox (16, 20, or 24), uniform stroke-width in [1.5, 2.0] px, and >= 1px perimeter safe zone."
    metric_or_bound: "1 viewBox per group; stroke-width 1.5-2.0px; >= 1px safe zone"
    verification_method: "static_code_audit"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-08"
  - id: "heur-03"
    rule_statement: "IF an action icon lies outside the 6-symbol universal allowlist {close, search, back, home, trash, menu}, THEN the control MUST render a persistent visible text label (1-2 words) and MUST NOT hide meaning behind hover-only tooltips."
    metric_or_bound: "100% persistent visible labels on non-universal actions; 0 hover-only tooltips"
    verification_method: "static_code_audit"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-05"
  - id: "heur-04"
    rule_statement: "IF a view exposes >= 2 AI-assisted or automated capture actions, THEN each action MUST use a distinct functional verb/noun silhouette rather than repeating generic sparkle/wand/star glyphs, always paired with a visible verb label."
    metric_or_bound: "0 duplicate icon stems per view; 0 unlabeled AI sparkles"
    verification_method: "static_code_audit"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-06"
  - id: "heur-05"
    rule_statement: "IF >= 3 peer icons sit adjacent in a mobile bar or card grid, THEN sibling icons MUST exhibit distinct outer silhouettes and maintain >= 2 SVG units of spacing between internal strokes on a 24x24 grid."
    metric_or_bound: ">= 2px internal/inter-element gap on 24x24 grid; distinct outer contours"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-08"
  - id: "heur-06"
    rule_statement: "IF an icon or badge communicates status, category, or interactive state, THEN its foreground-to-background luminance contrast MUST be >= 3.0:1 (target >= 4.5:1) AND each state MUST combine distinct shape geometry plus explicit visible text."
    metric_or_bound: "contrast >= 3.0:1 (target >= 4.5:1); 0 color-only states"
    verification_method: "state_matrix_check"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-07"
  - id: "heur-07"
    rule_statement: "IF an SVG sits beside visible button text, THEN set aria-hidden='true' and focusable='false' on the SVG; IF an allowlisted universal icon operates without visible text, THEN set an explicit action-verb aria-label on the parent button/link."
    metric_or_bound: "100% aria-hidden on paired SVGs; 100% action-verb aria-label on icon-only controls"
    verification_method: "static_code_audit"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-07"
  - id: "heur-08"
    rule_statement: "IF an icon triggers an interactive action, THEN its clickable hit envelope MUST be >= 44x44 CSS px on mobile touch viewports (>= 24x24 CSS px minimum on desktop pointer UIs) with >= 8px gap between adjacent touch targets."
    metric_or_bound: ">= 44x44 CSS px mobile; >= 24x24 CSS px desktop; >= 8px spacing"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-07"
  - id: "heur-09"
    rule_statement: "IF a custom or physical-hardware metaphor is proposed for a workflow action (e.g., floppy disk for save/sync), THEN align the symbol strictly to actual system behavior (circular arrows for sync, arrow-into-tray for download) and require >= 67% ISO 9186-1 open comprehension before omitting reinforcing copy."
    metric_or_bound: ">= 67% ISO 9186-1 comprehension; 0 behavior-mismatched hardware metaphors"
    verification_method: "runtime_telemetry"
    applies_to:
      - "mobile_consumer_capture"
      - "landing_onboarding_conversion"
    source_id: "src-09"
blind_spots:
  - id: "bs-01"
    failure_mode: "Persistent labeled icon bars consume editor real estate and impose KLM-GOMS hand-homing and pointing latency (H=0.4s + P=1.1s per action) in keyboard-intensive developer workflows where memorized text commands execute in K=0.28s."
    trigger_context: "ai_native_desktop_ide and code-centric desktop workbenches exceeding 200 command invocations per hour."
    counterweight_designer: "jef-raskin"
  - id: "bs-02"
    failure_mode: "Representational iconography exhausts distinguishable 1-bit silhouettes beyond ~20 distinct actions, causing toolbar clutter and scan fatigue in deep multi-entity enterprise software."
    trigger_context: "saas_b2b_intensive workspaces with >50 domain-specific workflow actions, batch mutations, and dense triage tables."
    counterweight_designer: "karri-saarinen"
  - id: "bs-03"
    failure_mode: "Pictographic road-sign metaphors cannot encode continuous quantitative distributions, statistical variance, or high-frequency telemetry; inserting icons into analytic tables degrades the data-ink ratio into chartjunk."
    trigger_context: "analytics_dense_telemetry observability consoles, financial matrices, and real-time operational monitoring dashboards."
    counterweight_designer: "edward-tufte"
debate_triggers:
  - id: "dbt-01"
    opposing_designer: "karri-saarinen"
    conflict_axis: "explicit_iconic_discoverability_vs_keyboard_first_chrome_reduction"
    this_designer_stance: "Primary capture and onboarding controls must remain persistently exposed as high-contrast 1-bit silhouettes paired with concise visible labels so touch and first-exposure users identify actions without hunting or memorizing shortcuts."
    opposing_stance: "Persistent labeled icon chrome steals screen density and introduces visual noise in daily productivity workspaces; actions belong inside a searchable Cmd+K command menu, single-key shortcuts, and right-click contextual menus."
    arbitration_rule: "IF regime IN {mobile_consumer_capture, landing_onboarding_conversion} OR touch_input_share > 50% OR weekly_repeat_sessions < 3, THEN susan-kare wins; IF regime IN {saas_b2b_intensive, ai_native_desktop_ide} AND desktop_keyboard_sessions > 80% AND command_vocabulary > 25, THEN karri-saarinen wins."
  - id: "dbt-02"
    opposing_designer: "jef-raskin"
    conflict_axis: "iconic_visual_anchoring_vs_universal_text_and_keyboard_habituation"
    this_designer_stance: "Distinct road-sign silhouettes paired with 1-2 word labels accelerate peripheral landmark scanning and cross-lingual comprehension on constrained mobile touchscreens where physical keyboard homing does not exist."
    opposing_stance: "Unlabeled icons are cryptic and icons alongside text often add redundant clutter; humane desktop systems should prioritize universal text commands, modeless keyboard habituation, and eliminating mouse homing cost (H=0.4s)."
    arbitration_rule: "IF viewport_width <= 480px (touch-only mobile capture) OR consumer onboarding serves multilingual/first-time cohorts, THEN susan-kare wins; IF physical_keyboard_present AND repeated_task_frequency > 30/hr AND KLM-GOMS pointer cost exceeds shortcut by > 1.0s/action, THEN jef-raskin wins."
  - id: "dbt-03"
    opposing_designer: "edward-tufte"
    conflict_axis: "pictographic_status_semiotics_vs_maximum_data_ink_quantitative_precision"
    this_designer_stance: "Discrete workflow states (e.g., Synced, Syncing, Upload failed, Offline draft) require distinct geometric icon shapes plus high-contrast text badges so operators perceive state transitions reliably without parsing raw numbers."
    opposing_stance: "Every non-data pixel competes with quantitative evidence; analytic displays should replace categorical pictograms with direct tabular numbers, range frames, small multiples, and word-sized sparklines targeting a data-ink ratio near 1.0."
    arbitration_rule: "IF state_cardinality <= 6 discrete categorical workflow states in capture or onboarding UIs, THEN susan-kare wins; IF display renders continuous time-series metrics, >= 10 simultaneous data columns, or statistical distributions, THEN edward-tufte wins."
primary_sources:
  - id: "src-01"
    title: "Swedish Campground (The Original Macintosh)"
    author_or_org: "Andy Hertzfeld (documenting Susan Kare and Steve Jobs)"
    year: 1983
    source_type: "engineering_post"
    url_or_identifier: "https://www.folklore.org/Swedish_Campground.html"
    extracted_invariant: "Command key symbol (U+2318) adapted from a Nordic point-of-interest sign (Bowen knot / St. Hannes cross) on a 16x16 1-bit bitmap to remove repetitive Apple logos from menus."
  - id: "src-02"
    title: "Interview with Susan Kare (Making the Macintosh: Technology and Culture in Silicon Valley)"
    author_or_org: "Susan Kare (interviewed by Alex Pang, Stanford University)"
    year: 2000
    source_type: "primary_talk"
    url_or_identifier: "https://web.stanford.edu/dept/SUL/sites/mac/primary/interviews/kare/trans.html"
    extracted_invariant: "1-bit monochrome pixel-grid methodology (16x16 and 32x32) via Icon Editor and MacPaint; silhouette-based class differentiation (folded-corner document vs active hand-with-pencil application) and sparse pixel refinement."
  - id: "src-03"
    title: "World Class Cities (The Original Macintosh)"
    author_or_org: "Susan Kare (Folklore.org)"
    year: 1983
    source_type: "engineering_post"
    url_or_identifier: "https://www.folklore.org/World_Class_Cities.html"
    extracted_invariant: "Proportional 1-bit UI font Chicago (Elefont) engineered without jagged diagonals for 1-bit displays (shipped 1984-1997 in Mac OS and 4 iPod generations), alongside Geneva and Monaco."
  - id: "src-04"
    title: "Icons: Susan Kare — Exhibition Press Dossier (quoting Nov 16, 2001 Stanford interview by Wendy Marinaccio)"
    author_or_org: "Susan Kare / Musée de l'Imprimerie et de la Communication Graphique de Lyon"
    year: 2022
    source_type: "primary_talk"
    url_or_identifier: "https://www.imprimerie.lyon.fr/sites/micg/files/2022-05/cp_susan_kare_web_en.pdf"
    extracted_invariant: "Good icons function like road signs rather than graphic illustrations—concise, memorable, and resolved through context and metaphor within 32x32 1-bit or 16-color VGA constraints rather than decorative tooling."
  - id: "src-05"
    title: "Icon Usability"
    author_or_org: "Aurora Harley, Nielsen Norman Group"
    year: 2014
    source_type: "empirical_benchmark"
    url_or_identifier: "https://www.nngroup.com/articles/icon-usability/"
    extracted_invariant: "Universal icons are rare (Home, Print, Search); unlabeled non-standard icons produce total discoverability failure (0 clicks on clock-for-history), hover-only labels fail on touchscreens, and persistent visible text labels are required."
  - id: "src-06"
    title: "The Proliferation and Problem of the Sparkles Icon"
    author_or_org: "Kate Kaplan, Nielsen Norman Group"
    year: 2024
    source_type: "empirical_benchmark"
    url_or_identifier: "https://www.nngroup.com/articles/ai-sparkles-icon-problem/"
    extracted_invariant: "In an n=107 quantitative icon study, 0% of participants attributed isolated sparkles to AI (16.82% save/favorite, 16.82% visual effects, 11.22% special/new), while 73% associated star icons with saving/favoriting."
  - id: "src-07"
    title: "Web Content Accessibility Guidelines (WCAG) 2.2 and WAI-ARIA Authoring Practices Guide"
    author_or_org: "World Wide Web Consortium (W3C)"
    year: 2023
    source_type: "official_standard"
    url_or_identifier: "https://www.w3.org/TR/WCAG22/"
    extracted_invariant: "Requires >= 3.0:1 non-text contrast (SC 1.4.11), no color-only state encoding (SC 1.4.1), >= 24x24 CSS px minimum / 44x44 CSS px enhanced target size (SC 2.5.8 / 2.5.5), explicit aria-label on icon-only controls, and aria-hidden='true' on decorative paired SVGs."
  - id: "src-08"
    title: "Lucide Icon Design Principles and SVG Code Conventions"
    author_or_org: "Lucide Contributors"
    year: 2024
    source_type: "shipped_oss_repo"
    url_or_identifier: "https://lucide.dev/contribute/icons/design-principles"
    extracted_invariant: "Mandates a uniform 24x24 integer canvas, >=1px safe zone, uniform 2px stroke-width, >=2px internal/element gap, fill='none', stroke='currentColor', and zero SVG filters, transforms, or child fills."
  - id: "src-09"
    title: "The Floppy Disk Icon as 'Save': Still Appropriate Today?"
    author_or_org: "Kate Kaplan, Nielsen Norman Group"
    year: 2025
    source_type: "empirical_benchmark"
    url_or_identifier: "https://www.nngroup.com/articles/floppy-disk-icon-understandability/"
    extracted_invariant: "83% associate floppy disk with Save, 73% circular arrows with Sync/Refresh, and 78% arrow-into-container with Download/Save; legacy hardware symbols should not represent cloud auto-sync or export workflows."
  - id: "src-10"
    title: "Flat Design vs Traditional Design: Comparative Experimental Study"
    author_or_org: "Ivan Burmistrov, Tatiana Zlokazova, Anna Izmalkova, and Anna Leonova (INTERACT 2015)"
    year: 2015
    source_type: "peer_reviewed_paper"
    url_or_identifier: "doi:10.1007/978-3-319-22668-2_10"
    extracted_invariant: "Ultra-flat icons nearly doubled visual search time compared with traditional icons (15.4s SD 4.6 vs 8.0s SD 2.2, p=0.000), lowered saccadic peak velocity (137 vs 174 deg/s), and flat webpages produced 28% false-alarm click errors."
  - id: "src-11"
    title: "Icon Identification in Context: The Changing Role of Icon Characteristics With User Experience"
    author_or_org: "Sarah J. Isherwood, Siné J. P. McDougall, and Martin B. Curry (Human Factors)"
    year: 2007
    source_type: "peer_reviewed_paper"
    url_or_identifier: "doi:10.1518/001872007X200102"
    extracted_invariant: "Icon characteristics explain up to 69% of identification performance variance; minimizing semantic distance dominates initial comprehension while familiarity governs long-term retrieval."
  - id: "src-12"
    title: "Susan Kare: Design Icon"
    author_or_org: "Eric S. Hintz (IEEE Annals of the History of Computing, Vol. 40, No. 2, pp. 48-61)"
    year: 2018
    source_type: "peer_reviewed_paper"
    url_or_identifier: "doi:10.1109/MAHC.2018.022921443"
    extracted_invariant: "Documents Kare's bitmapped icon systems and proportional screen fonts across Apple Macintosh (1984), NeXT, Microsoft Windows 3.0 (1990), and IBM OS/2."
  - id: "src-13"
    title: "The Humane Interface: New Directions for Designing Interactive Systems"
    author_or_org: "Jef Raskin (Addison-Wesley)"
    year: 2000
    source_type: "book"
    url_or_identifier: "ISBN 0-201-37937-6"
    extracted_invariant: "Quantifies KLM-GOMS pointer homing (H=0.4s) and pointing (P=1.1s) penalties vs keystroke habituation (K=0.28s) and documents cryptic failure modes of unlabeled icons (Sec. 6-3)."
  - id: "src-14"
    title: "The Visual Display of Quantitative Information (2nd Edition)"
    author_or_org: "Edward R. Tufte (Graphics Press)"
    year: 2001
    source_type: "book"
    url_or_identifier: "ISBN 0-9613921-4-2"
    extracted_invariant: "Establishes data-ink ratio maximization (pp. 93, 136) and chartjunk elimination (pp. 107-121), defining the quantitative counterweight against pictographic icons in dense telemetry."
  - id: "src-15"
    title: "How we redesigned the Linear UI (part II)"
    author_or_org: "Karri Saarinen et al. (Linear)"
    year: 2024
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/now/how-we-redesigned-the-linear-ui"
    extracted_invariant: "Documents chrome reduction, LCH contrast generation, keyboard-first command menus, and dense navigation hierarchy as the counterweight paradigm for intensive B2B SaaS workspaces."
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

Susan Kare's operational paradigm treats every user-interface icon as a **high-contrast traffic sign** engineered on an explicit integer grid rather than a miniature graphic illustration (`src-04`). Originating in the 1-bit monochrome constraints of the 1984 Apple Macintosh (32x32 desktop icons, 16x16 cursors and Command symbol, 12pt proportional *Chicago* bitmap font) and validated across 16-color VGA Microsoft Windows 3.0 (*Solitaire*, Control Panel) (`src-01`, `src-02`, `src-03`, `src-12`), this discipline reduces visual communication to four falsifiable invariants:

1. **The 32x32 1-Bit Silhouette Invariant:** An icon must communicate its structural identity strictly through binary figure-ground silhouette on an integer grid. If comprehension depends on gradients, drop shadows, partial opacity, or subpixel hairline strokes (`< 1.0 px`), the glyph collapses under glare, low-DPI scaling, or rapid visual scanning (`src-02`, `src-08`, `src-10`).
2. **Road-Sign Economy and Binary Labeling:** Because semantic distance governs up to 69% of first-exposure identification performance (`src-11`) and universal symbols are exceptionally rare (`src-05`), standalone icon-only controls are restricted to a closed 6-symbol universal set (`Close`, `Search`, `Back`, `Home`, `Trash`, `Menu`). Every domain-specific verb, workflow state, or generative-AI command—especially ambiguous sparkle glyphs showing 0% spontaneous AI attribution in isolated empirical testing (`n=107`, `src-06`)—requires a persistent visible text label.
3. **Sibling Silhouette Separation and Non-Color Redundancy:** Adjacent controls in a toolbar or status queue must present distinct outer contours with `>= 2` grid units of internal separation (`src-08`), achieve `>= 3.0:1` non-text luminance contrast (`src-07`), and never encode semantic state exclusively via color (`src-07`).
4. **Hardware-Decoupled Longevity and Accessible DOM Semantics:** Metaphors must align with actual system behavior rather than obsolete local-hardware mechanics (`src-09`), and every rendered SVG must honor strict WAI-ARIA semantics (`aria-hidden="true"` when paired with text; action-verb `aria-label` when icon-only) inside WCAG/HIG touch-target envelopes (`>= 44x44 CSS px` on mobile, `>= 24x24 CSS px` on desktop) (`src-07`).

## 2. Regime Boundaries & Out-of-Universe Rationale

This design system operates strictly within two in-universe regimes and enforces mandatory `HANDOFF` outside them:

| Regime | Classification | Structural Fit / Failure Mechanism | Target Counterweight |
| :--- | :--- | :--- | :--- |
| `mobile_consumer_capture` | **Primary (In-Universe)** | Coarse touch input (no hover), outdoor glare, one-handed operation, and rapid single-glance verb selection demand 1-bit silhouette legibility, persistent labels on non-universal actions, and `>= 44x44 CSS px` hit targets. | N/A (Primary Owner) |
| `landing_onboarding_conversion` | **Secondary (In-Universe)** | Zero-prior-training cohorts require low semantic-distance visual landmarks paired with crisp labels to convey product capabilities without decorative SVG bloat or ambiguous AI sparkles. | N/A (Secondary Owner) |
| `ai_native_desktop_ide` | **Out-of-Universe (`HANDOFF`)** | Physical-keyboard power users executing 200+ commands/hour incur severe KLM-GOMS homing (`H=0.4s`) and pointing (`P=1.1s`) penalties from labeled icon toolbars compared to keystroke commands (`K=0.28s`). | `jef-raskin` |
| `saas_b2b_intensive` | **Out-of-Universe (`HANDOFF`)** | Workspaces with >25-50 complex domain mutations exhaust distinguishable 1-bit silhouettes; persistent icon chrome reduces density and loses to neutral chrome + searchable `Cmd+K` command menus. | `karri-saarinen` |
| `analytics_dense_telemetry` | **Out-of-Universe (`HANDOFF`)** | Quantitative telemetry requires maximizing Tufte's data-ink ratio via tabular numerals, range frames, small multiples, and sparklines; pictographic icons act as non-data chartjunk. | `edward-tufte` |

## 3. Signal Detection Protocol

Text-only and multimodal agents execute the following 10-second deterministic inspection pass over JSX/TSX, HTML, SVG, and CSS source before issuing scores:

1. **Labeling Taxonomy Scan (`sig-01` — critical):** Enumerate every `<button>`, `<a>`, and `[role="button"]` containing an `<svg>` or icon component. Classify the icon name/semantic intent against the closed 6-item allowlist `{close, search, back, home, trash, menu}`. Flag any non-allowlisted control lacking a persistent visible text child (reject `sr-only`, `title`-only, and `:hover`-gated tooltips).
2. **Metaphor Collision & AI Sparkle Scan (`sig-02` — critical):** Extract all icon component names and SVG `<path d="...">` signatures within the view. Flag any duplicate icon stem bound to two distinct handlers (`onClick`/`href`) and any occurrence of sparkle/star/wand iconography bound to AI actions without explicit disambiguating text and distinct silhouettes.
3. **SVG Grid & Stroke Audit (`sig-03` — high):** Parse every sibling `<svg>` on the surface for `viewBox`, `width`, `height`, and `stroke-width` / `strokeWidth`. Flag mixed `viewBox` dimensions, non-integer `viewBox` bounds, any stroke `< 1.0 px`, or `stroke-width` variance `> 0.25 px` across siblings.
4. **Luminance Contrast & Color-Only State Matrix (`sig-04` — critical):** Compute WCAG 2.2 relative luminance contrast `((L1 + 0.05) / (L2 + 0.05))` between each icon's stroke/fill token and its rendered container background. Flag any ratio `< 3.0:1`. Inspect status/category components (e.g., `status === 'synced' | 'pending' | 'failed'`) and flag any state map that swaps only CSS color/background tokens while keeping identical geometry and omitting visible text.
5. **ARIA Contract & Hit-Box Envelope Check (`sig-05` — high):** Verify that every icon-only interactive control declares a non-empty action-verb `aria-label` (or `aria-labelledby`), every standalone meaningful SVG declares `role="img"` plus `aria-label`, every SVG inside a text-labeled control declares `aria-hidden="true"` and `focusable="false"`, and CSS classes/styles enforce `min-width >= 44px; min-height >= 44px` on mobile (`>= 24x24px` desktop).
6. **1-Bit Primitive Budget & Hardware Metaphor Audit (`sig-06` — medium):** Count geometric primitives (`path`, `line`, `rect`, `circle`, `ellipse`, `polyline`, `polygon`) per `<= 32px` action SVG. Flag counts `> 6`, any `<filter>`, `<linearGradient>`, or `<radialGradient>` node, and any floppy-disk glyph attached to `sync`, `auto-save`, `cloud`, or `export` handlers.

## 4. Hard Filters & Veto Playbook

### Mandatory Gate Filters (`-15` each on failure)
- **`flt-01` (`mandatory_visible_label_for_non_universal_actions`):** Rejects unlabeled domain/AI controls and hover-only label disclosure.
- **`flt-02` (`uniform_integer_svg_grid_and_minimum_stroke`):** Rejects mixed SVG grids, non-integer viewBoxes, and `< 1.0 px` hairlines.
- **`flt-03` (`non_text_contrast_and_non_color_state_encoding`):** Rejects `< 3.0:1` icon contrast and color-only status dots.
- **`flt-04` (`accessible_name_and_touch_target_envelope`):** Rejects missing ARIA attributes and sub-44px mobile touch boxes (sub-24px desktop).

### Deterministic Veto Triggers
- **`veto-01` (`hard_veto`, `-35`, cap `49`, `BLOCK`):** Triggered by unlabeled AI sparkle/domain icons or `>= 2` distinct handlers reusing the same icon stem in one view. **Remediation:** Assign unique functional verb/noun silhouettes and render persistent 1-2 word visible text labels.
- **`veto-02` (`hard_veto`, `-35`, cap `49`, `BLOCK`):** Triggered by mixed peer `viewBox` dimensions, `< 1.0 px` hairline strokes, or `> 0.25 px` stroke variance in one action bar. **Remediation:** Standardize on one integer square `viewBox` (e.g., `0 0 24 24`) and uniform `strokeWidth` in `[1.5, 2.0]` px with `>= 1px` safe padding.
- **`veto-03` (`hard_veto`, `-35`, cap `49`, `BLOCK`):** Triggered by functional icons with `< 3.0:1` luminance contrast or color-only status/category indicators. **Remediation:** Raise foreground contrast to `>= 3.0:1` (target `>= 4.5:1`) and pair distinct 1-bit geometric shapes with explicit text labels.
- **`veto-04` (`hard_veto`, `-35`, cap `49`, `BLOCK`):** Triggered by mobile icon buttons `< 44x44 CSS px` (desktop `< 24x24 CSS px`), icon-only buttons lacking `aria-label`, or paired SVGs lacking `aria-hidden="true"`. **Remediation:** Expand button hit boxes via padding to `>= 44x44 CSS px` (`>= 8px` gap) and complete the ARIA contract.
- **`veto-05` (`conditional_block`, `-15`, forces `REVISE`):** Triggered by `> 6` SVG primitives, `<filter>`/`<linearGradient>`/`<radialGradient>` dependencies in `<= 32px` UI icons, or legacy hardware metaphors (e.g., floppy disk) bound to cloud auto-sync or export behaviors. **Remediation:** Simplify to `<= 6` 1-bit primitives with `currentColor` and swap to behavior-accurate symbols (`Sync` circular arrows, `Download` arrow-into-tray) with visible text.

## 5. Executable Heuristics & Code Patterns

### Refactor 1: Mobile Consumer Capture Action Toolbar (`mobile_consumer_capture`)

#### BEFORE (Triggers `veto-01`, `veto-02`, `veto-03`, `veto-04`, `veto-05`; Score = `0`, Posture = `BLOCK`)
Violations: 5 icon-only buttons including 3 ambiguous AI sparkle variants (`Summarize`, `Auto-Tag`, `Enhance`), mixed `viewBox` (`16`, `20`, `24`, `32`), hairline `0.75px` and mismatched `2.5px` strokes, `<linearGradient>` dependency, failing WCAG luminance contrast (`#A3A3A3` = `2.52:1` and `#C4B5FD` = `1.85:1` on `#FFFFFF`), hover-only `title` strings, zero `aria-label`, and `20x20px` touch targets.

```tsx
// BEFORE — Fails flt-01, flt-02, flt-03, flt-04; triggers veto-01..veto-05
export function CaptureToolbarBefore({
  onSummarize,
  onAutoTag,
  onEnhance,
  onCrop,
  onDelete,
}: {
  onSummarize: () => void;
  onAutoTag: () => void;
  onEnhance: () => void;
  onCrop: () => void;
  onDelete: () => void;
}) {
  return (
    <div className="flex items-center gap-1 bg-white p-1">
      {/* 1. AI Sparkle variant A: mixed 16x16 viewBox, hairline 0.75px, 1.85:1 contrast, 20x20px box, no label/ARIA */}
      <button onClick={onSummarize} title="AI Summarize" className="h-5 w-5 text-[#C4B5FD]">
        <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="0.75">
          <defs>
            <linearGradient id="sparkGrad"><stop offset="0%" stopColor="#C4B5FD" /><stop offset="100%" stopColor="#DDD6FE" /></linearGradient>
          </defs>
          <path stroke="url(#sparkGrad)" d="M8 1l1.5 4.5L14 7l-4.5 1.5L8 13l-1.5-4.5L2 7l4.5-1.5L8 1z" />
        </svg>
      </button>

      {/* 2. AI Sparkle variant B: duplicate metaphor collision on 24x24 viewBox, 2.5px stroke */}
      <button onClick={onAutoTag} title="AI Auto-Tag" className="h-5 w-5 text-[#C4B5FD]">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
          <path d="M12 2l2 6 6 2-6 2-2 6-2-6-6-2 6-2 2-6z" />
          <path d="M19 15l1 3 3 1-3 1-1 3-1-3-3-1 3-1 1-3z" />
        </svg>
      </button>

      {/* 3. AI Sparkle variant C: third duplicate sparkle on 32x32 viewBox, 0.75px hairline */}
      <button onClick={onEnhance} title="AI Enhance" className="h-5 w-5 text-[#A3A3A3]">
        <svg viewBox="0 0 32 32" fill="none" stroke="currentColor" strokeWidth="0.75">
          <path d="M16 4l3 9 9 3-9 3-3 9-3-9-9-3 9-3 3-9z" />
        </svg>
      </button>

      {/* 4. Unlabeled domain action: 2.52:1 contrast (#A3A3A3 on #FFFFFF), 20x20px target */}
      <button onClick={onCrop} title="Crop" className="h-5 w-5 text-[#A3A3A3]">
        <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="0.75">
          <path d="M5 2v13h13M2 5h13v13" />
        </svg>
      </button>

      {/* 5. Unlabeled Trash missing aria-label, 2.52:1 contrast, 20x20px target */}
      <button onClick={onDelete} className="h-5 w-5 text-[#A3A3A3]">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
          <path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14" />
        </svg>
      </button>
    </div>
  );
}
```

#### AFTER (0 Vetos, 0 Failed Filters, 0 Failed Signals; Score = `100`, Posture = `APPROVE`)
Fixes: Uniform integer `viewBox="0 0 24 24"`, uniform `strokeWidth={1.75}`, `<= 4` primitives per SVG, zero gradients/filters, distinct 1-bit functional silhouettes (document-summary, tag, equalizer sliders, crop frame, trash bin), persistent concise visible text labels on all non-universal/AI actions, explicit `aria-label="Delete capture"` on universal icon-only Trash, `aria-hidden="true" focusable="false"` on every SVG, verified contrast (`#0F172A` `17.85:1`, `#1D4ED8` on `#EFF6FF` `6.16:1`, `#B91C1C` `6.47:1` on `#FFFFFF`), and `44x44px` minimum touch targets with `8px` spacing.

```tsx
// AFTER — Kare-compliant 1-bit grid, distinct road-sign silhouettes, persistent labels, WCAG AA/AAA touch targets
import React from "react";

interface CaptureToolbarProps {
  activeAction?: "summarize" | "tag" | "enhance" | "crop";
  onSummarize: () => void;
  onAutoTag: () => void;
  onEnhance: () => void;
  onCrop: () => void;
  onDelete: () => void;
}

const ICON_PROPS: React.SVGProps<SVGSVGElement> = {
  width: 20,
  height: 20,
  viewBox: "0 0 24 24",
  fill: "none",
  stroke: "currentColor",
  strokeWidth: 1.75,
  strokeLinecap: "round",
  strokeLinejoin: "round",
  "aria-hidden": true,
  focusable: "false",
};

export function CaptureToolbarAfter({
  activeAction,
  onSummarize,
  onAutoTag,
  onEnhance,
  onCrop,
  onDelete,
}: CaptureToolbarProps) {
  return (
    <div
      role="toolbar"
      aria-label="Capture note actions"
      className="capture-toolbar"
    >
      <button
        type="button"
        onClick={onSummarize}
        aria-pressed={activeAction === "summarize"}
        className={`capture-btn ${activeAction === "summarize" ? "capture-btn--active" : ""}`}
      >
        {/* Distinct silhouette: lined document summary (4 primitives, 24x24 grid) */}
        <svg {...ICON_PROPS}>
          <rect x="4" y="3" width="16" height="18" rx="2" />
          <line x1="8" y1="8" x2="16" y2="8" />
          <line x1="8" y1="12" x2="16" y2="12" />
          <line x1="8" y1="16" x2="12" y2="16" />
        </svg>
        <span>Summarize</span>
      </button>

      <button
        type="button"
        onClick={onAutoTag}
        aria-pressed={activeAction === "tag"}
        className={`capture-btn ${activeAction === "tag" ? "capture-btn--active" : ""}`}
      >
        {/* Distinct silhouette: angled tag + hole (2 primitives, 24x24 grid) */}
        <svg {...ICON_PROPS}>
          <path d="M12 2H4a2 2 0 0 0-2 2v8l9.5 9.5a2 2 0 0 0 2.8 0l7.2-7.2a2 2 0 0 0 0-2.8L12 2z" />
          <circle cx="7.5" cy="7.5" r="1.5" />
        </svg>
        <span>Tag</span>
      </button>

      <button
        type="button"
        onClick={onEnhance}
        aria-pressed={activeAction === "enhance"}
        className={`capture-btn ${activeAction === "enhance" ? "capture-btn--active" : ""}`}
      >
        {/* Distinct silhouette: 3 equalizer bars for Enhance (3 primitives, 24x24 grid) */}
        <svg {...ICON_PROPS}>
          <line x1="6" y1="20" x2="6" y2="10" />
          <line x1="12" y1="20" x2="12" y2="4" />
          <line x1="18" y1="20" x2="18" y2="13" />
        </svg>
        <span>Enhance</span>
      </button>

      <button
        type="button"
        onClick={onCrop}
        aria-pressed={activeAction === "crop"}
        className={`capture-btn ${activeAction === "crop" ? "capture-btn--active" : ""}`}
      >
        {/* Distinct silhouette: intersecting crop L-brackets (2 primitives, 24x24 grid) */}
        <svg {...ICON_PROPS}>
          <path d="M6 2v14a2 2 0 0 0 2 2h14" />
          <path d="M18 22V8a2 2 0 0 0-2-2H2" />
        </svg>
        <span>Crop</span>
      </button>

      {/* Allowlisted universal Trash icon: explicit action-verb aria-label, 44x44px hit box, 6.47:1 contrast */}
      <button
        type="button"
        onClick={onDelete}
        aria-label="Delete capture"
        className="capture-btn capture-btn--danger"
      >
        <svg {...ICON_PROPS}>
          <path d="M3 6h18" />
          <path d="M8 6V4h8v2" />
          <path d="M6 6l1 14a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2l1-14" />
        </svg>
      </button>
    </div>
  );
}
```

```css
.capture-toolbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  padding: 8px;
  background-color: #ffffff;
  border-top: 1px solid #475569; /* 7.58:1 vs #FFFFFF */
}

.capture-btn {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  min-width: 44px;
  min-height: 44px;
  padding: 6px 10px;
  border: 1px solid #475569; /* 7.58:1 vs #FFFFFF */
  border-radius: 8px;
  background-color: #ffffff;
  color: #0f172a; /* 17.85:1 vs #FFFFFF */
  font-size: 12px;
  font-weight: 600;
  line-height: 1;
}

.capture-btn--active {
  background-color: #eff6ff;
  border-color: #1d4ed8;
  color: #1d4ed8; /* 6.16:1 vs #EFF6FF */
}

.capture-btn--danger {
  color: #b91c1c; /* 6.47:1 vs #FFFFFF */
  border-color: #b91c1c;
}
```

---

### Refactor 2: Mobile Capture Queue Status & Category Indicators (`mobile_consumer_capture`)

#### BEFORE (Triggers `veto-03`, `flt-03`, `sig-04`, `sig-05`; Score = `35`, Posture = `BLOCK`)
Violations: Encodes 4 sync states exclusively with 10px pastel circles (`#86EFAC` `1.40:1`, `#FDE047` `1.32:1`, `#FCA5A5` `1.90:1`, `#CBD5E1` `1.48:1` on `#FFFFFF`) and hover-only `title` strings, paired with a cryptic unlabeled abstract category glyph (`#A3A3A3`, `2.52:1` on `#FFFFFF`) lacking both visible text and accessible name—failing WCAG 2.1/2.2 SC 1.1.1, SC 1.4.1 (Use of Color), and SC 1.4.11 (Non-text Contrast `>= 3.0:1`).

```tsx
// BEFORE — Color-only pastel status dots (<2.0:1) + cryptic unlabeled category glyph (2.52:1)
type CaptureStatus = "synced" | "pending" | "failed" | "draft";
type CaptureCategory = "receipt" | "voice" | "photo";

const DOT_COLORS: Record<CaptureStatus, string> = {
  synced: "#86EFAC",  // 1.40:1 vs #FFFFFF — FAIL
  pending: "#FDE047", // 1.32:1 vs #FFFFFF — FAIL
  failed: "#FCA5A5",  // 1.90:1 vs #FFFFFF — FAIL
  draft: "#CBD5E1",   // 1.48:1 vs #FFFFFF — FAIL
};

export function CaptureMetaBefore({
  status,
  category,
}: {
  status: CaptureStatus;
  category: CaptureCategory;
}) {
  return (
    <div style={{ display: "inline-flex", alignItems: "center", gap: 6 }}>
      <span
        title={status}
        style={{
          display: "inline-block",
          width: 10,
          height: 10,
          borderRadius: "50%",
          backgroundColor: DOT_COLORS[status],
        }}
      />
      {/* Cryptic unlabeled category symbol: 2.52:1 contrast (#A3A3A3 on #FFFFFF), no visible text, no ARIA */}
      <svg
        width="16"
        height="16"
        viewBox="0 0 20 20"
        fill="none"
        stroke="#A3A3A3"
        strokeWidth="1.5"
      >
        {category === "receipt" && <path d="M10 2l2 6 6 2-6 2-2 6-2-6-6-2 6-2z" />}
        {category === "voice" && <path d="M11 2L4 11h6l-1 7 7-9h-6l1-7z" />}
        {category === "photo" && <polygon points="10,2 18,10 10,18 2,10" />}
      </svg>
    </div>
  );
}
```

#### AFTER (0 Vetos, 0 Failed Filters, 0 Failed Signals; Score = `100`, Posture = `APPROVE`)
Fixes: Distinct 1-bit geometric silhouettes on a uniform `viewBox="0 0 20 20"` integer grid (`strokeWidth={1.75}`, `<= 3` primitives each) for both sync status (`Synced` check-circle, `Syncing` circular arrows, `Upload failed` warning-triangle, `Offline draft` dashed-square) and capture category (`Receipt` notched slip, `Voice note` microphone, `Photo` framed lens), paired with explicit visible text, `aria-hidden="true"` on decorative SVGs, and verified WCAG AA contrast (`6.37:1` to `9.45:1` foreground on badge surface; `5.02:1` to `7.58:1` borders on `#FFFFFF`).

```tsx
// AFTER — High-contrast 1-bit geometric shapes + explicit text for status and category (WCAG 2.2 SC 1.4.1, 1.4.3, 1.4.11)
import React from "react";

type CaptureStatus = "synced" | "pending" | "failed" | "draft";
type CaptureCategory = "receipt" | "voice" | "photo";

interface BadgeSpec {
  label: string;
  className: string;
  renderGlyph: () => React.ReactNode;
}

const BADGE_ICON_PROPS: React.SVGProps<SVGSVGElement> = {
  width: 16,
  height: 16,
  viewBox: "0 0 20 20",
  fill: "none",
  stroke: "currentColor",
  strokeWidth: 1.75,
  strokeLinecap: "round",
  strokeLinejoin: "round",
  "aria-hidden": true,
  focusable: "false",
};

const STATUS_SPECS: Record<CaptureStatus, BadgeSpec> = {
  synced: {
    label: "Synced",
    className: "meta-pill meta-pill--synced",
    renderGlyph: () => (
      <svg {...BADGE_ICON_PROPS}>
        <circle cx="10" cy="10" r="8" />
        <polyline points="6.5 10.5 9 13 13.5 7.5" />
      </svg>
    ),
  },
  pending: {
    label: "Syncing",
    className: "meta-pill meta-pill--pending",
    renderGlyph: () => (
      <svg {...BADGE_ICON_PROPS}>
        <path d="M16 10a6 6 0 0 0-10.5-4" />
        <polyline points="5 3 5.5 6.5 9 6" />
        <path d="M4 10a6 6 0 0 0 10.5 4" />
      </svg>
    ),
  },
  failed: {
    label: "Upload failed",
    className: "meta-pill meta-pill--failed",
    renderGlyph: () => (
      <svg {...BADGE_ICON_PROPS}>
        <polygon points="10 2 18.5 17 1.5 17" />
        <line x1="10" y1="7.5" x2="10" y2="11.5" />
        <line x1="10" y1="14.5" x2="10.01" y2="14.5" />
      </svg>
    ),
  },
  draft: {
    label: "Offline draft",
    className: "meta-pill meta-pill--draft",
    renderGlyph: () => (
      <svg {...BADGE_ICON_PROPS}>
        <rect x="3" y="3" width="14" height="14" rx="2" strokeDasharray="3 2.5" />
        <line x1="7" y1="10" x2="13" y2="10" />
      </svg>
    ),
  },
};

const CATEGORY_SPECS: Record<CaptureCategory, BadgeSpec> = {
  receipt: {
    label: "Receipt",
    className: "meta-pill meta-pill--neutral",
    renderGlyph: () => (
      <svg {...BADGE_ICON_PROPS}>
        <path d="M4 2h12v16l-2-1.5L12 18l-2-1.5L8 18l-2-1.5L4 18V2z" />
        <line x1="7" y1="7" x2="13" y2="7" />
        <line x1="7" y1="11" x2="11" y2="11" />
      </svg>
    ),
  },
  voice: {
    label: "Voice note",
    className: "meta-pill meta-pill--neutral",
    renderGlyph: () => (
      <svg {...BADGE_ICON_PROPS}>
        <rect x="7" y="2" width="6" height="9" rx="3" />
        <path d="M4.5 9.5a5.5 5.5 0 0 0 11 0" />
        <line x1="10" y1="15" x2="10" y2="18" />
      </svg>
    ),
  },
  photo: {
    label: "Photo",
    className: "meta-pill meta-pill--neutral",
    renderGlyph: () => (
      <svg {...BADGE_ICON_PROPS}>
        <rect x="2.5" y="4.5" width="15" height="11" rx="2" />
        <circle cx="10" cy="10" r="2.75" />
      </svg>
    ),
  },
};

export function CaptureMetaAfter({
  status,
  category,
}: {
  status: CaptureStatus;
  category: CaptureCategory;
}) {
  const statusSpec = STATUS_SPECS[status];
  const categorySpec = CATEGORY_SPECS[category];
  return (
    <div className="meta-pill-group">
      <span role="status" className={statusSpec.className}>
        {statusSpec.renderGlyph()}
        <span>{statusSpec.label}</span>
      </span>
      <span className={categorySpec.className}>
        {categorySpec.renderGlyph()}
        <span>{categorySpec.label}</span>
      </span>
    </div>
  );
}
```

```css
.meta-pill-group {
  display: inline-flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}

.meta-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 9999px;
  border: 1.5px solid;
  font-size: 12px;
  font-weight: 600;
  line-height: 1.2;
}

.meta-pill--synced {
  color: #166534;            /* 6.49:1 on #DCFCE7 */
  background-color: #dcfce7;
  border-color: #15803d;     /* 5.02:1 on #FFFFFF */
}

.meta-pill--pending {
  color: #92400e;            /* 6.37:1 on #FEF3C7 */
  background-color: #fef3c7;
  border-color: #b45309;     /* 5.02:1 on #FFFFFF */
}

.meta-pill--failed {
  color: #991b1b;            /* 6.80:1 on #FEE2E2 */
  background-color: #fee2e2;
  border-color: #b91c1c;     /* 6.47:1 on #FFFFFF */
}

.meta-pill--draft,
.meta-pill--neutral {
  color: #334155;            /* 9.45:1 on #F1F5F9 */
  background-color: #f1f5f9;
  border-color: #475569;     /* 7.58:1 on #FFFFFF */
}
```

## 6. Blind Spots & Counterweights

1. **Desktop Keyboard Efficiency Blind Spot (`jef-raskin`, `src-13`):** Persistent labeled icon toolbars optimize first-exposure recognition on touch screens, but in desktop IDEs and text-manipulation tools they force repeated keyboard-to-pointer homing (`H=0.4s`) plus target acquisition (`P=1.1s`). When command repetition exceeds 30 invocations per hour on a hardware keyboard, defer to `jef-raskin` for modeless text commands and habituated keystrokes (`K=0.28s`).
2. **High-Cardinality B2B Workspace Blind Spot (`karri-saarinen`, `src-15`):** Beyond roughly 20 domain verbs, adding more icons degrades discriminability and inflates chrome. In `saas_b2b_intensive` tools with 50+ CRUD mutations, defer to `karri-saarinen` for inverted-L neutral chrome reduction, single-key navigation, and searchable `Cmd+K` command menus.
3. **Quantitative Telemetry Blind Spot (`edward-tufte`, `src-14`):** Categorical pictograms cannot convey continuous numerical magnitudes, error bounds, or dense time series. In `analytics_dense_telemetry`, defer to `edward-tufte` to maximize the data-ink ratio through tabular numerals, small multiples, and word-sized sparklines.

## 7. Adversarial Debate Positions

- **vs. `karri-saarinen` (`explicit_iconic_discoverability_vs_keyboard_first_chrome_reduction`):** Kare defends persistent labeled icons on consumer mobile capture and onboarding surfaces where touch users have no `Cmd+K` reflex; Saarinen defends neutral chrome and keyboard-first menus on dense B2B desktop tools. Arbitration resolves strictly by touch-input share (`> 50%`), session cadence (`< 3/week`), and command vocabulary (`<= 25` vs `> 25`).
- **vs. `jef-raskin` (`iconic_visual_anchoring_vs_universal_text_and_keyboard_habituation`):** Kare defends 1-bit road-sign landmarks paired with 1-2 word labels on constrained `<= 480px` mobile viewports where homing latency does not apply; Raskin defends pure text commands and modeless keyboard habituation when physical keyboard KLM-GOMS savings exceed `1.0s/action`.
- **vs. `edward-tufte` (`pictographic_status_semiotics_vs_maximum_data_ink_quantitative_precision`):** Kare defends geometric state silhouettes plus text badges when status cardinality is `<= 6` discrete workflow states; Tufte wins whenever views display continuous metrics, `>= 10` numeric columns, or statistical distributions.

## 8. Primary Source Notes

- **Macintosh 1984 Iconography & Command Key (`src-01`, `src-02`, `src-04`, `src-12`):** Primary engineering history in Andy Hertzfeld's *Swedish Campground* (1983) documents the 16x16 Bowen-knot Command symbol (`U+2318`); Alex Pang's Sept 8, 2000 Stanford oral history (`src-02`) and Wendy Marinaccio's Nov 16, 2001 Stanford interview cited in Lyon's Musée de l'Imprimerie exhibition dossier (`src-04`) document the 32x32 1-bit Icon Editor, road-sign maxim, Paint Bucket, Lasso, Trash, Document vs. Application silhouettes, and 16-color VGA Windows 3.0 work. Additional archival records include MoMA's *Apple Macintosh OS icon sketchbook* (1982, Obj. 112.2015), Kare's self-published monograph *Susan Kare Icons: Selected Work from 1983–2011* (Watermark Press/Kare Prints, San Francisco, 2011, 160 pp.; no ISBN registered in consulted archival records), and her 2014 EG8 talk (*Susan Kare, Iconographer*).
- **Bitmap Typography Longevity (`src-03`, `src-12`):** Kare's *World Class Cities* (1983) and Bigelow & Holmes's *Notes on Apple 4 Fonts* (*Electronic Publishing*, Vol. 4, No. 3, Sept 1991) document *Chicago*, *Geneva*, and *Monaco* engineering constraints and multi-decade deployment across Mac OS (1984–1997), four monochrome iPod generations, and macOS.
- **Empirical Icon Usability & AI Sparkle Studies (`src-05`, `src-06`, `src-09`, `src-10`, `src-11`):** Grounded in NN/g's *Icon Usability* (Harley, 2014), *The Proliferation and Problem of the Sparkles Icon* (Kaplan, 2024; `n=107`, 0% AI attribution, 73% star = favorite), *The Floppy Disk Icon as 'Save'* (Kaplan, 2025; 83% floppy, 78% download tray, 73% sync arrows; sample median age 41, exact *N* undisclosed), Burmistrov et al. (*INTERACT 2015*, `doi:10.1007/978-3-319-22668-2_10`; 15.4s vs 8.0s search time, 28% webpage clickability false alarms), and Isherwood, McDougall, & Curry (*Human Factors*, 2007, `doi:10.1518/001872007X200102`; 69% variance explained).
- **Accessibility & SVG Grid Standards (`src-07`, `src-08`):** Grounded in W3C WCAG 2.2 (SC 1.1.1, 1.4.1, 1.4.3, 1.4.11, 2.5.5, 2.5.8), W3C WAI-ARIA APG Button/Toolbar patterns, Apple HIG Buttons (44x44 pt hit region), ISO 9186-1:2014 (67% open comprehension threshold), and Lucide SVG Design Principles and Code Conventions.
