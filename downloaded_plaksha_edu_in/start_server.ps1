# PowerShell Quick Start Script for Plaksha RAG Chatbot

Write-Host "`n" -NoNewline
Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host "  Plaksha University RAG Chatbot - Start Script" -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan

# Check if running as administrator for environment variable setting
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object System.Security.Principal.WindowsPrincipal($currentUser)

# Check if OpenAI API key is set
$apiKey = [System.Environment]::GetEnvironmentVariable("OPENAI_API_KEY")

if ([string]::IsNullOrEmpty($apiKey)) {
    Write-Host "`nERROR: OPENAI_API_KEY environment variable is not set!" -ForegroundColor Red
    Write-Host "`nPlease set your OpenAI API key:" -ForegroundColor Yellow
    Write-Host "`n  `$env:OPENAI_API_KEY = 'your-openai-api-key-here'" -ForegroundColor Green
    Write-Host "`nThen run this script again." -ForegroundColor Yellow
    Write-Host "`nGet your API key from: https://platform.openai.com/api-keys" -ForegroundColor Cyan
    Write-Host "`n"
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "`n✓ OpenAI API key detected" -ForegroundColor Green

# Check Python version
Write-Host "`nChecking Python installation..." -ForegroundColor Cyan
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion found" -ForegroundColor Green
}
catch {
    Write-Host "✗ Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "`nPlease install Python from: https://www.python.org/" -ForegroundColor Cyan
    Read-Host "Press Enter to exit"
    exit 1
}

# Install dependencies
Write-Host "`nInstalling dependencies..." -ForegroundColor Cyan
pip install -q -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Some dependencies may not have installed correctly" -ForegroundColor Yellow
}
else {
    Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
}

# Start the server
Write-Host "`n=====================================================" -ForegroundColor Cyan
Write-Host "  Starting FastAPI Server..." -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host "`nServer will run on: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Once ready, open index.html in your web browser" -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop the server`n" -ForegroundColor Yellow

# Run the server
uvicorn app:app --reload --host 0.0.0.0 --port 8000
