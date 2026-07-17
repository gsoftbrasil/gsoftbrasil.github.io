#Requires -Version 5.1
<#
.SYNOPSIS
  Instala/atualiza tarefa diária da automação version-docs (18:00 horário local).
#>
[CmdletBinding()]
param(
    [string]$TaskName = "Gsoft-VersionDocs-Daily",
    [string]$Time = "18:00"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Wrapper = Join-Path $PSScriptRoot "run_update_version_docs.ps1"

if (-not (Test-Path $Wrapper)) {
    throw "Wrapper não encontrado: $Wrapper"
}

# Parse HH:mm
try {
    $at = [DateTime]::ParseExact($Time, "HH:mm", [Globalization.CultureInfo]::InvariantCulture)
} catch {
    throw "Horário inválido '$Time'. Use HH:mm (ex.: 18:00)."
}

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument ("-NoProfile -ExecutionPolicy Bypass -File `"{0}`"" -f $Wrapper) `
    -WorkingDirectory $RepoRoot

$trigger = New-ScheduledTaskTrigger -Daily -At $at

$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2)

# Executa como usuário atual logado (herda CURSOR_API_KEY / gh do perfil)
$principal = New-ScheduledTaskPrincipal `
    -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel Limited

$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Tarefa existente removida: $TaskName"
}

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description "Atualiza documentação version/* via Cursor SDK local + gh e abre PR quando houver mudanças." |
    Out-Null

Write-Host "Tarefa registrada: $TaskName"
Write-Host "Horário: diário às $Time (horário local)"
Write-Host "Wrapper: $Wrapper"
Write-Host "Usuário: $env:USERDOMAIN\$env:USERNAME"
Write-Host ""
Write-Host "Importante: configure CURSOR_API_KEY em `.env` na raiz (copie de `.env.example`)."
Write-Host "Alternativa: variável de ambiente do USUÁRIO Windows."
Write-Host "Teste manual: powershell -NoProfile -ExecutionPolicy Bypass -File `"$Wrapper`" -PreflightOnly"
Write-Host "Listar: Get-ScheduledTask -TaskName $TaskName"
Write-Host "Rodar agora: Start-ScheduledTask -TaskName $TaskName"
