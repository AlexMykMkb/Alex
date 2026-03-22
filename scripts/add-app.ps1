param(
    [Parameter(Mandatory = $true)]
    [string]$Name
)

$root = Split-Path -Parent $PSScriptRoot
$appRoot = Join-Path $root "apps\$Name"

if (Test-Path $appRoot) {
    Write-Error "L'application '$Name' existe déjà."
    exit 1
}

New-Item -ItemType Directory -Path $appRoot | Out-Null
New-Item -ItemType Directory -Path (Join-Path $appRoot "backend") | Out-Null
New-Item -ItemType Directory -Path (Join-Path $appRoot "frontend") | Out-Null

@"
# $Name

## Démarrage

- Backend: `apps/$Name/backend`
- Frontend: `apps/$Name/frontend`
"@ | Set-Content -Path (Join-Path $appRoot "README.md") -Encoding UTF8

"# Variables d'environnement de $Name" | Set-Content -Path (Join-Path $appRoot ".env.example") -Encoding UTF8

Write-Host "Application créée: $appRoot" -ForegroundColor Green
