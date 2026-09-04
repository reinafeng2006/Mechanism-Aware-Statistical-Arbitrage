param([string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path)
$ErrorActionPreference = 'Stop'

function Assert-Doc($condition, $message) { if (-not $condition) { throw $message } }

$canonical = 0..5 | ForEach-Object { Join-Path $RepositoryRoot ("docs\{0:D2}_" -f $_) }
$rootDocs = @(Get-ChildItem (Join-Path $RepositoryRoot 'docs') -File -Filter '*.md')
Assert-Doc ($rootDocs.Count -eq 6) "docs root must contain exactly six canonical Markdown files."
foreach ($prefix in $canonical) { Assert-Doc (@(Get-ChildItem ((Split-Path $prefix) + '\' + (Split-Path $prefix -Leaf) + '*.md')).Count -eq 1) "Missing or duplicate canonical prefix: $prefix" }

$mapPath = Join-Path $RepositoryRoot 'docs\archive\DOCUMENTATION_MIGRATION_MAP.md'
$mapText = Get-Content -Raw -LiteralPath $mapPath
$mapped = [regex]::Matches($mapText, '(?m)^\| `(?<old>docs/[^`]+)` \| `(?<new>docs/[^`]+)` \|')
Assert-Doc ($mapped.Count -eq 30) "Migration map must reconcile exactly 30 pre-refactor docs; found $($mapped.Count)."
foreach ($m in $mapped) {
    $old = Join-Path $RepositoryRoot ($m.Groups['old'].Value -replace '/', '\')
    $new = Join-Path $RepositoryRoot ($m.Groups['new'].Value -replace '/', '\')
    Assert-Doc (Test-Path -LiteralPath $new) "Mapped target missing: $new"
    Assert-Doc (-not (Test-Path -LiteralPath $old)) "Old flat path still exists: $old"
}

$broken = @()
Get-ChildItem $RepositoryRoot -Recurse -File -Filter '*.md' | ForEach-Object {
    $file = $_
    $text = Get-Content -Raw -LiteralPath $file.FullName
    foreach ($match in [regex]::Matches($text, '\[[^\]]*\]\(([^)]+)\)')) {
        $target = $match.Groups[1].Value.Trim()
        if ($target -match '^(https?://|mailto:|#)') { continue }
        $pathPart = ($target -split '#')[0]
        if ([string]::IsNullOrWhiteSpace($pathPart)) { continue }
        $resolved = [System.IO.Path]::GetFullPath((Join-Path $file.DirectoryName $pathPart))
        if (-not (Test-Path -LiteralPath $resolved)) { $broken += "$($file.FullName): $target" }
    }
}
Assert-Doc ($broken.Count -eq 0) "Broken Markdown links:`n$($broken -join "`n")"

$thesis = Get-Content -Raw (Join-Path $RepositoryRoot 'docs\01_ECONOMIC_THESIS.md')
$architecture = Get-Content -Raw (Join-Path $RepositoryRoot 'docs\02_STRATEGY_ARCHITECTURE.md')
$evidence = Get-Content -Raw (Join-Path $RepositoryRoot 'docs\03_LITERATURE_EVIDENCE.md')
$measurement = Get-Content -Raw (Join-Path $RepositoryRoot 'docs\04_MEASUREMENT_DESIGN.md')
$governance = Get-Content -Raw (Join-Path $RepositoryRoot 'docs\05_RESEARCH_GOVERNANCE.md')
Assert-Doc ($thesis -match 'FROZEN / PASS' -and $thesis -match 'M0–M3 are falsifiable working hypotheses') 'Frozen G0 thesis boundary missing.'
Assert-Doc ($architecture -match 'Sequential Mechanism & Resolution Updating' -and $architecture -match 'U = Unresolved / Abstain') 'Active sequential architecture boundary missing.'
Assert-Doc ($evidence -match 'G1 PASS / FROZEN' -and $evidence -match 'NOT PERMITTED FOR DESIGN JUSTIFICATION') 'G1 freeze or permission boundary missing.'
Assert-Doc (($measurement.Contains('G2 ACTIVE — DESIGN ONLY')) -and ($measurement.Contains('G2-01 through G2-05 APPROVED / FROZEN')) -and ($measurement.Contains('G2-06 is not authorized'))) 'G2-05 freeze or design-only boundary missing.'
Assert-Doc ($governance -match 'G3 Point-in-Time Data & Database \| \*\*LOCKED' -and $governance -match 'Empirical work, data acquisition, implementation and outcome inspection remain unauthorized') 'Empirical authorization boundary changed.'
Assert-Doc ($governance -match 'Canonical docs = current truth' -and $governance -match 'Stage docs = active working state' -and $governance -match 'Archive = completed historical process') 'Documentation rule missing.'

[pscustomobject]@{
    PreRefactorDocsReconciled = $mapped.Count
    LostFiles = 0
    BrokenMarkdownLinks = $broken.Count
    CanonicalRootDocs = $rootDocs.Count
    G1Status = 'FROZEN'
    G2Status = 'ACTIVE_DESIGN_ONLY_G205_FROZEN_G206_NOT_AUTHORIZED'
    EmpiricalAuthorization = 'UNCHANGED_LOCKED'
    Result = 'PASS'
} | Format-List
