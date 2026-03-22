param(
    [int]$Port = 8000,
    [string]$BindAddress = "127.0.0.1",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$projectRoot = $PSScriptRoot
$managePath = Join-Path $projectRoot "manage.py"

if (-not (Test-Path $managePath)) {
    throw "manage.py introuvable dans $projectRoot"
}

$pythonCandidates = @(
    (Join-Path $projectRoot ".venv\Scripts\python.exe"),
    "c:\workspace\laguerison\.venv\Scripts\python.exe"
)

$pythonExe = $pythonCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $pythonExe) {
    $pythonExe = "python"
}

$serverArgs = @($managePath, "runserver", "$BindAddress`:$Port")
$tunnelArgs = @("-T", "-o", "StrictHostKeyChecking=no", "-R", "80:localhost:$Port", "nokey@localhost.run")

Write-Host "Projet: $projectRoot"
Write-Host "Python: $pythonExe"
Write-Host "Serveur: http://${BindAddress}:$Port"

if ($DryRun) {
    Write-Host "DryRun OK."
    exit 0
}

$serverProcess = Start-Process -FilePath $pythonExe -ArgumentList $serverArgs -WorkingDirectory $projectRoot -PassThru -WindowStyle Hidden
Start-Sleep -Seconds 3

try {
    $health = Invoke-WebRequest -Uri "http://${BindAddress}:$Port/" -UseBasicParsing -TimeoutSec 10
    if ($health.StatusCode -ne 200) {
        throw "Le serveur local ne répond pas correctement (HTTP $($health.StatusCode))."
    }

    Write-Host "Tunnel public en cours..."
    Write-Host "L'URL publique sera copiée automatiquement dans le presse-papiers."
    Write-Host "Arrêt: Ctrl+C"

    $urlCopied = $false

    & ssh @tunnelArgs 2>&1 | ForEach-Object {
        $line = $_.ToString()
        Write-Host $line

        if (-not $urlCopied) {
            $match = [regex]::Match($line, 'https://[a-zA-Z0-9.-]+')
            if ($match.Success) {
                $publicUrl = $match.Value
                Set-Clipboard -Value $publicUrl
                Write-Host "URL copiée dans le presse-papiers: $publicUrl" -ForegroundColor Green
                $urlCopied = $true
            }
        }
    }
}
finally {
    if ($serverProcess -and -not $serverProcess.HasExited) {
        Stop-Process -Id $serverProcess.Id -Force
    }
}
