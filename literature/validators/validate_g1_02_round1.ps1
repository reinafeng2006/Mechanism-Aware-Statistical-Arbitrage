param([string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path)
$ErrorActionPreference = "Stop"
function Assert-Condition { param([bool]$Condition, [string]$Message) if (-not $Condition) { throw $Message } }
$ids = @("PF-001", "PF-004", "PF-006", "PF-007", "PF-008", "PF-013")
$claims = @{"PF-001"="CL-PF-001"; "PF-004"="CL-PF-002"; "PF-008"="CL-PF-003"; "PF-006"="CL-PF-004"; "PF-007"="CL-PF-005"; "PF-013"="CL-PF-006"}
$fields = @("full_text_basis:", "what_identified:", "what_not_identified:", "logic_chain:", "competing_explanations:", "missing_link:", "validation_test_needed:", "project_testability:", "point_in_time_causal_timing_limitations:", "permitted_g2_candidate_use:")
foreach ($id in $ids) {
  $review = Join-Path $RepositoryRoot "literature\reviews\$id.md"
  $claimId = $claims[$id]; $claim = Join-Path $RepositoryRoot "literature\claims\$claimId.yaml"
  Assert-Condition (Test-Path $review) "Missing review artifact: $id"
  Assert-Condition (Test-Path $claim) "Missing claim schema: $claimId"
  $text = Get-Content -Raw $claim
  foreach ($field in $fields) { Assert-Condition ($text -match [regex]::Escape($field)) "Missing $field in $claimId" }
  Assert-Condition ($text -match "review_completion: SELECTIVE_DEEP_VERIFIED_G1_02_ROUND_1") "Unverified completion in $claimId"
}
$gate = Get-Content -Raw (Join-Path $RepositoryRoot "docs\05_RESEARCH_GOVERNANCE.md")
Assert-Condition ($gate -match "G1 Literature & Mechanism Evidence.*PASS / FROZEN") "G1 must remain frozen after the completed review lineage"
[PSCustomObject]@{VerifiedSelectiveDeepReviews=$ids.Count; G1Status="PASS_FROZEN"; Result="PASS"} | Format-List
