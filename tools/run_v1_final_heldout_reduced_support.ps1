param([ValidateSet('status','run','resume','validate','dry-run')][string]$Command='status')
$ErrorActionPreference = 'Stop'
$Repo = Split-Path -Parent $PSScriptRoot
$Root = 'D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1'
$LogDir = Join-Path $Root 'logs'
$Log = Join-Path $LogDir 'reduced_support_run.log'
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$Scratch = Join-Path $Root '_temp'
New-Item -ItemType Directory -Force -Path $Scratch | Out-Null
$env:TEMP = $Scratch
$env:TMP = $Scratch
$env:OMP_NUM_THREADS = '1'
$env:OPENBLAS_NUM_THREADS = '1'
$env:MKL_NUM_THREADS = '1'
Set-Location -LiteralPath $Repo
$Python = Join-Path $Repo '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $Python)) { $Python = 'python' }
try {
  $ErrorActionPreference = 'Continue'
  & $Python (Join-Path $Repo 'tools\v1_final_heldout_reduced_support.py') $Command 2>&1 | Tee-Object -FilePath $Log -Append
  $ExitCode = $LASTEXITCODE
  $ErrorActionPreference = 'Stop'
  if ($ExitCode -ne 0) { throw "runner exited with code $ExitCode" }
} catch {
  $_ | Out-String | Add-Content -LiteralPath $Log
  throw
}
