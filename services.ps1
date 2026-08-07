$ErrorActionPreference = "SilentlyContinue"
$dir = $PSScriptRoot
$pidFileBackend = "$dir\.backend.pid"
$pidFileBot = "$dir\.bot.pid"
$pidFileFrontend = "$dir\.frontend.pid"

function Stop-Tracked($pidFile) {
    if (Test-Path $pidFile) {
        $lines = Get-Content $pidFile
        foreach ($line in $lines) {
            $procId = [int]$line.Trim()
            if ($procId -gt 0) {
                Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
            }
        }
        Remove-Item $pidFile -Force
    }
}

function Start-Backend {
    Write-Host "Starting backend..."
    $proc = Start-Process python -ArgumentList "-m uvicorn backend.main:app --host 0.0.0.0 --port 8000" -WorkingDirectory $dir -PassThru -WindowStyle Hidden
    Start-Sleep -Seconds 1
    $proc.Id | Out-File $pidFileBackend -Encoding ascii
    Start-Sleep -Seconds 5
    try {
        $r = Invoke-WebRequest -Uri "http://localhost:8000/api/health" -TimeoutSec 5
        Write-Host "  Backend OK (PID $($proc.Id))"
    } catch {
        Write-Host "  Backend FAILED!"
    }
}

function Start-Bot {
    Write-Host "Starting bot..."
    $proc = Start-Process python -ArgumentList "-X utf8 bot\main.py" -WorkingDirectory $dir -PassThru -WindowStyle Hidden
    Start-Sleep -Seconds 1
    $proc.Id | Out-File $pidFileBot -Encoding ascii
    Write-Host "  Bot OK (PID $($proc.Id))"
}

function Start-Frontend {
    Write-Host "Starting frontend..."
    $proc = Start-Process node -ArgumentList "C:\temp\frontend_server.js" -WorkingDirectory $dir -PassThru -WindowStyle Hidden
    Start-Sleep -Seconds 1
    $proc.Id | Out-File $pidFileFrontend -Encoding ascii
    Write-Host "  Frontend OK (PID $($proc.Id))"
}

function Show-Status {
    Write-Host ""
    $services = @(
        @{Name="Backend";  File=$pidFileBackend},
        @{Name="Bot";      File=$pidFileBot},
        @{Name="Frontend"; File=$pidFileFrontend}
    )
    foreach ($s in $services) {
        $name = $s.Name
        $file = $s.File
        if (Test-Path $file) {
            $procId = [int](Get-Content $file).Trim()
            $p = Get-Process -Id $procId -ErrorAction SilentlyContinue
            if ($p) { Write-Host "  $name : RUNNING (PID $procId)" }
            else { Write-Host "  $name : DEAD" }
        } else {
            Write-Host "  $name : NOT TRACKED"
        }
    }
    Write-Host ""
}

$cmd = if ($args.Count -gt 0) { $args[0] } else { "help" }

switch ($cmd) {
    "start" {
        Stop-Tracked $pidFileBackend
        Stop-Tracked $pidFileBot
        Stop-Tracked $pidFileFrontend
        Start-Sleep -Seconds 2
        Start-Backend
        Start-Bot
        Start-Frontend
        Show-Status
    }
    "stop" {
        Stop-Tracked $pidFileBackend
        Stop-Tracked $pidFileBot
        Stop-Tracked $pidFileFrontend
        Show-Status
    }
    "restart" {
        Stop-Tracked $pidFileBackend
        Stop-Tracked $pidFileBot
        Stop-Tracked $pidFileFrontend
        Start-Sleep -Seconds 2
        Start-Backend
        Start-Bot
        Start-Frontend
        Show-Status
    }
    "bot" {
        Stop-Tracked $pidFileBot
        Start-Bot
        Show-Status
    }
    "backend" {
        Stop-Tracked $pidFileBackend
        Start-Backend
        Show-Status
    }
    "status" {
        Show-Status
    }
    default {
        Write-Host "services.ps1 <command>"
        Write-Host ""
        Write-Host "  start    - Start all"
        Write-Host "  stop     - Stop all"
        Write-Host "  restart  - Restart all"
        Write-Host "  bot      - Restart bot only"
        Write-Host "  backend  - Restart backend only"
        Write-Host "  status   - Show status"
    }
}
