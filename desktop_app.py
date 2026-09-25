"""Olives Chatbot - Standalone Desktop Launcher.

Designed for PyInstaller standalone .exe distribution.
Bakes in the API key fallback, seeds runtime work directories from bundled assets,
starts the web server, and automatically opens the user's default browser.
"""
import os
import sys
import time
import shutil
import threading
import webbrowser
import urllib.request
from pathlib import Path

# --- 1. Environment & API Key Configuration ---
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except Exception:
    pass

# Hardcoded fallback key requested for boss's standalone executable distribution
DEFAULT_API_KEY = "sk-6aae57a526ef4f3f8a13f925388e502c"
os.environ.setdefault("DEEPSEEK_API_KEY", DEFAULT_API_KEY)
os.environ.setdefault("CHATBOT_CLIENT", "105")
os.environ.setdefault("DB_HOST", "10.0.10.105")
os.environ.setdefault("DB_PORT", "1433")
os.environ.setdefault("CHATBOT_MODEL_FAST", "deepseek-flash")
os.environ.setdefault("CHATBOT_MODEL_HEAVY", "deepseek-flash")

# --- 2. Path Resolution (Frozen PyInstaller vs Normal Python) ---
IS_FROZEN = getattr(sys, "frozen", False)
if IS_FROZEN:
    # Extracted read-only bundle directory in temp
    BUNDLE_DIR = Path(sys._MEIPASS).resolve()
    # Directory where OlivesChatbot.exe lives on disk
    APP_DIR = Path(sys.executable).parent.resolve()
else:
    BUNDLE_DIR = Path(__file__).parent.resolve()
    APP_DIR = BUNDLE_DIR

# Ensure BUNDLE_DIR is at the top of sys.path
if str(BUNDLE_DIR) not in sys.path:
    sys.path.insert(0, str(BUNDLE_DIR))

# Seed writable work/ directory next to executable if missing
RUNTIME_WORK = APP_DIR / "work"
BUNDLED_WORK = BUNDLE_DIR / "work"

if not RUNTIME_WORK.exists() or not (RUNTIME_WORK / "105" / "schema_cache.json").exists():
    try:
        RUNTIME_WORK.mkdir(parents=True, exist_ok=True)
        if BUNDLED_WORK.exists():
            shutil.copytree(BUNDLED_WORK, RUNTIME_WORK, dirs_exist_ok=True)
    except Exception as e:
        print(f"[WARN] Failed to seed work directory to {RUNTIME_WORK}: {e}")

# Point the entire core pipeline to the writable work directory
os.environ["CHATBOT_WORK_DIR"] = str(RUNTIME_WORK)

# --- 3. Browser Opener & Health Watcher ---
PORT = int(os.environ.get("PORT", "8100"))
URL = f"http://127.0.0.1:{PORT}"

def _open_browser_when_ready():
    health_url = f"{URL}/health"
    start = time.time()
    while time.time() - start < 30:
        try:
            req = urllib.request.Request(health_url, headers={"User-Agent": "OlivesDesktop/1.0"})
            with urllib.request.urlopen(req, timeout=1) as resp:
                if resp.status == 200:
                    print(f"\n==> Server ready! Opening browser at {URL} ...")
                    webbrowser.open(URL)
                    return
        except Exception:
            pass
        time.sleep(0.5)
    # If health didn't respond in 30s, open browser anyway
    webbrowser.open(URL)


def main():
    print("=" * 60)
    print("           Olives Client Chatbot - Desktop App")
    print(f"  Target Client : {os.environ.get('CHATBOT_CLIENT')}")
    print(f"  SQL Server    : {os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}")
    print(f"  Interface URL : {URL}")
    print("=" * 60)
    print("Starting background server... (Close this window to quit)\n")

    # Start browser opener thread
    threading.Thread(target=_open_browser_when_ready, daemon=True).start()

    # Start Uvicorn
    import uvicorn
    from api.server import app

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=PORT,
        log_level="info",
        access_log=False,
    )


if __name__ == "__main__":
    main()
