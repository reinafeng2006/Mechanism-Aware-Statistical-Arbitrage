$ErrorActionPreference = 'Stop'
$c = Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'V1_A6_TG_A_CONTRACT.json') | ConvertFrom-Json
$checks = @(
  ($c.contract_id -eq 'V1-A6-TG-A-1.0'),
  ($c.status -in @('APPROVED_FROZEN_PENDING_PUBLICATION','PUBLISHED_BOUND_TO_PHASE1')),
  ($c.blocks.'2015H1' -eq 'TRAINING_EVIDENCE_ONLY'),
  ($c.blocks.first_prediction -eq '2015H2'),
  ($c.blocks.later_training -eq 'EXPANDING_PRIOR_COMPLETED_INNER_BLOCKS'),
  ($c.fitting_weights -eq 'EQUAL_TOTAL_PER_UNORDERED_PAIR_ROWS_DIVIDE_PAIR_WEIGHT'),
  ($c.pair_direction_specific_models -eq $false),
  ($c.forbidden -contains 'ROLLING_A6_WINDOW'),
  ($c.forbidden -contains 'OF4_ACCESS'),
  ($c.forbidden -contains 'HELD_OUT_ACCESS'),
  ($c.empirical_information_used_to_freeze -eq $false)
)
if ($checks -contains $false) { throw 'A6-TG-A invariant failed.' }
Write-Output 'PASS: A6-TG-A expanding completed-inner geometry and equal-total-pair fitting weights are frozen.'
