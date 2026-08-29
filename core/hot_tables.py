"""Canonical hot-table registry — db/hot_tables.json."""
import json
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
HOT_TABLES_PATH = _REPO / "db" / "hot_tables.json"


def load() -> dict:
    return json.loads(HOT_TABLES_PATH.read_text(encoding="utf-8"))


def table_names() -> frozenset[str]:
    data = load()
    return frozenset(data.get("tables") or [])
