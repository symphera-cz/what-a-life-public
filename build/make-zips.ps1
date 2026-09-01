# Zabalí každý skill do samostatného ZIPu pro nahrání na claude.ai
# Spuštění z kořene repa:  .\build\make-zips.ps1

$root = Split-Path -Parent $PSScriptRoot
$src  = Join-Path $root "plugins\what-a-life\skills"
$dist = Join-Path $root "dist"

if (-not (Test-Path $dist)) { New-Item -ItemType Directory -Path $dist | Out-Null }

# Maž jen ZIPy — v dist/ jsou i ručně udržované soubory (xlsx šablona, balíček pro ChatGPT)
Remove-Item (Join-Path $dist "*.zip") -Force -ErrorAction SilentlyContinue

Get-ChildItem $src -Directory | ForEach-Object {
    $zip = Join-Path $dist "$($_.Name).zip"
    Compress-Archive -Path $_.FullName -DestinationPath $zip -Force
    Write-Host "OK  $($_.Name).zip"
}

Write-Host ""
Write-Host "Hotovo. ZIPy jsou v: $dist"
Write-Host "Nahrání: claude.ai -> Customize -> Skills -> + -> Upload a skill"
