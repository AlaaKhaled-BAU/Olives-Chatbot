"""Short tenant context injected every turn — static BO names + cheap live facts."""
import datetime
from pathlib import Path

from . import sql

_BASE_DIR = Path(__file__).resolve().parent.parent
_SUMMARY_PATH = _BASE_DIR / "knowledge" / "reference" / "tables summary.md"

# Distilled from knowledge/reference/tables summary.md — BO names, not OSFA OT_*.
_STATIC_BO_NAMES = (
    "BO table names (use these in SQL, not OSFA OT_* names):\n"
    "- Sales invoices/returns: TransactionsHeaders + TransactionsDetails "
    "(OSFA OT_InvoiceHF/OT_InvoiceDF)\n"
    "- Sales orders: OrdersHeaders + OrdersDetails (not invoices; not OrdersHF)\n"
    "- Stock transfers: TransfersOrdersHeaders + TransfersOrdersDetails "
    "(OSFA OT_ConsOrderHF — consignment/van transfers, not sales)\n"
    "- Customers: Customers + CustomersFinancialDetails (OSFA OT_CustomerMF)\n"
    "- Price lists: PriceLists (header) + PriceListDetails (item/unit prices); "
    "customer list on CustomersFinancialDetails.PriceListID\n"
    "- Van stock: SalesPersonItemsBalance\n"
    "- Salespersons: SalesPersons (OSFA OT_SalesmanMF)"
)


def _static_from_summary() -> str:
    if not _SUMMARY_PATH.exists():
        return _STATIC_BO_NAMES
    text = _SUMMARY_PATH.read_text(encoding="utf-8")
    mappings = []
    for line in text.splitlines():
        if "| BO | `" in line and "↔" not in line:
            part = line.split("| BO |", 1)[1].split("|", 1)[0].strip()
            if part.startswith("`") and part.endswith("`"):
                mappings.append(part.strip("`"))
    if mappings:
        unique = sorted(set(mappings))
        return _STATIC_BO_NAMES + "\n- BO tables in mapping doc: " + ", ".join(unique[:12])
    return _STATIC_BO_NAMES


def _live_facts(company_id: int, client: str) -> dict:
    facts: dict = {}
    probes = [
        ("client_id", "SELECT ClientID FROM t.ClientsActive"),
        (
            "max_dates",
            "SELECT (SELECT MAX(TransactionDate) FROM t.TransactionsHeaders) AS max_invoice_date, "
            "(SELECT MAX(OrderDate) FROM t.OrdersHeaders) AS max_order_date",
        ),
        (
            "operational_balance",
            "SELECT (SELECT COUNT(*) FROM t.TransactionsHeaders WHERE TransactionTypeID = 1 AND ISNULL(IsVoid,0) = 0) AS invoice_count, "
            "(SELECT COUNT(*) FROM t.OrdersHeaders WHERE ISNULL(IsVoid,0) = 0) AS order_count",
        ),
        (
            "transaction_types",
            "SELECT ID, Name FROM t.TransactionsTypes ORDER BY ID",
        ),
    ]
    for key, query in probes:
        try:
            rows = sql.run_select(query, company_id, client)
            facts[key] = rows
        except Exception:  # noqa: BLE001 — fail soft when DB unavailable (tests mock)
            continue
    return facts


def build(client: str, company_id: int, question: str | None = None) -> str:
    """Tenant pack for system prompt — static BO guide + live facts + pinned CompanyID."""
    from . import module_map

    lines = [
        "## Tenant context",
        f"CompanyID: {company_id} (pinned for this session — t. views are scoped).",
        f"calendar_today: {datetime.date.today().isoformat()}",
    ]
    lines.append(_static_from_summary())
    if question:
        card = module_map.card_for_question(question, client)
        if card:
            lines.append(card)
    facts = _live_facts(company_id, client)
    if facts.get("client_id"):
        cid = facts["client_id"]
        if isinstance(cid, list) and cid:
            lines.append(f"ClientsActive ClientID: {cid[0].get('ClientID')}")
    if facts.get("max_dates"):
        row = facts["max_dates"]
        if isinstance(row, list) and row:
            if row[0].get("max_invoice_date") is not None:
                lines.append(f"max_invoice_date: {row[0].get('max_invoice_date')}")
            if row[0].get("max_order_date") is not None:
                lines.append(f"max_order_date: {row[0].get('max_order_date')}")
    if facts.get("operational_balance"):
        row = facts["operational_balance"]
        if isinstance(row, list) and row:
            inv = row[0].get("invoice_count") or 0
            ord_cnt = row[0].get("order_count") or 0
            if ord_cnt > 3 * max(inv, 1):
                mode = "Pre-Sales Dominant (حجز طلبيات هو النمط الغالب — انتبه لاستعلام OrdersHeaders عند السؤال عن المبيعات)"
            elif inv > 3 * max(ord_cnt, 1):
                mode = "Cash Van Dominant (فانات البيع المباشر هي النمط الغالب — TransactionsHeaders Type 1)"
            else:
                mode = "Hybrid (نمط مزدوج: فانات بيع مباشر + طلبيات توصيل مسبقة)"
            lines.append(f"operational_profile: {mode} [Total Invoices: {inv:,} | Total Orders: {ord_cnt:,}]")
    if facts.get("transaction_types"):
        types = facts["transaction_types"]
        if isinstance(types, list) and types:
            brief = ", ".join(f"{r.get('ID')}={r.get('Name')}" for r in types[:6])
            lines.append(f"TransactionsTypes: {brief}")
    return "\n".join(lines)
