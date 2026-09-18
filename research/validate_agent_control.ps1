$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$nextActionPath = Join-Path $PSScriptRoot 'NEXT_ACTION.json'
$statePath = Join-Path $PSScriptRoot 'AGENT_STATE.md'
$policyPath = Join-Path $PSScriptRoot 'AGENT_POLICY.md'
$rootPolicyPath = Join-Path $repoRoot 'AGENTS.md'
$contractPath = Join-Path $PSScriptRoot 'G4_05_MODEL_SPECIFICATION_CONTRACT.json'

foreach ($path in @($nextActionPath, $statePath, $policyPath, $rootPolicyPath, $contractPath)) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing control artifact: $path" }
}

$next = Get-Content -Raw -LiteralPath $nextActionPath | ConvertFrom-Json
if ($null -eq $next.action) { throw 'NEXT_ACTION must contain exactly one action object.' }
if ($next.action -is [System.Array]) { throw 'NEXT_ACTION action must not be an array.' }
if ([string]::IsNullOrWhiteSpace([string]$next.action.action_id)) { throw 'NEXT_ACTION action_id is required.' }

$state = Get-Content -Raw -LiteralPath $statePath
if ($state -notmatch 'CORE-DATASET-FREEZE-V1') { throw 'Agent state lacks the frozen dataset ID.' }
if ($state -notmatch '3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616') { throw 'Agent state lacks the frozen root fingerprint.' }
if ($state -notmatch 'SEALED') { throw 'Agent state does not preserve the held-out seal.' }

