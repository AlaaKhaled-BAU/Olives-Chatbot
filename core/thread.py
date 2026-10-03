"""Minimal session card (codes only). User-facing Arabic lives in locale_ar."""
from __future__ import annotations

import json
from datetime import datetime
from zoneinfo import ZoneInfo

from . import metrics

_AMMAN = ZoneInfo("Asia/Amman")
_MAX_VALUE_COLS = 8


def amman_today_iso() -> str:
    return datetime.now(_AMMAN).date().isoformat()


def make_card(tool_name: str, args: dict, row: dict | None) -> dict | None:
    """Structured card from one business tool call. Codes only — no Arabic here."""
    if tool_name != "run_metric" or not isinstance(row, dict):
        return None
    metric_arg = (args.get("metric") or "").strip()
    canonical = metrics.resolve_metric(metric_arg)
    if canonical != "sales":
        return None
    filters = dict(args.get("filters") or {})
    tax = (filters.get("tax") or "incl").strip().lower()
    returns = (filters.get("returns") or "gross").strip().lower()
    if tax not in ("incl", "excl"):
        tax = "incl"
    if returns not in ("gross", "net"):
        returns = "gross"
    from_d = (filters.get("from_date") or "").strip()
    to_d = (filters.get("to_date") or "").strip()
    if from_d and to_d:
        period_label = f"{from_d} .. {to_d}"
    else:
        period_label = from_d or to_d or ""
    primary_measure = "net_of_returns" if returns == "net" else "gross_sales"
    keys = list(row.keys())
    if len(keys) > _MAX_VALUE_COLS:
        values = {k: row[k] for k in keys[:_MAX_VALUE_COLS]}
    else:
        values = dict(row)
    return {
        "tool": tool_name,
        "metric": "sales",
        "tax": tax,
        "returns": returns,
        "period_label": period_label,
        "primary_measure": primary_measure,
        "values": values,
        "as_of": amman_today_iso(),
    }


def card_from_query_log(query_log: list | None) -> dict | None:
    """Last qualifying run_metric/sales entry with a single result row."""
    if not query_log:
        return None
    for entry in reversed(query_log):
        if entry.get("name") != "run_metric":
            continue
        rows = entry.get("rows")
        if not isinstance(rows, list) or len(rows) != 1:
            continue
        card = make_card("run_metric", entry.get("args") or {}, rows[0])
        if card:
            return card
    return None


def format_card_prompt(card: dict) -> str:
    today = amman_today_iso()
    return (
        "## Thread card (structured state from the last sales query; codes, not display labels)\n"
        f"{json.dumps(card, ensure_ascii=False, sort_keys=True)}\n"
        f"Today (Asia/Amman): {today}. Card as_of: {card.get('as_of', '')}. "
        "If the user does not name a period and card as_of is a different Amman calendar day, "
        "ask which period before reusing the card dates. "
        "Use metric sales with filters tax (incl|excl) and returns (gross|net). "
        "User-facing basis wording is in the locale table, not in this JSON."
    )


def card_followups(card: dict) -> list[str]:
    """Three short Arabic messages the UI can send as follow-ups."""
    period = (card.get("period_label") or "").strip()
    tax = card.get("tax") or "incl"
    returns = card.get("returns") or "gross"
    period_bit = f" {period}" if period else ""
    out: list[str] = []
    if tax != "excl":
        out.append(f"طيب قبل الضريبة{period_bit}".strip())
    else:
        out.append(f"وش الرقم شامل الضريبة{period_bit}".strip())
    if returns != "net":
        out.append(f"وبعد المرتجعات{period_bit}".strip())
    else:
        out.append(f"بدون خصم المرتجعات{period_bit}".strip())
    if period:
        out.append(f"نفس الفترة {period}")
    else:
        out.append("نفس الفترة السابقة")
    return out[:3]
