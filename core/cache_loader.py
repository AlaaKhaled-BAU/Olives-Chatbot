"""Thread-safe mtime-keyed caches for schema, templates, prompts, vault cards, client configs, and catalog procs."""
import json
from pathlib import Path
import sqlite3
import threading
import time
from typing import Any, Callable

import yaml

from .paths import app_root

_LOCK = threading.RLock()
_TTL_LOCK = threading.Lock()

_SCHEMA_CACHE: dict[tuple[str, str], tuple[int, int, dict]] = {}
_TEMPLATES_CACHE: dict[str, tuple[int, int, list[dict]]] = {}
_PROMPTS_CACHE: dict[str, tuple[int, int, str]] = {}
_VAULT_CARDS_CACHE: dict[tuple[str, str], tuple[int, int, list[dict]]] = {}
_CLIENT_CONFIG_CACHE: dict[tuple[str, str], tuple[int, int, dict]] = {}
_CATALOG_PROCS_CACHE: dict[tuple[str, str], tuple[Any, dict]] = {}
_TTL_CACHE: dict[str, tuple[float, Any]] = {}


def load_schema_cache(client: str) -> dict:
    from . import config
    path = config.work_dir(client) / "schema_cache.json"
    key = (client, str(path.resolve()))
    with _LOCK:
        st = path.stat()
        mtime_ns, size = st.st_mtime_ns, st.st_size
        if key in _SCHEMA_CACHE:
            cached_mtime, cached_size, data = _SCHEMA_CACHE[key]
            if cached_mtime == mtime_ns and cached_size == size:
                return data
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)
        _SCHEMA_CACHE[key] = (mtime_ns, size, data)
        return data


def load_templates() -> list[dict]:
    path = app_root() / "knowledge" / "report_templates" / "templates.json"
    key = str(path.resolve())
    with _LOCK:
        if not path.exists():
            return []
        st = path.stat()
        mtime_ns, size = st.st_mtime_ns, st.st_size
        if key in _TEMPLATES_CACHE:
            cached_mtime, cached_size, data = _TEMPLATES_CACHE[key]
            if cached_mtime == mtime_ns and cached_size == size:
                return data
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)
        _TEMPLATES_CACHE[key] = (mtime_ns, size, data)
        return data


def load_prompt(filename: str | Path) -> str:
    p = Path(filename)
    path = p if p.is_absolute() else app_root() / "prompts" / filename
    key = str(path.resolve())
    with _LOCK:
        st = path.stat()
        mtime_ns, size = st.st_mtime_ns, st.st_size
        if key in _PROMPTS_CACHE:
            cached_mtime, cached_size, data = _PROMPTS_CACHE[key]
            if cached_mtime == mtime_ns and cached_size == size:
                return data
        text = path.read_text(encoding="utf-8")
        _PROMPTS_CACHE[key] = (mtime_ns, size, text)
        return text


def load_vault_cards(client: str) -> list[dict]:
    from . import config
    path = config.work_dir(client) / "vault_cards.sqlite"
    key = (client, str(path.resolve()))
    with _LOCK:
        if not path.exists():
            return []
        st = path.stat()
        mtime_ns, size = st.st_mtime_ns, st.st_size
        if key in _VAULT_CARDS_CACHE:
            cached_mtime, cached_size, data = _VAULT_CARDS_CACHE[key]
            if cached_mtime == mtime_ns and cached_size == size:
                return data
        conn = sqlite3.connect(path)
        try:
            rows = conn.execute("SELECT card_json FROM cards").fetchall()
            data = [json.loads(r[0]) for r in rows]
        finally:
            conn.close()
        _VAULT_CARDS_CACHE[key] = (mtime_ns, size, data)
        return data


def load_client_config(client: str) -> dict:
    from . import config
    path = config.CLIENTS_DIR / f"{client}.yaml"
    key = (client, str(path.resolve()))
    with _LOCK:
        if not path.exists():
            raise FileNotFoundError(f"no client config at {path}")
        st = path.stat()
        mtime_ns, size = st.st_mtime_ns, st.st_size
        if key in _CLIENT_CONFIG_CACHE:
            cached_mtime, cached_size, data = _CLIENT_CONFIG_CACHE[key]
            if cached_mtime == mtime_ns and cached_size == size:
                return data
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        _CLIENT_CONFIG_CACHE[key] = (mtime_ns, size, data)
        return data


def load_catalog_procs(client: str, aliases: list[str] | tuple[str, ...] | None = None) -> dict:
    from . import catalog, config
    schema_path = config.work_dir(client) / "schema_cache.json"
    key = (client, str(schema_path.resolve()))
    with _LOCK:
        schema_stat = (schema_path.stat().st_mtime_ns, schema_path.stat().st_size) if schema_path.exists() else None
        clients_stats = tuple(
            (p.name, p.stat().st_mtime_ns, p.stat().st_size)
            for p in sorted(config.CLIENTS_DIR.glob("*.yaml"))
            if not p.name.startswith("_")
        ) if config.CLIENTS_DIR.exists() else ()
        aliases_tuple = tuple(sorted(aliases)) if aliases else None
        sig = (schema_stat, clients_stats, aliases_tuple)

        if key in _CATALOG_PROCS_CACHE:
            cached_sig, data = _CATALOG_PROCS_CACHE[key]
            if cached_sig == sig:
                return data

        data = catalog._compute_for_client(client, aliases)
        _CATALOG_PROCS_CACHE[key] = (sig, data)
        return data


def ttl_cache(key: str, ttl_s: float, loader: Callable[[], Any]) -> Any:
    now = time.monotonic()
    with _TTL_LOCK:
        if key in _TTL_CACHE:
            expires_at, val = _TTL_CACHE[key]
            if now < expires_at:
                return val
        val = loader()
        _TTL_CACHE[key] = (now + ttl_s, val)
        return val


def clear_all() -> None:
    with _LOCK:
        _SCHEMA_CACHE.clear()
        _TEMPLATES_CACHE.clear()
        _PROMPTS_CACHE.clear()
        _VAULT_CARDS_CACHE.clear()
        _CLIENT_CONFIG_CACHE.clear()
        _CATALOG_PROCS_CACHE.clear()
    with _TTL_LOCK:
        _TTL_CACHE.clear()
