$repo=Split-Path -Parent $PSScriptRoot
$c=Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'V1_PO_C_CONTRACT.json')|ConvertFrom-Json
$d=Get-Content -Raw -LiteralPath (Join-Path $repo 'docs/decisions/V1_PO_C_RELATIONSHIP_OF4_FREEZE.md')
if($c.decision_id -ne 'PO-C' -or $c.scope -ne 'RELATIONSHIP_STAGE_OF4_ONLY_2020_2023'){throw 'PO-C identity/scope mismatch.'}
if($c.a6_g5 -ne 'V1_NON_ESTIMABLE_NOT_EXECUTED' -or $c.retuning -ne 'PROHIBITED'){throw 'PO-C boundary mismatch.'}
if($c.outer_folds.Count -ne 4 -or $c.held_out_access -ne 'SEALED_DENIED'){throw 'Temporal boundary mismatch.'}
if($d -notmatch 'A3/A5 morphology is not mechanism identification'){throw 'Claim boundary missing.'}
Write-Output 'PASS: PO-C authorizes relationship/A3/A5 OF4 only; A6/G5 remain non-estimable and held-out sealed.'
