param(
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
)

$ErrorActionPreference = "Stop"

function Assert-Condition {
    param([bool]$Condition, [string]$Message)
    if (-not $Condition) { throw $Message }
}

$claimDirectory = Join-Path $RepositoryRoot "literature\claims"
$requiredClaims = @("CL-PF-006", "CL-PF-007", "CL-PF-008", "CL-B4-002")
$requiredFields = @(
    "claim_id:", "candidate_id:", "primary_question:", "construct_or_mechanism:", "pscr_role:",
    "full_text_basis:", "source_locator:", "claim_paraphrase:", "exact_observable_or_method:",
    "what_identified:", "what_not_identified:", "logic_chain:", "premise:", "measurement_identification:",
    "intermediate_evidence:", "inference:", "final_claim:", "limitations:",
    "point_in_time_causal_timing_limitations:", "sample_market_transferability:", "competing_explanations:",
    "missing_link:", "validation_test_needed:", "project_testability:", "data_requirement_ids:",
    "permitted_g2_candidate_use:", "prohibited_interpretations:", "review_depth:", "evidence_direction:",
    "ancestry:", "status:"
)

foreach ($claimId in $requiredClaims) {
    $path = Join-Path $claimDirectory "$claimId.yaml"
    Assert-Condition (Test-Path -LiteralPath $path) "Missing G1-02b claim record: $path"
    $text = Get-Content -Raw -LiteralPath $path
    foreach ($field in $requiredFields) {
        Assert-Condition ($text -match [regex]::Escape($field)) "Missing '$field' in $claimId"
    }
    Assert-Condition ($text -match "claim_id: $claimId") "Claim ID mismatch in $claimId"
    Assert-Condition ($text -match "status: PROVISIONAL_G1_02") "G1-02b status must remain provisional in $claimId"
    Assert-Condition ($text -notmatch '\bLC[0-9]{4}\b|\bP[0-9]{4}\b') "Predecessor identifier found in $claimId"
}

$gates = Get-Content -Raw -LiteralPath (Join-Path $RepositoryRoot "docs\GATES.md")
Assert-Condition ($gates -match "G1-02 REOPENED.*G1-03 LOCKED") "G1-03 must remain locked while G1-02 review is reopened"

[PSCustomObject]@{
    ValidatedG102bClaims = $requiredClaims.Count
    RequiredSchemaFields = $requiredFields.Count
    G103Status = "LOCKED; G1-02 REOPENED"
    Result = "PASS"
} | Format-List
