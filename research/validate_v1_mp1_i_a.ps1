$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$a=Get-Content -Raw -LiteralPath (Join-Path $root 'research/V1_MP1_I_A_CONTRACT.json') | ConvertFrom-Json
$e=Get-Content -Raw -LiteralPath (Join-Path $root 'research/V1_EXECUTABLE_SEMANTICS_CONTRACT_V1_1.json') | ConvertFrom-Json
$g=Get-Content -Raw -LiteralPath (Join-Path $root 'research/G5_TRADING_V1_CONTRACT_V1_2.json') | ConvertFrom-Json
$d=Get-Content -Raw -LiteralPath (Join-Path $root 'docs/decisions/V1_MP1_I_A_RATIO_NATIVE_INTERFACE_AMENDMENT.md')
if($a.amendment_id -ne 'V1-MP1-I-A-1.0'){throw 'MP1-I-A ID mismatch.'}
if($a.status -notin @('FROZEN_PENDING_PUBLICATION','PUBLISHED_BOUND_TO_PHASE1')){throw 'MP1-I-A status invalid.'}
if($a.normalized_state -ne 'MP1_ratio_log_state=log(q_t/q_ref_t)'){throw 'Ratio-native state mismatch.'}
if($a.pv_m2_additions_ordered.Count -ne 9 -or $e.a6.pv_m2_addition_count -ne 9){throw 'PV-M2 descendant shape mismatch.'}
foreach($f in @('MP1_amount_log_ratio','MP1_volume_log_ratio','amount_available','volume_available')){if($a.removed_legacy_fields -notcontains $f){throw "Legacy removal missing: $f"};if($e.a6.pv_m2_additions_ordered -contains $f){throw "Legacy field remains executable: $f"}}
if($g.entry_state.M2 -notmatch 'MP1_RATIO_LOG_STATE_GT_0' -or $g.entry_state.additional_threshold -ne 'NONE'){throw 'G5 ratio-native gate mismatch.'}
if($a.empirical_information_used -ne $false -or $a.of4_access -ne 'DENIED' -or $a.held_out_access -ne 'SEALED_DENIED'){throw 'MP1-I-A access boundary failed.'}
if($d -notmatch 'MP1_ratio_log_state > 0 != M2 identification'){throw 'Interpretation boundary missing.'}
Write-Output 'PASS: MP1-I-A consistently binds the ratio-native MP1 state across A6 PV-M2 and G5.'
