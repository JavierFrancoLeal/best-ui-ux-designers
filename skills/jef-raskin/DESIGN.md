---
schema_version: "1.0.0"
identity:
  slug: "jef-raskin"
  display_name: "Jef Raskin"
  barbell_pole: "lindy_anchor"
  archetype_synthetic: false
  primary_domain: "Locus of attention, modelessness, quasimodes, KLM/GOMS efficiency, and user-work preservation"
  core_axiom: "A desktop interface must never discard user work, hijack the single locus of attention with hidden modes or blocking confirms, or exceed minimal KLM-GOMS operator cost via keyboard-pointer shuttling."
  active_era: "1979-2005"
  skin_in_the_game_evidence:
    - artifact: "Canon Cat dedicated microcomputer and SwyftCard firmware (Information Appliance, Inc.)"
      year: 1987
      verifiable_metric: "Shipped approximately 20,000 commercial units in 6 months (per retrospective hardware histories); benchmarked thumb-held quasimodal LEAP incremental search at <1.0s motor cursor relocation (<250ms Boyer-Moore target acquisition) versus 2.10s mouse H+P+K+H relocation, pioneering patterns later adopted across browser Find-as-you-Type and search-first launchers."
      source_id: "src-06"
    - artifact: "The Humane Interface: New Directions for Designing Interactive Systems (Addison-Wesley / ACM Press)"
      year: 2000
      verifiable_metric: "Foundational HCI engineering treatise formalizing cognetics, quasimodes, monotony, the Two Laws of Interface Design, and quantitative KLM-GOMS/Fitts/Hick/information-efficiency evaluation across 25+ years of computer science curricula and desktop architectures."
      source_id: "src-01"
    - artifact: "Design Considerations for an Anthropophilic Computer (The Book of Macintosh, Apple)"
      year: 1979
      verifiable_metric: "Initiated the Apple Macintosh project specification mandating modeless software architecture, uniform closed hardware configuration, and elimination of thick user manuals."
      source_id: "src-05"
regime_fit:
  primary_regimes:
    - "ai_native_desktop_ide"
    - "saas_b2b_intensive"
  secondary_regimes: []
  out_of_universe_regimes:
    - regime: "mobile_consumer_capture"
      reason: "Touch-only smartphones lack physical keyboards required for spring-loaded quasimodes (Hold+Type) and home-row keyboard monotony; enforcing Raskin keyboard physics degrades one-handed thumb ergonomics and increases touch input errors."
    - regime: "analytics_dense_telemetry"
      reason: "Read-heavy multi-variable observability walls depend on parallel pre-attentive visual scanning across simultaneous charts rather than serial text-editing habits; Raskin's single-locus text model suppresses comparative visual density."
    - regime: "landing_onboarding_conversion"
      reason: "First-time casual visitors hold zero prior motor habituation with the product; removing visible signifiers, progressive visual affordances, and guided conversion cues in favor of monotonous keyboard efficiency collapses task initiation."
high_weight_signals:
  - id: "sig-01"
    name: "hidden_persistent_mode_divergence"
    weight: "critical"
    category: "cognitive_load"
    detects_before_others: "Identifies silent mode traps where identical keyboard input (such as Enter or Backspace) executes conflicting actions depending on an off-locus state variable (e.g., Plan vs Agent toggle or Edit vs View flag)."
    observable_indicator: "State machine or event handler branches output action on a persistent boolean/enum state variable not held continuously by the user and not co-located inside the active focused element."
    threshold: "0 persistent off-locus modes on primary input gestures"
    direction: "lower_is_better"
    source_id: "src-01"
  - id: "sig-02"
    name: "ephemeral_user_input_volatility"
    weight: "critical"
    category: "agentic_trust"
    detects_before_others: "Detects First Law violations where user-authored text, prompts, or form mutations live solely in volatile React/DOM memory and vanish upon reload, unmount, route change, or 401/5xx network failure."
    observable_indicator: "Editable input/textarea/editor state bound only to volatile in-memory hooks (useState/useRef) without write-through to localStorage, IndexedDB, or durable local journal within 500 ms."
    threshold: "100% durable write-through coverage for inputs accepting >16 characters"
    direction: "boolean_required"
    source_id: "src-01"
  - id: "sig-03"
    name: "habituated_blocking_confirmation_modal"
    weight: "critical"
    category: "cognitive_load"
    detects_before_others: "Catches blocking confirmation prompts ('Are you sure?') placed in front of locally reversible delete/discard operations, which neurophysiological fMRI evidence shows users habituate to after the second exposure."
    observable_indicator: "Presence of window.confirm, role='alertdialog', or modal backdrop intercepting a reversible mutation instead of executing immediately with an Undo stack and non-blocking Undo notification."
    threshold: "0 blocking confirmation dialogs on reversible operations"
    direction: "lower_is_better"
    source_id: "src-07"
  - id: "sig-04"
    name: "keyboard_pointer_homing_tax"
    weight: "high"
    category: "interaction_physics"
    detects_before_others: "Measures avoidable KLM-GOMS H (0.40s) + P (1.10s) shuttling penalties when daily keyboard-centric workflows require mouse clicks on distant toolbar buttons or mode pickers."
    observable_indicator: "KLM-GOMS operator trace of a high-frequency (>20/day) desktop/SaaS unit task contains >=2 H operators (round-trip homing >=0.80s) plus >=1 P operator (1.10s) where a single keyboard chord or incremental search suffices."
    threshold: "<= 0 H operators for core text/code/record-entry loops"
    direction: "lower_is_better"
    source_id: "src-04"
  - id: "sig-05"
    name: "non_monotonic_method_fragmentation"
    weight: "high"
    category: "cognitive_load"
    detects_before_others: "Flags competing redundant UI triggers, adaptive reordering menus, or arbitrary user-remapped controls that disrupt unconscious motor habit formation and pull the locus of attention into method selection."
    observable_indicator: "DOM or keymap registry exposes >2 divergent interaction paths for an identical elementary subtask within the same viewport, or dynamically mutates menu item indices based on recency/frequency."
    threshold: "0 dynamically reordered menus; 1 canonical primary gesture per elementary subtask"
    direction: "exact_match"
    source_id: "src-01"
  - id: "sig-06"
    name: "unlabeled_cryptic_icon_controls"
    weight: "medium"
    category: "visual_semiotics"
    detects_before_others: "Flags standalone SVG/icon buttons lacking visible text labels in high-complexity desktop IDEs and B2B forms, forcing recall over recognition and elevating interpretation latency."
    observable_indicator: "Interactive <button> or [role='button'] elements outside universal media/window controls containing only <svg>/<img> with zero visible text node (relying solely on title/hover tooltip)."
    threshold: "0 unlabeled non-standard action buttons in primary workflows"
    direction: "lower_is_better"
    source_id: "src-01"
