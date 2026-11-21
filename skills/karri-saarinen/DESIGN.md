---
schema_version: "1.0.0"
identity:
  slug: "karri-saarinen"
  display_name: "Karri Saarinen"
  barbell_pole: "convex_frontier"
  archetype_synthetic: false
  primary_domain: "Sub-100 ms local-first B2B software velocity, keyboard-first workflows, opinionated defaults, and tonal craft"
  core_axiom: "B2B tools must execute daily mutations locally in <=50ms with reversible sync, single-key shortcuts, opinionated defaults, and programmatic LCH tonal layers that strip administrative configuration and repetitive motion."
  active_era: "2013-present"
  skin_in_the_game_evidence:
    - artifact: "Linear (Product Development and Issue Tracking System, Co-founder and CEO)"
      year: 2019
      verifiable_metric: "Surpassed $100M ARR across 40,000+ paying companies with 177% NRR, $2.5B valuation (Aug 2026), positive cashflow, and AI agents installed in 95% of paid workspaces"
      source_id: "src-07"
    - artifact: "Linear Local-First Sync Engine and Delta Sync Read Path"
      year: 2022
      verifiable_metric: "Zero network round-trips on daily client mutations backed by >20 TB of sync actions (~1,000,000 sync actions/day in largest workspaces) with flat P95/P99 reconnect latency via Turbopuffer + Postgres late enrichment"
      source_id: "src-04"
    - artifact: "Linear UI Design Reset and Programmatic LCH Theme Generator"
      year: 2024
      verifiable_metric: "Collapsed theme specification from 98 manual HSL variables to 3 LCH base inputs (base color, accent color, contrast); full UI reset shipped in ~6 weeks by a 3-designer core team"
      source_id: "src-02"
    - artifact: "Airbnb Design Language System (DLS, Principal Designer and Co-creator)"
      year: 2016
      verifiable_metric: "Unified iOS and Android component architecture across 5 artboard categories enabling composition of ~50 interactive prototype screens in a few hours across nearly a dozen design functions"
      source_id: "src-08"
    - artifact: "Coinbase Merchant Tools, Multi-Signature Vault, and Mobile Apps (Founding Designer)"
      year: 2014
      verifiable_metric: "Merchant checkout tools adopted by 43,000 businesses (including Dell, Expedia, Wikipedia); iOS and Android apps rebuilt in <3 months achieving 4-star App Store and Google Play ratings"
      source_id: "src-09"
regime_fit:
  primary_regimes:
    - "saas_b2b_intensive"
  secondary_regimes:
    - "ai_native_desktop_ide"
  out_of_universe_regimes:
    - regime: "mobile_consumer_capture"
      reason: "Hardware keyboards are absent on smartphones where 49% of grips are one-handed and 75% of interactions are thumb-driven; single-key hotkeys and Cmd+K palettes yield 0% utility while dense tonal chrome degrades >=44px thumb-zone tap reliability."
    - regime: "analytics_dense_telemetry"
      reason: "Opinionated entity-execution workflows intentionally omit customizable OLAP slices, multivariate small-multiples, and high-density telemetry panels required for real-time observability diagnostics."
    - regime: "landing_onboarding_conversion"
      reason: "Anonymous first-visit marketing pages and signup funnels occur once per user rather than 100+ times daily; suppressing explicit narrative pacing, guided visual signifiers, and rare-tier motion harms comprehension and activation."
high_weight_signals:
  - id: "sig-01"
    name: "local_mutation_paint_latency"
    weight: "critical"
    category: "latency_perception"
    detects_before_others: "Detects server-roundtrip blocking on routine CRUD mutations (create, status, assignee, label, priority) within the first 10 seconds of workspace interaction."
    observable_indicator: "Performance.now() delta from keydown/click dispatch to DOM state reflection for primary entity mutations; static code audit inspects whether state updates await network fetch/GraphQL promises before mutating local store."
    threshold: "<= 50 ms local commit-to-paint (hard ceiling < 100 ms); 0 blocking network awaits prior to optimistic local write"
    direction: "lower_is_better"
    source_id: "src-16"
  - id: "sig-02"
    name: "daily_action_keyboard_coverage"
    weight: "critical"
    category: "interaction_physics"
    detects_before_others: "Detects mouse-locked CRUD and triage bottlenecks forcing repeated hand homing (H=0.40s) and pointer travel (P=1.10s) for top-10 daily entity actions."
    observable_indicator: "Fraction of top-10 daily workspace actions (create, assign, self-assign, label, status, priority, search, filter, select, undo) bound to single-key or chorded keydown handlers AND registered inside a global Cmd/Ctrl+K fuzzy command palette."
    threshold: "== 100% coverage for top-10 daily actions (>= 5 single-key bindings + 100% Cmd/Ctrl+K registration)"
    direction: "higher_is_better"
    source_id: "src-12"
  - id: "sig-03"
    name: "entity_creation_required_field_bloat"
    weight: "critical"
    category: "cognitive_load"
    detects_before_others: "Detects Jira-style administrative intake friction where creating a basic entity forces manual picks across un-defaulted mandatory dropdowns or multi-step wizards."
    observable_indicator: "Count of required form inputs lacking pre-populated contextual defaults (input[required], select[required], or schema validators blocking submit) inside the primary entity creation composer."
    threshold: "<= 1 manually typed mandatory field (title only; team and status pre-filled by defaults); == 1 composer view step"
    direction: "lower_is_better"
    source_id: "src-01"
  - id: "sig-04"
    name: "high_frequency_motion_tax"
    weight: "high"
    category: "interaction_physics"
    detects_before_others: "Detects decorative CSS/JS transition delays on command palettes, list row hovers, keyboard focus indicators, and quick pickers invoked >= 100 times/day (burning 2.08-2.95 hours/year in dead wait)."
    observable_indicator: "Computed CSS transition-duration and animation-duration (plus JS spring mount wrappers) on command palettes, hotkey-triggered pickers, list row hover highlights, and active focus cursors."
    threshold: "== 0 ms for keyboard-initiated and >= 100x/day elements; <= 180 ms (hard ceiling < 300 ms) for infrequent modals or drawers"
    direction: "lower_is_better"
    source_id: "src-11"
  - id: "sig-05"
    name: "inline_shortcut_signifier_parity"
    weight: "high"
    category: "visual_semiotics"
    detects_before_others: "Detects hidden-hotkey learnability cliffs where shortcuts exist in keydown listeners but never appear inline inside contextual menus, hover tooltips, or command palette rows."
    observable_indicator: "Percentage of bound actions rendered in [role='menuitem'], command palette rows, and primary tooltips that display an OS-aware <kbd> shortcut element matching the keybinding registry."
    threshold: ">= 90% inline <kbd> signifier parity across bound contextual menu and palette actions"
    direction: "higher_is_better"
    source_id: "src-05"
  - id: "sig-06"
    name: "programmatic_lch_tonal_layering"
    weight: "high"
    category: "visual_semiotics"
    detects_before_others: "Detects ad-hoc hex/HSL token sprawl, thick >= 2px borders, and dark-mode drop shadows that degrade visual surface hierarchy and inflate theme maintenance past 50+ manual variables."
    observable_indicator: "Static CSS/token audit checking perceptually uniform LCH/OKLCH surface definitions generated from <= 5 base inputs, structural container border-width <= 1px, and 0 hardcoded hex/rgb literals in component style files."
    threshold: "true (LCH/OKLCH programmatic tokens from <= 5 inputs, 0 hardcoded component color literals, structural border-width <= 1px)"
    direction: "boolean_required"
    source_id: "src-06"
  - id: "sig-07"
    name: "deterministic_agent_workbench_framing"
    weight: "medium"
    category: "agentic_trust"
    detects_before_others: "Detects unbounded chat-box overlays bolted onto B2B workspaces where AI outputs lack typed entity bindings, structured diffs, and deterministic human approval/revert controls."
    observable_indicator: "DOM and state-machine check confirming AI agent actions reference typed domain entity IDs and expose explicit preview, approve, reject, and rollback transitions instead of unparsed chat transcripts."
    threshold: "true (100% of agent mutations bound to typed domain entities with deterministic review and revert controls)"
    direction: "boolean_required"
    source_id: "src-10"
