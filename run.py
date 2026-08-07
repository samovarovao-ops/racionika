# -*- coding: utf-8 -*-
"""
Service manager for Рационика.
Starts backend, bot, frontend and restarts them if they crash.
"""
import subprocess
import sys
import time
import os
import signal
import logging
from pathlib import Path

BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / "services.log", encoding="utf-8"),
    ],
)
log = logging.getLogger("services")

SERVICES = [
    {
        "name": "backend",
        "cmd": [sys.executable, "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"],
        "ready_url": "http://localhost:8000/api/health",
        "restart_delay": 3,
    },
    {
        "name": "bot",
        "cmd": [sys.executable, "-X", "utf8", "bot/main.py"],
        "ready_url": None,
        "restart_delay": 2,
    },
    {
        "name": "frontend",
        "cmd": ["node", r"C:\temp\frontend_server.js"],
        "ready_url": None,
        "restart_delay": 2,
    },
]

procs: dict[str, subprocess.Popen] = {}
running = True


def stop_all():
    global running
    running = False
    for svc in SERVICES:
        name = svc["name"]
        p = procs.get(name)
        if p and p.poll() is None:
            log.info(f"Stopping {name} (PID {p.pid})")
            try:
                p.terminate()
                p.wait(timeout=5)
            except Exception:
                try:
                    p.kill()
                except Exception:
                    pass
    log.info("All services stopped.")


def start_service(svc: dict):
    name = svc["name"]
    cmd = svc["cmd"]
    log.info(f"Starting {name}: {' '.join(cmd)}")

    stdout_log = open(LOG_DIR / f"{name}_stdout.log", "a", encoding="utf-8")
    stderr_log = open(LOG_DIR / f"{name}_stderr.log", "a", encoding="utf-8")

    proc = subprocess.Popen(
        cmd,
        cwd=str(BASE_DIR),
        stdout=stdout_log,
        stderr=stderr_log,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    procs[name] = proc
    log.info(f"  {name} started (PID {proc.pid})")


def check_ready(svc: dict) -> bool:
    url = svc.get("ready_url")
    if not url:
        return True
    try:
        import httpx
        r = httpx.get(url, timeout=3)
        return r.status_code == 200
    except Exception:
        return False


def main():
    global running

    signal.signal(signal.SIGINT, lambda s, f: stop_all())
    signal.signal(signal.SIGTERM, lambda s, f: stop_all())

    log.info("=" * 50)
    log.info("Racionika service manager starting")
    log.info("=" * 50)

    # Start all services
    for svc in SERVICES:
        start_service(svc)
        time.sleep(1)

    # Wait for backend
    backend_svc = SERVICES[0]
    log.info("Waiting for backend...")
    for _ in range(20):
        if check_ready(backend_svc):
            log.info("Backend is ready!")
            break
        time.sleep(1)
    else:
        log.warning("Backend not ready in 20s, continuing...")

    # Monitor loop
    while running:
        time.sleep(5)
        for svc in SERVICES:
            name = svc["name"]
            p = procs.get(name)
            if p and p.poll() is not None:
                exit_code = p.returncode
                log.warning(f"{name} died (exit {exit_code}). Restarting in {svc['restart_delay']}s...")
                time.sleep(svc["restart_delay"])
                if running:
                    start_service(svc)

    stop_all()


if __name__ == "__main__":
    main()
