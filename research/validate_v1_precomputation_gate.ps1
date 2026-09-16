$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent $PSScriptRoot
$required = @(
    'docs/stages/G4/G4_05_V1_EXECUTABLE_SPECIFICATION_REGISTRY.md',
    'docs/stages/G4/G4_04A6_RESOLUTION_PREDICTIVE_VALIDATION_PROTOCOL_PROPOSAL.md',
    'docs/stages/G5/G5_TRADING_SIMULATION_V1_PROTOCOL_PROPOSAL.md',
    'docs/stages/G4/G4_G5_V1_PRECOMPUTATION_READINESS_AUDIT.md',
    'docs/stages/G4/PRE_COMPUTATION_TRADING_PROTOCOL_V1_GATE.md',
    'docs/stages/G4/V2_FUTURE_RESEARCH_REGISTER.md',
    'research/G5_TRADING_V1_CONTRACT.json'
)

foreach ($relative in $required) {
    $path = Join-Path $repo $relative
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing V1 gate artifact: $relative" }
}

$registry = Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/stages/G4/G4_05_V1_EXECUTABLE_SPECIFICATION_REGISTRY.md')
$trading = Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/stages/G5/G5_TRADING_SIMULATION_V1_PROTOCOL_PROPOSAL.md')
$gate = Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/stages/G4/PRE_COMPUTATION_TRADING_PROTOCOL_V1_GATE.md')
$action = Get-Content -Raw -LiteralPath (Join-Path $repo 'research/NEXT_ACTION.json') | ConvertFrom-Json
$contract = Get-Content -Raw -LiteralPath (Join-Path $repo 'research/G5_TRADING_V1_CONTRACT.json') | ConvertFrom-Json