hard_filters:
  - id: "flt-01"
    name: "reversible_optimistic_sync_contract"
    gate_type: "required"
    condition: "Every optimistic client mutation captures prior field values, persists a durable transaction entry (IndexedDB/SQLite) tagged with an idempotency key or monotonic sync reference, and executes deterministic state rollback plus visible error notification upon server rejection."
    failure_impact: "Under packet loss, offline work, or 4xx/5xx authorization rejections, optimistic UIs silently diverge from authoritative backend state, lose queued edits on browser reload, or corrupt multi-tab sessions."
  - id: "flt-02"
    name: "zero_blocking_loaders_on_cached_navigation"
    gate_type: "required"
    condition: "Switching between locally synced workspace views (issue list, board, detail pane, inbox, search) renders cached state in <= 100 ms with 0 full-page spinners or blocking skeleton overlays."
    failure_impact: "Under elevated RTT (> 250 ms) or large datasets, recurrent spinner flashes break Nielsen's 100 ms direct-manipulation boundary across hundreds of daily view switches."
  - id: "flt-03"
    name: "input_focus_hotkey_isolation"
    gate_type: "required"
    condition: "Single-key global shortcuts (C, A, I, L, S, P, X, J, K, /) MUST return early without firing whenever document.activeElement matches input, textarea, select, [contenteditable='true'], or when KeyboardEvent.isComposing === true."
    failure_impact: "Typing issue titles, comments, date values, or IME CJK text accidentally triggers navigation or state mutations mid-keystroke, causing severe input corruption."
  - id: "flt-04"
    name: "zero_runtime_css_injection_thrashing"
    gate_type: "required"
    condition: "Navigating across dense views (>= 100 rows) injects 0 dynamic component <style> rules into document.head (build-time atomic CSS or static tokenized stylesheets only, excluding root/subtree theme variable scopes)."
    failure_impact: "Runtime CSS-in-JS rule injection adds 20-35% main-thread CPU overhead on view-heavy pages and induces dropped frames on mid-tier hardware during rapid keyboard scrolling."
  - id: "flt-05"
    name: "unbounded_admin_schema_proliferation"
    gate_type: "disqualifier"
    condition: "Primary entity creation or routine status-transition paths dynamically fetch and require completion of > 3 arbitrary admin-defined custom mandatory fields before local commit."
    failure_impact: "Routine task capture degrades into a multi-second bureaucratic form requiring 6+ clicks and remote validation waits, driving operators to abandon the tracker for shadow notes."
veto_triggers:
  - id: "veto-01"
    name: "blocking_server_mutation_spinner"
    severity: "hard_veto"
    target_antipattern: "Cloud-first SaaS forms, list rows, or kanban cards that disable controls and display a spinner while awaiting HTTP/GraphQL round-trips (> 150 ms to 3,000 ms) during daily CRUD edits."
    detection_rule: "Static AST or runtime audit detects submit, toggle, assign, label, or status handlers calling await fetch()/mutateAsync() prior to updating client store state, or setting disabled/isLoading UI lockouts during routine mutations."
    mandatory_remediation: "Invert the write path: apply synchronous in-memory store updates (<= 50 ms), record prior field snapshots into a persistent IndexedDB transaction queue, flush asynchronously via batched mutations, and execute deterministic rollback with an error toast only on server rejection."
  - id: "veto-02"
    name: "bureaucratic_multi_click_entity_modal"
    severity: "hard_veto"
    target_antipattern: "Jira-style entity creation dialogs requiring >= 4 mouse clicks, multiple un-defaulted mandatory dropdowns (Project, Type, Priority, Component), or multi-step forms to capture one item."
    detection_rule: "DOM/JSX audit of the primary creation component finds > 1 required field lacking a contextual default, > 1 modal step, missing autofocus on the title input, or absence of a single-key trigger ('C') and keyboard submit ('Cmd/Ctrl+Enter')."
    mandatory_remediation: "Collapse creation into a single instant composer triggered by 'C' with autofocused title input, pre-populate team and default workflow status from active view context, relegate optional metadata to inline chips/hotkeys, and commit via Cmd/Ctrl+Enter."
  - id: "veto-03"
    name: "animated_high_frequency_chrome"
    severity: "hard_veto"
    target_antipattern: "Adding 200-500 ms CSS transitions, fade-out hover tails, or spring mount animations to Cmd+K command palettes, keyboard-navigated list highlights, instant quick pickers, or hotkey-triggered surfaces executed >= 100 times/day."
    detection_rule: "CSS/TSX audit finds transition-duration > 0ms, animation-duration > 0ms, or Framer Motion/spring entrance wrappers on command palettes, keyboard-triggered popovers, or high-frequency list row hover/selection highlights."
    mandatory_remediation: "Enforce transition: none and animation: none (0 ms) on all keyboard-initiated controls, command palettes, and list row hover highlights; restrict transitions (<= 180 ms ease-out) strictly to infrequent overlays or rare onboarding moments."
  - id: "veto-04"
    name: "mouse_locked_nested_toolbar_without_shortcuts"
    severity: "conditional_block"
    target_antipattern: "Hiding daily triage actions (assign, label, priority, status, move) behind nested mouse-only toolbar dropdowns with zero keyboard bindings, missing <kbd> hints, and brittle Manhattan-path submenus."
    detection_rule: "Code/DOM audit detects >= 3 primary entity actions lacking both keydown listeners and Cmd/Ctrl+K registration, < 90% <kbd> hint coverage inside [role='menuitem'], or cascading hover submenus without a dynamic triangular pointer safe zone."
    mandatory_remediation: "Bind all primary actions to single-key shortcuts and a Cmd/Ctrl+K fuzzy command palette, render OS-aware <kbd> hints inline inside right-click contextual menus, and mount a dynamic CSS clip-path triangular safe zone on cascading submenus."
  - id: "veto-05"
    name: "untokenized_hex_chrome_and_heavy_borders"
    severity: "conditional_block"
    target_antipattern: "Hand-maintained hex/HSL palettes exceeding 20 manual theme variables, structural border-width >= 2px, or dark-mode box-shadows substituted for perceptual tonal surface elevation."
    detection_rule: "Static CSS/token lint identifies hardcoded hex/rgb/hsl color literals outside token generator files, structural panel border-width > 1px, or elevated dark-mode panels lacking monotonic LCH/OKLCH lightness steps."
    mandatory_remediation: "Migrate to a programmatic LCH/OKLCH token generator parameterized by <= 3 base inputs (base, accent, contrast), differentiate layers with subtle lightness shifts plus <= 1px tokenized hairlines, and enforce token usage via build-time lint rules."
