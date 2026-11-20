"""One-file Windows entry.

The exe carries clients, prompts, static, and the schema/docs files.
.env stays beside the exe and is not packed in. Chat files that must be
writable are copied once to %LOCALAPPDATA%\\OlivesChatbot\\work.
Nothing in this file sets a host, a password, or an API key.
"""
import os
import shutil
import sys
from pathlib import Path

os.environ["PYTHONUNBUFFERED"] = "1"
try:
    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)
except Exception:
    pass
print("Olives chatbot: loading. The window stays quiet while the exe unpacks.", flush=True)


def _bundle() -> Path:
    if getattr(sys, "frozen", False):
        return Path(getattr(sys, "_MEIPASS")).resolve()
    return Path(__file__).resolve().parent.parent


def _seed_work(bundle: Path) -> Path:
    dest = Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / "OlivesChatbot" / "work"
    dest.mkdir(parents=True, exist_ok=True)
    src = bundle / "work"
    if not src.is_dir():
        return dest
    for item in src.rglob("*"):
        if not item.is_file():
            continue
        target = dest / item.relative_to(src)
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)
    return dest


def main() -> None:
    bundle = _bundle()
    os.chdir(bundle)
    if str(bundle) not in sys.path:
        sys.path.insert(0, str(bundle))
    try:
        from dotenv import load_dotenv
        env_file = Path(sys.executable).resolve().parent / ".env" if getattr(sys, "frozen", False) else bundle / ".env"
        if not env_file.is_file():
            print(f"Missing {env_file}", flush=True)
            print("Put .env in the same folder as OlivesChatbot.exe, then start again.", flush=True)
            input("Press Enter to close.")
            raise SystemExit(1)
        load_dotenv(env_file)
    except ImportError:
        pass
    os.environ["CHATBOT_WORK_DIR"] = str(_seed_work(bundle))

    import uvicorn
    from api.server import app

    port = int(os.environ.get("PORT", "8100"))
    print(f"Olives chatbot: listening on http://127.0.0.1:{port}", flush=True)
    print("Close this window to stop.", flush=True)
    try:
        uvicorn.run(app, host="127.0.0.1", port=port, log_level="info")
    except SystemExit as exc:
        if exc.code not in (0, None):
            print(flush=True)
            print(f"The bot stopped (code {exc.code}).", flush=True)
            print(
                f"If the line above says port {port} is already in use, "
                "close the other Olives chatbot window (python.exe or an older exe) and start this one again.",
                flush=True,
            )
            input("Press Enter to close.")
        raise


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        traceback.print_exc()
        input("Press Enter to close.")
        raise
