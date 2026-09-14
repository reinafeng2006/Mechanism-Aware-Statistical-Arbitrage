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
    $action.action.action_id -eq 'V1-PHASE1-C04-INNER-EXECUTION-V1' -and
    $action.action.empirical_result_visibility -eq '2015_2019_INNER_ONLY' -and
    $contract.status -eq 'FROZEN_PHASE1_INNER_AUTHORIZED_C04_CONDITIONAL'
)
$pairUniversePause = (
    $action.action.action_id -eq 'NONE' -and
    $action.action.empirical_result_visibility -eq 'DENIED' -and
    $action.action.dataset_access -eq 'DENIED_PENDING_PAIR_UNIVERSE_DECISION' -and
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
    ($action.action.held_out_access -eq 'SEALED_DENIED'),
    ($activeInner -or $pairUniversePause),
    ($contract.forbidden -contains 'PNL_TO_UPSTREAM_SELECTION'),
    ($contract.forbidden -contains 'HELD_OUT_ACCESS')
)

if ($checks -contains $false) { throw 'V1 pre-computation gate invariant failed.' }

if ($pairUniversePause) {
    Write-Output 'PASS: V1 protocol remains frozen; Phase 1 is safely paused pending a frozen pair-universe rule, and all empirical/OF4/held-out access is denied.'
} else {
    Write-Output 'PASS: V1 protocol is frozen; only conditional 2015-2019 inner development is authorized, while OF4 and held-out access remain denied.'
}
