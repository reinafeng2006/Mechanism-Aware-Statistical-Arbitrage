param([Parameter(Position=0)][ValidateSet('status','run','resume','validate')][string]$Command='status')
$ErrorActionPreference = 'Stop'
$repo = [System.IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$python = [System.IO.Path]::GetFullPath('C:\Users\rfeng\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe')
$batchRunner = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot 'v1_a1_h126_synthesis_batch.py'))
$materializer = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot 'v1_a1_h126_candidate_neutral.py'))
$logRoot = 'D:\MechanismAwareStatArbData\A1_H126\synthesis_checkpoint_v1\logs'
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
$log = Join-Path $logRoot ("{0}.log" -f $Command)
$started = Get-Date -Format o
"[$started] command=$Command repo=$repo python=$python runner=$batchRunner" | Add-Content -LiteralPath $log -Encoding utf8
try {
    if (-not (Test-Path -LiteralPath $python -PathType Leaf)) { throw "Python executable not found: $python" }
    if (-not (Test-Path -LiteralPath $batchRunner -PathType Leaf)) { throw "Batch runner not found: $batchRunner" }
    if ($batchRunner -eq $materializer -or [System.IO.Path]::GetFileName($batchRunner) -ne 'v1_a1_h126_synthesis_batch.py') {
        throw "Refusing non-batch H126 entrypoint: $batchRunner"
    }
    Push-Location -LiteralPath $repo
    try {
        & $python $batchRunner $Command 2>&1 | ForEach-Object {
            $line = [string]$_
            Write-Output $line
            $line | Add-Content -LiteralPath $log -Encoding utf8
        }
        $pythonExitCode = $LASTEXITCODE
    } finally {
        Pop-Location
    }
    if ($pythonExitCode -ne 0) { throw "H126 synthesis batch runner failed with exit code $pythonExitCode" }
} catch {
    "[$(Get-Date -Format o)] STARTUP_OR_RUN_FAILURE: $($_.Exception.Message)" | Add-Content -LiteralPath $log -Encoding utf8
    throw
}
