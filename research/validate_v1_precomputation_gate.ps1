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
    ($activeInner -or $pairUniversePause -or $c06AvailabilityPause -or $c06AmendmentActive -or $c06AmendmentQualified -or $executableSemanticsPause -or $execAPublication -or $r4FeasibilityPause -or $r4Conditional -or $cfADispositionPublication -or $a6TrainingGeometryPause -or $a6TgaPublication -or $decisionCadencePause -or $dcAEpAPublication -or $directionalEpisodePause),
    ($contract.forbidden -contains 'PNL_TO_UPSTREAM_SELECTION'),
    ($contract.forbidden -contains 'HELD_OUT_ACCESS')
)

if ($checks -contains $false) { throw 'V1 pre-computation gate invariant failed.' }

if ($directionalEpisodePause) {
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
