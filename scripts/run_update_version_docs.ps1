#Requires -Version 5.1
<#
.SYNOPSIS
  Wrapper local da automação version-docs (Cursor SDK + gh).
#>
[CmdletBinding()]
param(
    [switch]$PreflightOnly,
    [string]$Model = $env:CURSOR_MODEL
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LogDir = Join-Path $RepoRoot ".cursor\automation-logs"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$LogFile = Join-Path $LogDir "version-docs-$Stamp.log"

function Write-Log([string]$Message) {
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
    Add-Content -Path $LogFile -Value $line -Encoding UTF8
    Write-Host $line
}

Write-Log "Repo: $RepoRoot"
Write-Log "Log: $LogFile"

# Prefer venv python
$VenvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
if (Test-Path $VenvPython) {
    $Python = $VenvPython
} else {
    $PythonCmd = Get-Command python -ErrorAction SilentlyContinue
    if (-not $PythonCmd) {
        Write-Log "ERRO: python não encontrado. Crie .venv e instale requirements.txt"
        exit 1
    }
    $Python = $PythonCmd.Source
}

Write-Log "Python: $Python"

# Ensure gh is findable for scheduled tasks
$GhDir = "C:\Program Files\GitHub CLI"
if (Test-Path (Join-Path $GhDir "gh.exe")) {
    if ($env:Path -notlike "*$GhDir*") {
        $env:Path = "$GhDir;$env:Path"
        Write-Log "PATH atualizado com GitHub CLI"
    }
}

$Script = Join-Path $PSScriptRoot "update_version_docs.py"
$Args = @($Script)
if ($PreflightOnly) {
    $Args += "--preflight-only"
}
if ($Model) {
    $Args += @("--model", $Model)
}

Write-Log ("Executando: {0} {1}" -f $Python, ($Args -join " "))

$proc = Start-Process -FilePath $Python `
    -ArgumentList $Args `
    -WorkingDirectory $RepoRoot `
    -NoNewWindow `
    -Wait `
    -PassThru `
    -RedirectStandardOutput (Join-Path $LogDir "version-docs-$Stamp.stdout.log") `
    -RedirectStandardError (Join-Path $LogDir "version-docs-$Stamp.stderr.log")

$stdoutPath = Join-Path $LogDir "version-docs-$Stamp.stdout.log"
$stderrPath = Join-Path $LogDir "version-docs-$Stamp.stderr.log"
if (Test-Path $stdoutPath) {
    Get-Content $stdoutPath -Encoding UTF8 | ForEach-Object {
        Write-Host $_
        Add-Content -Path $LogFile -Value $_ -Encoding UTF8
    }
}
if (Test-Path $stderrPath) {
    Get-Content $stderrPath -Encoding UTF8 | ForEach-Object {
        Write-Host $_
        Add-Content -Path $LogFile -Value $_ -Encoding UTF8
    }
}

Write-Log ("Exit code: {0}" -f $proc.ExitCode)
exit $proc.ExitCode
