$ErrorActionPreference='Stop'
$repo=Split-Path -Parent $PSScriptRoot
$c=Get-Content -Raw -LiteralPath (Join-Path $repo 'research/V1_RT3_A_CONTRACT.json') | ConvertFrom-Json
$d=Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/decisions/V1_RT3_A_RELATIONSHIP_STATE_AUGMENTATION_FREEZE.md')
if($c.decision_id -ne 'V1-RT3-A-1.0'){throw 'RT3-A ID mismatch.'}
if($c.status -notin @('FROZEN_PENDING_PUBLICATION','PUBLISHED_STATE_AUGMENTATION_ACTIVE','PUBLISHED_AUGMENTATION_QUALIFIED')){throw 'RT3-A status invalid.'}
if($c.original_outputs -ne 'IMMUTABLE_NO_OVERWRITE'){throw 'Original relationship outputs are not protected.'}
if($c.of4_access -ne 'DENIED' -or $c.held_out_access -ne 'SEALED_DENIED' -or $c.empirical_interpretation -ne 'DENIED'){throw 'RT3-A access boundary failed.'}
if($d -notmatch 'RT3 RELATIONSHIP REPLAY EQUIVALENCE BLOCKER'){throw 'Equivalence stop missing.'}
Write-Output 'PASS: RT3-A freezes a no-overwrite, equivalence-gated relationship-state augmentation only.'
