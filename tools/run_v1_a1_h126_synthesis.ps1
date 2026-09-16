param([Parameter(Position=0)][ValidateSet('status','run','resume','validate')][string]$Command='status')
$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
$python = 'C:\Users\rfeng\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$runner = Join-Path $PSScriptRoot 'v1_a1_h126_synthesis_batch.py'
$logRoot = 'D:\MechanismAwareStatArbData\A1_H126\synthesis_checkpoint_v1\logs'
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
$log = Join-Path $logRoot ("{0}.log" -f $Command)
Set-Location -LiteralPath $repo
& $python $runner $Command 2>&1 | Tee-Object -FilePath $log -Append
if ($LASTEXITCODE -ne 0) { throw "H126 synthesis runner failed with exit code $LASTEXITCODE" }
