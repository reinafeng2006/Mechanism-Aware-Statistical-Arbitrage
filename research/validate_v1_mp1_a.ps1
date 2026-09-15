$ErrorActionPreference='Stop'
$repo=Split-Path -Parent $PSScriptRoot
$c=Get-Content -Raw -LiteralPath (Join-Path $repo 'research/V1_MP1_A_CONTRACT.json') | ConvertFrom-Json
$d=Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/decisions/V1_MP1_A_PIT_REFERENCE_FREEZE.md')
if($c.decision_id -ne 'V1-MP1-A-1.0'){throw 'MP1-A ID mismatch.'}
if($c.status -notin @('FROZEN_PENDING_PUBLICATION','PUBLISHED_BOUND_TO_PHASE1')){throw 'MP1-A status invalid.'}
if($c.reference_object -ne 'AMOUNT_DIVIDED_BY_VOLUME' -or $c.estimator -ne 'MEDIAN'){throw 'MP1-A reference mismatch.'}
if($c.history -ne 'MOST_RECENT_126_QUALIFIED_OBSERVATIONS'){throw 'MP1-A H126 mismatch.'}
if($c.refresh -ne 'FIRST_AUTHORIZED_ELIGIBLE_ISO_WEEK_POINT' -or $c.pit_order -ne 'STRICTLY_BEFORE_REFRESH_ORIGIN'){throw 'MP1-A PIT cadence mismatch.'}
if($c.cross_candidate -ne 'COMMON_R0_R1_R3_R4'){throw 'MP1-A cross-candidate mismatch.'}
if($c.of4_access -ne 'DENIED' -or $c.held_out_access -ne 'SEALED_DENIED'){throw 'MP1-A access boundary failed.'}
if($d -notmatch 'H126' -or $d -notmatch 'U1W'){throw 'MP1-A decision incomplete.'}
Write-Output 'PASS: MP1-A freezes a common candidate-neutral H126/U1W PIT amount/volume reference.'
