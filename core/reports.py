"""Report catalog matcher — metadata from vault Rpt_* notes, never EXEC."""
import json
import re
from pathlib import Path

from . import config

_TOKEN_RE = re.compile(r"[a-zA-Z\u0600-\u06FF]{3,}")


def catalog_path(client: str) -> Path:
    return config.work_dir(client) / "report_catalog.json"


def load_catalog(client: str) -> list:
    path = catalog_path(client)
    if not path.exists():
        return []
    return json.loads(path.read_text())


def _tokens(text: str) -> set:
    return {t.lower() for t in _TOKEN_RE.findall(text)}


def match_reports(question: str, client: str, limit: int = 3) -> list:
    """Keyword overlap match against report metadata cards."""
    catalog = load_catalog(client)
    if not catalog:
        return []
    q_tokens = _tokens(question)
    if not q_tokens:
        return []
    scored = []
    for card in catalog:
        blob = " ".join(str(card.get(k, "")) for k in ("name", "purpose", "tables", "params"))
        card_tokens = _tokens(blob)
        overlap = len(q_tokens & card_tokens)
        if overlap:
            scored.append((overlap, card))
    scored.sort(key=lambda x: (-x[0], x[1].get("name", "")))
    return [c for _, c in scored[:limit]]
