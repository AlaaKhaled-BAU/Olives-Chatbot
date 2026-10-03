# Starts the Olives chatbot API on Windows
$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

if (-not (Test-Path ".env")) {
    Write-Host "ERROR: .env file not found. Copy .env.example to .env and configure it." -ForegroundColor Red
    exit 1
}

# Load .env variables into process environment
Get-Content ".env" | ForEach-Object {
    $line = $_.Trim()
    if ($line -and -not $line.StartsWith("#") -and $line.Contains("=")) {
        $parts = $line.Split("=", 2)
        $key = $parts[0].Trim()
        $val = $parts[1].Trim()
        [System.Environment]::SetEnvironmentVariable($key, $val, "Process")
    }
}

if (-not [System.Environment]::GetEnvironmentVariable("DEEPSEEK_API_KEY")) {
    Write-Host "ERROR: DEEPSEEK_API_KEY not set in .env" -ForegroundColor Red
    exit 1
}

$port = if ($env:PORT) { $env:PORT } else { "8100" }
Write-Host "Starting chatbot API on :$port (127.0.0.1)..." -ForegroundColor Cyan

# Detect Python 3.13 launcher (py -3.13) or python
$pyCmd = "py"
$pyArgs = @("-3.13", "-m", "uvicorn", "api.server:app", "--host", "127.0.0.1", "--port", $port)
try {
    & py -3.13 --version >$null 2>&1
} catch {
    $pyCmd = "python"
    $pyArgs = @("-m", "uvicorn", "api.server:app", "--host", "127.0.0.1", "--port", $port)
}

Write-Host "Olives Chatbot: http://localhost:$port" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the API server." -ForegroundColor Yellow

& $pyCmd $pyArgs
