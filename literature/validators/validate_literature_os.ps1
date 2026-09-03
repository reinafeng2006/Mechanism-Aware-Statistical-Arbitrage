param(
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
)

$ErrorActionPreference = "Stop"

function Get-TableIds {
    param([string]$Path, [string]$Pattern)
    return @(
        Get-Content -LiteralPath $Path |
        Where-Object { $_ -match $Pattern } |
        ForEach-Object { [regex]::Match($_, $Pattern).Groups[1].Value } |
        Sort-Object -Unique
    )
}

function Assert-Condition {
    param([bool]$Condition, [string]$Message)
    if (-not $Condition) { throw $Message }
}

$evidencePath = Join-Path $RepositoryRoot "registers\LITERATURE_EVIDENCE.md"
$requirementsPath = Join-Path $RepositoryRoot "registers\DATA_REQUIREMENTS.md"
$reconciliationPath = Join-Path $RepositoryRoot "literature\reconciliation_g1_02.md"
$hierarchyPath = Join-Path $RepositoryRoot "docs\G1_STAGE_HIERARCHY.md"
$gatesPath = Join-Path $RepositoryRoot "docs\GATES.md"
$migrationPath = Join-Path $RepositoryRoot "docs\LITERATURE_OS_MIGRATION.md"
$libraryPath = Join-Path $RepositoryRoot "literature\library"

@($evidencePath, $requirementsPath, $reconciliationPath, $hierarchyPath, $gatesPath, $migrationPath, $libraryPath) | ForEach-Object {
    Assert-Condition (Test-Path -LiteralPath $_) "Missing required Literature OS artifact: $_"
}

$claimIds = Get-TableIds $evidencePath '^\| (CL-[A-Z0-9-]+) \|'
$claimReconIds = Get-TableIds $reconciliationPath '^\| RC-[0-9]+ \| (CL-[A-Z0-9-]+) \|'
$dataIds = Get-TableIds $requirementsPath '^\| (DR-[0-9]+) \|'
$dataReconIds = Get-TableIds $reconciliationPath '^\| RD-[0-9]+ \| (DR-[0-9]+) \|'

Assert-Condition ($claimIds.Count -eq 15) "Expected 15 canonical Claim IDs; found $($claimIds.Count)."
Assert-Condition ($claimReconIds.Count -eq 15) "Expected 15 reconciled Claim IDs; found $($claimReconIds.Count)."
Assert-Condition (-not (Compare-Object $claimIds $claimReconIds)) "Claim reconciliation is not one-to-one with canonical evidence IDs."
Assert-Condition ($dataIds.Count -eq 15) "Expected 15 canonical Data Requirement IDs; found $($dataIds.Count)."
Assert-Condition ($dataReconIds.Count -eq 15) "Expected 15 reconciled Data Requirement IDs; found $($dataReconIds.Count)."
Assert-Condition (-not (Compare-Object $dataIds $dataReconIds)) "Data Requirement reconciliation is not one-to-one with canonical IDs."

$dataLines = Get-Content -LiteralPath $requirementsPath | Where-Object { $_ -match '^\| DR-[0-9]+ \|' }
foreach ($line in $dataLines) {
    Assert-Condition ($line -match 'CL-[A-Z0-9-]+') "Data Requirement lacks a current Claim ID linkage: $line"
}

$reconciliationText = Get-Content -Raw -LiteralPath $reconciliationPath
Assert-Condition ($reconciliationText -notmatch '\bLC[0-9]{4}\b') "Predecessor Claim ID found in current reconciliation control."
Assert-Condition ($reconciliationText -notmatch '\bP[0-9]{4}\b') "Predecessor Paper ID found in current reconciliation control."

$hierarchyText = Get-Content -Raw -LiteralPath $hierarchyPath
$gatesText = Get-Content -Raw -LiteralPath $gatesPath
Assert-Condition ($hierarchyText -match 'G1-03.*NOT YET APPROVED/STARTED') "G1-03 must remain unauthorized during migration."
Assert-Condition ($gatesText -match 'G1-02 COMPLETE.*G1-03 LOCKED') "Gate status must keep G1-03 locked."

$unexpectedLibraryFiles = @(
    Get-ChildItem -LiteralPath $libraryPath -File -Recurse |
    Where-Object { $_.Name -ne '.gitkeep' }
)
Assert-Condition ($unexpectedLibraryFiles.Count -eq 0) "Migration must not import predecessor full text; found: $($unexpectedLibraryFiles.FullName -join ', ')"

[PSCustomObject]@{
    CanonicalClaims = $claimIds.Count
    ReconciledClaims = $claimReconIds.Count
    CanonicalDataRequirements = $dataIds.Count
    ReconciledDataRequirements = $dataReconIds.Count
    DataRequirementsWithClaimLinkage = $dataLines.Count
    PredecessorIdentifiersInReconciliation = 'None'
    ImportedFullTexts = 0
    G103Status = 'LOCKED'
    Result = 'PASS'
} | Format-List
