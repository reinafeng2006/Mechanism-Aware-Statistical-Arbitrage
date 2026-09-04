$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '..\\..')
$required = @(
  'learning/README.md','learning/cards/economic_proximity.md','learning/cards/raw_price_distance.md','learning/cards/relationship_representations.md','learning/cards/residual_replication.md','learning/cards/stability_and_breaks.md','learning/cards/multiple_testing_fdr.md','learning/cards/global_matching_overlap.md','learning/cards/layer_separation.md',
  'learning/paper-guides/PF-001.md','learning/paper-guides/PF-004.md','learning/paper-guides/PF-006.md','learning/paper-guides/PF-007.md','learning/paper-guides/PF-008.md','learning/paper-guides/PF-013.md',
  'learning/walkthroughs/pair_validity.md','learning/walkthroughs/residual_and_fdr.md','learning/dashboard/index.html','learning/dashboard/README.md')
foreach ($file in $required) { if (-not (Test-Path (Join-Path $root $file))) { throw "Missing learning artifact: $file" } }
$all = Get-ChildItem (Join-Path $root 'learning') -Recurse -File | Where-Object { $_.Directory.Name -ne 'validators' } | ForEach-Object { Get-Content -Raw $_.FullName }
$forbidden = '(?<!CL-)PF-003\\b','(?<!CL-)PF-012\\b','M1-001\\b','M1-002\\b','M1-008\\b'
foreach ($id in $forbidden) { if ($all -match $id) { throw "Prohibited non-completed-review ancestry in Learning Layer: $id" } }
$dashboard = Get-Content -Raw (Join-Path $root 'learning/dashboard/index.html')
foreach ($view in @('data-view="stage"','data-view="concept"','data-view="paper"')) { if ($dashboard -notmatch $view) { throw "Missing dashboard view: $view" } }
if ((Get-Content -Raw (Join-Path $root 'docs/LEARNING_LAYER.md')) -notmatch 'never evidence sources') { throw 'Evidence boundary missing' }
Write-Output 'PASS: Learning Layer is complete, bounded, and pedagogical only.'