concrete_heuristics:
  - id: "heur-01"
    rule_statement: "IF a user executes a daily entity mutation (create, status, assignee, label, priority, reorder), THEN commit synchronously to the reactive in-memory object graph and repaint the DOM before dispatching network sync."
    metric_or_bound: "<= 50 ms local commit-to-paint (hard ceiling < 100 ms); 0 network awaits before UI state commit"
    verification_method: "runtime_telemetry"
    applies_to:
      - "saas_b2b_intensive"
      - "ai_native_desktop_ide"
    source_id: "src-16"
  - id: "heur-02"
    rule_statement: "IF an optimistic write executes locally, THEN snapshot prior property values, persist the transaction in IndexedDB via microtask batching, order server application by monotonic sync ID, and revert deterministically on server rejection."
    metric_or_bound: "100% of mutation transaction classes implement deterministic revert(snapshot) and survive browser reloads in IndexedDB"
    verification_method: "state_matrix_check"
    applies_to:
      - "saas_b2b_intensive"
      - "ai_native_desktop_ide"
    source_id: "src-14"
  - id: "heur-03"
    rule_statement: "IF a domain action occurs >= 10 times per workday per operator, THEN bind it to a single-key shortcut (C create, A assign, I self-assign, L label, S status, P priority, X select, J/K navigate) AND register it in the Cmd/Ctrl+K fuzzy command palette."
    metric_or_bound: "0 mouse homing ops (H=0) and 0 pointing ops (P=0) for top-10 workflows; modeled KLM speedup >= 2.5x vs nested mouse menus"
    verification_method: "klm_goms_estimate"
    applies_to:
      - "saas_b2b_intensive"
      - "ai_native_desktop_ide"
    source_id: "src-12"
  - id: "heur-04"
    rule_statement: "IF a command exposes a keyboard shortcut, THEN render its OS-aware keybinding inline (<kbd>) inside right-click contextual menus, hover tooltips, and Cmd/Ctrl+K rows to convert mouse users into shortcut users passively."
    metric_or_bound: ">= 90% <kbd> parity between keybinding registry and visible [role='menuitem'] / command palette rows"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "saas_b2b_intensive"
      - "ai_native_desktop_ide"
    source_id: "src-05"
  - id: "heur-05"
    rule_statement: "IF a contextual menu spawns cascading hover sub-menus, THEN render a dynamic CSS clip-path triangular safe-zone polygon spanning from cursor (mouseX, mouseY) to the sub-menu bounds to protect diagonal Euclidean movement."
    metric_or_bound: "0 accidental sub-menu dismissals on diagonal pointer paths; removes 1.0-2.0 s Manhattan-path penalty per invocation"
    verification_method: "static_code_audit"
    applies_to:
      - "saas_b2b_intensive"
      - "ai_native_desktop_ide"
    source_id: "src-05"
  - id: "heur-06"
    rule_statement: "IF opening the primary entity creation composer, THEN require only a title string from the user, pre-populate team and initial workflow status via active view defaults, autofocus the title field, and submit on Cmd/Ctrl+Enter."
    metric_or_bound: "<= 1 un-defaulted required input; <= 3 non-typing keystrokes (C + Cmd+Enter); 0 mandatory custom-field blockers"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "saas_b2b_intensive"
    source_id: "src-01"
  - id: "heur-07"
    rule_statement: "IF an element is triggered by keyboard input or encountered >= 100 times/day (command palette, list row hover, active focus ring, consecutive tooltip hover), THEN set CSS transition-duration and animation-duration to 0 ms."
    metric_or_bound: "== 0 ms for keyboard and >= 100x/day elements; <= 180 ms (max < 300 ms) ease-out for infrequent modals/drawers"
    verification_method: "static_code_audit"
    applies_to:
      - "saas_b2b_intensive"
      - "ai_native_desktop_ide"
    source_id: "src-11"
  - id: "heur-08"
    rule_statement: "IF theming a high-density workspace, THEN compute all surface, text, icon, and <= 1px border tokens programmatically in LCH/OKLCH from <= 3 base parameters (base color, accent color, contrast) and regenerate subtree variables when container surfaces change state."
    metric_or_bound: "<= 3 base theme inputs deriving 100+ semantic tokens; structural border-width <= 1px; >= 4.5:1 WCAG AA text contrast"
    verification_method: "static_code_audit"
    applies_to:
      - "saas_b2b_intensive"
      - "ai_native_desktop_ide"
    source_id: "src-06"
  - id: "heur-09"
    rule_statement: "IF an entity state transition maps deterministically to an upstream engineering event (branch push -> In Progress, PR merge -> Done, cycle end -> rollover, stale backlog -> auto-archive), THEN automate the transition instead of prompting manual updates."
    metric_or_bound: "0 manual status updates required for Git-linked issue lifecycles and scheduled n-week cycle rollovers"
    verification_method: "state_matrix_check"
    applies_to:
      - "saas_b2b_intensive"
      - "ai_native_desktop_ide"
    source_id: "src-01"
  - id: "heur-10"
    rule_statement: "IF integrating AI agents into a workspace, THEN anchor agent inputs and outputs onto deterministic workbench entities (issues, code diffs, review queues, approval controls) rather than an unstructured chat transcript."
    metric_or_bound: "100% of agent mutations bind to typed entity IDs with explicit diff preview and 1-action approve/revert controls"
    verification_method: "state_matrix_check"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-10"
blind_spots:
  - id: "bs-01"
    failure_mode: "Cold-start discoverability cliff and hidden-hotkey blindness: empirical HCI research found only 1.59% (strict) to 6.37% (loose) of users organically favor keyboard shortcuts (familiarity r=0.13), causing infrequent or non-technical stakeholders to miss functionality hidden behind terse tonal chrome and single-key bindings."
    trigger_context: "First-time workspace onboarding (< 5 sessions), occasional executive/legal/marketing reviewers, or cross-functional organizations where non-engineers represent > 40% of active seats."
    counterweight_designer: "don-norman"
  - id: "bs-02"
    failure_mode: "Schema rigidity, compliance-gate deadlocks, and external sync divergence: refusing arbitrary mandatory custom fields, multi-stage approval gates, and fine-grained field-level RBAC breaks regulated enterprise governance—documented in Linear's own Jira sync where Jira required fields block issue creation and workflow constraints cause silent out-of-sync states."
    trigger_context: "Regulated enterprise environments (healthcare, fintech, defense, > 1,000-person orgs) enforcing mandatory compliance metadata, multi-party audit sign-offs, or complex Gantt dependency tracking."
    counterweight_designer: "ben-shneiderman"
  - id: "bs-03"
    failure_mode: "Coarse-pointer touch failure and single-visit conversion friction: keyboard-centric dense views and 0 ms austere surfaces fail on mobile touchscreens (no hardware keyboard; 49% one-handed grip, 75% thumb-driven) and depress comprehension in one-time public signup or checkout funnels."
    trigger_context: "Mobile consumer capture apps (viewport < 480px, pointer: coarse) and anonymous top-of-funnel onboarding or e-commerce conversion flows."
    counterweight_designer: "luke-wroblewski"
debate_triggers:
  - id: "dbt-01"
    opposing_designer: "don-norman"
    conflict_axis: "keyboard_first_velocity_vs_explicit_discoverability"
    this_designer_stance: "Remove persistent toolbar chrome in favor of single-key shortcuts (C, A, I, L, S, P) and a 0 ms Cmd+K palette so high-frequency operators save 0.659-1.484 s per action and eliminate mouse homing (H=0.40s)."
    opposing_stance: "Relying on knowledge in the head fails infrequent users (only 1.59%-6.37% prefer shortcuts organically); interfaces must place persistent visible signifiers and physical constraints directly in the world."
    arbitration_rule: "IF median active user executes >= 20 entity actions/day across >= 4 days/week (saas_b2b_intensive, ai_native_desktop_ide), enforce Karri Saarinen's keyboard-first surface PLUS mandatory >= 90% inline <kbd> hints in contextual menus; IF user visits < 3 times/month or is within sessions 1-3, prioritize Don Norman's persistent labeled controls and explicit signifiers."
  - id: "dbt-02"
    opposing_designer: "ben-shneiderman"
    conflict_axis: "opinionated_minimal_defaults_vs_flexible_exploratory_control"
    this_designer_stance: "Constrain workflows to a minimal opinionated schema (Team -> Status -> Title, automated cycles, zero per-project custom fields) so builders eliminate administrative maintenance and execute writes in <= 50 ms."
    opposing_stance: "Complex regulated domains require direct manipulation over rich visual state, layered novice-to-expert scaffolding, and explicit reversible safety interlocks rather than rigid workflow defaults that force brittle external workarounds."
    arbitration_rule: "IF regulatory mandatory-field count == 0 and workflow variance is low (software product delivery), enforce Karri Saarinen's opinionated defaults (<= 1 manual required field); IF compliance mandates >= 3 audit-verified fields or formal multi-party sign-off gates, yield to Ben Shneiderman's staged direct-manipulation validation and explicit reversible confirmation scaffolds."
  - id: "dbt-03"
    opposing_designer: "luke-wroblewski"
    conflict_axis: "desktop_keyboard_density_vs_mobile_thumb_first_ergonomics"
    this_designer_stance: "Optimize primary workspace surfaces for desktop viewports (>= 1280px), fine pointers, single-key shortcuts, and 0 ms dense tonal lists designed for hundreds of daily triage actions."
    opposing_stance: "Architect mobile-first around one-handed thumb arcs (49% one-handed hold, 75% thumb-driven), >= 44px touch targets, single-column progressive disclosure, and obvious visible primary buttons."
    arbitration_rule: "IF >= 75% of sessions occur on desktop viewports (>= 1024px, pointer: fine, hardware keyboard), enforce Karri Saarinen's keyboard-first high-density architecture; IF >= 40% of capture or conversion sessions occur on coarse touch pointers (< 768px), yield to Luke Wroblewski's thumb-zone ergonomics and >= 44px visible touch controls."
  - id: "dbt-04"
    opposing_designer: "rauno-freiberg"
    conflict_axis: "zero_motion_daily_utility_vs_tactile_spring_physics"
    this_designer_stance: "Suppress transitions completely (0 ms) on keyboard-triggered actions, command palettes, and hover states triggered >= 100 times/day because 300-425 ms motion burns 2.08-2.95 hours/year in cumulative drag."
    opposing_stance: "Interruptible spring physics and continuous spatial transitions preserve state provenance, reduce change blindness, and elevate tactile precision on direct-manipulation controls."
    arbitration_rule: "IF an action is keyboard-initiated OR exceeds 50 daily invocations per user, enforce Karri Saarinen's 0 ms instant state cut; IF an action is pointer/gesture-driven AND occurs < 20 times/day (modals, drag-and-drop continuity, rare onboarding moments), permit Rauno Freiberg's interruptible ease-out/spring physics capped at <= 180-250 ms."