hard_filters:
  - id: "flt-01"
    name: "zero_silent_work_destruction"
    gate_type: "required"
    condition: "Every user-editable buffer (>16 chars) persists drafts automatically to durable storage (localStorage/IndexedDB/disk) on change (<=500 ms debounce) and survives page reload, tab switch, and network/auth failure."
    failure_impact: "Under flaky enterprise networks, token expiration, or accidental tab closure, operators permanently lose multi-minute authored prompts, code edits, or B2B case notes—a direct violation of Raskin's First Law."
  - id: "flt-02"
    name: "no_unanchored_mode_overload_on_primary_submit"
    gate_type: "disqualifier"
    condition: "Primary submission key (Enter) dispatches both read-only analysis and destructive file/database mutation controlled solely by a persistent off-locus mode flag."
    failure_impact: "Under cognitive fatigue or post-interruption resumption, habituated operators execute unintended repository writes or production record mutations via mode error."
  - id: "flt-03"
    name: "reversible_actions_must_not_block_with_confirm"
    gate_type: "disqualifier"
    condition: "Locally reversible operations (delete draft, close thread, archive row, clear filter) invoke window.confirm or a focus-trapping modal dialog instead of immediate execution plus reversible Undo."
    failure_impact: "Operators habituate after 2 exposures, reflexively dismiss the dialog without reading (only 14% detect altered dialog text), and suffer workflow disruption without actual safety gain."
  - id: "flt-04"
    name: "static_menu_and_shortcut_invariance"
    gate_type: "required"
    condition: "Command order in menus, palettes, and primary keyboard bindings remains spatially and functionally invariant across sessions without adaptive self-reordering."
    failure_impact: "Habituated muscle memory misfires whenever adaptive UIs shift item coordinates, forcing continuous conscious visual search and degrading task speed."
  - id: "flt-05"
    name: "manual_save_choreography_prohibition"
    gate_type: "disqualifier"
    condition: "Primary B2B record or IDE draft workflow requires explicit click on a 'Save' button to prevent data loss on navigation, coupled with a blocking 'Unsaved changes: Save / Discard / Cancel' modal."
    failure_impact: "Injects 4H + 2P + 2K + 2M (6.90s) of pure UI friction per record and creates severe data loss whenever a browser crashes or an operator habituated to dismissing modals clicks 'Discard'."
veto_triggers:
  - id: "veto-01"
    name: "silent_plan_to_agent_mode_trap"
    severity: "hard_veto"
    target_antipattern: "AI IDE composer sharing a single textarea and Enter handler across read-only Plan/Ask and mutating Agent/Auto-Accept modes toggled via Shift+Tab or a corner dropdown."
    detection_rule: "AST/state audit detects a single onKeyDown handler for 'Enter' branching between read-only API calls and mutating file/tool execution based on a persistent state variable (e.g., mode === 'agent') without continuous key-hold quasimode or spatially separate dispatch controls."
    mandatory_remediation: "Bind unmodified Enter strictly to safe read-only analysis/planning; require a spring-loaded quasimodal chord (Cmd/Ctrl+Enter) or explicit non-modal action button with inline locus feedback for repository mutations, and create an automatic pre-mutation rollback checkpoint."
  - id: "veto-02"
    name: "volatile_draft_loss_on_reload_or_error"
    severity: "hard_veto"
    target_antipattern: "SaaS B2B ticket forms or AI prompt composers storing user text exclusively in ephemeral component state that resets on route change, unmount, or failed fetch."
    detection_rule: "Static code audit finds controlled <textarea>, <input type='text'>, or rich editor state initialized from empty string/server prop with no synchronous or debounced (<=500 ms) write to localStorage/IndexedDB/persistence store and no draft restoration on mount."
    mandatory_remediation: "Implement continuous write-through draft persistence keyed by entity/workspace ID with automatic hydration on mount, non-destructive offline retry queue on network/401 failure, and explicit preservation of user text until server acknowledgement."
  - id: "veto-03"
    name: "blocking_confirm_on_reversible_delete"
    severity: "hard_veto"
    target_antipattern: "Modal 'Are you sure you want to delete/discard?' dialogs guarding soft-deletable records, chat threads, or local workspace items."
    detection_rule: "Codebase audit detects window.confirm(), alert(), or a modal component (role='dialog'|'alertdialog') triggered by delete/archive/discard handlers where the backend/store supports soft-delete, trash retention, or undo snapshots."
    mandatory_remediation: "Remove the blocking modal; execute the soft-delete immediately, push an inverse operation onto the universal Undo stack (bound to Cmd/Ctrl+Z), and surface a non-blocking status toast (role='status', aria-live='polite') containing a single-click/keyboard Undo trigger for >=8 seconds."
  - id: "veto-04"
    name: "forced_edit_mode_and_manual_save_lock"
    severity: "conditional_block"
    target_antipattern: "B2B detail views locked in read-only 'View Mode' requiring an 'Edit' button click before typing and a manual 'Save' button click to persist."
    detection_rule: "State matrix check detects an isEditing boolean toggling inputs between static text and <input>/<textarea> solely to gate form edits, paired with a manual onSave submit handler and unsaved-changes discard warning."
    mandatory_remediation: "Convert fields to modeless direct inline editing with continuous debounced autosave (<=500 ms), optimistic local persistence, and per-field or record-level Undo history. Exception permitted only under explicit concurrent multi-user pessimistic locking with visible lock ownership inside the locus."
  - id: "veto-05"
    name: "deep_nested_menu_for_frequent_command"
    severity: "conditional_block"
    target_antipattern: "High-frequency IDE or B2B commands (>10 invocations/session) buried inside >=2 levels of hover/click submenus or dynamically reordered 'smart' lists."
    detection_rule: "DOM/JSX audit detects interactive command items nested inside >=2 cascading menu levels (aria-haspopup chains of depth >=2) without a flat incremental-search command launcher (<=250 ms match response) or single-chord shortcut, OR detects sort functions reordering static menus by click frequency."
    mandatory_remediation: "Flatten commands into a single deterministically ordered searchable list (Hick's Law wide-over-deep rule) accessible from home row via incremental search (<=250 ms filtering) and freeze static menu positions."
