$ErrorActionPreference = 'Stop'
$c = Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'V1_DC_A_EP_A_CONTRACT.json') | ConvertFrom-Json
$checks = @(
  ($c.contract_id -eq 'V1-DC-A-EP-A-1.0'),
  ($c.status -in @('APPROVED_FROZEN_PENDING_PUBLICATION','PUBLISHED_BOUND_TO_PHASE1')),
  ($c.decision_event_cadence -eq 'EACH_CANDIDATE_ELIGIBLE_SESSION'),
  ($c.refresh_independence -eq $true),
  ($c.maximum_active_episodes_per_identity -eq 1),
  ($c.active_signal_disposition -eq 'BLOCKED_RE_ENTRY'),
  ($c.blocked_reentry_effects.anchor_reset -eq $false),
  ($c.blocked_reentry_effects.pnl -eq $false),
  ($c.forbidden -contains 'EPISODE_STACKING'),
  ($c.forbidden -contains 'OF4_ACCESS'),
  ($c.forbidden -contains 'HELD_OUT_ACCESS'),
  ($c.empirical_information_used_to_freeze -eq $false)
)
if ($checks -contains $false) { throw 'DC-A + EP-A invariant failed.' }
Write-Output 'PASS: daily decision events and one-active-episode admission are frozen without changing model refresh clocks.'