primary_sources:
  - id: "src-01"
    title: "The Linear Method: Principles & Practices"
    author_or_org: "Karri Saarinen / Linear"
    year: 2020
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/method/introduction"
    extracted_invariant: "Purpose-built B2B tools embed opinionated defaults (fixed conceptual model, automated n-week cycles, elimination of admin busy-work) because unconstrained flexibility creates workflow chaos as teams scale."
  - id: "src-02"
    title: "How we redesigned the Linear UI (part II)"
    author_or_org: "Karri Saarinen, Yann-Edern Gillet, Romain Cascino, Andreas Eldh (Linear)"
    year: 2024
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/now/how-we-redesigned-the-linear-ui"
    extracted_invariant: "Migrating from 98 manual HSL theme variables to 3 perceptually uniform LCH inputs (base color, accent color, contrast) mathematically derives consistent elevation surfaces and accessible contrast ramps across light and dark modes."
  - id: "src-03"
    title: "A design reset (part I)"
    author_or_org: "Karri Saarinen (Linear)"
    year: 2024
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/now/a-design-reset"
    extracted_invariant: "Fast-evolving software accumulates holistic visual design debt that must be paid down in comprehensive sweeps every 2-3 years rather than fragmented view-by-view updates."
  - id: "src-04"
    title: "Rebuilding Linear's delta sync read path"
    author_or_org: "Peter Travers (Linear Engineering)"
    year: 2026
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/now/rebuilding-delta-sync-read-path"
    extracted_invariant: "Each client maintains a local database so daily mutations execute with zero network round-trips; permission-scoped delta catch-up over >20 TB of sync actions (~1M/day in largest workspaces) uses Turbopuffer inverted posting lists plus Postgres late enrichment to keep reconnect tail latency flat."
  - id: "src-05"
    title: "Invisible details - Building contextual menus"
    author_or_org: "Andreas Eldh (Linear)"
    year: 2020
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/now/invisible-details"
    extracted_invariant: "Contextual menus display inline keyboard shortcut hints to onboard mouse users into hotkeys, while a 40-line dynamic CSS clip-path triangular safe zone preserves diagonal Euclidean cursor movement and removes 1-2 s Manhattan-path friction repeated hundreds of times daily."
  - id: "src-06"
    title: "Styling Linear for the future with StyleX"
    author_or_org: "Kenneth Skovhus (Linear Engineering)"
    year: 2026
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/now/styling-linear-for-the-future-stylex"
    extracted_invariant: "Build-time atomic CSS with Oxlint-enforced tokens (colors, typography, shadows, animations, cursors, thin borders) and nested LCH ThemeProviders eliminates hundreds of runtime CSS injections (0 on navigation), cutting main-thread CPU work by 20-35% and boosting mid-tier rendering by ~30%."
  - id: "src-07"
    title: "Sharing Linear's growth with the people building it"
    author_or_org: "Karri Saarinen (Linear)"
    year: 2026
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/now/sharing-growth-with-the-people-building-linear"
    extracted_invariant: "Craft-first engineering scaled Linear past $100M ARR, 40,000+ paying companies, 177% NRR, $2.5B valuation, and 95% workspace AI-agent adoption (50% of work created by agents) with positive cashflow."
  - id: "src-08"
    title: "Building a Visual Language: Behind the scenes of our Airbnb design system"
    author_or_org: "Karri Saarinen (Airbnb Design)"
    year: 2016
    source_type: "engineering_post"
    url_or_identifier: "https://medium.com/airbnb-design/building-a-visual-language-behind-the-scenes-of-our-airbnb-design-system-224748775e4e"
    extracted_invariant: "Because software lacks physical constraints, design teams must self-impose strict, self-contained component systems (rather than loosely recombined atoms) to prevent divergence and prototype ~50 screens in hours."
  - id: "src-09"
    title: "Designing Coinbase - Clarity and Trust for Bitcoin"
    author_or_org: "Karri Saarinen"
    year: 2016
    source_type: "engineering_post"
    url_or_identifier: "https://karrisaarinen.com/posts/designing-coinbase/"
    extracted_invariant: "Distilling complex multi-signature vault and merchant checkout mechanics into focused single-purpose workflows drove adoption across 43,000 merchants and 4-star iOS/Android financial apps rebuilt in <3 months."
  - id: "src-10"
    title: "Design for the AI age"
    author_or_org: "Karri Saarinen (Linear)"
    year: 2025
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/now/design-for-the-ai-age"
    extracted_invariant: "Generic chat containers suffer high prompt variance and poor system integration; agentic software requires a deterministic UI workbench where agents operate on typed entities under explicit human review."
  - id: "src-11"
    title: "You Don't Need Animations"
    author_or_org: "Emil Kowalski (former Linear Design Engineer)"
    year: 2025
    source_type: "engineering_post"
    url_or_identifier: "https://emilkowal.ski/ui/you-dont-need-animations"
    extracted_invariant: "Keyboard-initiated actions, command palettes, hover sweeps, and elements seen 100+ times daily require 0 ms transitions; infrequent dropdowns perform best <= 180 ms (hard ceiling < 300 ms)."
  - id: "src-12"
    title: "The Keystroke-Level Model for User Performance Time with Interactive Systems"
    author_or_org: "Stuart K. Card, Thomas P. Moran, Allen Newell"
    year: 1980
    source_type: "peer_reviewed_paper"
    url_or_identifier: "Communications of the ACM, 23(7), 396-410"
    extracted_invariant: "Expert routine task time equals the sum of operators (K=0.20s, P=1.10s, H=0.40s, M=1.35s, R=wait); removing hand homing and mouse pointing via single-key shortcuts cuts modeled execution latency by 67-70%."
  - id: "src-13"
    title: "Hidden Costs of Graphical User Interfaces: Failure to Make the Transition from Menus and Icon Toolbars to Keyboard Shortcuts"
    author_or_org: "David M. Lane, H. Albert Napier, S. Camille Peres, Aniko Sandor"
    year: 2005
    source_type: "peer_reviewed_paper"
    url_or_identifier: "DOI:10.1207/s15327590ijhc1802_1"
    extracted_invariant: "Keyboard shortcuts executed 0.659 s faster than icon toolbars and 1.484 s faster than menus in Study 2, yet only 1.59% (strict) to 6.37% (loose) of users favored them spontaneously in Study 1 (familiarity r=0.13), quantifying the discoverability blind spot."
  - id: "src-14"
    title: "Reverse Engineering Linear's Sync Engine"
    author_or_org: "Wenzhao Hu (endorsed by Linear CTO Tuomas Artman)"
    year: 2024
    source_type: "shipped_oss_repo"
    url_or_identifier: "https://github.com/wzhudev/reverse-linear-sync-engine"
    extracted_invariant: "Linear mutates an in-memory MobX object graph synchronously, captures prior property values for rollback, persists microtask-batched transactions in IndexedDB (__transactions), and applies server delta packets in strict monotonic sync-ID order."
  - id: "src-15"
    title: "Response Times: The 3 Important Limits (Usability Engineering, Ch. 5)"
    author_or_org: "Jakob Nielsen"
    year: 1993
    source_type: "book"
    url_or_identifier: "https://www.nngroup.com/articles/response-times-3-important-limits/"
    extracted_invariant: "UI response <= 100 ms maintains the perception of direct manipulation with zero progress chrome; > 1,000 ms interrupts operator flow of thought."
  - id: "src-16"
    title: "Linear 2022 Release — Sync Engine"
    author_or_org: "Linear"
    year: 2022
    source_type: "engineering_post"
    url_or_identifier: "https://linear.app/releases/2022"
    extracted_invariant: "Real-time local sync architecture targets 50 ms / 0 ms instant interactions and 10x faster initial load times with zero blocking spinners."
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

