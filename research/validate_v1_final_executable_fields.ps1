$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$a=Get-Content -Raw -LiteralPath (Join-Path $root 'research/V1_FINAL_EXECUTABLE_FIELD_AUDIT.json')|ConvertFrom-Json
$c=Get-Content -Raw -LiteralPath (Join-Path $root 'research/V1_EXECUTABLE_CLOSURE_EV_A_V1_FD_A_ER_A.json')|ConvertFrom-Json
$e=Get-Content -Raw -LiteralPath (Join-Path $root 'research/V1_EXECUTABLE_SEMANTICS_CONTRACT_V1_1.json')|ConvertFrom-Json
$g=Get-Content -Raw -LiteralPath (Join-Path $root 'research/G5_TRADING_V1_CONTRACT_V1_2.json')|ConvertFrom-Json
if($a.status -ne 'PASS' -or $a.empirical_access -ne $false){throw 'Final executable audit status invalid.'}
if($a.layers.A6_PV0.column_count -ne $c.pv0.column_count -or $e.a6.pv0_column_count -ne $c.pv0.column_count){throw 'PV0 schema disagreement.'}
if($a.layers.A6_PV_M1.addition_count -ne $c.pv_m1.addition_count -or $e.a6.pv_m1_additions -ne $c.pv_m1.addition_count){throw 'PV-M1 schema disagreement.'}
if($a.layers.A6_PV_M2.addition_count -ne $c.pv_m2.addition_count -or $e.a6.pv_m2_addition_count -ne $c.pv_m2.addition_count){throw 'PV-M2 schema disagreement.'}
if($a.layers.A6_PV_M1.unavailable_field -ne 'M1_evidence_unavailable'){throw 'M1 unavailable field missing.'}
if($g.execution.opportunity -ne 'NEXT_ELIGIBLE_OPEN_ONLY' -or $g.execution.carry_forward -ne $false){throw 'FD-A binding failed.'}
if($g.reporting.annualization_sessions -ne 252 -or $g.reporting.annualization_role -ne 'REPORTING_ONLY_NOT_SELECTION'){throw 'ER-A binding failed.'}
if($a.unresolved_estimand_target_or_trading_policy_fields.Count -ne 0){throw 'Substantive executable fields remain unresolved.'}
if($a.declaration -ne 'V1 EXECUTABLE SEMANTICS CLOSED' -or $a.of4_access -ne 'DENIED' -or $a.held_out_access -ne 'SEALED_DENIED'){throw 'Final boundary mismatch.'}
Write-Output 'PASS: V1 EXECUTABLE SEMANTICS CLOSED; OF4 and held-out remain denied.'
