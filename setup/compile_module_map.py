#!/usr/bin/env python3.13
"""Compile work/<client>/module_map.json — BO tables grouped by domain (Lane B).

Sources: vault table tags, high-support procedure reads_from, tables summary.md.

Vault column drift is patched separately (setup only, not runtime):
  python3.13 setup/sync_vault_from_cache.py --client <name>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import config, vault  # noqa: E402

VAULT_BO = BASE_DIR / "obsidian" / "olives" / "Olives_BO"
SUMMARY_PATH = BASE_DIR / "knowledge" / "reference" / "tables summary.md"

DOMAIN_SEEDS: dict[str, dict] = {
    "sales": {
        "label": "Sales invoices & returns",
        "tags": {"#sales", "#invoice"},
        "seeds": {
            "TransactionsHeaders", "TransactionsDetails", "TransactionsTypes",
            "DocumentsTypes", "InvoiceReturnLink",
        },
        "hints": [
            "Sales invoices: TransactionTypeID=1, ISNULL(IsVoid,0)=0 on TransactionsHeaders.",
            "Header ⋈ details on CompanyID, TransactionTypeID, TransactionYear, TransactionNo.",
        ],
    },
    "orders": {
        "label": "Sales orders (not invoices)",
        "tags": {"#order"},
        "seeds": {"OrdersHeaders", "OrdersDetails", "PendingOrdersHeaders", "PendingOrdersDetails"},
        "hints": ["OrdersHeaders is طلبات — not the same grain as TransactionsHeaders invoices."],
    },
    "receipts": {
        "label": "Receipts & collections",
        "tags": {"#receipt", "#payment"},
        "seeds": {"Receipts", "Checks", "Receipts_PaidTrans", "BankDepositHF", "BankDepositDF"},
        "hints": ["Exclude voided receipts: ISNULL(Receipts.IsVoid, 0) = 0."],
    },
    "cfd": {
        "label": "Customer financial details & territory (CFD)",
        "tags": {"#customer"},
        "seeds": {
            "CustomersFinancialDetails", "Positions", "Customers", "SalesPersons",
            "RoutesInformation", "PriceLists", "CustomersClasses",
        },
        "hints": [
            "Territory: CustomersFinancialDetails.PositionsID → Positions.ID → SalesPersons.PositionID.",
            "Never join CFD.CustomerID to SalesPersons.ID for territory.",
        ],
    },
    "van": {
        "label": "Van stock & transfers",
        "tags": {"#inventory", "#van"},
        "seeds": {
            "SalesPersonItemsBalance", "TransfersOrdersHeaders", "TransfersOrdersDetails",
            "VanTransferHeader", "VanTransferDetails",
        },
        "hints": [
            "Van stock: SalesPersonItemsBalance by SalesPersonID + ItemCode (live FK to Items, SalesPersons).",
        ],
    },
    "items": {
        "label": "Items & inventory",
        "tags": {"#item", "#inventory"},
        "seeds": {"Items", "ItemsInventory", "ItemsCategories", "ItemsGroups", "ItemsClasses"},
        "hints": [],
    },
    "routes": {
        "label": "Routes & visits",
        "tags": {"#route"},
        "seeds": {"RoutesInformation", "SalespersonRouteByDate", "SalespersonCustomersVisitsByDate"},
        "hints": [],
    },
    "system_options": {
        "label": "System options & configuration",
        "tags": {"#system", "#option", "#config"},
        "seeds": {"SystemOptions", "SystemOptionsTypes", "CompanyParameters", "OlivesMenu"},
        "hints": ["Use search_docs for screen numbers and option names — not raw SystemOptions dumps."],
    },
}

_PROC_DOMAIN_HINTS = [
    (re.compile(r"sales|invoice|transaction|مبيعات", re.I), "sales"),
    (re.compile(r"order|طلب", re.I), "orders"),
    (re.compile(r"receipt|payment|check|تحصيل", re.I), "receipts"),
    (re.compile(r"customer|cfd|position|territory|مندوب", re.I), "cfd"),
    (re.compile(r"van|stock|balance|transfer|رصيد", re.I), "van"),
    (re.compile(r"item|inventory|صنف", re.I), "items"),
    (re.compile(r"route|visit|مسار", re.I), "routes"),
    (re.compile(r"system.?option|parameter|menu", re.I), "system_options"),
]

_BO_TABLE_RE = re.compile(r"`([A-Za-z][A-Za-z0-9_]*)`")


def _normalize_tags(raw) -> set[str]:
    if isinstance(raw, list):
        return {str(t).lower() for t in raw}
    if isinstance(raw, str) and raw:
        return {raw.lower()}
    return set()


def _wiki_tables(raw) -> list[str]:
    if not raw:
        return []
    if isinstance(raw, str):
        raw = [raw]
    out = []
    for item in raw:
        name = vault._wiki_name(str(item)).split("/")[-1]
        if name and name[0].isupper():
            out.append(name)
    return out


def _tables_from_summary() -> dict[str, set[str]]:
    by_domain: dict[str, set[str]] = {k: set() for k in DOMAIN_SEEDS}
    if not SUMMARY_PATH.exists():
        return by_domain
    text = SUMMARY_PATH.read_text(encoding="utf-8")
    current: str | None = None
    for line in text.splitlines():
        if "↔" in line and "`" in line:
            for m in _BO_TABLE_RE.finditer(line):
                table = m.group(1)
                upper = line.upper()
                if "TRANSACTION" in upper or "INVOICE" in upper:
                    by_domain["sales"].add(table)
                elif "ORDER" in upper:
                    by_domain["orders"].add(table)
                elif "RECEIPT" in upper or "PAYMENT" in upper:
                    by_domain["receipts"].add(table)
                elif "CUSTOMER" in upper or "SALESMAN" in upper or "SALESPERSON" in upper:
                    by_domain["cfd"].add(table)
                elif "STOCK" in upper or "BALANCE" in upper or "VAN" in upper:
                    by_domain["van"].add(table)
                elif "ITEM" in upper:
                    by_domain["items"].add(table)
                elif "ROUTE" in upper:
                    by_domain["routes"].add(table)
    return by_domain


def _proc_domain(proc_name: str) -> str | None:
    for rx, domain_id in _PROC_DOMAIN_HINTS:
        if rx.search(proc_name):
            return domain_id
    return None


def compile_map() -> dict:
    domains: dict[str, dict] = {}
    for domain_id, spec in DOMAIN_SEEDS.items():
        domains[domain_id] = {
            "label": spec["label"],
            "tables": sorted(spec["seeds"]),
            "hints": list(spec["hints"]),
        }

    summary_tables = _tables_from_summary()
    for domain_id, tables in summary_tables.items():
        domains[domain_id]["tables"] = sorted(set(domains[domain_id]["tables"]) | tables)

    tables_dir = VAULT_BO / "Tables"
    if tables_dir.is_dir():
        for path in tables_dir.glob("*.md"):
            fm = vault.parse_frontmatter(path.read_text(encoding="utf-8"))
            name = str(fm.get("name", path.stem))
            tags = _normalize_tags(fm.get("tags"))
            for domain_id, spec in DOMAIN_SEEDS.items():
                if tags & {t.lower() for t in spec["tags"]}:
                    domains[domain_id]["tables"].append(name)
            domains[domain_id]["tables"] = sorted(set(domains[domain_id]["tables"]))

    procs_dir = VAULT_BO / "Procedures"
    if procs_dir.is_dir():
        for path in procs_dir.glob("*.md"):
            content = path.read_text(encoding="utf-8")
            fm = vault.parse_frontmatter(content)
            relevance = str(fm.get("support_relevance", "")).lower()
            if relevance not in ("high", "medium"):
                continue
            proc_name = str(fm.get("name", path.stem))
            domain_id = _proc_domain(proc_name)
            if not domain_id:
                continue
            for table in _wiki_tables(fm.get("reads_from")):
                domains[domain_id]["tables"].append(table)
            domains[domain_id]["tables"] = sorted(set(domains[domain_id]["tables"]))

    return {"version": 1, "domains": domains}


def write(client: str, data: dict) -> Path:
    out = config.work_dir(client) / "module_map.json"
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(description="Compile BO module map for a client")
    parser.add_argument("--client", required=True)
    args = parser.parse_args()
    data = compile_map()
    out = write(args.client, data)
    counts = {k: len(v["tables"]) for k, v in data["domains"].items()}
    print(f"Wrote module_map.json to {out}")
    for domain_id, n in counts.items():
        print(f"  {domain_id}: {n} tables")


if __name__ == "__main__":
    main()
