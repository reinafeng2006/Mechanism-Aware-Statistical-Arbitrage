$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
$contract = Get-Content -Raw -LiteralPath (Join-Path $repo 'research/V1_SG_A_CONTRACT.json') | ConvertFrom-Json
$decision = Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/decisions/V1_SG_A_C06_STALE_GAP_FREEZE.md')

if ($contract.decision_id -ne 'V1-SG-A-1.0') { throw 'SG-A decision ID mismatch.' }
if ($contract.status -notin @('FROZEN_PENDING_PUBLICATION','PUBLISHED_BOUND_TO_PHASE1')) { throw 'SG-A status invalid.' }
if ($contract.ancestor_dataset -ne 'CORE-DATASET-FREEZE-V1') { throw 'SG-A dataset ancestry mismatch.' }
if ($contract.c06_availability_ancestor -ne 'C06-AVAILABILITY-AMENDMENT-V1') { throw 'SG-A C06 ancestry mismatch.' }
if ($contract.boolean_state -ne 'STRUCTURAL_MISSED_EXPECTED_OFFICIAL_UPDATE_OPPORTUNITY') { throw 'SG-A is not structural.' }
if ($contract.empirical_information_used -ne $false -or $contract.of4_accessed -ne $false -or $contract.held_out_accessed -ne $false) { throw 'SG-A anti-contamination invariant failed.' }
if ($contract.regime_awareness.'2012_regime' -ne 'AUTHORITATIVE_QUARTERLY_SEQUENCE') { throw 'Quarterly regime missing.' }
if ($contract.regime_awareness.'2023_regime' -ne 'AUTHORITATIVE_SEMIANNUAL_SEQUENCE') { throw 'Semiannual regime missing.' }
if ($contract.qualification_values -notcontains 'UNRESOLVED') { throw 'Unresolved qualification state missing.' }
$required = @(
  'classification age != stale-gap indicator',
  'no 90/120/180-day or other day-count threshold',
  'no default `0` or `1` when regime qualification is unresolved',
  'no relationship-output recomputation caused by this amendment'
)
foreach ($text in $required) { if ($decision -notmatch [regex]::Escape($text)) { throw "SG-A decision text missing: $text" } }

Write-Output 'PASS: SG-A is frozen as a regime-aware structural stale-gap state separate from continuous classification age.'
