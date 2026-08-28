"""Cached BO module map — tables grouped by business domain (Lane B).

Compiled offline by setup/compile_module_map.py into work/<client>/module_map.json.
Runtime: match user question to one domain and inject a short card into tenant_pack.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from . import config

_TOKEN_RE = re.compile(r"[a-zA-Z\u0600-\u06FF]{2,}")

# Domain keywords for question matching (Arabic product language + English regression).
_DOMAIN_KEYWORDS: dict[str, dict] = {
    "sales": {
        "label": "Sales invoices & returns",
        "keywords": [
            "مبيعات", "فاتورة", "فواتير", "مرتجع", "مرتجعات", "invoice", "sales",
            "transaction", "return", "netsales",
        ],
    },
    "orders": {
        "label": "Sales orders (not invoices)",
        "keywords": ["طلب", "طلبات", "order", "ordersheaders"],
    },
    "receipts": {
        "label": "Receipts & collections",
        "keywords": ["تحصيل", "سند", "receipt", "check", "cheque", "collection"],
    },
    "cfd": {
        "label": "Customer financial details & territory (CFD)",
        "keywords": [
            "cfd", "عملاء المندوب", "زبائن المندوب", "territory", "assignment", "positions",
            "customersfinancialdetails", "financialdetails",
        ],
    },
    "van": {
        "label": "Van stock & transfers",
        "keywords": [
            "رصيد", "سيارة", "van", "stock", "salespersonitemsbalance", "transfer",
        ],
    },
    "items": {
        "label": "Items & inventory",
        "keywords": ["صنف", "أصناف", "item", "inventory", "stocktaking", "barcode"],
    },
    "routes": {
        "label": "Routes & visits",
        "keywords": ["مسار", "route", "visit", "visits", "journey", "زيارات", "زيارة"],
    },
    "system_options": {
        "label": "System options & configuration",
        "keywords": [
            "خيار", "خيارات", "system option", "systemoption", "إعداد", "شاشة",
            "screen", "parameter",
        ],
    },
}


def map_path(client: str) -> Path:
    return config.work_dir(client) / "module_map.json"


def load(client: str) -> dict:
    path = map_path(client)
    if not path.exists():
        return {"domains": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def _tokens(text: str) -> set[str]:
    return {t.lower() for t in _TOKEN_RE.findall(text)}


def match_domain(question: str, client: str) -> str | None:
    """Return domain id with highest keyword overlap, or None."""
    data = load(client)
    if not data.get("domains"):
        return None
    q = question.lower()
    q_tokens = _tokens(question)
    best_id: str | None = None
    best_score = 0
    for domain_id, meta in _DOMAIN_KEYWORDS.items():
        if domain_id not in data["domains"]:
            continue
        score = 0
        for kw in meta["keywords"]:
            if kw in q or kw.lower() in q_tokens:
                score += 3 if len(kw) > 4 else 2
        if score > best_score:
            best_score = score
            best_id = domain_id
    return best_id if best_score > 0 else None


def format_card(domain_id: str, client: str) -> str:
    """Short module card for tenant_pack injection."""
    data = load(client)
    domain = data.get("domains", {}).get(domain_id)
    if not domain:
        return ""
    label = domain.get("label") or _DOMAIN_KEYWORDS.get(domain_id, {}).get("label", domain_id)
    tables = domain.get("tables") or []
    hints = domain.get("hints") or []
    lines = [f"## Module: {label}"]
    if tables:
        shown = ", ".join(tables[:14])
        if len(tables) > 14:
            shown += f" (+{len(tables) - 14} more)"
        lines.append(f"Core tables: {shown}")
    for hint in hints[:4]:
        lines.append(f"- {hint}")
    return "\n".join(lines)


def card_for_question(question: str, client: str) -> str:
    domain_id = match_domain(question, client)
    if not domain_id:
        return ""
    return format_card(domain_id, client)
