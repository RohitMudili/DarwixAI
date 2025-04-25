# PowerShell script to set up ngrok tunneling
Write-Host "Setting up ngrok tunnel for Speech-to-Text API..." -ForegroundColor Green

# Check if ngrok is installed
try {
    $ngrokVersion = ngrok --version
    Write-Host "ngrok is installed: $ngrokVersion" -ForegroundColor Green
} catch {
    Write-Host "ngrok is not installed. Please install it from https://ngrok.com/download" -ForegroundColor Red
    Write-Host "After installation, run this script again." -ForegroundColor Yellow
    exit
}

# Start the FastAPI server in the background
Write-Host "Starting FastAPI server in the background..." -ForegroundColor Green
Start-Process -NoNewWindow -FilePath "uvicorn" -ArgumentList "app:app", "--host", "0.0.0.0", "--port", "8000"

# Wait for the server to start
Write-Host "Waiting for server to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Start ngrok tunnel
Write-Host "Starting ngrok tunnel..." -ForegroundColor Green
Write-Host "Your API will be available at the ngrok URL + /transcribe" -ForegroundColor Cyan
Write-Host "Example: https://abc123.ngrok.io/transcribe" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the tunnel" -ForegroundColor Yellow

# Start ngrok
ngrok http 8000 