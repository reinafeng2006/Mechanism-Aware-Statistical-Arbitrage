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

Write-Output 'PASS: bounded agent control state and G4-05 computation gate are structurally valid.'
