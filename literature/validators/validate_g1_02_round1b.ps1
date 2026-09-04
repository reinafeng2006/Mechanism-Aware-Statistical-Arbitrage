param([string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path)
$ErrorActionPreference = "Stop"
function Assert-Condition { param([bool]$Condition, [string]$Message) if (-not $Condition) { throw $Message } }
foreach ($id in @("PF-005", "PF-010")) { Assert-Condition (Test-Path (Join-Path $RepositoryRoot "literature\reviews\$id.md")) "Missing completed Round 1B artifact: $id" }
foreach ($id in @("PF-003", "PF-012")) {
  $path = Join-Path $RepositoryRoot "literature\reviews\$id.md"; Assert-Condition (Test-Path $path) "Missing access record: $id"
  Assert-Condition ((Get-Content -Raw $path) -match "NOT ADMITTED FOR SUBSTANTIVE REVIEW") "Blocked paper must not be represented as reviewed: $id"
}
foreach ($id in @("CL-PF-009", "CL-PF-010")) {
  $text = Get-Content -Raw (Join-Path $RepositoryRoot "literature\claims\$id.yaml")
  Assert-Condition ($text -match "review_completion: LIGHT_VERIFIED_G1_02_ROUND_1B") "Round 1B claim lacks verified Light review: $id"
  foreach ($field in @("what_identified:", "what_not_identified:", "logic_chain:", "missing_link:", "validation_test_needed:", "project_testability:")) { Assert-Condition ($text -match [regex]::Escape($field)) "Missing $field in $id" }
}
$checkpoint = Get-Content -Raw (Join-Path $RepositoryRoot "docs\archive\G1\G1_02_ROUND_1B_PAIR_FORMATION.md")
Assert-Condition ($checkpoint -match "SATURATED SUBJECT TO UNRESOLVED SOURCE ACCESS") "Round 1B saturation decision must preserve unresolved source access"
Assert-Condition ($checkpoint -match "No claim from PF-003/PF-012 was admitted") "Blocked-source non-admission must be explicit"
[PSCustomObject]@{LightReviews=2; UnresolvedSourceAccess=2; PairFormationSaturation="SATURATED SUBJECT TO UNRESOLVED SOURCE ACCESS"; Result="PASS"} | Format-List