Karri Saarinen treats B2B software as a precision instrument for daily makers rather than a configurable administrative database for procurement committees. Four architectural invariants define this operational worldview:

1. **Speed is an architectural property, not a frontend polish pass.** Any interface whose read and write paths traverse an HTTP round-trip before painting violates Jakob Nielsen's 100 ms direct-manipulation ceiling. Daily mutations (creating issues, updating statuses, assigning owners, applying labels, switching views) must commit synchronously to an in-memory reactive object graph in `<= 50 ms`, persist reversible transaction logs to IndexedDB, and synchronize asynchronously via monotonic server sync IDs.
2. **Keyboard-first input eliminates KLM motor overhead.** Under Card, Moran, and Newell's Keystroke-Level Model (`K=0.20s`, `P=1.10s`, `H=0.40s`, `M=1.35s`), moving a hand from keyboard to mouse (`H`) and hunting nested menus (`P + M`) dominates task duration. Binding top-10 daily mutations to single-key triggers (`C`, `A`, `I`, `L`, `S`, `P`, `X`, `J/K`) and indexing every command inside a `0 ms` `Cmd/Ctrl+K` fuzzy palette reduces modeled routine creation and triage latency by `67.0%–69.7%` (`3.03x–3.30x` speedup).
3. **Opinionated defaults defeat administrative entropy via Via Negativa.** Every software layer encodes opinions; pretending to be neutral pushes workflow design onto end users, yielding 50-dropdown views, mandatory custom-field gates, and dedicated tool administrators. Purpose-built tools lock a coherent conceptual hierarchy (`Workspace > Team > Workflow/Triage/Cycles > Initiative > Project > Milestone > Issue`), pre-fill context defaults so creation demands only a title, automate lifecycle transitions from upstream Git/schedule telemetry, and frame AI agents inside deterministic entity workbenches rather than generic chat threads.
4. **Programmatic tonal craft and zero-motion restraint sustain visual endurance.** Instead of hand-authoring ~100 fragile HSL variables, dark-mode shadows, or `>= 2px` structural chrome, themes derive mathematically in perceptually uniform LCH/OKLCH from `<= 3` inputs (`base`, `accent`, `contrast`), compiled via build-time atomic CSS (`0` runtime style injections on navigation, `20%–35%` less main-thread CPU). High-frequency controls (`>= 100x/day` or keyboard-triggered) run at `0 ms` transition duration because a `300–425 ms` animation wastes `2.08–2.95 hours/year` per operator.

## 2. Regime Boundaries & Out-of-Universe Rationale

| Regime | Fit Status | Structural Rationale |
| :--- | :--- | :--- |
| `saas_b2b_intensive` | **Primary** | Operators spend hours daily creating, triaging, and mutating structured entities on desktop hardware keyboards (`>= 100` interactions/day). Local-first `<= 50 ms` sync, single-key bindings, opinionated defaults, and `0 ms` tonal chrome compound directly into shipping momentum. |
| `ai_native_desktop_ide` | **Secondary** | Engineers and technical operators coordinate coding agents, PR diffs, and review queues on fine-pointer desktop displays. Saarinen's deterministic workbench model replaces high-variance chat threads with typed entity bindings, instant diff reviews, and keyboard triage. |
| `mobile_consumer_capture` | **Out of Universe** | Hardware keyboards do not exist on mobile touchscreens where 49% of holds are one-handed and 75% of taps are thumb-driven. Single-key bindings yield `0%` value and dense tonal rows break `>= 44px` touch ergonomics. Route to `luke-wroblewski`. |
| `analytics_dense_telemetry` | **Out of Universe** | Observability, APM, and BI dashboards demand high-density multivariate encodings, sparklines, and open-ended OLAP slicing—capabilities Linear intentionally omits to stay execution-focused. Route to `edward-tufte`. |
| `landing_onboarding_conversion` | **Out of Universe** | Anonymous first-visit pages and checkout funnels occur once per user. Removing explicit narrative cues, guided visual signifiers, and purposeful onboarding transitions suppresses comprehension and conversion. Route to `luke-wroblewski` or `don-norman`. |

## 3. Signal Detection Protocol

Text-only coding agents evaluate target codebases, DOM snapshots, CSS token files, and state machines against seven deterministic signals (`sig-01` through `sig-07`) in strict priority order:

| Signal ID | Weight | Verification Probe (Text-Only Executable) | Pass Threshold |
| :--- | :--- | :--- | :--- |
| `sig-01` | `critical` | Inspect mutation handlers (`onSubmit`, `onClick`, `onKeyDown`) for `await fetch/axios/graphql` calls preceding local state setters; inspect latency telemetry if available. | `<= 50 ms` local paint (`< 100 ms` ceiling); `0` blocking awaits before optimistic local commit. |
| `sig-02` | `critical` | Enumerate top-10 daily entity actions; verify registered `keydown` bindings and global `Cmd/Ctrl+K` command registry entries. | `100%` of top-10 actions in `Cmd/Ctrl+K`; `>= 5` primary mutations bound to single keys. |
| `sig-03` | `critical` | Parse primary entity creation JSX/schema (`required`, Zod/Yup rules, multi-step wizard state). | `<= 1` un-defaulted required field (title only); `== 1` view step; title `autoFocus` present. |
| `sig-04` | `high` | Grep CSS/StyleX/Tailwind/Framer Motion definitions attached to command palettes, hotkey pickers, and dense list-row hover/focus states. | `== 0 ms` (`transition: none`) on keyboard & `>= 100x/day` elements; `<= 180 ms` (`< 300 ms`) on infrequent overlays. |
| `sig-05` | `high` | Cross-reference keybinding map against `[role="menuitem"]`, command palette items, and primary tooltips for inline `<kbd>` or shortcut badge nodes. | `>= 90%` of bound actions surface OS-aware shortcut hints inline. |
| `sig-06` | `high` | Audit CSS token files and component stylesheets for LCH/OKLCH definitions, hardcoded `#hex`/`rgb()`/`hsl()` literals, and structural `border-width`. | LCH/OKLCH token generator (`<= 5` base inputs), `0` hardcoded color literals in components, `border-width <= 1px`. |
| `sig-07` | `medium` | Inspect AI/agent UI components for entity ID binding, diff/preview state, and explicit human approve/reject/revert actions. | `100%` of agent mutations bound to typed workspace entities with deterministic review and undo controls. |

## 4. Hard Filters & Veto Playbook

Every audit first executes the five binary gate checks (`flt-01`..`flt-05`) and five antipattern vetoes (`veto-01`..`veto-05`):

1. **Mandatory Gate Audit (`hard_filters`):**
   - `flt-01` (`required`): Confirm optimistic writes snapshot prior values, persist to IndexedDB/SQLite with idempotency or monotonic sync IDs, and execute deterministic rollback on server rejection.
   - `flt-02` (`required`): Confirm cached navigation between workspace views paints in `<= 100 ms` with `0` blocking spinners or full-page skeleton loaders.
   - `flt-03` (`required`): Confirm single-key global listeners guard against `INPUT`, `TEXTAREA`, `SELECT`, `isContentEditable`, and `event.isComposing === true`.
   - `flt-04` (`required`): Confirm zero runtime `<style>` rule injection during dense view navigation (build-time atomic CSS or static tokenized CSS).
   - `flt-05` (`disqualifier`): Trigger immediate failure if primary creation or status paths force `> 3` admin-configured custom mandatory fields before local commit.