$activeInner = (
    @('V1-PHASE1-C04-INNER-EXECUTION-V1', 'V1-PAIR-A-PHASE1-INNER-EXECUTION-V1') -contains $action.action.action_id -and
    $action.action.empirical_result_visibility -eq '2015_2019_INNER_ONLY' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$pairUniversePause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_PAIR_UNIVERSE_DECISION' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$c06AvailabilityPause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_C06_AVAILABILITY_TIME_AMENDMENT' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$c06AmendmentActive = (
    $action.action.action_id -eq 'V1-C06-AVAILABILITY-AMENDMENT-V1' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'C06_METADATA_AND_MEMBERSHIP_STRUCTURE_ONLY' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$c06AmendmentQualified = (
    $action.action.action_id -eq 'V1-C06-AVAILABILITY-AMENDMENT-V1' -and
    $action.action.execution_state -eq 'QUALIFIED_PENDING_PROTOCOL_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'C06_METADATA_AND_MEMBERSHIP_STRUCTURE_ONLY' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$executableSemanticsPause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_EXECUTABLE_SEMANTICS_AMENDMENT' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$execAPublication = (
    $action.action.action_id -eq 'V1-EXEC-A-AMENDMENT-V1' -and
    $action.action.execution_state -eq 'QUALIFIED_PENDING_PROTOCOL_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_EXEC_A_PROTOCOL_PUBLICATION' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$r4FeasibilityPause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_PAIRA_R4_COMPUTE_DECISION' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$r4Conditional = (
    $action.action.action_id -eq 'V1-R4-CONDITIONAL-COMPUTE-V1' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'STRUCTURAL_COUNTS_AND_SYNTHETIC_KERNELS_ONLY' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$cfADispositionPublication = (
    $action.action.action_id -eq 'V1-PAIR-A-PHASE1-INNER-EXECUTION-V1' -and
    $action.action.execution_state -eq 'CF_A_PASSED_PENDING_DISPOSITION_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED_UNTIL_CF_A_DISPOSITION_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_CF_A_DISPOSITION_PUBLICATION' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$a6TrainingGeometryPause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_A6_TRAINING_GEOMETRY_NOT_FROZEN' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_A6_TRAINING_GEOMETRY_DECISION' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$a6TgaPublication = (
    $action.action.action_id -eq 'V1-A6-TG-A-PUBLICATION-V1' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_A6_TG_A_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$decisionCadencePause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_DECISION_CADENCE_EPISODE_ADMISSION_NOT_FROZEN' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_DECISION_CADENCE_EPISODE_ADMISSION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$dcAEpAPublication = (
    $action.action.action_id -eq 'V1-DC-A-EP-A-PUBLICATION-V1' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_DC_A_EP_A_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$directionalEpisodePause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_DIRECTIONAL_EPISODE_COLLISION_NOT_FROZEN' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_DIRECTIONAL_EPISODE_COLLISION_RULE' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$decaAPublication = (
    $action.action.action_id -eq 'V1-DECA-A-PUBLICATION-V1' -and
    $action.action.execution_state -eq 'DECA_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_DECA_A_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$a6StaleGapPause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_A6_C06_STALE_GAP_INDICATOR_NOT_FROZEN' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_A6_C06_STALE_GAP_RULE' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$sgAPublication = (
    $action.action.action_id -eq 'V1-SG-A-PUBLICATION-V1' -and
    $action.action.execution_state -eq 'SG_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_SG_A_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$rt3StatePause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_A5_RT3_RELATIONSHIP_STATE_NOT_MATERIALIZED' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_A5_RT3_RELATIONSHIP_STATE_RESOLUTION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$rt3APublication = (
    $action.action.action_id -eq 'V1-RT3-A-PUBLICATION-V1' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_RT3_A_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$rt3AActive = (
    $action.action.action_id -eq 'V1-RT3-A-RELATIONSHIP-STATE-AUGMENTATION-V1' -and
    $action.action.dataset_access -eq 'FROZEN_WARMUP_PLUS_2015_2019_RELATIONSHIP_REPLAY_ONLY' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$mp1ReferencePause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_MP1_PIT_REFERENCE_WINDOW_NOT_FROZEN' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_MP1_PIT_REFERENCE_WINDOW_DECISION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$mp1APublication = (
    $action.action.action_id -eq 'V1-MP1-A-PUBLICATION-V1' -and
    $action.action.execution_state -eq 'MP1_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_MP1_A_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$mp1InterfacePause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_MP1_EXECUTABLE_INTERFACE_CONFLICT' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_MP1_INTERFACE_DECISION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$mp1IApublication = (
    $action.action.action_id -eq 'V1-MP1-I-A-PUBLICATION-V1' -and
    $action.action.execution_state -eq 'MP1_I_A_QUALIFIED_PENDING_PROTOCOL_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_MP1_I_A_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$executableFieldScan = (
    $action.action.action_id -eq 'V1-EXECUTABLE-UNRESOLVED-FIELD-SCAN-V1' -and
    $action.action.execution_state -eq 'EXECUTABLE_UNRESOLVED_FIELD_SCAN_ACTIVE_NO_EMPIRICAL_ACCESS' -and
    $action.action.dataset_access -eq 'CONTRACT_DOCUMENTATION_ONLY' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$consolidatedExecutablePause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_CONSOLIDATED_EXECUTABLE_FIELD_SEMANTICS' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_CONSOLIDATED_EXECUTABLE_FIELD_DECISION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$executableClosurePublication = (
    $action.action.action_id -eq 'V1-EV-A-V1-FD-A-ER-A-PUBLICATION-V1' -and
    $action.action.execution_state -eq 'EV_A_V1_FD_A_ER_A_QUALIFIED_PENDING_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_EXECUTABLE_CLOSURE_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$evRowMappingPause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PAUSED_AFTER_VALIDATED_A3_A5_BEFORE_A6_G5' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_EV_A_ROW_MAPPING_DECISION' -and
    $action.action.empirical_result_visibility -eq 'DENIED'
)
$evMapBPublication = (
    $action.action.action_id -eq 'V1-EV-MAP-B-PUBLICATION' -and
    $action.action.execution_state -eq 'EV_MAP_B_QUALIFIED_PENDING_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_EV_MAP_B_PUBLICATION' -and
    $action.action.empirical_result_visibility -eq 'DENIED'
)
$preOuterGate = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PRE_OUTER_V1_GATE' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_PRE_OUTER_DECISION' -and
    $action.action.held_out_access -eq 'SEALED_DENIED'
)
$poCPublication = (
    $action.action.action_id -eq 'V1-PO-C-PUBLICATION' -and
    $action.action.execution_state -eq 'PO_C_QUALIFIED_PENDING_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_PO_C_PUBLICATION' -and
    $action.action.held_out_access -eq 'SEALED_DENIED'
)
$externalStoragePublication = (
    $action.action.action_id -eq 'V1-PO-C-EXTERNAL-STORAGE-PUBLICATION' -and
    $action.action.execution_state -eq 'OF4_EXTERNAL_STORAGE_QUALIFIED_PENDING_PUBLICATION' -and
    $action.action.dataset_access -eq 'DENIED_UNTIL_EXTERNAL_STORAGE_PUBLICATION' -and
    $action.action.held_out_access -eq 'SEALED_DENIED'
)
$poCOf4Execution = (
    $action.action.action_id -eq 'V1-PO-C-RELATIONSHIP-OF4-EXECUTION' -and
    $action.action.execution_state -eq 'AUTHORIZED_2020_2023_RELATIONSHIP_OF4' -and
    $action.action.dataset_access -eq 'FROZEN_2013_2019_ANCESTRY_PLUS_2020_2023_OF4_ONLY' -and
    $action.action.held_out_access -eq 'SEALED_DENIED'
)
$preHeldOutA1Gate = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.execution_state -eq 'PRE_HELD_OUT_V1_GATE_A1_SCALE_BINDING_REQUIRED' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_A1_COMMON_SCALE_RESEARCHER_DECISION' -and
    $action.action.held_out_access -eq 'SEALED_DENIED'
)
$h126Amendment = (
    $action.action.action_id -eq 'V1-A1-H126-CANDIDATE-NEUTRAL-AMENDMENT' -and
    $action.action.execution_state -in @('A1_H126_AMENDMENT_QUALIFIED_PENDING_PUBLICATION','AUTHORIZED_A1_H126_PRE_HELD_OUT_EXECUTION','READY_FOR_EXTERNAL_SYNTHESIS_EXECUTION','PARTIAL_READY_FOR_EXTERNAL_SYNTHESIS_RESUME') -and
    $action.action.held_out_access -eq 'SEALED_DENIED'
)

$checks = @(
    ($registry -match 'R2-LIS.*V1 NOT DATA-READY'),
    ($registry -match 'R5-EG-ECM.*NO V1 EXECUTION'),
    ($registry -match 'seven-tuple'),
    ($trading -match 'Trading performance cannot redefine'),
    ($trading -match 'TC10'),
    ($gate -match 'PRE-COMPUTATION \+ TRADING-PROTOCOL V1 GATE — APPROVED / FROZEN'),
    ($gate -match 'C04-A'),
    ((Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/decisions/V1_PAIR_UNIVERSE_FREEZE.md')) -match 'PAIR-A COMPLETE PIT ALL-PAIRS'),
    ($action.action.held_out_access -eq 'SEALED_DENIED'),
    ($activeInner -or $pairUniversePause -or $c06AvailabilityPause -or $c06AmendmentActive -or $c06AmendmentQualified -or $executableSemanticsPause -or $execAPublication -or $r4FeasibilityPause -or $r4Conditional -or $cfADispositionPublication -or $a6TrainingGeometryPause -or $a6TgaPublication -or $decisionCadencePause -or $dcAEpAPublication -or $directionalEpisodePause -or $decaAPublication -or $a6StaleGapPause -or $sgAPublication -or $rt3StatePause -or $rt3APublication -or $rt3AActive -or $mp1ReferencePause -or $mp1APublication -or $mp1InterfacePause -or $mp1IApublication -or $executableFieldScan -or $consolidatedExecutablePause -or $executableClosurePublication -or $evRowMappingPause -or $evMapBPublication -or $preOuterGate -or $poCPublication -or $externalStoragePublication -or $poCOf4Execution -or $preHeldOutA1Gate -or $h126Amendment),
    ($contract.forbidden -contains 'PNL_TO_UPSTREAM_SELECTION'),
    ($contract.forbidden -contains 'HELD_OUT_ACCESS')
)

if ($checks -contains $false) {
    $failedIndexes = for ($index = 0; $index -lt $checks.Count; $index++) { if (-not $checks[$index]) { $index } }
    throw "V1 pre-computation gate invariant failed at check indexes: $($failedIndexes -join ',')."
}

if ($h126Amendment) {
    Write-Output 'PASS: H126 candidate-neutral A1 amendment is bounded to pre-held-out execution; held-out remains denied.'
} elseif ($preHeldOutA1Gate) {
    Write-Output 'PASS: OF4 materialization is complete; A1 comparison and held-out access are denied pending the common-scale researcher decision.'
} elseif ($poCOf4Execution) {
    Write-Output 'PASS: frozen PO-C relationship-only 2020-2023 OF4 is active; A6/G5 and held-out remain denied.'
} elseif ($externalStoragePublication) {
    Write-Output 'PASS: PO-C and qualified external storage are pending publication; no OF4 or held-out access is permitted yet.'
} elseif ($poCPublication) {
    Write-Output 'PASS: PO-C is frozen pending publication; no OF4 or held-out access is permitted yet.'
} elseif ($preOuterGate) {
    Write-Output 'PASS: inner EV-MAP-B/A6/G5 execution is complete; OF4 and held-out remain denied at the pre-outer gate.'
} elseif ($evMapBPublication) {
    Write-Output 'PASS: EV-MAP-B is frozen pending publication; A6/G5 data access remains denied.'
} elseif ($evRowMappingPause) {
    Write-Output 'PASS: corrected A3/A5 is preserved; A6/G5 access is denied pending source-bound EV-A row mapping.'
} elseif ($executableClosurePublication) {
    Write-Output 'PASS: EV-A-V1, FD-A, and ER-A are frozen pending publication; empirical access remains denied.'
} elseif ($consolidatedExecutablePause) {
    Write-Output 'PASS: MP1-I-A is published; downstream execution is paused at one consolidated executable-field checkpoint.'
} elseif ($executableFieldScan) {
    Write-Output 'PASS: MP1-I-A is published; the executable field scan is documentation-only and empirical access remains denied.'
} elseif ($mp1IApublication) {
    Write-Output 'PASS: MP1-I-A ratio-native descendant is frozen pending publication; empirical access remains denied.'
} elseif ($mp1InterfacePause) {
    Write-Output 'PASS: MP1-A is published; downstream execution is paused on the ratio-reference versus frozen PV-M2/G5 interface conflict.'
} elseif ($mp1APublication) {
    Write-Output 'PASS: MP1-A is frozen pending publication; downstream empirical access remains denied.'
} elseif ($mp1ReferencePause) {
    Write-Output 'PASS: RT3 augmentation is published and preserved; downstream execution is paused before MP1 on an unfrozen PIT reference-window contract.'
} elseif ($rt3AActive) {
    Write-Output 'PASS: RT3-A permits only deterministic relationship-state replay with no interpretation; OF4 and held-out remain denied.'
} elseif ($rt3APublication) {
    Write-Output 'PASS: RT3-A is frozen pending publication; relationship replay, empirical interpretation, OF4, and held-out access remain denied.'
} elseif ($rt3StatePause) {
    Write-Output 'PASS: SG-A is published and relationship outputs remain preserved; downstream execution is paused because frozen RT3 lacks event-time mapping state.'
} elseif ($sgAPublication) {
    Write-Output 'PASS: SG-A structural stale-gap semantics are frozen pending publication; empirical, OF4, and held-out access remains denied.'
} elseif ($a6StaleGapPause) {
    Write-Output 'PASS: all inner relationship outputs are structurally materialized; A6 is paused on the unfrozen C06 stale-gap indicator while empirical, OF4, and held-out access is denied.'
} elseif ($decaAPublication) {
    Write-Output 'PASS: DECA-A is frozen pending publication; empirical, OF4, and held-out access remains denied.'
} elseif ($directionalEpisodePause) {
    Write-Output 'PASS: Phase 1 is paused before fitting on the unresolved same-channel dual-direction episode collision; empirical, OF4, and held-out access is denied.'
} elseif ($dcAEpAPublication) {
    Write-Output 'PASS: DC-A + EP-A is frozen pending publication; empirical, OF4, and held-out access remains denied.'
} elseif ($decisionCadencePause) {
    Write-Output 'PASS: Phase 1 is paused before fitting on unresolved decision-event cadence and active-episode admission; empirical, OF4, and held-out access is denied.'
} elseif ($a6TgaPublication) {
    Write-Output 'PASS: A6-TG-A is frozen pending publication; empirical, OF4, and held-out access remains denied.'
} elseif ($a6TrainingGeometryPause) {
    Write-Output 'PASS: Phase 1 is paused on the unresolved A6 inner-training estimator geometry; model fitting, empirical visibility, OF4, and held-out access are denied.'
} elseif ($cfADispositionPublication) {
    Write-Output 'PASS: CF-A passed the structural/synthetic benchmark and awaits publication; empirical, OF4, and held-out access remains denied.'
} elseif ($r4Conditional) {
    Write-Output 'PASS: conditional R4 contract/benchmark action is active with structural/synthetic access only; empirical, OF4, and held-out access is denied.'
} elseif ($r4FeasibilityPause) {
    Write-Output 'PASS: V1/PAIR-A/EXEC-A remain frozen; Phase 1 is paused before empirical access on exact R4 computational feasibility.'
} elseif ($execAPublication) {
    Write-Output 'PASS: EXEC-A is qualified for publication; all empirical, OF4, and held-out access remains denied until its commit is pushed.'
} elseif ($executableSemanticsPause) {
    Write-Output 'PASS: V1, PAIR-A, C04-A, and C06 amendment remain frozen; Phase 1 is paused before empirical access pending executable scientific semantics.'
} elseif ($c06AmendmentQualified) {
    Write-Output 'PASS: C06-FIX-A is structurally qualified and awaiting protocol publication; V1 empirical/OF4/held-out access remains denied.'
} elseif ($c06AmendmentActive) {
    Write-Output 'PASS: V1 and PAIR-A protocols remain frozen; only the versioned C06 availability-time amendment is active, and all empirical/OF4/held-out access is denied.'
} elseif ($c06AvailabilityPause) {
    Write-Output 'PASS: V1 and PAIR-A protocols remain frozen; Phase 1 is safely paused on a C06 availability-time integrity mismatch, and all empirical/OF4/held-out access is denied.'
} elseif ($pairUniversePause) {
    Write-Output 'PASS: V1 protocol remains frozen; Phase 1 is safely paused pending a frozen pair-universe rule, and all empirical/OF4/held-out access is denied.'
} else {
    Write-Output 'PASS: V1 protocol is frozen; only conditional 2015-2019 inner development is authorized, while OF4 and held-out access remain denied.'
}
