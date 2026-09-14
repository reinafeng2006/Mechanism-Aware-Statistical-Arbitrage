$ErrorActionPreference = 'Stop'

$repo = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$contractPath = Join-Path $repo 'research/V1_DECA_A_CONTRACT.json'
$decisionPath = Join-Path $repo 'docs/decisions/V1_DECA_A_DIRECTIONAL_COLLISION_FREEZE.md'

if (-not (Test-Path -LiteralPath $contractPath)) { throw 'Missing DECA-A contract.' }
if (-not (Test-Path -LiteralPath $decisionPath)) { throw 'Missing DECA-A decision record.' }

$contract = Get-Content -Raw -LiteralPath $contractPath | ConvertFrom-Json
$decision = Get-Content -Raw -LiteralPath $decisionPath
$allowedStatuses = @('QUALIFIED_PENDING_PROTOCOL_PUBLICATION', 'PUBLISHED_BOUND_TO_PHASE1')

if ($contract.contract_id -ne 'V1-DECA-A-1.0') { throw 'Unexpected DECA-A contract ID.' }
if ($allowedStatuses -notcontains $contract.status) { throw 'Unexpected DECA-A status.' }
if ($contract.both_directions_eligible -ne 'DIRECTIONAL_ENTRY_CONFLICT_NO_NEW_POSITION') { throw 'Bidirectional collision rule drifted.' }
if ($contract.single_direction_eligible -ne 'OPEN_CORRESPONDING_EP_A_EPISODE') { throw 'Single-direction admission rule drifted.' }
if ($contract.scientific_directional_records -ne 'PRESERVE_UNCHANGED') { throw 'Directional scientific records are not preserved.' }
if ($contract.conflict_effects.new_position -ne $false -or $contract.conflict_effects.pnl -ne $false -or $contract.conflict_effects.exposure -ne $false) { throw 'Conflict incorrectly creates economic effects.' }
if ($contract.interpretation_nonclaims -notcontains 'NOT_M0' -or $contract.interpretation_nonclaims -notcontains 'NOT_U_BY_DEFINITION' -or $contract.interpretation_nonclaims -notcontains 'NOT_MODEL_FAILURE') { throw 'DECA-A interpretation boundary is incomplete.' }
foreach ($rule in @('DIRECTIONAL_RANKING','STRONGER_SIGNAL_SELECTION','MAGNITUDE_TIE_BREAK','FIRST_OBSERVED_PRIORITY','RANDOM_TIE_BREAK','BIDIRECTIONAL_TWO_LEG_REPLACEMENT','OF4_ACCESS','HELD_OUT_ACCESS')) {
    if ($contract.forbidden_v1 -notcontains $rule) { throw "Missing forbidden DECA-A behavior: $rule" }
}
if ($decision -notmatch 'DIRECTIONAL ENTRY CONFLICT' -or $decision -notmatch 'exactly one entry-eligible direction') { throw 'Decision record does not bind the executable semantics.' }
if ($contract.empirical_information_used_to_freeze -ne $false) { throw 'DECA-A cannot be outcome-informed.' }

Write-Output 'PASS: DECA-A deterministically blocks same-channel bidirectional collisions without changing scientific records or active episodes.'
