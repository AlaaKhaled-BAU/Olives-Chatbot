"""Tiered KV-cache-friendly context builder for DeepSeek prompt prefix and tenant context."""
from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path
from typing import Any

from core.paths import app_root
from . import cache_loader
from . import gate

# 45 core Olives BO business tables (lowercase bare names).
CORE_TABLES: frozenset[str] = frozenset({
    "transactionsheaders",
    "transactionsdetails",
    "transactionstypes",
    "documentstypes",
    "ordersheaders",
    "ordersdetails",
    "receipts",
    "checks",
    "bankdeposithf",
    "customers",
    "customersfinancialdetails",
    "positions",
    "salespersons",
    "salespersonsdevicepermissions",
    "salespersonsroutes",
    "salespersonroutebydate",
    "routesinformation",
    "deliveryroute",
    "items",
    "itemsunits",
    "itemscategories",
    "pricelists",
    "pricelistdetails",
    "logactiontransaction",
    "logactions",
    "salespersonitemsbalance",
    "storesbalances",
    "salespersonstocktacking",
    "transfersordersheaders",
    "transfersordersdetails",
    "deliverycars",
    "companies",
    "clientsactive",
    "currencies",
    "systemoptions",
    "systemcodes",
    "customertargets",
    "promotions",
    "promotiontypes",
    "requesttoadddiscount",
    "requestsalesmanwillnotvisit",
    "requesttovisitcustomernotinroute",
    "ot_storeitemsqty",
    "ot_storeitemsqty_main",
    "ot_itemsmf",
})


def _strip_wiki(name: str) -> str:
    """Strip Obsidian [[...]] brackets and |alias cleanly (e.g. '[[Customers]]' -> 'Customers')."""
    if not name:
        return ""
    s = str(name).strip()
    if s.startswith("[["):
        s = s[2:]
    if s.endswith("]]"):
        s = s[:-2]
    s = s.strip()
    if "|" in s:
        s = s.split("|", 1)[0].strip()
    return s


def schema_block(cache: dict, *, core_only: bool = True) -> str:
    """Queryable schema block with core-only filtering option.

    Respects gate.HIDDEN_TABLES, has_tenant_view, and _old/_temp/_ filtering,
    and strips CompanyID columns.
    When core_only=True: outputs full - table(...) lines for CORE_TABLES, plus a
    compact directory of remaining queryable table names.
    When core_only=False: outputs full lines for all queryable tables.
    """
    views = cache.get("has_tenant_view") or {}
    tables = cache.get("tables") or {}
    lines = [
        "## Full schema of queryable tenant views",
        "Every table below is a `t.*` view automatically scoped to the session CompanyID.",
        "Write SQL directly against these; introspect_schema is only for anything NOT listed here.",
    ]
    hidden = gate.HIDDEN_TABLES
    other_names: list[str] = []

    for name in sorted(tables):
        bare = name.split(".")[-1].lower()
        if bare in hidden:
            continue
        if views and not views.get(name, False):
            continue
        if bare.endswith("_old") or bare.endswith("_temp") or bare.endswith("_"):
            continue

        if core_only and bare not in CORE_TABLES:
            other_names.append(name)
            continue

        cols = tables[name] or []
        col_names = [
            c.get("column")
            for c in cols
            if isinstance(c, dict)
            and c.get("column")
            and str(c.get("column")).lower() != "companyid"
        ]
        lines.append(f"- {name}({', '.join(col_names)})")

    if core_only and other_names:
        lines.append("## Other queryable tenant views (names only — use introspect_schema for columns)")
        lines.append(", ".join(sorted(other_names)))

    return "\n".join(lines)


def all_cards_block(client: str, *, core_only: bool = True) -> str:
    """Compiled vault cards block with core-only filtering option.

    Loads cards via cache_loader.load_vault_cards(client) (fail-soft -> '').
    Skips gate.HIDDEN_TABLES.
    When core_only=True: keeps table cards whose bare name is in CORE_TABLES and
    relation cards where parent or referenced matches CORE_TABLES.
    """
    try:
        cards = cache_loader.load_vault_cards(client)
    except Exception:
        return ""
    if not cards:
        return ""

    hidden = gate.HIDDEN_TABLES
    lines = ["## Vault knowledge cards (compiled schema memory)"]

    for card in sorted(cards, key=lambda c: (c.get("kind") or "", c.get("name") or "", c.get("parent") or "", c.get("referenced") or "")):
        kind = card.get("kind")
        if kind == "relation":
            parent = str(card.get("parent") or "")
            referenced = str(card.get("referenced") or "")
            p_bare = _strip_wiki(parent).split(".")[-1].lower()
            r_bare = _strip_wiki(referenced).split(".")[-1].lower()
            if p_bare in hidden or r_bare in hidden:
                continue
            if core_only:
                p_in_core = p_bare in CORE_TABLES or _strip_wiki(parent).lower() in CORE_TABLES
                r_in_core = r_bare in CORE_TABLES or _strip_wiki(referenced).lower() in CORE_TABLES
                if not (p_in_core or r_in_core):
                    continue
            lines.append(
                f"- REL {card.get('parent')}→{card.get('referenced')}: "
                f"{str(card.get('columns', ''))[:120]}"
                + (f" — {str(card.get('business_meaning'))[:100]}" if card.get("business_meaning") else "")
            )
        else:
            name = str(card.get("name") or "")
            bare = _strip_wiki(name).split(".")[-1].lower()
            if bare in hidden:
                continue
            if core_only and bare not in CORE_TABLES:
                continue
            purpose = str(card.get("purpose", ""))[:110]
            fk = str(card.get("foreign_keys", ""))[:80]
            line = f"- TBL {card.get('name')}"
            if purpose:
                line += f" — {purpose}"
            if fk:
                line += f" | FK {fk}"
            lines.append(line)

    if len(lines) <= 1:
        return ""
    return "\n".join(lines)