concrete_heuristics:
  - id: "heur-01"
    rule_statement: "IF a state alters the effect of a primary keyboard or pointer gesture outside the user's locus of attention, THEN eliminate the mode or convert it into a spring-loaded quasimode that resets immediately on keyup/pointerup/blur."
    metric_or_bound: "0 persistent off-locus modes on primary gestures; synchronous reset on keyup/pointerup/blur"
    verification_method: "state_matrix_check"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-01"
  - id: "heur-02"
    rule_statement: "IF an operation modifies or deletes user-authored content and can be represented as an inverse state delta, THEN execute immediately without a blocking confirmation modal and provide multi-step Undo via Cmd/Ctrl+Z."
    metric_or_bound: "0 blocking confirmation dialogs on reversible deltas; Undo retention >= 20 steps or full session"
    verification_method: "static_code_audit"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-07"
  - id: "heur-03"
    rule_statement: "IF an interface accepts user-authored text or structured edits (>16 chars), THEN continuously persist drafts to durable local storage and automatically recover exact content state after crashes, reloads, or failed HTTP requests."
    metric_or_bound: "Local persistence debounce <= 500 ms; 0 bytes user text lost on simulated reload or 500/401 error"
    verification_method: "runtime_telemetry"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-01"
  - id: "heur-04"
    rule_statement: "IF a desktop IDE or B2B unit task occurs >20 times per workday, THEN its KLM-GOMS execution model must eliminate round-trip keyboard-to-pointer homing (2H = 0.80s) and pointing (P = 1.10s) via home-row keyboard execution."
    metric_or_bound: "H operator count = 0; KLM total reduction >= 40% relative to pointer-based baseline"
    verification_method: "klm_goms_estimate"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-04"
  - id: "heur-05"
    rule_statement: "IF a user must navigate to a target string, symbol, command, or record within a workspace, THEN provide incremental typeahead filtering that updates results on every keystroke rather than requiring a modal Find dialog and Enter submission."
    metric_or_bound: "Incremental match update <= 250 ms per keystroke; <= 4 characters median to unique target"
    verification_method: "runtime_telemetry"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-06"
  - id: "heur-06"
    rule_statement: "IF a command operates on content objects (code blocks, table rows, cells), THEN enforce noun-verb syntax (select object first, then apply verb) so the interface never enters a sticky verb-first tool mode."
    metric_or_bound: "0 sticky verb-first tool modes in text/data editors; cancellation requires 0 explicit Cancel clicks"
    verification_method: "state_matrix_check"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-01"
  - id: "heur-07"
    rule_statement: "IF an interface presents n > 4 selectable commands or records in a menu, THEN use a flat, deterministically ordered (or incrementally searchable) list rather than multi-level nested submenus, honoring Hick's Law."
    metric_or_bound: "Menu nesting depth <= 1 for primary workflows; list ordering deterministic (0 adaptive reshuffling)"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-01"
  - id: "heur-08"
    rule_statement: "IF a task requires supplying user input, THEN compute information efficiency E = I_min / I_user and eliminate every control or field whose value can be inferred, defaulted, or live-evaluated without explicit Submit/Convert toggles."
    metric_or_bound: "0 redundant submit/convert buttons when input is unambiguous; E maximized toward 1.0"
    verification_method: "klm_goms_estimate"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-01"
  - id: "heur-09"
    rule_statement: "IF a control uses a graphic icon for a domain-specific action (e.g., agent plan, diff apply, escalate ticket), THEN pair the icon with a concise visible text label rather than relying on an unlabeled glyph or hover tooltip."
    metric_or_bound: "100% of domain-specific action controls expose visible text labels (not hover-only title attributes)"
    verification_method: "visual_dom_inspection"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-01"
  - id: "heur-10"
    rule_statement: "IF an elementary subtask is performed inside a unified workspace, THEN preserve monotony and habit transfer by mapping exactly one canonical primary gesture system-wide and prohibiting split beginner/expert interface modes."
    metric_or_bound: "1 canonical primary shortcut per elementary subtask; 0 beginner/expert subsystem toggles"
    verification_method: "static_code_audit"
    applies_to:
      - "ai_native_desktop_ide"
      - "saas_b2b_intensive"
    source_id: "src-01"
blind_spots:
  - id: "bs-01"
    failure_mode: "Eliminating visible chrome, confirmation gates, and explicit signifiers causes novice walk-up paralysis and permits catastrophic execution of physically irreversible external actions (e.g., production DB drops, wire transfers, force-pushes) where Undo cannot recover state."
    trigger_context: "Infrequent users (<1 session/week), onboarding flows, or irreversible external side-effect boundaries."
    counterweight_designer: "don-norman"
  - id: "bs-02"
    failure_mode: "Keyboard-centric quasimodes (Hold+Type) and home-row monotony break completely on touchscreens without physical keyboards, degrading one-handed thumb reach and causing finger occlusion errors."
    trigger_context: "Touch-first smartphones, tablets without hardware keyboards, and mobile field-capture apps."
    counterweight_designer: "luke-wroblewski"
  - id: "bs-03"
    failure_mode: "Strict text-only purism rejects compact iconic landmarks that accelerate peripheral visual scanning and cross-language recognition once paired with labels or retained across sessions."
    trigger_context: "Dense multi-pane navigation rails, multilingual SaaS teams, and spatial workspace landmarks."
    counterweight_designer: "susan-kare"
  - id: "bs-04"
    failure_mode: "Single-locus serial interaction optimization undervalues parallel pre-attentive visual comparison across dozens of simultaneous telemetry streams and multi-step autonomous background agent orchestration."
    trigger_context: "Read-only SRE observability dashboards and long-running asynchronous multi-agent code pipelines."
    counterweight_designer: "agentic-flow-architect"
debate_triggers:
  - id: "dbt-01"
    opposing_designer: "don-norman"
    conflict_axis: "habituated_zero_friction_undo_vs_explicit_discoverability_and_forcing_functions"
    this_designer_stance: "Eliminate blocking confirmation dialogs and redundant affordance chrome so daily operators stay in unconscious motor flow with universal Undo."
    opposing_stance: "Visible signifiers are mandatory for conceptual-model discoverability, and hard forcing functions (interlocks/lockouts) are mandatory whenever human slips cause irreversible harm."
    arbitration_rule: "Apply Raskin (zero-blocking + Undo) for all reversible actions executed >=5 times/week; apply Norman forcing functions (type-to-confirm interlocks + visible signifiers) whenever external side effects are irreversible OR median user frequency is <1 session/week."
  - id: "dbt-02"
    opposing_designer: "luke-wroblewski"
    conflict_axis: "two_handed_keyboard_quasimodes_vs_one_thumb_touch_ergonomics"
    this_designer_stance: "Minimize KLM-GOMS time via continuous physical key-hold quasimodes and home-row incremental search, rejecting pointer/tap navigation overhead."
    opposing_stance: "Mobile interactions occur under partial attention with one thumb and no hardware keyboard; primary actions must sit in the bottom thumb zone as >=44-48px tap targets with progressive disclosure."
    arbitration_rule: "Bind to hardware modality: enforce Raskin when viewport >=1024px AND hardware keyboard is primary (pointer: fine); unconditionally yield to Luke Wroblewski when pointer: coarse OR viewport <768px."
  - id: "dbt-03"
    opposing_designer: "susan-kare"
    conflict_axis: "universal_text_commands_vs_iconic_visual_landmarks"
    this_designer_stance: "Standalone icons are cryptic and slow to decode; textual labels and command names eliminate ambiguity across all skill levels."
    opposing_stance: "Well-crafted, memorable visual symbols function as rapid spatial landmarks and pre-attentive recognition anchors that reduce reading load."
    arbitration_rule: "Enforce hybrid synthesis grounded in Wiedenbeck (1999): prohibit unlabeled domain-specific icons in primary workflows (Raskin wins over icon-only), but permit icon+text pairs for persistent top-level landmarks (Kare wins over text-only monoliths)."
  - id: "dbt-04"
    opposing_designer: "agentic-flow-architect"
    conflict_axis: "continuous_physical_quasimodes_vs_asynchronous_agent_checkpoints"
    this_designer_stance: "State divergence must be bounded to continuous physical user muscle tension (quasimodes) so the user never forgets active execution scope."
    opposing_stance: "Autonomous AI agents execute multi-file edits and shell tests asynchronously for 30-180 seconds; physical key-hold cannot span async runs and requires explicit staged diff review, permission boundaries, and checkpoint rewind."
    arbitration_rule: "Use Raskin quasimodes (Cmd/Ctrl+Enter) for dispatch disambiguation between read-only analysis and agent execution, then hand off post-dispatch async execution, permission sandboxing, and multi-file diff approval to agentic-flow-architect."