2. **Veto Escalation (`veto_triggers`):**
   - Any hit on `veto-01` (blocking server mutation spinner), `veto-02` (bureaucratic multi-click entity modal), or `veto-03` (animated high-frequency chrome) triggers a `hard_veto` (`-35` pts each, caps final score at `49`, forces stance `BLOCK`).
   - Any hit on `veto-04` (mouse-locked nested toolbar without shortcuts/hints/safe-zone) or `veto-05` (untokenized hex chrome / `>= 2px` structural borders / dark-mode drop-shadow elevation) triggers a `conditional_block` (`-15` pts each, blocks `APPROVE` and forces at least `REVISE` until remediated).

## 5. Executable Heuristics & Code Patterns

### Refactoring 1: Bureaucratic Blocking Creation Modal vs. Local-First Optimistic Composer (`C` + Defaults + Rollback)

**Before (Violates `veto-01`, `veto-02`, `veto-03`, `flt-01`, `flt-03`, `sig-01`, `sig-03`, `sig-04`):**
Blocks submission behind a `POST /api/issues` spinner, forces 4 un-defaulted required dropdowns, lacks `'C'` hotkey and `Cmd+Enter` commit, and animates open over `300 ms`.

```tsx
// BEFORE: Bureaucratic cloud-first creation modal (KLM ~22.25s–24.25s, 7 clicks, 3 homings)
import React, { useState } from "react";

export function LegacyCreateIssueModal({ onCreated, onClose }: { onCreated: () => void; onClose: () => void }) {
  const [project, setProject] = useState("");
  const [issueType, setIssueType] = useState("");
  const [component, setComponent] = useState("");
  const [priority, setPriority] = useState("");
  const [title, setTitle] = useState("");
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!project || !issueType || !component || !priority || !title.trim()) return;
    setSubmitting(true); // VETO-01: locks UI behind network round-trip
    try {
      const res = await fetch("/api/issues", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ project, issueType, component, priority, title }),
      });
      if (!res.ok) throw new Error("Server validation failed");
      onCreated();
      onClose();
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div style={{ transition: "opacity 300ms ease, transform 300ms ease", background: "#1e1e24", border: "2px solid #444" }}>
      <form onSubmit={handleSubmit}>
        <select required value={project} onChange={(e) => setProject(e.target.value)}>
          <option value="">Select Project...</option>
          <option value="CORE">Core Platform</option>
        </select>
        <select required value={issueType} onChange={(e) => setIssueType(e.target.value)}>
          <option value="">Select Issue Type...</option>
          <option value="TASK">Task</option>
          <option value="BUG">Bug</option>
        </select>
        <select required value={component} onChange={(e) => setComponent(e.target.value)}>
          <option value="">Select Component...</option>
          <option value="SYNC">Sync Engine</option>
        </select>
        <select required value={priority} onChange={(e) => setPriority(e.target.value)}>
          <option value="">Select Priority...</option>
          <option value="HIGH">High</option>
        </select>
        <input required value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Issue summary" />
        <button type="submit" disabled={submitting}>
          {submitting ? "Saving to server..." : "Create Issue"}
        </button>
      </form>
    </div>
  );
}
```

**After (Satisfies `heur-01`, `heur-02`, `heur-03`, `heur-06`, `heur-07`, `heur-08`, `flt-01`, `flt-03`):**
Opens instantaneously (`0 ms`) via single-key `C` (with strict input/IME focus isolation), pre-fills `teamId` and `status` via active workspace defaults so only `title` is typed, commits synchronously (`<= 50 ms`) to the local reactive store + persistent IndexedDB transaction queue, submits via `Cmd/Ctrl+Enter`, and rolls back deterministically if the server rejects the batch.

```tsx
// AFTER: Local-first optimistic composer with opinionated defaults & deterministic rollback (KLM ~7.34s, 0 clicks, 0 homings)
import React, { useEffect, useRef, useState } from "react";

interface Issue {
  id: string;
  teamId: string;
  status: "todo" | "in_progress" | "done";
  priority: 0 | 1 | 2 | 3 | 4;
  title: string;
  syncState: "pending" | "synced";
}

interface LocalSyncStore {
  activeTeamId: string;
  defaultStatus: Issue["status"];
  upsertLocal: (issue: Issue) => void;
  deleteLocal: (id: string) => void;
  enqueueIdbTransaction: (tx: { txId: string; kind: "create"; payload: Issue }) => Promise<void>;
  flushToServer: (txId: string) => Promise<{ ok: boolean; error?: string }>;
  notifyError: (message: string, retry: () => void) => void;
}

function isEditableTarget(el: Element | null): boolean {
  if (!el) return false;
  const tag = el.tagName;
  return tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || (el as HTMLElement).isContentEditable;
}

export function LocalFirstIssueComposer({ store }: { store: LocalSyncStore }) {
  const [open, setOpen] = useState(false);
  const [title, setTitle] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  // FLT-03 + HEUR-03: Single-key 'C' trigger with strict editable/IME isolation
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (e.isComposing || e.metaKey || e.ctrlKey || e.altKey) return;
      if (isEditableTarget(document.activeElement)) return;
      if (e.key.toLowerCase() === "c") {
        e.preventDefault();
        setOpen(true);
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, []);

  useEffect(() => {
    if (open) inputRef.current?.focus(); // Synchronous focus, 0ms transition delay
  }, [open]);

  function commitOptimistically() {
    const trimmed = title.trim();
    if (!trimmed) return;

    const id = crypto.randomUUID();
    const txId = crypto.randomUUID();
    // HEUR-06: Opinionated defaults eliminate 4 mandatory dropdowns
    const optimisticIssue: Issue = {
      id,
      teamId: store.activeTeamId,
      status: store.defaultStatus,
      priority: 0,
      title: trimmed,
      syncState: "pending",
    };

    // HEUR-01: Synchronous in-memory write + instant UI close (<= 50ms, 0 network await)
    store.upsertLocal(optimisticIssue);
    setTitle("");
    setOpen(false);

    // FLT-01 + HEUR-02: Durable IndexedDB queue + async sync + deterministic rollback
    void store
      .enqueueIdbTransaction({ txId, kind: "create", payload: optimisticIssue })
      .then(() => store.flushToServer(txId))
      .then((result) => {
        if (!result.ok) {
          store.deleteLocal(id); // Deterministic snapshot rollback
          store.notifyError(result.error ?? "Server rejected issue creation; local change reverted.", () => {
            setTitle(trimmed);
            setOpen(true);
          });
        }
      });
  }

  if (!open) return null;

  return (
    <div
      role="dialog"
      aria-label="Create issue"
      style={{
        transition: "none", // HEUR-07: 0ms on keyboard-initiated high-frequency composer
        background: "var(--lch-surface-elevated)",
        border: "1px solid var(--lch-hairline-subtle)", // HEUR-08: LCH token + <=1px border
        color: "var(--lch-text-primary)",
      }}
      onKeyDown={(e) => {
        if (e.key === "Escape") {
          e.preventDefault();
          setOpen(false);
        } else if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
          e.preventDefault();
          commitOptimistically();
        }
      }}
    >
      <div style={{ color: "var(--lch-text-secondary)", fontSize: 12 }}>
        {store.activeTeamId} / {store.defaultStatus}
      </div>
      <input
        ref={inputRef}
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Issue title"
        style={{ background: "transparent", color: "var(--lch-text-primary)", border: "none", outline: "none" }}
      />
      <button type="button" onClick={commitOptimistically}>
        Create <kbd>Cmd+Enter</kbd>
      </button>
    </div>
  );
}
```

### Refactoring 2: Mouse-Locked Nested Toolbar vs. Keyboard-First Triage + Contextual `<kbd>` Hints + `MouseSafeArea`

**Before (Violates `veto-01`, `veto-03`, `veto-04`, `veto-05`, `sig-02`, `sig-04`, `sig-05`, `sig-06`):**
Requires hovering nested dropdowns along a brittle Manhattan path, applies `250 ms` hover fades on every list row, omits shortcuts and `<kbd>` signifiers, blocks on server PATCH requests, and hardcodes hex borders.

