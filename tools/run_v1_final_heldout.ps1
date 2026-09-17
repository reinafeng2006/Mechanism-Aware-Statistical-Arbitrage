param([Parameter(Position=0)][ValidateSet('status','run','resume','validate')][string]$Command='status')
$ErrorActionPreference = 'Stop'
$repo = [System.IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$python = [System.IO.Path]::GetFullPath('C:\Users\rfeng\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe')
$runner = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot 'v1_final_heldout_batch.py'))
$logRoot = 'D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1\logs'
$scratch = 'D:\MechanismAwareStatArbData\FINAL_HELDOUT_V1\_temp'
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
New-Item -ItemType Directory -Force -Path $scratch | Out-Null
$log = Join-Path $logRoot ("{0}.log" -f $Command)
"[$(Get-Date -Format o)] command=$Command repo=$repo runner=$runner" | Add-Content -LiteralPath $log -Encoding utf8
try {
    if (-not (Test-Path -LiteralPath $python -PathType Leaf)) { throw "Python executable not found: $python" }
    if (-not (Test-Path -LiteralPath $runner -PathType Leaf)) { throw "Held-out runner not found: $runner" }
    Push-Location -LiteralPath $repo
    try {
        $psi = [System.Diagnostics.ProcessStartInfo]::new()
        $psi.FileName = $python; $psi.Arguments = "`"$runner`" $Command"
        $psi.UseShellExecute = $false; $psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true; $psi.CreateNoWindow = $true
        $psi.Environment['TEMP'] = $scratch; $psi.Environment['TMP'] = $scratch
        foreach ($name in @('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS')) { $psi.Environment[$name] = '1' }
        $psi.Environment['V1_R4_WORKERS'] = '4'
        $process = [System.Diagnostics.Process]::new(); $process.StartInfo = $psi
        if (-not $process.Start()) { throw 'Failed to start final held-out runner' }
        $stdout = $process.StandardOutput.ReadToEnd(); $stderr = $process.StandardError.ReadToEnd(); $process.WaitForExit()
        foreach ($text in @($stdout,$stderr)) { if (-not [string]::IsNullOrEmpty($text)) { Write-Output $text.TrimEnd(); $text | Add-Content -LiteralPath $log -Encoding utf8 } }
        if ($process.ExitCode -ne 0) { throw "Final held-out runner failed with exit code $($process.ExitCode); see $log" }
    } finally { Pop-Location }
} catch {
    "[$(Get-Date -Format o)] STARTUP_OR_RUN_FAILURE: $($_.Exception.ToString())" | Add-Content -LiteralPath $log -Encoding utf8
    throw
}