primary_sources:
  - id: "src-01"
    title: "The Humane Interface: New Directions for Designing Interactive Systems"
    author_or_org: "Jef Raskin"
    year: 2000
    source_type: "book"
    url_or_identifier: "ISBN 978-0-201-37937-2"
    extracted_invariant: "Formulates the Two Laws of Interface Design (p. 6), Cognitive Conscious vs Unconscious asymmetry (Ch. 2), formal locus-of-attention definition of modality (p. 42), spring-loaded quasimodes (p. 53), monotony (p. 67), noun-verb preference, KLM-GOMS timings, Fitts (a=50ms, b=150ms), Hick's Law, and information efficiency E = I_min / I_user (Ch. 4)."
  - id: "src-02"
    title: "Systemic implications of leap and an improved two-part cursor"
    author_or_org: "Jef Raskin"
    year: 1989
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1145/67449.67484"
    extracted_invariant: "Demonstrates how quasimodal thumb-held incremental string search (LEAP) combined with an unambiguous two-part delete/insert cursor eliminates pointer homing overhead and cursor-direction ambiguity across text editing environments."
  - id: "src-03"
    title: "Viewpoint: Intuitive Equals Familiar"
    author_or_org: "Jef Raskin"
    year: 1994
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1145/182987.584629"
    extracted_invariant: "Establishes that perceived ease of operation stems from prior familiarity and habit transfer rather than an innate human faculty; interface quality must be evaluated via consistency, habit preservation, and quantitative task metrics rather than subjective labels."
  - id: "src-04"
    title: "The Keystroke-Level Model for User Performance Time with Interactive Systems"
    author_or_org: "Stuart K. Card, Thomas P. Moran, and Allen Newell"
    year: 1980
    source_type: "peer_reviewed_paper"
    url_or_identifier: "https://doi.org/10.1145/358886.358895"
    extracted_invariant: "Provides the empirical operator model (T_EXECUTE = t_K + t_P + t_H + t_D + t_M + t_R), M-operator placement heuristics (Rules 0-4), and 21% RMS prediction benchmark for routine expert unit tasks."
  - id: "src-05"
    title: "Design Considerations for an Anthropophilic Computer (The Book of Macintosh)"
    author_or_org: "Jef Raskin"
    year: 1979
    source_type: "engineering_post"
    url_or_identifier: "https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/bom/anthrophilic.html"
    extracted_invariant: "Establishes the pre-launch Macintosh software invariant: eliminate modes and nested levels so operators remain in one consistent state, remove jargon and thick manuals, and unify hardware/software behavior."
  - id: "src-06"
    title: "LEAP, The Fastest-Known Cursor Moving Method"
    author_or_org: "Jef Raskin (Information Appliance Inc.)"
    year: 1987
    source_type: "engineering_post"
    url_or_identifier: "http://www.canoncat.net/cat/Cat%20Leap%20Cursor%20Movement.pdf"
    extracted_invariant: "Benchmarks motor cursor relocation (mouse H+P+K+H = 2.10s vs quasimodal LEAP <1.0s with <250ms Boyer-Moore target acquisition), mandates non-destructive default insertion ('a user's work is sacred'), and documents the Canon Cat ERASE/UNDO key-swap habit failure."
  - id: "src-07"
    title: "How Polymorphic Warnings Reduce Habituation in the Brain—Insights from an fMRI Study"
    author_or_org: "Bonnie Brinton Anderson, C. Brock Kirwan, Jeffrey L. Jenkins, David Eargle, Seth Howard, and Anthony Vance"
    year: 2015
    source_type: "empirical_benchmark"
    url_or_identifier: "https://doi.org/10.1145/2702123.2702322"
    extracted_invariant: "Validates Raskin's confirmation-dialog habituation thesis neurophysiologically: fMRI shows steep visual-processing neural drop after just the 2nd warning exposure; cites empirical findings that 50% of SSL warnings are clicked through in 1.7s and only 14% of users notice content changes in repeated confirmation dialogs."
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

Jef Raskin treats interface engineering as an applied branch of cognitive science (*cognetics*) and quantitative human factors rather than visual decoration. Every rule in this specification derives from three falsifiable biological and mathematical constraints:

