$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent $PSScriptRoot
$decision = Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/decisions/V1_EXECUTABLE_SEMANTICS_AMENDMENT_FREEZE.md')
$contract = Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'V1_EXECUTABLE_SEMANTICS_CONTRACT.json') | ConvertFrom-Json

$checks = @(
    ($contract.amendment_id -eq 'V1-EXECUTABLE-SEMANTICS-A1'),
    ($contract.status -eq 'APPROVED_FROZEN_BEFORE_EMPIRICAL_ACCESS'),
    ($contract.scale.PS0 -eq '1.4826_TIMES_FINITE_SAMPLE_MAD'),
    ($contract.scale.PS1 -eq 'SAMPLE_SD_DDOF_1'),
    ($contract.scale.minimum_finite_observations -eq 2),
    ($contract.r1_mi.cross_34_35_blend -eq 'PROHIBITED'),
    ($contract.r3.strata.Count -eq 3),
    ($contract.r4.pit_order -eq 'PREDICT_THEN_EVALUATE_THEN_UPDATE'),
    ($contract.a6.pv0_column_count -eq 23),
    ($contract.a6.future_target_as_predictor -eq 'PROHIBITED'),
    ($contract.g5.extra_abnormality_threshold -eq 'PROHIBITED'),
    ($contract.empirical_information_used_to_freeze -eq $false),
    ($contract.of4_access -eq 'DENIED'),
    ($contract.held_out_access -eq 'SEALED_DENIED'),
    ($decision -match 'measurement != evidence != belief != probability != label != trade decision')
)

if ($checks -contains $false) { throw 'V1 executable-semantics invariant failed.' }
Write-Output 'PASS: V1 executable semantics E1-E6 are frozen without empirical, OF4, or held-out access.'
