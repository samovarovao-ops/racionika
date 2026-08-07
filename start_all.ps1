Write-Host "Stopping services..."
Stop-Process -Name python, node -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2

Write-Host "Starting backend..."
Start-Process -FilePath "python" -ArgumentList "-m uvicorn backend.main:app --host 0.0.0.0 --port 8000" -WorkingDirectory $PSScriptRoot -WindowStyle Hidden
Start-Sleep -Seconds 3

try {
    $r = Invoke-WebRequest -Uri "http://localhost:8000/api/health" -TimeoutSec 5
    Write-Host "Backend OK: $($r.StatusCode)"
} catch {
    Write-Host "Backend FAILED"
}

Write-Host "Starting bot..."
Start-Process -FilePath "python" -ArgumentList "-X utf8 bot\main.py" -WorkingDirectory $PSScriptRoot -WindowStyle Hidden

Write-Host "Starting frontend..."
Start-Process -FilePath "node" -ArgumentList "C:\temp\frontend_server.js" -WorkingDirectory $PSScriptRoot -WindowStyle Hidden

Start-Sleep -Seconds 2
Write-Host "All services started!"
Get-Process python, node -ErrorAction SilentlyContinue | Format-Table Id, ProcessName -AutoSize