```tsx
// BEFORE: Mouse-locked nested toolbar with 250ms hover lag and synchronous PATCH (KLM ~17.35s)
import React, { useState } from "react";

export function LegacyIssueToolbar({ issueId, onRefresh }: { issueId: string; onRefresh: () => void }) {
  const [menuOpen, setMenuOpen] = useState(false);
  const [subMenu, setSubMenu] = useState<"none" | "priority">("none");

  async function patchField(patch: Record<string, unknown>) {
    await fetch(`/api/issues/${issueId}`, { method: "PATCH", body: JSON.stringify(patch) });
    onRefresh();
    setMenuOpen(false);
  }

  return (
    <div style={{ border: "2px solid #333333", background: "#141418", transition: "background-color 250ms ease" }}>
      <button onClick={() => setMenuOpen((v) => !v)}>Actions ▾</button>
      {menuOpen && (
        <div role="menu" style={{ transition: "opacity 250ms ease", background: "#1c1c22" }}>
          <button role="menuitem" onClick={() => patchField({ assigneeId: "me" })}>
            Assign to me
          </button>
          <div onMouseEnter={() => setSubMenu("priority")} onMouseLeave={() => setSubMenu("none")}>
            <button role="menuitem">Set Priority ▸</button>
            {subMenu === "priority" && (
              <div role="menu">
                <button role="menuitem" onClick={() => patchField({ priority: 2 })}>
                  High
                </button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
```

