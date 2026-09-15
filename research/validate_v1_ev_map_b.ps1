$repo=Split-Path -Parent $PSScriptRoot
$c=Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'V1_EV_MAP_B_CONTRACT.json')|ConvertFrom-Json
$d=Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/decisions/V1_EV_MAP_B_FREEZE.md')
if($c.decision_id -ne 'EV-MAP-B'){throw 'EV-MAP-B ID mismatch.'}
if($c.global_unavailable.Count -ne 5){throw 'Unsupported proposition registry mismatch.'}
if(@($c.row_level_qualified.PSObject.Properties).Count -lt 6){throw 'Qualified row-level exceptions missing.'}
if($c.a6.silent_drop -ne $false -or $c.g5.profit_is_identification -ne $false){throw 'A6/G5 boundary mismatch.'}
if($c.of4_access -ne 'DENIED' -or $c.held_out_access -ne 'SEALED_DENIED'){throw 'Temporal boundary mismatch.'}
if($d -notmatch 'M1-MOTIVATED DIRECTIONAL PROBE' -or $d -notmatch 'Profitability cannot establish mechanism identification'){throw 'Claim scope missing.'}
Write-Output 'PASS: EV-MAP-B freezes unsupported propositions as unavailable while retaining qualified row-level exceptions.'
