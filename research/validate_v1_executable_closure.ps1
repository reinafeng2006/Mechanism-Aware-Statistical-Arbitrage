$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$c=Get-Content -Raw -LiteralPath (Join-Path $root 'research/V1_EXECUTABLE_CLOSURE_EV_A_V1_FD_A_ER_A.json')|ConvertFrom-Json
$d=Get-Content -Raw -LiteralPath (Join-Path $root 'docs/decisions/V1_EV_A_V1_FD_A_ER_A_EXECUTABLE_CLOSURE.md')
if($c.contract_id -ne 'V1-EXECUTABLE-CLOSURE-EV-A-V1-FD-A-ER-A-1.0'){throw 'Closure ID mismatch.'}
if($c.status -notin @('FROZEN_PENDING_PUBLICATION','PUBLISHED_BOUND_TO_PHASE1')){throw 'Closure status invalid.'}
if($c.pv0.column_count -ne 32 -or $c.pv_m1.addition_count -ne 7 -or $c.pv_m2.addition_count -ne 15){throw 'Design-matrix shape mismatch.'}
if($c.pv_m1.state_fields -notcontains 'M1_evidence_unavailable' -or $c.pv_m1.morphology_alone_sets_support -ne $false){throw 'M1 conservative mapping mismatch.'}
if($c.pv0.m0_no_record -ne 'UNAVAILABLE_WITHOUT_EXHAUSTIVE_NEGATIVE_COVERAGE'){throw 'M0 negative-inference boundary failed.'}
if($c.pv0.invalidity_fields.Count -ne 2 -or $c.pv0.break_fields.Count -ne 2){throw 'Invalidity/break split missing.'}
if($c.pv_m2.contamination_dimensions.Count -ne 6 -or $c.pv_m2.contamination_encoding -ne 'PRESENT_AND_UNAVAILABLE_PER_DIMENSION'){throw 'M2 contamination mapping mismatch.'}
if($c.fd_a.execution_opportunity -ne 'NEXT_ELIGIBLE_OPEN_ONLY' -or $c.fd_a.carry_forward -ne $false){throw 'FD-A mismatch.'}
if($c.er_a.sessions_per_year -ne 252 -or $c.er_a.role -ne 'REPORTING_ONLY_NOT_SELECTION'){throw 'ER-A mismatch.'}
if($c.empirical_information_used -ne $false -or $c.of4_access -ne 'DENIED' -or $c.held_out_access -ne 'SEALED_DENIED'){throw 'Access boundary failed.'}
if($d -notmatch 'V1 EXECUTABLE SEMANTICS CLOSED'){throw 'Closure declaration missing.'}
Write-Output 'PASS: EV-A-V1, FD-A, and ER-A close the V1 downstream executable field semantics.'