$contract = Get-Content -Raw -LiteralPath $contractPath | ConvertFrom-Json
$allowedGates = @(
    'DENIED_UNTIL_ALL_BINDINGS_FROZEN_AND_RESEARCHER_AUTHORIZED',
    'AUTHORIZED_2015_2019_INNER_ONLY_AFTER_PROTOCOL_PUBLICATION_AND_C04_A_VALIDATION',
    'PAUSED_PAIR_UNIVERSE_FORMATION_RULE_NOT_FROZEN',
    'PAUSED_C06_AVAILABILITY_TIME_CONTRACT_MISMATCH',
    'C06_AVAILABILITY_AMENDMENT_ACTIVE_NO_EMPIRICAL_ACCESS',
    'C06_AMENDMENT_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'PAUSED_EXECUTABLE_SEMANTICS_NOT_CLOSED'
    ,'EXEC_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'PAUSED_PAIRA_R4_COMPUTATIONAL_FEASIBILITY'
    ,'R4_CONDITIONAL_CONTRACT_PENDING_PUBLICATION'
    ,'CF_A_PASSED_PENDING_DISPOSITION_PUBLICATION'
    ,'PAUSED_A6_TRAINING_GEOMETRY_NOT_FROZEN'
    ,'A6_TG_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'PAUSED_DECISION_CADENCE_EPISODE_ADMISSION_NOT_FROZEN'
    ,'DC_A_EP_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'PAUSED_DIRECTIONAL_EPISODE_COLLISION_NOT_FROZEN'
    ,'DECA_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'PAUSED_A6_C06_STALE_GAP_INDICATOR_NOT_FROZEN'
    ,'SG_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'PAUSED_A5_RT3_RELATIONSHIP_STATE_NOT_MATERIALIZED'
    ,'RT3_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'RT3_A_STATE_AUGMENTATION_ACTIVE_NO_INTERPRETATION'
    ,'PAUSED_MP1_PIT_REFERENCE_WINDOW_NOT_FROZEN'
    ,'MP1_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'PAUSED_MP1_EXECUTABLE_INTERFACE_CONFLICT'
    ,'MP1_I_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION'
    ,'EXECUTABLE_UNRESOLVED_FIELD_SCAN_ACTIVE_NO_EMPIRICAL_ACCESS'
    ,'PAUSED_CONSOLIDATED_EXECUTABLE_FIELD_SEMANTICS'
    ,'EV_A_V1_FD_A_ER_A_QUALIFIED_PENDING_PUBLICATION'
    ,'PAUSED_EV_A_ROW_LEVEL_MAPPING_NOT_BOUND'
    ,'EV_MAP_B_QUALIFIED_PENDING_PUBLICATION'
    ,'PRE_OUTER_V1_GATE_RESEARCHER_DECISION_REQUIRED'
    ,'PO_C_QUALIFIED_PENDING_PUBLICATION'
    ,'OF4_EXTERNAL_STORAGE_QUALIFIED_PENDING_PUBLICATION'
    ,'AUTHORIZED_2020_2023_RELATIONSHIP_OF4'
    ,'PRE_HELD_OUT_V1_GATE_RESEARCHER_DECISION_REQUIRED'
    ,'A1_H126_AMENDMENT_QUALIFIED_PENDING_PUBLICATION'
    ,'AUTHORIZED_A1_H126_PRE_HELD_OUT_EXECUTION'
    ,'A1_H126_EXTERNAL_SYNTHESIS_READY'
    ,'AUTHORIZED_FINAL_2024_2025_HELDOUT_EXTERNAL_EXECUTION'
    ,'FINAL_H1_H5_EVIDENCE_COMPLETE_TRADING_V1_1_DECISION_REQUIRED'
    ,'AUTHORIZED_TRADING_V1_1_OPTION_A_BATCH'
    ,'PAUSED_TRADING_V1_1_C04_COVERAGE'
    ,'AUTHORIZED_C04_THROUGH_2025_QUALIFICATION_NO_PNL'
    ,'RESEARCH_TRADING_V1_FINAL_FROZEN'
    ,'TRADING_V1_1_MATHEMATICAL_REVIEW_NO_EXECUTION'
)
if ($allowedGates -notcontains $contract.computation_gate) { throw 'Model computation gate has an unrecognized state.' }
if ($contract.computation_gate -eq 'AUTHORIZED_2015_2019_INNER_ONLY_AFTER_PROTOCOL_PUBLICATION_AND_C04_A_VALIDATION') {
    $authorizedInnerActions = @('V1-PHASE1-C04-INNER-EXECUTION-V1', 'V1-PAIR-A-PHASE1-INNER-EXECUTION-V1')
    if ($authorizedInnerActions -notcontains $next.action.action_id) { throw 'Inner authorization lacks the matching active action.' }
    if ($next.action.empirical_result_visibility -ne '2015_2019_INNER_ONLY') { throw 'Inner authorization has an invalid visibility boundary.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($next.action.action_id -eq 'V1-PAIR-A-PHASE1-INNER-EXECUTION-V1') {
        if ($next.action.dataset_access -notin @('CORE_V1_PLUS_C04_A_PLUS_C06_AMENDMENT_PLUS_EXEC_A_RESTRICTED_2013_2019','FROZEN_2013_2014_WARMUP_INPUT_PLUS_2015_2019_INNER_ONLY')) { throw 'PAIR-A inner action lacks the frozen warm-up plus inner-only dataset guard.' }
        if ($contract.pair_universe.construction -ne 'COMPLETE_PIT_ALL_PAIRS_C06_34_35') { throw 'PAIR-A construction is not bound.' }
        if ($contract.pair_universe.pre_screening -ne 'PROHIBITED') { throw 'PAIR-A pre-screen prohibition is not bound.' }
        if ($contract.c06_availability_amendment.status -ne 'QUALIFIED_ALL_REQUIRED_INNER_ORIGINS') { throw 'PAIR-A inner action lacks qualified C06 availability lineage.' }
        if ($contract.executable_semantics_amendment.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PAIR-A inner action lacks published EXEC-A semantics.' }
        if ($contract.decision_episode_semantics.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PAIR-A inner action lacks published DC-A/EP-A semantics.' }
        if ($contract.directional_collision_semantics.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PAIR-A inner action lacks published DECA-A semantics.' }
        if ($contract.a6_c06_stale_gap.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PAIR-A inner action lacks published SG-A semantics.' }
        if ($contract.rt3_state_augmentation.status -ne 'PUBLISHED_AUGMENTATION_QUALIFIED') { throw 'PAIR-A inner action lacks the qualified RT3 state augmentation.' }
        if ($contract.mp1_reference.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PAIR-A inner action lacks published MP1-A semantics.' }
        if ($contract.mp1_executable_interface.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PAIR-A inner action lacks published MP1-I-A semantics.' }
        if ($contract.downstream_executable_closure.status -ne 'PUBLISHED_BOUND_TO_PHASE1' -or $contract.downstream_executable_closure.final_field_audit -ne 'PASS') { throw 'PAIR-A inner action lacks the final executable closure.' }
    }
}
if ($contract.computation_gate -eq 'PAUSED_PAIR_UNIVERSE_FORMATION_RULE_NOT_FROZEN') {
    if ($next.action.action_id -ne 'NONE') { throw 'Pair-universe pause must not retain an executable action.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'Pair-universe pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'PAUSED_C06_AVAILABILITY_TIME_CONTRACT_MISMATCH') {
    if ($next.action.action_id -ne 'NONE') { throw 'C06 availability-time pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_C06_AVAILABILITY_TIME_AMENDMENT') { throw 'C06 pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'C06 pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'C06_AVAILABILITY_AMENDMENT_ACTIVE_NO_EMPIRICAL_ACCESS') {
    if ($next.action.action_id -ne 'V1-C06-AVAILABILITY-AMENDMENT-V1') { throw 'C06 amendment action is not bound.' }
    if ($next.action.dataset_access -ne 'C06_METADATA_AND_MEMBERSHIP_STRUCTURE_ONLY') { throw 'C06 amendment dataset access is too broad.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'C06 amendment must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'C06_AMENDMENT_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-C06-AVAILABILITY-AMENDMENT-V1') { throw 'Qualified C06 amendment is not bound to its publication action.' }
    if ($next.action.execution_state -ne 'QUALIFIED_PENDING_PROTOCOL_PUBLICATION') { throw 'Qualified C06 amendment publication state mismatch.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'No empirical visibility is permitted before amendment publication.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.c06_availability_amendment.status -ne 'QUALIFIED_ALL_REQUIRED_INNER_ORIGINS') { throw 'C06 amendment qualification is not bound.' }
}
if ($contract.computation_gate -eq 'PAUSED_EXECUTABLE_SEMANTICS_NOT_CLOSED') {
    if ($next.action.action_id -ne 'NONE') { throw 'Executable-semantics pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_EXECUTABLE_SEMANTICS_AMENDMENT') { throw 'Executable-semantics pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'Executable-semantics pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'EXEC_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-EXEC-A-AMENDMENT-V1') { throw 'EXEC-A publication action is not bound.' }
    if ($next.action.execution_state -ne 'QUALIFIED_PENDING_PROTOCOL_PUBLICATION') { throw 'EXEC-A publication state mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_EXEC_A_PROTOCOL_PUBLICATION') { throw 'EXEC-A publication must deny empirical dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'EXEC-A publication must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.executable_semantics_amendment.status -ne 'QUALIFIED_PENDING_PROTOCOL_PUBLICATION') { throw 'EXEC-A qualification is not bound.' }
}
if ($contract.computation_gate -eq 'PAUSED_PAIRA_R4_COMPUTATIONAL_FEASIBILITY') {
    if ($next.action.action_id -ne 'NONE') { throw 'R4 feasibility pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_PAIRA_R4_COMPUTE_DECISION') { throw 'R4 feasibility pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'R4 feasibility pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'R4_CONDITIONAL_CONTRACT_PENDING_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-R4-CONDITIONAL-COMPUTE-V1') { throw 'R4 conditional publication action is not bound.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'R4 contract publication must deny empirical visibility.' }
    if ($next.action.dataset_access -ne 'STRUCTURAL_COUNTS_AND_SYNTHETIC_KERNELS_ONLY') { throw 'R4 benchmark scope is too broad.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'CF_A_PASSED_PENDING_DISPOSITION_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-PAIR-A-PHASE1-INNER-EXECUTION-V1') { throw 'CF-A disposition publication action is not bound.' }
    if ($next.action.execution_state -ne 'CF_A_PASSED_PENDING_DISPOSITION_PUBLICATION') { throw 'CF-A disposition publication state mismatch.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED_UNTIL_CF_A_DISPOSITION_PUBLICATION') { throw 'CF-A disposition publication must deny empirical visibility.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_CF_A_DISPOSITION_PUBLICATION') { throw 'CF-A disposition publication must deny empirical dataset access.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.r4_conditional_compute_contract.status -ne 'CF_A_PASSED_BOUND_TO_PHASE1') { throw 'CF-A pass is not bound to Phase 1.' }
}
if ($contract.computation_gate -eq 'PAUSED_A6_TRAINING_GEOMETRY_NOT_FROZEN') {
    if ($next.action.action_id -ne 'NONE') { throw 'A6 training-geometry pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_A6_TRAINING_GEOMETRY_DECISION') { throw 'A6 training-geometry pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'A6 training-geometry pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'A6_TG_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-A6-TG-A-PUBLICATION-V1') { throw 'A6-TG-A publication action is not bound.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_A6_TG_A_PUBLICATION') { throw 'A6-TG-A publication must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'A6-TG-A publication must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'PAUSED_DECISION_CADENCE_EPISODE_ADMISSION_NOT_FROZEN') {
    if ($next.action.action_id -ne 'NONE') { throw 'Decision-cadence pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_DECISION_CADENCE_EPISODE_ADMISSION') { throw 'Decision-cadence pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'Decision-cadence pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'DC_A_EP_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-DC-A-EP-A-PUBLICATION-V1') { throw 'DC-A + EP-A publication action is not bound.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_DC_A_EP_A_PUBLICATION') { throw 'DC-A + EP-A publication must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'DC-A + EP-A publication must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'PAUSED_DIRECTIONAL_EPISODE_COLLISION_NOT_FROZEN') {
    if ($next.action.action_id -ne 'NONE') { throw 'Directional episode-collision pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_DIRECTIONAL_EPISODE_COLLISION_RULE') { throw 'Directional episode-collision pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'Directional episode-collision pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'DECA_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-DECA-A-PUBLICATION-V1') { throw 'DECA-A publication guard action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_DECA_A_PUBLICATION') { throw 'DECA-A publication guard must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'DECA-A publication guard must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'PAUSED_A6_C06_STALE_GAP_INDICATOR_NOT_FROZEN') {
    if ($next.action.action_id -ne 'NONE') { throw 'A6 stale-gap pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_A6_C06_STALE_GAP_RULE') { throw 'A6 stale-gap pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'A6 stale-gap pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'SG_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-SG-A-PUBLICATION-V1') { throw 'SG-A publication action mismatch.' }
    if ($next.action.execution_state -ne 'SG_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') { throw 'SG-A publication state mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_SG_A_PUBLICATION') { throw 'SG-A publication guard must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'SG-A publication guard must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.a6_c06_stale_gap.status -ne 'FROZEN_PENDING_PUBLICATION') { throw 'SG-A contract status mismatch.' }
}
if ($contract.computation_gate -eq 'PAUSED_A5_RT3_RELATIONSHIP_STATE_NOT_MATERIALIZED') {
    if ($next.action.action_id -ne 'NONE') { throw 'RT3 state-sufficiency pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_A5_RT3_RELATIONSHIP_STATE_RESOLUTION') { throw 'RT3 pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'RT3 pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.a6_c06_stale_gap.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'RT3 pause regressed SG-A publication.' }
}
if ($contract.computation_gate -eq 'RT3_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-RT3-A-PUBLICATION-V1') { throw 'RT3-A publication action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_RT3_A_PUBLICATION') { throw 'RT3-A publication must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'RT3-A publication must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.rt3_state_augmentation.status -ne 'FROZEN_PENDING_PUBLICATION') { throw 'RT3-A contract binding mismatch.' }
}
if ($contract.computation_gate -eq 'RT3_A_STATE_AUGMENTATION_ACTIVE_NO_INTERPRETATION') {
    if ($next.action.action_id -ne 'V1-RT3-A-RELATIONSHIP-STATE-AUGMENTATION-V1') { throw 'RT3-A augmentation action mismatch.' }
    if ($next.action.dataset_access -ne 'FROZEN_WARMUP_PLUS_2015_2019_RELATIONSHIP_REPLAY_ONLY') { throw 'RT3-A replay scope mismatch.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'RT3-A replay must deny empirical interpretation.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.rt3_state_augmentation.status -ne 'PUBLISHED_STATE_AUGMENTATION_ACTIVE') { throw 'RT3-A active status mismatch.' }
}
if ($contract.computation_gate -eq 'PAUSED_MP1_PIT_REFERENCE_WINDOW_NOT_FROZEN') {
    if ($next.action.action_id -ne 'NONE') { throw 'MP1 reference-window pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_MP1_PIT_REFERENCE_WINDOW_DECISION') { throw 'MP1 pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'MP1 pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.rt3_state_augmentation.status -ne 'PUBLISHED_AUGMENTATION_QUALIFIED') { throw 'MP1 pause regressed RT3 qualification.' }
}
if ($contract.computation_gate -eq 'MP1_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-MP1-A-PUBLICATION-V1') { throw 'MP1-A publication action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_MP1_A_PUBLICATION') { throw 'MP1-A publication must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'MP1-A publication must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.mp1_reference.status -ne 'FROZEN_PENDING_PUBLICATION') { throw 'MP1-A contract binding mismatch.' }
}
if ($contract.computation_gate -eq 'PAUSED_MP1_EXECUTABLE_INTERFACE_CONFLICT') {
    if ($next.action.action_id -ne 'NONE') { throw 'MP1 interface conflict must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_MP1_INTERFACE_DECISION') { throw 'MP1 interface conflict must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'MP1 interface conflict must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.mp1_reference.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'MP1-A publication regressed.' }
    if ($contract.rt3_state_augmentation.status -ne 'PUBLISHED_AUGMENTATION_QUALIFIED') { throw 'RT3 qualification regressed.' }
}
if ($contract.computation_gate -eq 'MP1_I_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-MP1-I-A-PUBLICATION-V1') { throw 'MP1-I-A publication action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_MP1_I_A_PUBLICATION') { throw 'MP1-I-A publication must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'MP1-I-A publication must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.mp1_executable_interface.status -ne 'FROZEN_PENDING_PUBLICATION') { throw 'MP1-I-A binding mismatch.' }
}
if ($contract.computation_gate -eq 'EXECUTABLE_UNRESOLVED_FIELD_SCAN_ACTIVE_NO_EMPIRICAL_ACCESS') {
    if ($next.action.action_id -ne 'V1-EXECUTABLE-UNRESOLVED-FIELD-SCAN-V1') { throw 'Executable scan action mismatch.' }
    if ($next.action.dataset_access -ne 'CONTRACT_DOCUMENTATION_ONLY') { throw 'Executable scan must not access data.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'Executable scan must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.mp1_executable_interface.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'MP1-I-A publication binding mismatch.' }
}
if ($contract.computation_gate -eq 'PAUSED_CONSOLIDATED_EXECUTABLE_FIELD_SEMANTICS') {
    if ($next.action.action_id -ne 'NONE') { throw 'Executable-field pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_CONSOLIDATED_EXECUTABLE_FIELD_DECISION') { throw 'Executable-field pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'Executable-field pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.mp1_executable_interface.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'MP1-I-A publication regressed.' }
}
if ($contract.computation_gate -eq 'EV_A_V1_FD_A_ER_A_QUALIFIED_PENDING_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-EV-A-V1-FD-A-ER-A-PUBLICATION-V1') { throw 'Executable closure publication action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_EXECUTABLE_CLOSURE_PUBLICATION') { throw 'Closure publication must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'Closure publication must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.downstream_executable_closure.status -ne 'FROZEN_PENDING_PUBLICATION') { throw 'Executable closure binding mismatch.' }
}
if ($contract.computation_gate -eq 'PAUSED_EV_A_ROW_LEVEL_MAPPING_NOT_BOUND') {
    if ($next.action.action_id -ne 'NONE') { throw 'EV-A row-mapping pause must not retain an executable action.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_EV_A_ROW_MAPPING_DECISION') { throw 'EV-A row-mapping pause must deny dataset access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'EV-A row-mapping pause must deny empirical visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if (-not (Test-Path -LiteralPath (Join-Path $repoRoot 'data/manifests/V1_INNER_A3_A5.json'))) { throw 'Validated A3/A5 checkpoint manifest missing.' }
}
if ($contract.computation_gate -eq 'EV_MAP_B_QUALIFIED_PENDING_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-EV-MAP-B-PUBLICATION') { throw 'EV-MAP-B publication action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_EV_MAP_B_PUBLICATION') { throw 'EV-MAP-B publication guard must deny data access.' }
    if ($next.action.empirical_result_visibility -ne 'DENIED') { throw 'EV-MAP-B publication guard must deny result visibility.' }
    if ($contract.ev_map_b.status -ne 'FROZEN_PENDING_PUBLICATION') { throw 'EV-MAP-B contract binding mismatch.' }
}
if ($contract.computation_gate -eq 'PRE_OUTER_V1_GATE_RESEARCHER_DECISION_REQUIRED') {
    if ($next.action.action_id -ne 'NONE') { throw 'Pre-outer gate must not retain an executable action.' }
    if ($next.action.execution_state -ne 'PRE_OUTER_V1_GATE') { throw 'Pre-outer execution state mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_PRE_OUTER_DECISION') { throw 'Pre-outer gate must deny data access.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.ev_map_b.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'Published EV-MAP-B binding missing.' }
    if (-not (Test-Path -LiteralPath (Join-Path $repoRoot 'data/manifests/V1_INNER_EV_MAP_B_A6_G5.json'))) { throw 'Inner completion manifest missing.' }
}
if ($contract.computation_gate -eq 'PO_C_QUALIFIED_PENDING_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-PO-C-PUBLICATION') { throw 'PO-C publication action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_PO_C_PUBLICATION') { throw 'PO-C publication must deny OF4 access.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.po_c.status -ne 'FROZEN_PENDING_PUBLICATION') { throw 'PO-C contract binding mismatch.' }
}
if ($contract.computation_gate -eq 'OF4_EXTERNAL_STORAGE_QUALIFIED_PENDING_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-PO-C-EXTERNAL-STORAGE-PUBLICATION') { throw 'External storage publication action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_EXTERNAL_STORAGE_PUBLICATION') { throw 'External storage publication must deny OF4 access.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.po_c.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PO-C publication binding mismatch.' }
}
if ($contract.computation_gate -eq 'AUTHORIZED_2020_2023_RELATIONSHIP_OF4') {
    if ($next.action.action_id -ne 'V1-PO-C-RELATIONSHIP-OF4-EXECUTION') { throw 'PO-C OF4 execution action mismatch.' }
    if ($next.action.dataset_access -ne 'FROZEN_2013_2019_ANCESTRY_PLUS_2020_2023_OF4_ONLY') { throw 'PO-C OF4 dataset role mismatch.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.po_c.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PO-C publication binding mismatch.' }
}
if ($contract.computation_gate -eq 'PRE_HELD_OUT_V1_GATE_RESEARCHER_DECISION_REQUIRED') {
    if ($next.action.action_id -ne 'NONE') { throw 'Pre-held-out gate must have no active action.' }
    if ($next.action.execution_state -notin @('PRE_HELD_OUT_V1_GATE_A1_SCALE_BINDING_REQUIRED','PRE_HELD_OUT_V1_GATE_RESEARCHER_DECISION_REQUIRED')) { throw 'Pre-held-out gate state mismatch.' }
    if ($next.action.dataset_access -notin @('DENIED_PENDING_A1_COMMON_SCALE_RESEARCHER_DECISION','DENIED_PENDING_PRE_HELD_OUT_RESEARCHER_DECISION')) { throw 'Pre-held-out gate must deny dataset access.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
}
if ($contract.computation_gate -eq 'A1_H126_AMENDMENT_QUALIFIED_PENDING_PUBLICATION') {
    if ($next.action.action_id -ne 'V1-A1-H126-CANDIDATE-NEUTRAL-AMENDMENT') { throw 'H126 amendment action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_UNTIL_A1_H126_AMENDMENT_PUBLICATION') { throw 'H126 publication guard must deny empirical access.' }
    if ($next.action.empirical_result_visibility -notmatch '^DENIED') { throw 'H126 publication guard must deny result visibility.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.a1_candidate_neutral_scale.status -ne 'FROZEN_PENDING_PUBLICATION') { throw 'H126 publication status mismatch.' }
}
if ($contract.computation_gate -eq 'AUTHORIZED_A1_H126_PRE_HELD_OUT_EXECUTION') {
    if ($next.action.action_id -ne 'V1-A1-H126-CANDIDATE-NEUTRAL-AMENDMENT') { throw 'H126 execution action mismatch.' }
    if ($next.action.dataset_access -ne 'IMMUTABLE_2013_2023_ANCESTRY_INNER_2015_2019_AND_OF4_2020_2023_ONLY') { throw 'H126 execution dataset role mismatch.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.a1_candidate_neutral_scale.status -ne 'PUBLISHED_BOUND_TO_PRE_HELD_OUT_V1') { throw 'H126 amendment is not published.' }
}
if ($contract.computation_gate -eq 'A1_H126_EXTERNAL_SYNTHESIS_READY') {
    if ($next.action.execution_state -notin @('READY_FOR_EXTERNAL_SYNTHESIS_EXECUTION','PARTIAL_READY_FOR_EXTERNAL_SYNTHESIS_RESUME')) { throw 'External H126 runner readiness state mismatch.' }
    if ($next.action.dataset_access -ne 'EXTERNAL_RUNNER_ONLY_IMMUTABLE_H126_LAYER_INNER_AND_OF4') { throw 'External H126 runner dataset boundary mismatch.' }
    if ($next.action.held_out_access -ne 'SEALED_DENIED') { throw 'Held-out access is not denied.' }
    if ($contract.a1_candidate_neutral_scale.status -ne 'PUBLISHED_BOUND_TO_PRE_HELD_OUT_V1') { throw 'H126 amendment is not published.' }
}
if ($contract.computation_gate -eq 'AUTHORIZED_FINAL_2024_2025_HELDOUT_EXTERNAL_EXECUTION') {
    if ($next.action.action_id -ne 'V1-FINAL-HELDOUT-CONFIRMATORY-EVALUATION') { throw 'Final held-out action mismatch.' }
    if ($next.action.status -ne 'AUTHORIZED') { throw 'Final held-out action is not authorized.' }
    if ($next.action.dataset_access -ne 'ONE_TIME_2024_2025_FINAL_HELDOUT_VIA_CHECKPOINTED_EXTERNAL_RUNNER_ONLY') { throw 'Final held-out dataset boundary mismatch.' }
    if ($next.action.held_out_access -ne 'AUTHORIZED_ONE_TIME_ACCESS_EVENT_REQUIRED_BEFORE_FIRST_READ') { throw 'Final held-out access-event guard mismatch.' }
    if ($contract.final_heldout.status -ne 'AUTHORIZED_ACCESS_NOT_YET_OPENED') { throw 'Final held-out contract status mismatch.' }
    if ($contract.final_heldout.a6_g5 -ne 'V1_NON_ESTIMABLE_NOT_EXECUTED') { throw 'A6/G5 disposition changed.' }
}

if ($contract.computation_gate -eq 'FINAL_H1_H5_EVIDENCE_COMPLETE_TRADING_V1_1_DECISION_REQUIRED') {
    if ($next.action.action_id -ne 'NONE' -or $next.action.status -eq 'AUTHORIZED') { throw 'Completed research must not authorize trading implicitly.' }
    if ($next.action.dataset_access -ne 'DENIED_PENDING_TRADING_V1_1_POLICY_DECISION') { throw 'Trading policy gate must deny fresh empirical execution.' }
    if ($next.action.held_out_access -ne 'PREVIOUSLY_OPENED_ACCESS_EVENT_PRESERVED_NO_NEW_EXECUTION') { throw 'Completed research access history mismatch.' }
    if ($contract.final_heldout.a6_g5 -ne 'V1_NON_ESTIMABLE_NOT_EXECUTED') { throw 'A6/G5 disposition changed.' }
    $evidencePath = Join-Path $repoRoot 'data/manifests/V1_FINAL_HELDOUT_EVIDENCE_CHECKPOINT.json'
    if (-not (Test-Path -LiteralPath $evidencePath)) { throw 'Final evidence manifest missing.' }
    $evidence = Get-Content -Raw -LiteralPath $evidencePath | ConvertFrom-Json
    if ($evidence.trading_pnl_accessed -ne $false) { throw 'Trading PnL must remain uninspected.' }
    if ($evidence.hypotheses.H4.heldout.status -ne 'COMPUTATION-INCOMPLETE / NO FINAL HELD-OUT DISPOSITION') { throw 'H4 terminal disposition changed.' }
    $completion = Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'research/V1_FINAL_HELDOUT_COMPLETION.json') | ConvertFrom-Json
    if ($completion.next_execution_authorized -ne $false -or $completion.trading_pnl_computed_or_inspected -ne $false) { throw 'Completion record must not activate trading.' }
    if ($completion.checkpoint_counts.exact_a1_cs2_units -ne 44 -or $completion.checkpoint_counts.native_h5_reporting_units -ne 110) { throw 'Completion unit counts mismatch.' }
    foreach ($binding in $completion.repository_artifacts.psobject.Properties) {
        $artifact = Join-Path $repoRoot $binding.Value.path
        if ((Get-FileHash -LiteralPath $artifact -Algorithm SHA256).Hash -ne $binding.Value.sha256) { throw "Completion repository hash mismatch: $($binding.Name)" }
    }
    foreach ($binding in $completion.external_artifacts.psobject.Properties) {
        $artifact = Join-Path $completion.external_root $binding.Value.path
        if ((Get-FileHash -LiteralPath $artifact -Algorithm SHA256).Hash -ne $binding.Value.sha256) { throw "Completion external hash mismatch: $($binding.Name)" }
    }
}

if ($contract.computation_gate -in @('AUTHORIZED_TRADING_V1_1_OPTION_A_BATCH', 'PAUSED_TRADING_V1_1_C04_COVERAGE', 'AUTHORIZED_C04_THROUGH_2025_QUALIFICATION_NO_PNL')) {
    if ($next.action.action_id -ne 'TRADING-V1-1-BATCH-EXECUTION') { throw 'Trading descendant lacks explicit action.' }
    if ($contract.computation_gate -eq 'PAUSED_TRADING_V1_1_C04_COVERAGE') {
        if ($next.action.status -ne 'BLOCKED_PREREQUISITE' -or $next.action.dataset_access -ne 'DENIED_UNTIL_REGISTERED_TEMPORAL_C04_COVERAGE_QUALIFIED_OR_SCOPE_EXPLICITLY_AMENDED') { throw 'C04 prerequisite must block empirical execution.' }
    } elseif ($next.action.status -ne 'AUTHORIZED') { throw 'Trading execution requires AUTHORIZED status.' }
    if ($contract.computation_gate -eq 'AUTHORIZED_C04_THROUGH_2025_QUALIFICATION_NO_PNL' -and $next.action.dataset_access -ne 'C04_OFFICIAL_SOURCE_ACQUISITION_AND_QUALIFICATION_ONLY_THEN_TRADING_AFTER_PUBLISHED_PASS') { throw 'C04 acquisition must not disclose PnL.' }
    $trading = Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'research/TRADING_V1_1_POLICY.json') | ConvertFrom-Json
    if ($trading.policy_id -ne 'TRADING-V1.1-MORPHOLOGY-OPTION-A-BATCH-1.0' -or $trading.candidates.Count -ne 6 -or $trading.candidates -contains 'V1-R4-63D') { throw 'Trading policy identity mismatch.' }
    if ($trading.retuning -ne $false -or $trading.security_cap -ne 0.1 -or $trading.gross_cap -ne 1 -or $trading.cash_return -ne 0) { throw 'Trading frozen constants mismatch.' }
    if ($contract.final_heldout.a6_g5 -ne 'V1_NON_ESTIMABLE_NOT_EXECUTED') { throw 'Original A6/G5 changed.' }
    if ($next.action.empirical_result_visibility -ne 'NO_PNL_DISCLOSURE_UNTIL_COMPLETE_OUTPUT_VALIDATION') { throw 'Trading reveal gate mismatch.' }
}
if ($contract.computation_gate -eq 'RESEARCH_TRADING_V1_FINAL_FROZEN') {
    if ($next.action.action_id -ne 'NONE' -or $next.action.next_execution_authorized -ne $false) { throw 'Final freeze must deny further execution.' }
    if ($next.action.dataset_access -ne 'DENIED_FINAL_FROZEN_NO_NEW_EXECUTION') { throw 'Final access guard mismatch.' }
    $final = Get-Content -Raw (Join-Path $repoRoot 'research/V1_FINAL_FREEZE.json') | ConvertFrom-Json
    if ($final.trading_units -ne 60 -or $final.complete_evaluable_cost_folds -ne 0 -or $final.no_v2_execution -ne $true) { throw 'Final disposition mismatch.' }
    if ($final.h4 -ne 'COMPUTATION-INCOMPLETE / NO FINAL HELD-OUT DISPOSITION' -or $final.a6_g5 -ne 'V1_NON_ESTIMABLE_NOT_EXECUTED') { throw 'Frozen unavailable states changed.' }
}
if ($contract.computation_gate -eq 'TRADING_V1_1_MATHEMATICAL_REVIEW_NO_EXECUTION') {
    if ($next.action.next_execution_authorized -ne $false) { throw 'Design review/migration must not enable empirical execution.' }
    if ($next.action.action_id -notin @('TRADING-V1-1-MATHEMATICAL-SPECIFICATION-AUDIT','TRADING-ECONOMIC-REDESIGN-CHECKPOINT','S3-SCALE-THRESHOLD-DESIGN','PRE-CLIENT-MIGRATION-CANONICALIZATION','NONE')) { throw 'Mathematical review action mismatch.' }
    if ($next.action.dataset_access -ne 'DENIED_SPECIFICATION_ONLY' -or $next.action.empirical_result_visibility -ne 'DENIED_NO_PNL_OR_TRADING_RESULT_INSPECTION') { throw 'Mathematical review must deny empirical access.' }
    if ($next.action.action_id -eq 'PRE-CLIENT-MIGRATION-CANONICALIZATION') {
        if ($next.action.status -ne 'AUTHORIZED' -or $next.action.push_destination -ne 'https://github.com/reinafeng2006/Mechanism-Aware-Statistical-Arbitrage.git main') { throw 'Migration publication scope mismatch.' }
    } elseif ($next.action.commit_permitted -ne $false -or $next.action.push_permitted -ne $false) { throw 'No publication authority for this review.' }
}
Write-Output 'PASS: bounded agent control state and G4-05 computation gate are structurally valid.'
