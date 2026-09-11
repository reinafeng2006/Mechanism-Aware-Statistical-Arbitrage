$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$nextActionPath = Join-Path $PSScriptRoot 'NEXT_ACTION.json'
$statePath = Join-Path $PSScriptRoot 'AGENT_STATE.md'
$policyPath = Join-Path $PSScriptRoot 'AGENT_POLICY.md'
$rootPolicyPath = Join-Path $repoRoot 'AGENTS.md'
$contractPath = Join-Path $PSScriptRoot 'G4_05_MODEL_SPECIFICATION_CONTRACT.json'

foreach ($path in @($nextActionPath, $statePath, $policyPath, $rootPolicyPath, $contractPath)) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing control artifact: $path" }
}

$next = Get-Content -Raw -LiteralPath $nextActionPath | ConvertFrom-Json
if ($null -eq $next.action) { throw 'NEXT_ACTION must contain exactly one action object.' }
if ($next.action -is [System.Array]) { throw 'NEXT_ACTION action must not be an array.' }
if ([string]::IsNullOrWhiteSpace([string]$next.action.action_id)) { throw 'NEXT_ACTION action_id is required.' }

$state = Get-Content -Raw -LiteralPath $statePath
if ($state -notmatch 'CORE-DATASET-FREEZE-V1') { throw 'Agent state lacks the frozen dataset ID.' }
if ($state -notmatch '3952FC92E5AB88787E82AE5629609C87150035A449A3D31C6030D0ADEE0C3616') { throw 'Agent state lacks the frozen root fingerprint.' }
if ($state -notmatch 'SEALED') { throw 'Agent state does not preserve the held-out seal.' }

$contract = Get-Content -Raw -LiteralPath $contractPath | ConvertFrom-Json
if ($contract.computation_gate -ne 'DENIED_UNTIL_ALL_BINDINGS_FROZEN_AND_RESEARCHER_AUTHORIZED') { throw 'Model computation gate is not closed.' }

Write-Output 'PASS: bounded agent control state and G4-05 computation gate are structurally valid.'

