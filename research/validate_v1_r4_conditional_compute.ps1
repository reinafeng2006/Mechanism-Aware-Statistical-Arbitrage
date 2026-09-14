$ErrorActionPreference = 'Stop'
$contract = Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'V1_R4_CONDITIONAL_COMPUTE_CONTRACT.json') | ConvertFrom-Json
$checks = @(
  ($contract.contract_id -eq 'V1-R4-CF-A-CF-B-1.0'),
  ($contract.status -eq 'APPROVED_FROZEN_PRE_BENCHMARK'),
  ($contract.primary.state_update -eq 'U1D'),
  ($contract.primary.qr_reestimate -eq 'U1M_FIRST_CANDIDATE_ELIGIBLE_EXCHANGE_SESSION'),
  ($contract.primary.qr_information -eq 'STRICTLY_BEFORE_MONTHLY_ORIGIN'),
  ($contract.fallback.trigger -eq 'COMPUTATIONAL_RUNTIME_OR_RESOURCE_INFEASIBILITY_ONLY'),
  ($contract.fallback.R4 -eq 'V1_COMPUTATION_DEFERRED_V2'),
  ($contract.prohibited -contains 'PAIR_SCREENING'),
  ($contract.prohibited -contains 'OF4_ACCESS'),
  ($contract.prohibited -contains 'HELD_OUT_ACCESS')
)
if ($checks -contains $false) { throw 'Conditional R4 compute contract invariant failed.' }
Write-Output 'PASS: conditional CF-A/CF-B contract is frozen before benchmark and empirical access.'
