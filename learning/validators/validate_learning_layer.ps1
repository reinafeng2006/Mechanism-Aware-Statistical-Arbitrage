$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '..\\..')
$required = @(
  'learning/README.md','learning/cards/economic_proximity.md','learning/cards/raw_price_distance.md','learning/cards/relationship_representations.md','learning/cards/residual_replication.md','learning/cards/stability_and_breaks.md','learning/cards/multiple_testing_fdr.md','learning/cards/global_matching_overlap.md','learning/cards/layer_separation.md',
  'learning/paper-guides/PF-001.md','learning/paper-guides/PF-004.md','learning/paper-guides/PF-006.md','learning/paper-guides/PF-007.md','learning/paper-guides/PF-008.md','learning/paper-guides/PF-013.md',
  'learning/cards/m1_information_diffusion.md','learning/cards/event_time_provenance.md','learning/cards/m2_pressure_identification.md','learning/paper-guides/M1-001.md','learning/paper-guides/M2-001.md','learning/paper-guides/M2-002.md','learning/paper-guides/M2-003.md','learning/paper-guides/M2-005.md','learning/paper-guides/B4-004.md','learning/walkthroughs/pair_validity.md','learning/walkthroughs/residual_and_fdr.md','learning/walkthroughs/m1_attribution_boundary.md','learning/MECHANISM_SIGNAL_MAP.md','learning/SIGNAL_MODEL_REGISTRY.md','learning/mechanisms/M0.md','learning/mechanisms/M1.md','learning/mechanisms/M2.md','learning/mechanisms/M3.md','learning/mechanisms/U.md','learning/dashboard/index.html','learning/dashboard/README.md','learning/RESEARCH_KNOWLEDGE_MAP.md')
foreach ($file in $required) { if (-not (Test-Path (Join-Path $root $file))) { throw "Missing learning artifact: $file" } }
$all = Get-ChildItem (Join-Path $root 'learning') -Recurse -File | Where-Object { $_.Directory.Name -ne 'validators' } | ForEach-Object { Get-Content -Raw $_.FullName }
$forbidden = '(?<!CL-)PF-003\\b','(?<!CL-)PF-012\\b','M1-002\\b'
foreach ($id in $forbidden) { if ($all -match $id) { throw "Prohibited non-completed-review ancestry in Learning Layer: $id" } }
$dashboard = Get-Content -Raw (Join-Path $root 'learning/dashboard/index.html')
foreach ($view in @('data-view="stage"','data-view="mechanism"','data-view="registry"','data-view="concept"','data-view="paper"')) { if ($dashboard -notmatch $view) { throw "Missing dashboard view: $view" } }
foreach ($stage in @('Company Representation','Industry-Specific Relationship Prior','Pair-Specific Normal Relationship','Continuous Pair-Specific Abnormality','Sequential Mechanism & Resolution Updating','Trade / Update / Reject / Abstain')) { if ($dashboard -notmatch [regex]::Escape($stage)) { throw "Missing active architecture element: $stage" } }
if ($dashboard -notmatch 'ILLUSTRATIVE / UNAUTHORIZED FORMULA') { throw 'Unfrozen formula label missing' }
if ($dashboard -notmatch 'Relationship / Rejection' -or $dashboard -notmatch 'Discriminator / Updating') { throw 'G2 measurement-family boundary missing' }
foreach ($state in @('M0','M1','M2','M3','U')) { if ($dashboard -notmatch ([regex]::Escape($state) + ':\{')) { throw "Missing mechanism drill-down data: $state" } }
foreach ($role in @('Relationship','Detection','Discriminator','Updating','Rejection','Resolution','Decision')) { if ($dashboard -notmatch "'$role'") { throw "Missing Signal Model Registry role: $role" } }
foreach ($boundary in @('WEAK / NON-IDENTIFIED','epistemic state — not mechanism','future signed follower catch-up；validation only','future source reversal/normalization；validation only','opposite-direction movement ≠ automatically abnormal','signal concept ≠ candidate measurement ≠ frozen factor ≠ model output ≠ trade rule')) { if ($dashboard -notmatch [regex]::Escape($boundary)) { throw "Missing mechanism/signal boundary: $boundary" } }
if ($dashboard -match 'P\(M3 \| F_t\)(?! would not create identifiability)') { throw 'M3 illustrative notation may not imply positive identification' }
if ((Get-Content -Raw (Join-Path $root 'docs/05_RESEARCH_GOVERNANCE.md')) -notmatch 'never evidence sources') { throw 'Evidence boundary missing' }
Write-Output 'PASS: Learning Layer is complete, bounded, and pedagogical only.'
