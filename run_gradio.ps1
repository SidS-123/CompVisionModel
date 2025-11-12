# Helper to activate .venv-gradio and launch the Gradio app (PowerShell)
param(
    [string]$VenvPath = ".\.venv-gradio",
    [string]$App = "app.py"
)

if (-not (Test-Path $VenvPath)) {
    Write-Host "Virtual environment '$VenvPath' not found. Create it with:`npython -m venv $VenvPath`" -ForegroundColor Yellow
    exit 1
}

# Ensure the script can run activation
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$activate = Join-Path $VenvPath 'Scripts\Activate.ps1'
if (-not (Test-Path $activate)) {
    Write-Host "Activation script not found at $activate" -ForegroundColor Red
    exit 1
}

. $activate
Write-Host "Activated virtual environment: $VenvPath"

python $App