def static_prefix(client: str, cache: dict, *, max_queries: int = 4, core_only: bool = True) -> list[dict]:
    """Messages [0..n] whose bytes NEVER change across turns for this client.
    DeepSeek disk-caches whole prefix units, so stable content goes first."""
    try:
        base = cache_loader.load_prompt("system.md")
    except Exception:
        base = (app_root() / "prompts" / "system.md").read_text(encoding="utf-8")

    base = base.replace("{{CLIENT}}", client).replace("{{MAX_QUERIES}}", str(max_queries))

    playbook = ""
    try:
        playbook = cache_loader.load_prompt("join_playbook.md")
    except Exception:
        p_path = app_root() / "prompts" / "join_playbook.md"
        if p_path.exists():
            playbook = p_path.read_text(encoding="utf-8")

    if playbook:
        base += "\n\n## Join playbook\n" + playbook

    msgs = [{"role": "system", "content": base}]
    msgs.append({"role": "system", "content": schema_block(cache, core_only=core_only)})
    cards = all_cards_block(client, core_only=core_only)
    if cards:
        msgs.append({"role": "system", "content": cards})
    return msgs


def prefix_hash(client: str, cache: dict, *, max_queries: int = 4, core_only: bool = True) -> str:
    """Identity of the cached prefix. A playbook or schema edit changes it."""
    blob = json.dumps(
        static_prefix(client, cache, max_queries=max_queries, core_only=core_only),
        ensure_ascii=False,
        sort_keys=True,
    )
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def tenant_freshness(client: str, company_id: int, *, ttl_s: float = 300.0) -> dict:
    """Uses cache_loader.ttl_cache keyed by ('freshness', client, int(company_id)).
    Runs ONE lightweight SQL probe and computes operational_profile. Fails soft to {}."""
    key = ("freshness", client, int(company_id))

    def _probe() -> dict:
        try:
            from . import sql
            query = (
                "SELECT "
                "(SELECT MAX(TransactionDate) FROM t.TransactionsHeaders WHERE TransactionTypeID = 1 AND ISNULL(IsVoid,0) = 0) AS max_invoice_date, "
                "(SELECT COUNT(*) FROM t.TransactionsHeaders WHERE TransactionTypeID = 1 AND ISNULL(IsVoid,0) = 0) AS invoice_count, "
                "(SELECT MAX(OrderDate) FROM t.OrdersHeaders WHERE ISNULL(IsVoid,0) = 0) AS max_order_date, "
                "(SELECT COUNT(*) FROM t.OrdersHeaders WHERE ISNULL(IsVoid,0) = 0) AS order_count"
            )
            rows = sql.run_select(query, company_id, client)
            if not rows or not isinstance(rows, list):
                return {}
            row = rows[0]
            if not isinstance(row, dict):
                return {}

            raw_inv_date = row.get("max_invoice_date")
            raw_ord_date = row.get("max_order_date")
            max_inv = str(raw_inv_date)[:10] if raw_inv_date is not None else None
            max_ord = str(raw_ord_date)[:10] if raw_ord_date is not None else None
            inv_cnt = int(row.get("invoice_count") or 0)
            ord_cnt = int(row.get("order_count") or 0)

            if ord_cnt > 3 * max(inv_cnt, 1):
                profile = "Pre-Sales Dominant"
            elif inv_cnt > 3 * max(ord_cnt, 1):
                profile = "Cash Van Dominant"
            else:
                profile = "Hybrid"

            return {
                "max_invoice_date": max_inv,
                "invoice_count": inv_cnt,
                "max_order_date": max_ord,
                "order_count": ord_cnt,
                "operational_profile": profile,
            }
        except Exception:
            return {}

    try:
        return cache_loader.ttl_cache(key, ttl_s, _probe)
    except Exception:
        return _probe()


def format_tenant_context(client: str, company_id: int, freshness: dict | None = None) -> str:
    """Concise 3-5 line block with pinned CompanyID, calendar_today, max_invoice_date,
    max_order_date, and operational_profile."""
    calendar_today = datetime.date.today().isoformat()
    fresh = freshness or {}
    max_inv = fresh.get("max_invoice_date") or "none"
    max_ord = fresh.get("max_order_date") or "none"
    profile = fresh.get("operational_profile") or "none"
    lines = [
        "## Tenant context",
        f"CompanyID: {company_id} (pinned)",
        f"calendar_today: {calendar_today}",
        f"max_invoice_date: {max_inv}",
        f"max_order_date: {max_ord}",
        f"operational_profile: {profile}",
    ]
    return "\n".join(lines)