**After (Satisfies `heur-01`, `heur-03`, `heur-04`, `heur-05`, `heur-07`, `heur-08`, `flt-03`):**
Binds single-key actions (`I`, `L`, `P`) plus a `0 ms` `Cmd/Ctrl+K` command palette, renders OS-aware `<kbd>` hints inline inside right-click contextual menus (`100%` parity), protects diagonal sub-menu cursor paths with a dynamic CSS `clip-path` triangular `MouseSafeArea` (Linear's 40-line pattern), and executes synchronous local mutations with rollback.

```tsx
// AFTER: Keyboard-first triage + 0ms Cmd+K palette + inline <kbd> hints + triangular MouseSafeArea (KLM ~5.25s)
import React, { useEffect, useMemo, useRef, useState } from "react";

interface TriageCommand {
  id: string;
  label: string;
  shortcut: string;
  run: (issueId: string) => void;
}

interface SafeAreaProps {
  subMenuRef: React.RefObject<HTMLDivElement | null>;
  mousePos: { x: number; y: number };
}

// HEUR-05: Dynamic CSS clip-path triangle protecting diagonal Euclidean cursor trajectories
function MouseSafeArea({ subMenuRef, mousePos }: SafeAreaProps) {
  const rect = subMenuRef.current?.getBoundingClientRect();
  if (!rect || rect.height === 0) return null;

  const isRightOfCursor = mousePos.x <= rect.x;
  const width = Math.max(isRightOfCursor ? rect.x - mousePos.x : mousePos.x - (rect.x + rect.width), 10);
  const relY = Math.min(100, Math.max(0, ((mousePos.y - rect.y) / rect.height) * 100));
  const clipPath = isRightOfCursor
    ? `polygon(100% 0%, 0% ${relY}%, 100% 100%)`
    : `polygon(0% 0%, 0% 100%, 100% ${relY}%)`;

  return (
    <div
      aria-hidden="true"
      style={{
        position: "absolute",
        top: 0,
        height: rect.height,
        width: `${width}px`,
        left: isRightOfCursor ? `-${width}px` : undefined,
        right: isRightOfCursor ? undefined : `-${width}px`,
        clipPath,
      }}
    />
  );
}

export function KeyboardFirstTriageSurface({
  activeIssueId,
  mutateOptimistically,
}: {
  activeIssueId: string;
  mutateOptimistically: (issueId: string, patch: Record<string, unknown>) => void;
}) {
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [contextMenuOpen, setContextMenuOpen] = useState(false);
  const [prioritySubOpen, setPrioritySubOpen] = useState(false);
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  const subMenuRef = useRef<HTMLDivElement>(null);

  const commands: TriageCommand[] = useMemo(
    () => [
      { id: "assign-me", label: "Assign to me", shortcut: "I", run: (id) => mutateOptimistically(id, { assigneeId: "me" }) },
      { id: "label-bug", label: "Add label: bug", shortcut: "L", run: (id) => mutateOptimistically(id, { addLabel: "bug" }) },
      { id: "priority-high", label: "Set priority: High", shortcut: "P", run: (id) => mutateOptimistically(id, { priority: 2 }) },
      { id: "status-progress", label: "Move to In Progress", shortcut: "S", run: (id) => mutateOptimistically(id, { status: "in_progress" }) },
    ],
    [mutateOptimistically]
  );

  // HEUR-03 + FLT-03: Single-key bindings + global Cmd/Ctrl+K with input/IME isolation
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (e.isComposing) return;
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setPaletteOpen((v) => !v);
        setQuery("");
        return;
      }
      const el = document.activeElement;
      if (el && (["INPUT", "TEXTAREA", "SELECT"].includes(el.tagName) || (el as HTMLElement).isContentEditable)) return;
      if (e.metaKey || e.ctrlKey || e.altKey) return;

      const match = commands.find((c) => c.shortcut.toLowerCase() === e.key.toLowerCase());
      if (match) {
        e.preventDefault();
        match.run(activeIssueId);
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [activeIssueId, commands]);

  const filtered = commands.filter((c) => c.label.toLowerCase().includes(query.toLowerCase()));

  return (
    <div
      onContextMenu={(e) => {
        e.preventDefault();
        setContextMenuOpen(true);
      }}
      onMouseMove={(e) => setMousePos({ x: e.clientX, y: e.clientY })}
      style={{
        transition: "none", // HEUR-07: 0ms hover/selection on high-frequency list rows
        background: "var(--lch-surface-row)",
        borderBottom: "1px solid var(--lch-hairline-row)",
        color: "var(--lch-text-primary)",
      }}
    >
      {/* Contextual menu with 100% inline <kbd> signifiers (HEUR-04) + MouseSafeArea (HEUR-05) */}
      {contextMenuOpen && (
        <div
          role="menu"
          style={{
            transition: "none",
            background: "var(--lch-surface-menu)",
            border: "1px solid var(--lch-hairline-subtle)",
          }}
        >
          {commands.map((cmd) => (
            <button
              key={cmd.id}
              role="menuitem"
              onClick={() => {
                cmd.run(activeIssueId);
                setContextMenuOpen(false);
              }}
              style={{ display: "flex", justifyContent: "space-between", width: "100%", transition: "none" }}
            >
              <span>{cmd.label}</span>
              <kbd>{cmd.shortcut}</kbd>
            </button>
          ))}
          <div
            style={{ position: "relative" }}
            onMouseEnter={() => setPrioritySubOpen(true)}
            onMouseLeave={() => setPrioritySubOpen(false)}
          >
            <button role="menuitem" style={{ display: "flex", justifyContent: "space-between", width: "100%" }}>
              <span>Priority levels</span>
              <kbd>P</kbd>
            </button>
            {prioritySubOpen && (
              <div ref={subMenuRef} role="menu" style={{ position: "absolute", left: "100%", top: 0 }}>
                <MouseSafeArea subMenuRef={subMenuRef} mousePos={mousePos} />
                <button role="menuitem" onClick={() => mutateOptimistically(activeIssueId, { priority: 1 })}>
                  <span>Urgent</span>
                  <kbd>1</kbd>
                </button>
                <button role="menuitem" onClick={() => mutateOptimistically(activeIssueId, { priority: 2 })}>
                  <span>High</span>
                  <kbd>2</kbd>
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* 0ms Command Palette (Cmd/Ctrl+K) */}
      {paletteOpen && (
        <div
          role="dialog"
          aria-label="Command palette"
          style={{
            transition: "none", // HEUR-07: 0ms open/close on >=100x/day command bar
            background: "var(--lch-surface-elevated)",
            border: "1px solid var(--lch-hairline-subtle)",
          }}
        >
          <input
            autoFocus
            role="combobox"
            aria-expanded="true"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Type a command..."
          />
          {filtered.map((cmd) => (
            <button
              key={cmd.id}
              role="option"
              onClick={() => {
                cmd.run(activeIssueId);
                setPaletteOpen(false);
              }}
              style={{ display: "flex", justifyContent: "space-between", width: "100%", transition: "none" }}
            >
              <span>{cmd.label}</span>
              <kbd>{cmd.shortcut}</kbd>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
```

## 6. Blind Spots & Counterweights

1. **Hidden-Shortcut Cliff and Cross-Functional Exclusion (`bs-01` -> `don-norman`):**
   Peer-reviewed research by Lane et al. (2005) found that while keyboard shortcuts saved `0.659–1.484 s` per command in controlled trials, only `1.59%` (strict) to `6.37%` (loose) of users favored them organically, with experience correlating at just `r = 0.13`. Applying Saarinen's stripped chrome to cold-start users or non-engineering cohorts (marketing, legal, executive reviewers) causes feature invisibility and abandonment. Mitigate by enforcing `>= 90%` `<kbd>` signifier parity inside visible contextual menus (`sig-05`) and deferring to `don-norman` whenever visit cadence drops below 3 sessions/month.
2. **Enterprise Compliance Rigidity and Sync Divergence (`bs-02` -> `ben-shneiderman`):**
   Refusing arbitrary required custom fields, complex RBAC matrix rules, and multi-stage approval workflows creates operational failures in regulated enterprises. Linear's official Jira integration documentation confirms that mandatory Jira fields prevent Linear from creating synced issues and workflow constraints trigger silent out-of-sync divergence when Linear applies local mutations. Audit logs retain `90 days` only on Enterprise tiers. In regulated environments requiring `>= 3` mandatory compliance fields or formal sign-off interlocks, defer to `ben-shneiderman`'s direct-manipulation validation scaffolds.
3. **Coarse-Pointer Touch and One-Time Conversion Mismatch (`bs-03` -> `luke-wroblewski`):**
   With 49% one-handed mobile holds and 75% thumb-driven interactions, desktop single-key ergonomics have zero applicability on coarse touch pointers. Similarly, applying `0 ms` austere utility chrome to first-visit signup or checkout funnels eliminates progressive onboarding cues. Route mobile capture and public conversion surfaces to `luke-wroblewski`.

## 7. Adversarial Debate Positions

| Debate ID | Opponent | Conflict Axis | Quantitative Arbitration Rule |
| :--- | :--- | :--- | :--- |
| `dbt-01` | `don-norman` | `keyboard_first_velocity_vs_explicit_discoverability` | `>= 20` actions/day across `>= 4` days/week -> Saarinen keyboard-first + `>= 90%` inline `<kbd>` hints; `< 3` visits/month or sessions `1–3` -> Norman persistent labeled signifiers. |
| `dbt-02` | `ben-shneiderman` | `opinionated_minimal_defaults_vs_flexible_exploratory_control` | `0` regulatory mandatory fields -> Saarinen opinionated defaults (`<= 1` manual required input); `>= 3` compliance-mandated audit fields or multi-party gates -> Shneiderman staged reversible validation. |
| `dbt-03` | `luke-wroblewski` | `desktop_keyboard_density_vs_mobile_thumb_first_ergonomics` | `>= 75%` desktop sessions (`>= 1024px`, `pointer: fine`) -> Saarinen keyboard-first density; `>= 40%` coarse touch sessions (`< 768px`) -> Wroblewski thumb-zone + `>= 44px` controls. |
| `dbt-04` | `rauno-freiberg` | `zero_motion_daily_utility_vs_tactile_spring_physics` | Keyboard-triggered OR `> 50` invocations/day -> Saarinen `0 ms` instant state cut; pointer/gesture-driven AND `< 20` invocations/day -> Freiberg interruptible ease-out/spring physics `<= 180–250 ms`. |

## 8. Primary Source Notes

- **`src-01` (`linear.app/method/introduction`, 2020):** Codifies Linear's opinionated product-building principles—build for creators over managers, purpose-built workflows over generic configurability, automated `n`-week cycles, manageable backlogs, and eliminating administrative busy-work.
- **`src-02` (`linear.app/now/how-we-redesigned-the-linear-ui`, Mar 28, 2024):** Documents the 6-week redesign by a 3-designer core team, migrating from `98` HSL variables to `3` LCH inputs (`base`, `accent`, `contrast`), perceptual lightness uniformity across surface elevations, contrast tuning (`30` vs. `100`), and Inter Display headings.
- **`src-03` (`linear.app/now/a-design-reset`, Mar 27, 2024):** Establishes why visual product experience accrues holistic design debt requiring comprehensive resets every 2–3 years rather than disjointed module-by-module updates.
- **`src-04` (`linear.app/now/rebuilding-delta-sync-read-path`, Aug 18, 2026):** Details Linear's local-first client database eliminating network round-trips on daily actions and its Turbopuffer + Postgres late-enrichment read path handling `> 20 TB` of sync actions (`~1M/day` in largest workspaces) with flat P95/P99 reconnect latency.
- **`src-05` (`linear.app/now/invisible-details`, Sep 17, 2020):** Specifies Linear's 40-line `MouseSafeArea` CSS `clip-path` triangular safe zone preserving diagonal Euclidean paths (`1–2 s` saved across hundreds of daily interactions) and inline shortcut hints in contextual menus.
- **`src-06` (`linear.app/now/styling-linear-for-the-future-stylex`, Aug 26, 2026):** Reports the `> 1,000`-PR migration from `styled-components` to StyleX (`Mar–Aug 2026`), `100+` dynamic LCH variables with nested `ThemeProvider` regeneration, `Oxlint` token enforcement (including thin borders, shadows, animations), `0` runtime navigation CSS injections, `20%–35%` main-thread CPU reduction, and `~30%` mid-tier render speedup.
- **`src-07` (`linear.app/now/sharing-growth-with-the-people-building-linear`, Aug 26, 2026):** Verifies `$100M+` ARR, `40,000+` paying companies, `177%` NRR, `$2.5B` valuation, positive cashflow, `95%` workspace AI-agent installation, `50%` agent-created work share, and `7x` PR-attached issue growth in 2026.
- **`src-08` (Airbnb Design Medium, Aug 6, 2016):** Karri Saarinen's DLS architecture treatise explaining software's absence of physical constraints, self-contained components over arbitrary atomic combinations, 5 artboard categories, and `~50`-screen prototyping in hours.
- **`src-09` (`karrisaarinen.com/posts/designing-coinbase/`, Jun 29, 2016):** Primary record of Coinbase's Merchant Tools (`43,000` merchants), multi-signature Vault UX, and `< 3`-month native iOS/Android rebuild (`4-star` ratings).
- **`src-10` (`linear.app/now/design-for-the-ai-age`, Apr 7, 2025):** Formalizes why generic chat threads fail precision workflows and defines the deterministic UI "workbench" governing AI agent deployment and human approval.
- **`src-11` (`emilkowal.ski/ui/you-dont-need-animations`, 2025):** Codifies the Linear-era motion restraint standard: `0 ms` for keyboard-initiated actions, command palettes, and `>= 100x/day` controls; `<= 180 ms` (`< 300 ms` max) for infrequent overlays.
- **`src-12` (Card, Moran & Newell, *CACM* 1980):** Empirical KLM-GOMS operator constants (`K=0.20s`, `P=1.10s`, `H=0.40s`, `M=1.35s`, `R(t)`) enabling deterministic routine execution-time estimates.
- **`src-13` (Lane et al., *IJHCI* 2005, `DOI:10.1207/s15327590ijhc1802_1`):** Peer-reviewed study finding shortcuts executed `0.659 s` faster than toolbars and `1.484 s` faster than menus yet attracted only `1.59%–6.37%` spontaneous user preference.
- **`src-14` (`github.com/wzhudev/reverse-linear-sync-engine`, 2024):** CTO-endorsed technical dissection of Linear's MobX object pool, IndexedDB `__transactions` queue, microtask batching, monotonic sync IDs, and prior-value server-rejection rollback.
- **`src-15` (Nielsen, *Usability Engineering*, 1993):** Foundational perceptual latency thresholds (`100 ms` direct manipulation, `1,000 ms` flow continuity, `10 s` attention limit).
- **`src-16` (`linear.app/releases/2022`, 2022):** Official Linear Sync Engine release highlighting `50 ms` / `0 ms` instant interactions, `10x` faster initial load times, and elimination of blocking spinners.
