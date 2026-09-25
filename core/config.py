"""Per-client config loader (PLAN.md Phase 9): db name, company scope,
catalog aliases, locale. Each client also gets its own work/<client>/
directory (schema_cache.json, ro_password.txt) so two clients' cached
state never collides -- core/memory.py's cache.sqlite stays a single
shared file since its tables already key every row by client (Phase 5)."""
from pathlib import Path

import yaml
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
CLIENTS_DIR = BASE_DIR / "clients"

# Automatically load .env if present
load_dotenv(BASE_DIR / ".env")


def load_client(name: str) -> dict:
    path = CLIENTS_DIR / f"{name}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"no client config at {path}")
    return yaml.safe_load(path.read_text())


def work_dir(client: str) -> Path:
    import os
    env_work = os.environ.get("CHATBOT_WORK_DIR")
    if env_work:
        d = Path(env_work) / client
    else:
        d = BASE_DIR / "work" / client
    d.mkdir(parents=True, exist_ok=True)
    return d