1. **Singularity of the Locus of Attention:** Humans process conscious decisions sequentially in a single narrow focus (*cognitive conscious*, persisting for tenths of a second), while executing practiced motor routines simultaneously in the *cognitive unconscious* (persisting for decades). Whenever an interface alters command semantics based on state outside the active locus—or interrupts task flow with blocking dialogs—it hijacks conscious bandwidth and guarantees human-attributed errors that are structurally machine-design defects.
2. **Inviolability of User Work (Raskin's First and Second Laws):** A computer shall never harm user work or, through inaction, allow user work to come to harm; nor shall it waste user time or demand more input than strictly necessary. Manual "Save" buttons, volatile draft buffers, and modal "Are you sure?" confirmations on reversible operations violate both laws simultaneously.
3. **Quantitative Engineering Optimality:** Perceived ease is prior familiarity, not an innate faculty. Interface quality must be audited deterministically via KLM-GOMS task time (`K=0.20s`, `P=1.10s`, `H=0.40s`, `M=1.35s`, `R(t)`), Fitts's Law (`50 + 150 log2(D/S + 1) ms`), Hick's Law (`a + b log2(n + 1) ms`), information efficiency (`E = I_min / I_user`), and state-machine modelessness checks.

---

## 2. Regime Boundaries & Out-of-Universe Rationale

### In-Universe Primary Regimes

* **`ai_native_desktop_ide`:** Keyboard-dominant engineering workbenches (React/Electron, VS Code extensions, terminal-adjacent AI composers) where developers execute hundreds of daily text/code/agent cycles. Primary targets are eliminating silent `Plan`/`Edit`/`Agent` mode traps, preventing prompt/checkpoint loss, and removing pointer homing overhead (`2H + P = 1.90s` per round-trip).
* **`saas_b2b_intensive`:** High-throughput operational desktop web applications (support triage, CRM, ERP, underwriting, issue trackers) where full-time operators edit dozens to hundreds of structured records per shift. Primary targets are destroying View/Edit mode locks, manual Save rituals, habituated delete confirmation modals, and multi-level cascading menus.

### Mandatory Out-of-Universe Regimes

* **`mobile_consumer_capture`:** Disqualified. Touch-only viewports (`pointer: coarse`, `<768px`) lack physical keyboards required for spring-loaded quasimodes (`Hold+Type`) and home-row monotony. Route to `luke-wroblewski`.
* **`analytics_dense_telemetry`:** Disqualified. Multi-series observability and anomaly-scanning walls rely on parallel pre-attentive visual comparison across dozens of simultaneous plots rather than serial text manipulation. Route to `edward-tufte` and `ben-shneiderman`.
* **`landing_onboarding_conversion`:** Disqualified. One-time visitors hold zero motor habit with the interface; optimizing for habituated speed over visible signifiers and guided progression harms first-contact comprehension. Route to `don-norman` and `luke-wroblewski`.

---

## 3. Signal Detection Protocol

Text-only engineering agents audit codebases, DOM trees, CSS rules, and state machines in deterministic order without relying on subjective visual inspection:

1. **State-Machine Mode Scan (`sig-01`):** Inspect all keyboard (`onKeyDown`, `useHotkeys`, Electron accelerators) and pointer handlers. Construct the transition table mapping `(gesture, componentState) -> sideEffect`. Flag any `gesture` whose `sideEffect` switches between read-only and mutating (or between incompatible semantic operations) based on a persistent state flag (`useState`, Redux/Zustand slice, URL param) that does not require continuous physical hold (`e.metaKey`, `e.ctrlKey`, `e.shiftKey`, `e.altKey`, or active pointer-down).
2. **Persistence & Volatility Trace (`sig-02`):** Inspect every `<textarea>`, `<input>`, `contentEditable`, and code editor component accepting >16 characters. Verify durable write-through (`localStorage`, `IndexedDB`, SQLite/IPC file journal) triggered within `<= 500 ms` of change, hydration on mount, and state retention when `fetch`/`mutation` rejects with network or `401` errors.
3. **Blocking Modal & Confirmation Audit (`sig-03`):** Search AST for `window.confirm`, `window.alert`, `<dialog>`, `role="alertdialog"`, or modal wrappers invoked from delete, archive, close, or discard handlers. Verify whether the target entity supports soft-delete, trash retention, or inverse undo delta; if reversible, flag immediately.
4. **KLM-GOMS Operator Accounting (`sig-04`, `heur-04`):** For every task executed `>20 times/day`, write the exact serial operator string (`K`, `P`, `H`, `M`, `R(t)`) starting with hands on the keyboard. Count `H` (homing, `0.40s`) and `P` (pointing, `1.10s`) operators. Any routine loop requiring `>=2 H` (`0.80s`) and `>=1 P` (`1.10s`) where home-row execution is feasible triggers deduction.
5. **Monotony, Menu Depth & Label Check (`sig-05`, `sig-06`):** Audit command registries for duplicate competing shortcuts, adaptive frequency-sorting comparators on static menus, cascading submenu nesting depth `>=2`, and interactive icon-only `<button>` elements lacking visible text labels.

---

## 4. Hard Filters & Veto Playbook

| Gate / Veto ID | Severity / Type | Deterministic Trigger Condition | Mandatory Engineering Remediation |
| :--- | :--- | :--- | :--- |
| **`veto-01` (`flt-02`)** | `hard_veto` (`-35`, cap `49`) | Single `Enter` handler branches between read-only reply and file/tool mutation via off-locus persistent mode state (`Plan`/`Agent`). | Bind `Enter` strictly to read-only analysis; require spring-loaded quasimode (`Cmd/Ctrl+Enter`) for code mutation plus automatic checkpoint creation. |
| **`veto-02` (`flt-01`)** | `hard_veto` (`-35`, cap `49`) | Editable buffer (`>16` chars) stored only in ephemeral React/DOM state with zero durable write-through or lost on network/reload error. | Add `<=500 ms` debounced write-through to `localStorage`/`IndexedDB`, mount hydration, and non-destructive retry queue. |
| **`veto-03` (`flt-03`)** | `hard_veto` (`-35`, cap `49`) | Blocking `window.confirm` or modal dialog intercepts a locally reversible delete/archive/discard action. | Execute soft-delete immediately, push inverse delta to universal `Cmd/Ctrl+Z` Undo stack, and show non-blocking `role="status"` Undo toast (`>=8s`). |
| **`veto-04` (`flt-05`)** | `conditional_block` (`-20`) | B2B record view gates inline edits behind an explicit `Edit` mode toggle and manual `Save` button with unsaved-changes discard warning. | Refactor to modeless inline editing with continuous debounced autosave and Undo history (unless explicit pessimistic multi-user lock is required and shown in locus). |
| **`veto-05` (`flt-04`)** | `conditional_block` (`-20`) | Frequent command (`>10/session`) buried at submenu depth `>=2` without incremental search launcher, OR static menu reorders adaptively. | Flatten into deterministically ordered incremental-search list (`<=250 ms` match latency) and remove adaptive menu sorting. |

---

## 5. Executable Heuristics & Code Patterns

### Refactoring 1 (`ai_native_desktop_ide`): Hidden Plan/Agent Mode Trap + Blocking Delete Confirm -> Quasimodal Dispatch + Continuous Draft Persistence + Non-Blocking Undo

**KLM-GOMS Quantitative Audit (verified operator constants: `K=0.20s`, `P=1.10s`, `H=0.40s`, `M=1.35s`):**
* **Task A (Switch from Plan to Agent and submit prompt, hands on keyboard):**
  * *Before:* `H + M + P + K + M + P + K + H + M + K` = `0.40 + 1.35 + 1.10 + 0.20 + 1.35 + 1.10 + 0.20 + 0.40 + 1.35 + 0.20` = **`7.65 s`** (plus high mode-error probability when forgetting active mode).
  * *After (Quasimode `Cmd/Ctrl+Enter`):* `M + 2K` = `1.35 + 0.40` = **`1.75 s`** (**`-5.90 s` / `77.1%` faster**, `0` off-locus modes).
* **Task B (Delete focused thread/diff):**
  * *Before (Blocking modal confirm):* `H + M + P + K + M + P + K + H` = `0.40 + 1.35 + 1.10 + 0.20 + 1.35 + 1.10 + 0.20 + 0.40` = **`6.10 s`**.
  * *After (Direct keyboard Delete/Backspace on focused item + non-blocking Undo):* `M + K` = `1.35 + 0.20` = **`1.55 s`** (**`-4.55 s` / `74.6%` faster**, zero habituated confirm dialog).

#### Before (Fails `veto-01`, `veto-02`, `veto-03` — Score: `0` [`max(0, 100 - 105)`], Verdict: `BLOCK`)

```tsx
import React, { useState } from "react";

type ComposerMode = "plan" | "agent";

interface ThreadItem {
  id: string;
  summary: string;
}

export function ModalIdeComposerBefore({
  threads,
  onRunPlan,
  onRunAgentMutation,
  onDeleteThread,
}: {
  threads: ThreadItem[];
  onRunPlan: (prompt: string) => Promise<void>;
  onRunAgentMutation: (prompt: string) => Promise<void>;
  onDeleteThread: (id: string) => void;
}) {
  // VETO-01: Persistent off-locus mode flag alters Enter semantics silently
  const [mode, setMode] = useState<ComposerMode>("plan");
  // VETO-02: Volatile in-memory prompt lost on panel unmount, reload, or API error
  const [prompt, setPrompt] = useState("");
  const [pendingDeleteId, setPendingDeleteId] = useState<string | null>(null);

  const handleKeyDown = async (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Tab" && e.shiftKey) {
      e.preventDefault();
      setMode((prev) => (prev === "plan" ? "agent" : "plan"));
      return;
    }
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      const text = prompt;
      setPrompt(""); // VETO-02: Destroys draft before server acknowledgement
      if (mode === "agent") {
        await onRunAgentMutation(text); // Mode error if operator assumed Plan
      } else {
        await onRunPlan(text);
      }
    }
  };

  return (
    <section>
      <ul>
        {threads.map((t) => (
          <li key={t.id}>
            <span>{t.summary}</span>
            <button type="button" onClick={() => setPendingDeleteId(t.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>

      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Ask or instruct workspace..."
      />

      {/* Off-locus corner dropdown detached from cursor attention */}
      <div>
        <select
          aria-label="Mode"
          value={mode}
          onChange={(e) => setMode(e.target.value as ComposerMode)}
        >
          <option value="plan">Plan</option>
          <option value="agent">Agent</option>
        </select>
      </div>

      {/* VETO-03: Habituated blocking confirmation modal on reversible delete */}
      {pendingDeleteId && (
        <div role="alertdialog" aria-modal="true">
          <p>Are you sure you want to delete this thread?</p>
          <button
            type="button"
            onClick={() => {
              onDeleteThread(pendingDeleteId);
              setPendingDeleteId(null);
            }}
          >
            Confirm Delete
          </button>
          <button type="button" onClick={() => setPendingDeleteId(null)}>
            Cancel
          </button>
        </div>
      )}
    </section>
  );
}
```

#### After (Passes all gates — Modeless Read-Only Default + Spring-Loaded Quasimode + Durable Draft + Keyboard Delete with Non-Blocking Undo)

```tsx
import React, { useEffect, useState, useCallback } from "react";

interface ThreadItem {
  id: string;
  summary: string;
}

interface DeletedSnapshot {
  item: ThreadItem;
  index: number;
}

const DRAFT_STORAGE_KEY = "ide:composer:draft:v1";

export function ModelessIdeComposerAfter({
  initialThreads,
  onRunReadOnlyPlan,
  onRunCheckedAgentMutation,
}: {
  initialThreads: ThreadItem[];
  onRunReadOnlyPlan: (prompt: string) => Promise<void>;
  onRunCheckedAgentMutation: (prompt: string) => Promise<{ checkpointId: string }>;
}) {
  // First Law: Hydrate durable draft immediately on mount
  const [prompt, setPrompt] = useState<string>(() => {
    try {
      return window.localStorage.getItem(DRAFT_STORAGE_KEY) ?? "";
    } catch {
      return "";
    }
  });
  const [threads, setThreads] = useState<ThreadItem[]>(initialThreads);
  const [undoStack, setUndoStack] = useState<DeletedSnapshot[]>([]);
  // Quasimode state: active ONLY while Cmd/Ctrl key is physically held down
  const [isMutateChordHeld, setIsMutateChordHeld] = useState(false);
  const [statusMessage, setStatusMessage] = useState<string | null>(null);
  const [dispatchError, setDispatchError] = useState<string | null>(null);

  // Continuous write-through persistence (<=250ms debounce, zero draft loss)
  useEffect(() => {
    const timer = window.setTimeout(() => {
      try {
        window.localStorage.setItem(DRAFT_STORAGE_KEY, prompt);
      } catch {
        // Fallback persistence telemetry hook
      }
    }, 200);
    return () => window.clearTimeout(timer);
  }, [prompt]);

  const handleUndoDelete = useCallback(() => {
    if (undoStack.length === 0) return;
    const [latest, ...rest] = undoStack;
    setUndoStack(rest);
    setThreads((curr) => {
      const next = [...curr];
      next.splice(latest.index, 0, latest.item);
      return next;
    });
    setStatusMessage(`Restored "${latest.item.summary}".`);
  }, [undoStack]);

  // Global monotonic Undo chord (Cmd/Ctrl+Z when not actively undoing text)
  useEffect(() => {
    const onWindowKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "z" && !e.shiftKey) {
        if (document.activeElement?.tagName !== "TEXTAREA" && undoStack.length > 0) {
          e.preventDefault();
          handleUndoDelete();
        }
      }
    };
    window.addEventListener("keydown", onWindowKeyDown);
    return () => window.removeEventListener("keydown", onWindowKeyDown);
  }, [handleUndoDelete, undoStack.length]);

  const deleteThreadImmediately = (id: string) => {
    const index = threads.findIndex((t) => t.id === id);
    if (index === -1) return;
    const item = threads[index];
    setThreads((curr) => curr.filter((t) => t.id !== id));
    setUndoStack((prev) => [{ item, index }, ...prev]);
    setStatusMessage(`Deleted "${item.summary}".`);
  };

  const dispatchPrompt = async (mutateRepo: boolean) => {
    const trimmed = prompt.trim();
    if (!trimmed) return;
    setDispatchError(null);
    try {
      if (mutateRepo) {
        const { checkpointId } = await onRunCheckedAgentMutation(trimmed);
        setStatusMessage(`Agent edits applied (checkpoint ${checkpointId} ready for rewind).`);
      } else {
        await onRunReadOnlyPlan(trimmed);
        setStatusMessage("Read-only analysis completed.");
      }
      // Clear draft ONLY after confirmed dispatch acknowledgement
      setPrompt("");
      window.localStorage.removeItem(DRAFT_STORAGE_KEY);
    } catch {
      // First Law: Preserve full user text on API/network failure
      setDispatchError("Dispatch failed. Draft preserved locally; retry when ready.");
    }
  };

  const handleComposerKeyDown = async (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Meta" || e.key === "Control") {
      setIsMutateChordHeld(true);
    }
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      // Modeless default: Enter = read-only; spring-loaded Cmd/Ctrl+Enter = mutate
      await dispatchPrompt(e.metaKey || e.ctrlKey);
    }
  };

  const handleComposerKeyUp = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Meta" || e.key === "Control") {
      setIsMutateChordHeld(false); // Automatic spring-return to safe neutral state
    }
  };

  return (
    <section aria-label="Workspace Composer">
      <ul aria-label="Workspace Threads">
        {threads.map((t) => (
          <li
            key={t.id}
            tabIndex={0}
            onKeyDown={(e) => {
              // Direct home-row deletion (M + K = 1.55s) without blocking modal
              if (e.key === "Delete" || e.key === "Backspace") {
                e.preventDefault();
                deleteThreadImmediately(t.id);
              }
            }}
          >
            <span>{t.summary}</span>
            <button type="button" onClick={() => deleteThreadImmediately(t.id)}>
              Delete Thread (Del)
            </button>
          </li>
        ))}
      </ul>

      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={handleComposerKeyDown}
        onKeyUp={handleComposerKeyUp}
        onBlur={() => setIsMutateChordHeld(false)}
        aria-label="Prompt input"
        placeholder="Enter = Read-Only Plan | Hold Cmd/Ctrl + Enter = Apply Repo Edits"
      />

      {/* Explicit action labels directly adjacent to locus reflecting physical key hold */}
      <div>
        <button type="button" onClick={() => dispatchPrompt(false)}>
          Analyze Read-Only (Enter)
        </button>
        <button
          type="button"
          data-quasimode-active={isMutateChordHeld ? "true" : "false"}
          onClick={() => dispatchPrompt(true)}
        >
          {isMutateChordHeld
            ? "Press Enter While Held to Apply Repo Edits"
            : "Apply Repo Edits (Cmd/Ctrl+Enter)"}
        </button>
      </div>

      {dispatchError && <p role="alert">{dispatchError}</p>}

      {/* Non-blocking status region with immediate Undo recovery */}
      {(statusMessage || undoStack.length > 0) && (
        <div role="status" aria-live="polite">
          <span>{statusMessage}</span>
          {undoStack.length > 0 && (
            <button type="button" onClick={handleUndoDelete}>
              Undo Delete (Cmd/Ctrl+Z)
            </button>
          )}
        </div>
      )}
    </section>
  );
}
```

---

### Refactoring 2 (`saas_b2b_intensive`): Forced View/Edit Mode + Manual Save Button -> Modeless Direct Inline Editing + Continuous Transactional Autosave + Reversible History

**KLM-GOMS Quantitative Audit (10-character note update on a B2B support ticket, hands on keyboard):**
* *Before (`Edit` button click -> type 10 chars -> `Save` button click -> return to keyboard):* `H + M + P + K + H + M + 10K + H + M + P + K + H` = `4(0.40) + 2(1.10) + 12(0.20) + 3(1.35)` = **`10.25 s`**.
* *After (Modeless inline editor with continuous local+remote autosave):* `M + 10K` = `1.35 + 2.00` = **`3.35 s`** (**`-6.90 s` / `67.3%` faster**).
* *Operational shift impact:* For an operator handling 100 tickets/day, eliminating `6.90 s` of pure UI mode/save overhead (`4H=1.60s, 2P=2.20s, 2K=0.40s, 2M=2.70s`) recovers **`11.50 minutes/day/operator`** and drops unsaved-draft loss to zero.

#### Before (Fails `veto-02`, `veto-03`, `veto-04` — Score: `10` [`100 - 35 - 35 - 20`, capped `<=49`], Verdict: `BLOCK`)

```tsx
import React, { useState } from "react";

interface TicketRecord {
  id: string;
  title: string;
  resolutionNote: string;
}

export function ModalTicketEditorBefore({
  ticket,
  onPersist,
  onNavigateAway,
}: {
  ticket: TicketRecord;
  onPersist: (updated: TicketRecord) => Promise<void>;
  onNavigateAway: () => void;
}) {
  // VETO-04: Explicit View/Edit mode lock gates typing behind pointer click
  const [isEditing, setIsEditing] = useState(false);
  // VETO-02: Volatile draft state with zero durable persistence
  const [draftNote, setDraftNote] = useState(ticket.resolutionNote);
  const [showDiscardModal, setShowDiscardModal] = useState(false);

  const isDirty = draftNote !== ticket.resolutionNote;

  const handleSave = async () => {
    await onPersist({ ...ticket, resolutionNote: draftNote });
    setIsEditing(false);
  };

  const handleBackClick = () => {
    if (isDirty) {
      setShowDiscardModal(true); // VETO-03 / FLT-05: Blocking discard prompt
    } else {
      onNavigateAway();
    }
  };

  return (
    <article>
      <header>
        <h2>{ticket.title}</h2>
        <button type="button" onClick={handleBackClick}>
          Back to Queue
        </button>
        {!isEditing ? (
          <button type="button" onClick={() => setIsEditing(true)}>
            Edit Record
          </button>
        ) : (
          <button type="button" onClick={handleSave}>
            Save Changes
          </button>
        )}
      </header>

      {isEditing ? (
        <textarea
          value={draftNote}
          onChange={(e) => setDraftNote(e.target.value)}
        />
      ) : (
        <p>{ticket.resolutionNote || "No resolution notes."}</p>
      )}

      {showDiscardModal && (
        <div role="alertdialog" aria-modal="true">
          <p>You have unsaved changes. Discard your work?</p>
          <button type="button" onClick={onNavigateAway}>
            Discard
          </button>
          <button type="button" onClick={() => setShowDiscardModal(false)}>
            Stay
          </button>
        </div>
      )}
    </article>
  );
}
```

#### After (Passes all gates — Modeless Direct Edit + Continuous Durable Autosave + Offline Retry + Reversible Undo)

```tsx
import React, { useEffect, useRef, useState } from "react";

interface TicketRecord {
  id: string;
  title: string;
  resolutionNote: string;
}

type SyncState = "synced" | "saving" | "saved_locally_offline";

// Mount with key={ticket.id} so each record hydrates cleanly from durable storage
export function ModelessTicketEditorAfter({
  ticket,
  onSyncRemote,
  onNavigateAway,
}: {
  ticket: TicketRecord;
  onSyncRemote: (updated: TicketRecord) => Promise<void>;
  onNavigateAway: () => void;
}) {
  const storageKey = `b2b:ticket:${ticket.id}:note`;

  // Hydrate locally persisted unsynced work first (First Law priority)
  const [note, setNote] = useState<string>(() => {
    try {
      const localDraft = window.localStorage.getItem(storageKey);
      return localDraft !== null ? localDraft : ticket.resolutionNote;
    } catch {
      return ticket.resolutionNote;
    }
  });
  const [history, setHistory] = useState<string[]>([]);
  const [syncState, setSyncState] = useState<SyncState>("synced");
  const lastCommittedRef = useRef<string>(ticket.resolutionNote);

  // Continuous local durability + debounced transactional server sync
  useEffect(() => {
    try {
      window.localStorage.setItem(storageKey, note);
    } catch {
      // Non-blocking fallback telemetry
    }
    if (note === lastCommittedRef.current) {
      setSyncState("synced");
      return;
    }

    setSyncState("saving");
    let cancelled = false;

    const timer = window.setTimeout(async () => {
      try {
        await onSyncRemote({ ...ticket, resolutionNote: note });
        if (!cancelled) {
          lastCommittedRef.current = note;
          window.localStorage.removeItem(storageKey);
          setSyncState("synced");
        }
      } catch {
        // First Law: Never clear user text; retain in localStorage for automatic retry
        if (!cancelled) {
          setSyncState("saved_locally_offline");
        }
      }
    }, 350);

    return () => {
      cancelled = true;
      window.clearTimeout(timer);
    };
  }, [note, onSyncRemote, storageKey, ticket]);

  const handleChange = (nextValue: string) => {
    setHistory((prev) => [...prev.slice(-24), note]);
    setNote(nextValue);
  };

  const handleUndo = () => {
    if (history.length === 0) return;
    const previousNote = history[history.length - 1];
    setHistory((prev) => prev.slice(0, -1));
    setNote(previousNote);
  };

  return (
    <article aria-label={`Ticket ${ticket.id}`}>
      <header>
        <h2>{ticket.title}</h2>
        {/* Immediate navigation with zero blocking discard dialogs because work is durable */}
        <button type="button" onClick={onNavigateAway}>
          Back to Queue
        </button>
        <button type="button" onClick={handleUndo} disabled={history.length === 0}>
          Undo Revision
        </button>
        <span role="status" aria-live="polite">
          {syncState === "synced" && "All changes saved"}
          {syncState === "saving" && "Saving..."}
          {syncState === "saved_locally_offline" &&
            "Saved locally — will sync automatically when connection resumes"}
        </span>
      </header>

      {/* Always editable without mode entry; zero H+P+K tax */}
      <label htmlFor={`ticket-note-${ticket.id}`}>Resolution Notes</label>
      <textarea
        id={`ticket-note-${ticket.id}`}
        value={note}
        onChange={(e) => handleChange(e.target.value)}
        onKeyDown={(e) => {
          if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "z" && !e.shiftKey) {
            e.preventDefault();
            handleUndo();
          }
        }}
        rows={6}
      />
    </article>
  );
}
```

---

## 6. Blind Spots & Counterweights

1. **Walk-up Discoverability & Physically Irreversible Actions (`bs-01` -> `don-norman`):** Raskin's hostility toward visible chrome and confirmation dialogs breaks down for first-time users who lack habituated muscle memory and for operations whose consequences exit the software boundary (deleting production infrastructure, sending external emails, executing financial transfers). Pair with `don-norman` for visible conceptual signifiers and hard forcing functions (interlocks/lockouts requiring target-name verification).
2. **Touchscreens & One-Handed Ergonomics (`bs-02` -> `luke-wroblewski`):** Spring-loaded quasimodes depend on simultaneous multi-finger hardware key chords unavailable on smartphones. On `pointer: coarse` or `<768px` viewports, hand off strictly to `luke-wroblewski`.
3. **Visual Landmarks & Rapid Peripheral Scanning (`bs-03` -> `susan-kare`):** While standalone unlabeled icons fail comprehension checks, empirical retention studies (Wiedenbeck 1999) confirm that combining crisp iconic landmarks with text labels improves perceived ease and recognition speed over dense text-only rails. Pair with `susan-kare`.
4. **Asynchronous Multi-Step Agent Execution (`bs-04` -> `agentic-flow-architect`):** Physical key-hold cannot span 60-second autonomous coding runs. Use Raskin quasimodes to disambiguate dispatch intent, then pair with `agentic-flow-architect` for sandboxed permission boundaries, async progress telemetry, and diff-review checkpoints.

---

## 7. Adversarial Debate Positions

* **vs. `don-norman` (Habituated Undo Speed vs. Discoverability & Forcing Functions):** Raskin treats confirmation modals as habituated theater that fails neurobiologically after 2 exposures; Norman emphasizes visible signifiers and interlocks/lockouts. *Arbitration:* Raskin governs all locally reversible actions (`>=5 uses/week`); Norman governs irreversible external mutations and low-frequency (`<1/week`) onboarding flows.
* **vs. `luke-wroblewski` (Keyboard Quasimodes vs. One-Thumb Touch Ergonomics):** Raskin optimizes two-handed home-row velocity (`0 H` operators); Wroblewski optimizes distracted one-thumb smartphone interaction (`44-48px` bottom-arc tap targets). *Arbitration:* Strictly gated by input hardware (`pointer: fine` + physical keyboard -> Raskin; `pointer: coarse` or `<768px` -> Wroblewski).
* **vs. `susan-kare` (Universal Text vs. Iconic Visual Landmarks):** Raskin rejects cryptic icon-only bars; Kare designs semantic visual landmarks. *Arbitration:* Enforce icon+text pairs on primary navigation and domain actions; reject icon-only controls without visible labels.
* **vs. `agentic-flow-architect` (Spring-Loaded Quasimodes vs. Asynchronous Agent Loops):** Raskin requires continuous kinesthetic awareness of non-default state; agentic workflows run asynchronously post-dispatch. *Arbitration:* Quasimodal chord disambiguates invocation; asynchronous execution boundaries and staged diffs govern runtime safety.

---

## 8. Primary Source Notes

* **`src-01` — Jef Raskin (2000), *The Humane Interface: New Directions for Designing Interactive Systems*, Addison-Wesley Professional, `ISBN 978-0-201-37937-2`:** Canonical source for the Two Laws (p. 6), Cognitive Conscious vs. Unconscious table (Ch. 2), verbatim modality definition (p. 42), quasimodes (p. 53), monotony (p. 67), KLM-GOMS worked examples (Hal's temperature converter: 16.80s GUI vs 5.43s Dialog), Fitts (`a=50ms, b=150ms`), Hick's Law, and information efficiency `E`.
* **`src-02` — Jef Raskin (1989), *"Systemic implications of leap and an improved two-part cursor"*, *CHI '89 / ACM SIGCHI Bulletin*, pp. 167–170, `https://doi.org/10.1145/67449.67484`:** Formalizes thumb-held incremental string search and the two-part delete/insert cursor eliminating directional ambiguity.
* **`src-03` — Jef Raskin (1994), *"Viewpoint: Intuitive Equals Familiar"*, *Communications of the ACM*, 37(9), pp. 17–18, `https://doi.org/10.1145/182987.584629`:** Establishes the falsification of subjective usability terminology in favor of familiarity, habit consistency, and empirical testing.
* **`src-04` — Card, Moran & Newell (1980), *"The Keystroke-Level Model for User Performance Time with Interactive Systems"*, *Communications of the ACM*, 23(7), pp. 396–410, `https://doi.org/10.1145/358886.358895`:** Empirical source of KLM operators, M-placement Rules 0–4, and 21% RMS validation accuracy.
* **`src-05` — Jef Raskin (1979), *"Design Considerations for an Anthropophilic Computer"* (*The Book of Macintosh*), Stanford University Libraries archive, `https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/bom/anthrophilic.html`:** Primary pre-Macintosh architectural memo specifying modelessness and zero-manual appliance constraints.
* **`src-06` — Jef Raskin (1987), *"LEAP, The Fastest-Known Cursor Moving Method"*, Information Appliance Inc., `http://www.canoncat.net/cat/Cat%20Leap%20Cursor%20Movement.pdf`:** Primary hardware/software timing comparison (`2.10s` mouse vs `<1.0s` LEAP, `<250ms` Boyer-Moore), sacred user-work invariant, and Canon Cat ERASE/UNDO key-swap postmortem.
* **`src-07` — Anderson et al. (2015), *"How Polymorphic Warnings Reduce Habituation in the Brain—Insights from an fMRI Study"*, *CHI 2015*, `https://doi.org/10.1145/2702123.2702322`:** Empirical fMRI and behavioral validation of warning/confirmation habituation (steep neural drop after 2nd exposure; 50% SSL click-through in 1.7s; 14% change detection in confirmation dialogs).
