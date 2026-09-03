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
$reconciliation02bPath = Join-Path $RepositoryRoot "literature\reconciliation_g1_02b.md"
$reconciliationRound1bPath = Join-Path $RepositoryRoot "literature\reconciliation_g1_02_round1b.md"
$hierarchyPath = Join-Path $RepositoryRoot "docs\G1_STAGE_HIERARCHY.md"
$gatesPath = Join-Path $RepositoryRoot "docs\GATES.md"
$migrationPath = Join-Path $RepositoryRoot "docs\LITERATURE_OS_MIGRATION.md"
$libraryPath = Join-Path $RepositoryRoot "literature\library"

@($evidencePath, $requirementsPath, $reconciliationPath, $reconciliation02bPath, $reconciliationRound1bPath, $hierarchyPath, $gatesPath, $migrationPath, $libraryPath) | ForEach-Object {
    Assert-Condition (Test-Path -LiteralPath $_) "Missing required Literature OS artifact: $_"
}

$claimIds = Get-TableIds $evidencePath '^\| (CL-[A-Z0-9-]+) \|'
$claimReconIds = Get-TableIds $reconciliationPath '^\| RC-[0-9]+ \| (CL-[A-Z0-9-]+) \|'
$dataIds = Get-TableIds $requirementsPath '^\| (DR-[0-9]+) \|'
$dataReconIds = Get-TableIds $reconciliationPath '^\| RD-[0-9]+ \| (DR-[0-9]+) \|'
$claim02bIds = Get-TableIds $reconciliation02bPath '^\| RC2-[0-9]+ \| (CL-[A-Z0-9-]+) \|'
$data02bIds = Get-TableIds $reconciliation02bPath '^\| RD2-[0-9]+ \| (DR-[0-9]+) \|'
$claimRound1bIds = Get-TableIds $reconciliationRound1bPath '^\| R1B-[0-9]+ \| (CL-[A-Z0-9-]+) \|'
$dataRound1bIds = Get-TableIds $reconciliationRound1bPath '^\| R1B-DR-[0-9]+ \| (DR-[0-9]+) \|'

Assert-Condition ($claimIds.Count -eq 21) "Expected 21 canonical Claim IDs after G1-02 Round 1B; found $($claimIds.Count)."
Assert-Condition ($claimReconIds.Count -eq 15) "Expected 15 reconciled Claim IDs; found $($claimReconIds.Count)."
Assert-Condition ($claim02bIds.Count -eq 4) "Expected 4 G1-02b reconciled Claim IDs; found $($claim02bIds.Count)."
Assert-Condition ($claimRound1bIds.Count -eq 2) "Expected 2 G1-02 Round 1B reconciled Claim IDs; found $($claimRound1bIds.Count)."
Assert-Condition (@(Compare-Object $claimReconIds $claimIds | Where-Object { $_.SideIndicator -eq '<=' }).Count -eq 0) "Baseline claim reconciliation is not a subset of canonical evidence IDs."
Assert-Condition (@(Compare-Object $claim02bIds $claimIds | Where-Object { $_.SideIndicator -eq '<=' }).Count -eq 0) "G1-02b claim reconciliation is not a subset of canonical evidence IDs."
Assert-Condition (@(Compare-Object $claimRound1bIds $claimIds | Where-Object { $_.SideIndicator -eq '<=' }).Count -eq 0) "G1-02 Round 1B claim reconciliation is not a subset of canonical evidence IDs."
Assert-Condition ($dataIds.Count -eq 17) "Expected 17 canonical Data Requirement IDs after G1-02 Round 1B; found $($dataIds.Count)."
Assert-Condition ($dataReconIds.Count -eq 15) "Expected 15 reconciled Data Requirement IDs; found $($dataReconIds.Count)."
Assert-Condition ($data02bIds.Count -eq 1) "Expected 1 G1-02b reconciled Data Requirement ID; found $($data02bIds.Count)."
Assert-Condition ($dataRound1bIds.Count -eq 1) "Expected 1 G1-02 Round 1B reconciled Data Requirement ID; found $($dataRound1bIds.Count)."
Assert-Condition (@(Compare-Object $dataReconIds $dataIds | Where-Object { $_.SideIndicator -eq '<=' }).Count -eq 0) "Baseline data reconciliation is not a subset of canonical IDs."
Assert-Condition (@(Compare-Object $data02bIds $dataIds | Where-Object { $_.SideIndicator -eq '<=' }).Count -eq 0) "G1-02b data reconciliation is not a subset of canonical IDs."
Assert-Condition (@(Compare-Object $dataRound1bIds $dataIds | Where-Object { $_.SideIndicator -eq '<=' }).Count -eq 0) "G1-02 Round 1B data reconciliation is not a subset of canonical IDs."

$dataLines = Get-Content -LiteralPath $requirementsPath | Where-Object { $_ -match '^\| DR-[0-9]+ \|' }
foreach ($line in $dataLines) {
    Assert-Condition ($line -match 'CL-[A-Z0-9-]+') "Data Requirement lacks a current Claim ID linkage: $line"
}

$reconciliationText = Get-Content -Raw -LiteralPath $reconciliationPath
$reconciliation02bText = Get-Content -Raw -LiteralPath $reconciliation02bPath
Assert-Condition (($reconciliationText + $reconciliation02bText) -notmatch '\bLC[0-9]{4}\b') "Predecessor Claim ID found in current reconciliation control."
Assert-Condition (($reconciliationText + $reconciliation02bText) -notmatch '\bP[0-9]{4}\b') "Predecessor Paper ID found in current reconciliation control."

$hierarchyText = Get-Content -Raw -LiteralPath $hierarchyPath
$gatesText = Get-Content -Raw -LiteralPath $gatesPath
Assert-Condition ($hierarchyText -match 'G1-03.*NOT YET APPROVED/STARTED') "G1-03 must remain unauthorized during migration."
Assert-Condition ($gatesText -match 'G1-02 REOPENED.*G1-03 LOCKED') "Gate status must keep G1-03 locked while G1-02 review is reopened."

$unexpectedLibraryFiles = @(
    Get-ChildItem -LiteralPath $libraryPath -File -Recurse |
    Where-Object { $_.Name -ne '.gitkeep' }
)
Assert-Condition ($unexpectedLibraryFiles.Count -eq 0) "Migration must not import predecessor full text; found: $($unexpectedLibraryFiles.FullName -join ', ')"

[PSCustomObject]@{
    CanonicalClaims = $claimIds.Count
    BaselineReconciledClaims = $claimReconIds.Count
    G102bReconciledClaims = $claim02bIds.Count
    G102Round1bReconciledClaims = $claimRound1bIds.Count
    CanonicalDataRequirements = $dataIds.Count
    BaselineReconciledDataRequirements = $dataReconIds.Count
    G102bReconciledDataRequirements = $data02bIds.Count
    G102Round1bReconciledDataRequirements = $dataRound1bIds.Count
    DataRequirementsWithClaimLinkage = $dataLines.Count
    PredecessorIdentifiersInReconciliation = 'None'
    ImportedFullTexts = 0
    G103Status = 'LOCKED'
    Result = 'PASS'
} | Format-List
