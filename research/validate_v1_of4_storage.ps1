$ErrorActionPreference = 'Stop'
$audit = Get-Content -Raw (Join-Path $PSScriptRoot 'V1_OF4_STORAGE_FEASIBILITY_AUDIT.json') | ConvertFrom-Json
$storage = Get-Content -Raw (Join-Path $PSScriptRoot 'V1_OF4_EXTERNAL_STORAGE_CONTRACT.json') | ConvertFrom-Json
$po = Get-Content -Raw (Join-Path $PSScriptRoot 'V1_PO_C_CONTRACT.json') | ConvertFrom-Json
if ($po.status -ne 'PUBLISHED_BOUND_TO_PHASE1') { throw 'PO-C publication binding missing.' }
if ($audit.original_disposition -ne 'FAIL_UNSAFE_CAPACITY_ON_C_DRIVE') { throw 'Original storage blocker not preserved.' }
if ($audit.scientific_access -ne 'NO_OF4_MARKET_VALUES_OR_OUTCOMES_ACCESSED') { throw 'Preflight crossed scientific access boundary.' }
if ($storage.preflight.status -ne 'PASS') { throw 'External storage preflight failed.' }
if ([int64]$storage.preflight.free_bytes -lt [int64]$storage.preflight.minimum_required_free_bytes) { throw 'External free space below 60 GB.' }
if ([int64]$storage.preflight.free_bytes -lt [int64]$storage.preflight.projected_safe_peak_bytes) { throw 'Projected peak does not fit.' }
if ($storage.held_out -ne 'SEALED_NOT_CREATED_NOT_ACCESSED') { throw 'Held-out boundary mismatch.' }
$requiredProhibitions = @('TOP_K','SAMPLING','PAIR_UNIVERSE_REDUCTION','FIELD_DELETION','LOSSY_ROUNDING','YEAR_REDUCTION','SCIENTIFIC_SEMANTIC_MODIFICATION')
foreach ($item in $requiredProhibitions) {
    if ($storage.storage_only_prohibitions -notcontains $item) { throw "Missing storage-only prohibition: $item" }
}
if ($storage.materialization -ne 'TEMPORARY_WRITE_VALIDATE_CHECKSUM_ATOMIC_FINALIZE') { throw 'Atomic materialization contract mismatch.' }
if ($storage.compression -ne 'DETERMINISTIC_LOSSLESS') { throw 'Lossless compression contract mismatch.' }
Write-Output 'PASS: external OF4 storage is authorized and structurally feasible without scientific access.'
