from fastapi import FastAPI
import os
import subprocess
import time

app = FastAPI(title="Danish Systems 3 Bots Controller")

PROCS = {}

SERVICES = {
    "danish": {
        "cwd": "services/danish-systems-bot",
        "cmd": os.getenv("DANISH_CMD", "python bot.py"),
    },
    "encryption": {
        "cwd": "services/simple-encryption-telegram-bot",
        "cmd": os.getenv("ENCRYPTION_CMD", "python main.py"),
    },
    "maigret": {
        "cwd": "services/maigret-search",
        "cmd": os.getenv("MAIGRET_CMD", "pnpm start"),
    },
}


def service_status(name: str):
    proc = PROCS.get(name)
    running = proc is not None and proc.poll() is None
    return {
        "name": name,
        "running": running,
        "pid": proc.pid if running else None,
    }


@app.get("/")
def root():
    return {
        "ok": True,
        "name": "Danish Systems 3 Bots Controller",
        "services": list(SERVICES.keys()),
    }


@app.get("/status")
def status():
    return {name: service_status(name) for name in SERVICES}


@app.post("/start/{name}")
def start(name: str):
    if name not in SERVICES:
        return {"ok": False, "error": "Unknown service"}

    current = PROCS.get(name)
    if current and current.poll() is None:
        return {"ok": True, "message": "Already running", **service_status(name)}

    spec = SERVICES[name]
    proc = subprocess.Popen(spec["cmd"], cwd=spec["cwd"], shell=True)
    PROCS[name] = proc
    time.sleep(0.2)
    return {"ok": True, **service_status(name)}


@app.post("/stop/{name}")
def stop(name: str):
    if name not in SERVICES:
        return {"ok": False, "error": "Unknown service"}

    proc = PROCS.get(name)
    if not proc or proc.poll() is not None:
        return {"ok": True, "message": "Not running", **service_status(name)}

    proc.terminate()
    return {"ok": True, "message": "Stopping", **service_status(name)}


@app.post("/restart/{name}")
def restart(name: str):
    stop(name)
    time.sleep(1)
    return start(name)
