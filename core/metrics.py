"""Named business metrics — pre-built SELECTs through sql.run_select + gate.
Never EXEC procs; never dbo."""
import re
from datetime import date

from . import gate, sql

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

METRICS = {
    "sales": {
        "aliases": ["مبيعات", "sales", "إجمالي المبيعات", "اجمالي المبيعات"],
        "description": (
            "Parameterized sales scan: gross_sales, returns, net_of_returns, "
            "invoice_count, return_count (types 1/2, single SELECT)."
        ),
    },
    "net_sales": {
        "aliases": ["gross_sales"],
        "description": "Non-void sales invoices (TransactionTypeID=1) with optional gross from line items.",
    },
    "net_sales_by_salesperson": {
        "aliases": [
            "أفضل مندوب",
            "best salesman",
            "sales_by_salesperson",
            "أعلى مندوب",
            "اعلى مندوب",
            "أعلى المناديب",
            "ترتيب المناديب",
        ],
        "description": (
            "Net sales invoices grouped by SalesPersonID (type 1 non-void) with salesperson name."
        ),
    },
    "returns": {
        "aliases": ["مرتجعات", "return_sales"],
        "description": "Non-void return invoices (TransactionTypeID=2).",
    },
    "orders": {
        "aliases": ["طلبات", "order_count"],
        "description": "Sales orders in OrdersHeaders (not invoices); includes undelivered count.",
    },
    "van_stock": {
        "aliases": [
            "رصيد السيارة",
            "van_balance",
            "بضاعة سيارات",
            "بضاعة السيارات",
            "رصيد سيارات",
            "رصيد السيارات",
        ],
        "description": "Salesperson van stock from SalesPersonItemsBalance.",
    },
    "cfd_assignment": {
        "aliases": ["عملاء المندوب", "customer_assignment", "customers_per_salesperson"],
        "description": "Customers assigned to salespersons via CFD.PositionsID → SalesPersons.PositionID.",
    },
    "daily_sales_pack": {
        "aliases": ["محصلة يومية", "daily sales", "daily_sales"],
        "description": (
            "Single-day sales pack: sales/returns value and qty (ABS qty), net, "
            "top item by quantity and by value (type 1/2 non-void invoices)."
        ),
    },
    "sales_pipeline": {
        "aliases": ["مسار المبيعات", "المبيعات والطلبات", "sales_pipeline", "orders_and_sales"],
        "description": (
            "Consolidated sales overview: invoiced sales (TransactionsHeaders Type 1) and "
            "booked sales orders (OrdersHeaders with approved and undelivered status)."
        ),
    },
}


def _alias_map() -> dict[str, str]:
    out: dict[str, str] = {}
    for name, meta in METRICS.items():
        out[name.lower()] = name
        for alias in meta["aliases"]:
            out[alias.lower()] = name
    return out


_ALIASES = _alias_map()


def resolve_metric(name: str) -> str | None:
    return _ALIASES.get((name or "").strip().lower())


def question_mentions_metric(question: str) -> bool:
    """True when the question text contains a known metric name or alias."""
    q = (question or "").lower()
    return any(alias in q for alias in _ALIASES)


def _safe_date(value: str) -> str | None:
    if not value or not _DATE_RE.match(value):
        return None
    try:
        date.fromisoformat(value)
    except ValueError:
        return None
    return value


def _safe_int(value) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _company_id_filter(company_id: int, *aliases: str) -> str:
    cid = int(company_id)
    return " AND " + " AND ".join(f"{alias}.CompanyID = {cid}" for alias in aliases)


def _single_day_filter(filters: dict, alias: str = "th") -> str:
    day = _safe_date(filters.get("date") or filters.get("from_date") or filters.get("to_date"))
    if not day:
        return ""
    return f" AND {alias}.TransactionDate = '{day}'"


def _detail_join(alias_th: str = "th", alias_td: str = "td") -> str:
    return (
        f"INNER JOIN t.TransactionsDetails {alias_td} ON "
        f"{alias_th}.CompanyID = {alias_td}.CompanyID "
        f"AND {alias_th}.TransactionTypeID = {alias_td}.TransactionTypeID "
        f"AND {alias_th}.TransactionYear = {alias_td}.TransactionYear "
        f"AND {alias_th}.TransactionNo = {alias_td}.TransactionNo "
    )


def _invoice_date_filters(filters: dict, alias: str = "th") -> str:
    parts = []
    from_date = _safe_date(filters.get("from_date", ""))
    to_date = _safe_date(filters.get("to_date", ""))
    if from_date:
        parts.append(f"{alias}.TransactionDate >= '{from_date}'")
    if to_date:
        parts.append(f"{alias}.TransactionDate <= '{to_date}'")
    sp = _safe_int(filters.get("sales_person_id"))
    if sp is not None:
        parts.append(f"{alias}.SalesPersonID = {sp}")
    return (" AND " + " AND ".join(parts)) if parts else ""


def _order_date_filters(filters: dict, alias: str = "oh") -> str:
    parts = []
    from_date = _safe_date(filters.get("from_date", ""))
    to_date = _safe_date(filters.get("to_date", ""))
    if from_date:
        parts.append(f"{alias}.OrderDate >= '{from_date}'")
    if to_date:
        parts.append(f"{alias}.OrderDate <= '{to_date}'")
    sp = _safe_int(filters.get("sales_person_id"))
    if sp is not None:
        parts.append(f"{alias}.SalesPersonID = {sp}")
    if filters.get("undelivered_only"):
        parts.append(f"ISNULL({alias}.IsDelivered, 0) = 0")
    return (" AND " + " AND ".join(parts)) if parts else ""


def line_amount_sql(alias: str = "td") -> str:
    """Charged line total. Price is the extended amount and already includes tax.
    Do not multiply by Quantity."""
    return (
        f"ABS({alias}.Price) - ABS({alias}.DiscountAmount) "
        f"- ABS({alias}.VoucherDiscount) "
        f"- ABS(ISNULL({alias}.CustomerDiscountAmount,0))"
    )


_SALES_GROUP_BY = frozenset({"salesperson", "customer", "item", "day"})


def _sales_line_amount(tax: str, alias: str = "td") -> str:
    base = line_amount_sql(alias)
    if tax == "excl":
        return f"({base} - ABS({alias}.TaxAmount))"
    return base


def _sales_half_open_dates(filters: dict, alias: str = "th") -> str:
    parts = []
    from_date = _safe_date(filters.get("from_date", ""))
    to_date = _safe_date(filters.get("to_date", ""))
    if from_date:
        parts.append(f"{alias}.TransactionDate >= '{from_date}'")
    if to_date:
        parts.append(f"{alias}.TransactionDate < '{to_date}'")
    return (" AND " + " AND ".join(parts)) if parts else ""


def _sales_filter_basis(filters: dict) -> tuple[str, str]:
    tax = (filters.get("tax") or "incl").strip().lower()
    returns = (filters.get("returns") or "gross").strip().lower()
    if tax not in ("incl", "excl"):
        raise ValueError(f"invalid tax filter {tax!r}; use incl or excl")
    if returns not in ("gross", "net"):
        raise ValueError(f"invalid returns filter {returns!r}; use gross or net")
    return tax, returns


def build_sales_sql(company_id: int, filters: dict | None = None) -> str:
    """Single-scan sales/returns SELECT with optional GROUP BY dimension."""
    filters = dict(filters or {})
    tax, _returns = _sales_filter_basis(filters)
    cid = int(company_id)
    amt = _sales_line_amount(tax)
    gross_expr = f"SUM(CASE WHEN th.TransactionTypeID = 1 THEN {amt} ELSE 0 END)"
    returns_expr = f"SUM(CASE WHEN th.TransactionTypeID = 2 THEN {amt} ELSE 0 END)"
    invoice_cnt = (
        "COUNT(DISTINCT CASE WHEN th.TransactionTypeID = 1 "
        "THEN th.TransactionNo END)"
    )
    return_cnt = (
        "COUNT(DISTINCT CASE WHEN th.TransactionTypeID = 2 "
        "THEN th.TransactionNo END)"
    )
    select_dims = ""
    join_extra = ""
    group_by = ""
    group_key = (filters.get("group_by") or "").strip().lower() or None
    if group_key:
        if group_key not in _SALES_GROUP_BY:
            raise ValueError(
                f"invalid group_by {group_key!r}; "
                f"use one of {', '.join(sorted(_SALES_GROUP_BY))}"
            )
        if group_key == "salesperson":
            select_dims = "th.SalesPersonID, sp.Name AS SalesPersonName, "
            join_extra = (
                "INNER JOIN t.SalesPersons sp ON sp.ID = th.SalesPersonID "
                "AND sp.CompanyID = th.CompanyID "
            )
            group_by = " GROUP BY th.SalesPersonID, sp.Name"
        elif group_key == "customer":
            select_dims = "th.CustomerID, c.Name AS CustomerName, "
            join_extra = (
                "INNER JOIN t.Customers c ON c.ID = th.CustomerID "
                "AND c.CompanyID = th.CompanyID "
            )
            group_by = " GROUP BY th.CustomerID, c.Name"
        elif group_key == "item":
            select_dims = "td.ItemCode, i.Name AS ItemName, "
            join_extra = (
                "INNER JOIN t.Items i ON i.ItemCode = td.ItemCode "
                "AND i.CompanyID = td.CompanyID "
            )
            group_by = " GROUP BY td.ItemCode, i.Name"
        elif group_key == "day":
            select_dims = "th.TransactionDate AS sale_day, "
            group_by = " GROUP BY th.TransactionDate"

    return (
        "SELECT "
        + select_dims
        + f"ISNULL({gross_expr}, 0) AS gross_sales, "
        + f"ISNULL({returns_expr}, 0) AS returns, "
        + f"ISNULL({gross_expr}, 0) - ISNULL({returns_expr}, 0) AS net_of_returns, "
        + f"ISNULL({invoice_cnt}, 0) AS invoice_count, "
        + f"ISNULL({return_cnt}, 0) AS return_count "
        "FROM t.TransactionsHeaders th "
        + _detail_join()
        + join_extra
        + "WHERE th.TransactionTypeID IN (1, 2) AND ISNULL(th.IsVoid, 0) = 0"
        + _company_id_filter(cid, "th", "td")
        + _sales_half_open_dates(filters)
        + group_by
    )


def build_sql(metric: str, filters: dict | None = None, *, company_id: int) -> str:
    """Return the SELECT for a canonical metric name. Raises ValueError if unknown."""
    filters = filters or {}
    cid = int(company_id)
    if metric == "net_sales":
        extra = _invoice_date_filters(filters)
        return (
            "SELECT (SELECT COUNT(*) FROM t.TransactionsHeaders thc "
            "WHERE thc.TransactionTypeID = 1 AND ISNULL(thc.IsVoid, 0) = 0"
            + _company_id_filter(cid, "thc")
            + extra.replace("th.", "thc.")
            + ") AS invoice_count, "
            f"SUM({line_amount_sql('td')}) AS gross_amount "
            "FROM t.TransactionsHeaders th "
            "INNER JOIN t.TransactionsDetails td ON "
            "th.CompanyID = td.CompanyID AND th.TransactionTypeID = td.TransactionTypeID "
            "AND th.TransactionYear = td.TransactionYear AND th.TransactionNo = td.TransactionNo "
            "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th", "td")
            + extra
        )
    if metric == "net_sales_by_salesperson":
        extra = _invoice_date_filters(filters)
        extra_gross = extra.replace("th.", "th2.")
        return (
            "SELECT th.SalesPersonID, sp.Name AS SalesPersonName, "
            "COUNT(*) AS invoice_count, "
            f"(SELECT SUM({line_amount_sql('td')}) FROM t.TransactionsHeaders th2 "
            "INNER JOIN t.TransactionsDetails td ON "
            "th2.CompanyID = td.CompanyID AND th2.TransactionTypeID = td.TransactionTypeID "
            "AND th2.TransactionYear = td.TransactionYear AND th2.TransactionNo = td.TransactionNo "
            "WHERE th2.SalesPersonID = th.SalesPersonID "
            "AND th2.TransactionTypeID = 1 AND ISNULL(th2.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th2", "td")
            + extra_gross
            + ") AS gross_amount "
            "FROM t.TransactionsHeaders th "
            "INNER JOIN t.SalesPersons sp ON sp.ID = th.SalesPersonID AND sp.CompanyID = th.CompanyID "
            "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th", "sp")
            + extra
            + " GROUP BY th.SalesPersonID, sp.Name "
            "ORDER BY gross_amount DESC"
        )
    if metric == "returns":
        extra = _invoice_date_filters(filters)
        return (
            "SELECT COUNT(*) AS return_count "
            "FROM t.TransactionsHeaders th "
            "WHERE th.TransactionTypeID = 2 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th")
            + extra
        )
    if metric == "orders":
        extra = _order_date_filters(filters)
        return (
            "SELECT COUNT(*) AS total_orders, "
            "SUM(CASE WHEN ISNULL(oh.IsDelivered, 0) = 0 THEN 1 ELSE 0 END) AS undelivered_orders "
            "FROM t.OrdersHeaders oh WHERE 1=1"
            + _company_id_filter(cid, "oh")
            + extra
        )
    if metric == "van_stock":
        sp = _safe_int(filters.get("sales_person_id"))
        where = f" WHERE CompanyID = {cid}"
        if sp is not None:
            where += f" AND SalesPersonID = {sp}"
        return f"SELECT * FROM t.SalesPersonItemsBalance{where}"
    if metric == "cfd_assignment":
        sp = _safe_int(filters.get("sales_person_id"))
        where = f" AND sp.ID = {sp}" if sp is not None else ""
        return (
            "SELECT sp.ID AS SalesPersonID, sp.Name AS SalesPersonName, "
            "COUNT(DISTINCT c.ID) AS customer_count "
            "FROM t.Customers c "
            "INNER JOIN t.CustomersFinancialDetails cfd ON "
            "cfd.CustomerID = c.ID AND cfd.CompanyID = c.CompanyID "
            "INNER JOIN t.SalesPersons sp ON "
            "sp.PositionID = cfd.PositionsID AND sp.CompanyID = cfd.CompanyID "
            f"WHERE 1=1{_company_id_filter(cid, 'c', 'cfd', 'sp')}{where} "
            "GROUP BY sp.ID, sp.Name"
        )
    if metric == "sales_pipeline":
        extra_th = _invoice_date_filters(filters, alias="th")
        extra_oh = _order_date_filters(filters, alias="oh")
        return (
            "SELECT "
            "(SELECT COUNT(*) FROM t.TransactionsHeaders th WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th") + extra_th + ") AS invoiced_count, "
            f"(SELECT SUM({line_amount_sql('td')}) FROM t.TransactionsHeaders th "
            "INNER JOIN t.TransactionsDetails td ON th.CompanyID = td.CompanyID AND th.TransactionTypeID = td.TransactionTypeID "
            "AND th.TransactionYear = td.TransactionYear AND th.TransactionNo = td.TransactionNo "
            "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th", "td") + extra_th + ") AS invoiced_amount, "
            "(SELECT COUNT(*) FROM t.OrdersHeaders oh WHERE ISNULL(oh.IsVoid, 0) = 0"
            + _company_id_filter(cid, "oh") + extra_oh + ") AS total_orders_count, "
            "(SELECT COUNT(*) FROM t.OrdersHeaders oh WHERE ISNULL(oh.IsVoid, 0) = 0 AND ISNULL(oh.WFApproved, 0) = 1"
            + _company_id_filter(cid, "oh") + extra_oh + ") AS approved_orders_count, "
            "(SELECT COUNT(*) FROM t.OrdersHeaders oh WHERE ISNULL(oh.IsVoid, 0) = 0 AND ISNULL(oh.IsDelivered, 0) = 0"
            + _company_id_filter(cid, "oh") + extra_oh + ") AS undelivered_orders_count"
        )
    if metric == "daily_sales_pack":
        day_filter = _single_day_filter(filters)
        if not day_filter:
            raise ValueError("daily_sales_pack requires filters.date (YYYY-MM-DD)")
        base_where = (
            "WHERE ISNULL(th.IsVoid, 0) = 0 AND th.TransactionTypeID IN (1, 2)"
            + _company_id_filter(cid, "th", "td")
            + day_filter
        )
        item_join = (
            "INNER JOIN t.Items i ON i.ItemCode = td.ItemCode AND i.CompanyID = td.CompanyID "
        )
        return (
            "SELECT agg.sales_value, agg.sales_qty, agg.returns_value, agg.returns_qty, "
            "agg.sales_value - ISNULL(agg.returns_value, 0) AS net_value, "
            "agg.sales_qty - ISNULL(agg.returns_qty, 0) AS net_qty, "
            "top_qty.top_qty_item_code, top_qty.top_qty_item_name, top_qty.top_qty, "
            "top_val.top_val_item_code, top_val.top_val_item_name, top_val.top_val "
            "FROM ("
            "SELECT "
            f"SUM(CASE WHEN th.TransactionTypeID = 1 THEN {line_amount_sql('td')} ELSE 0 END) AS sales_value, "
            "SUM(CASE WHEN th.TransactionTypeID = 1 THEN ABS(td.Quantity) ELSE 0 END) AS sales_qty, "
            f"SUM(CASE WHEN th.TransactionTypeID = 2 THEN {line_amount_sql('td')} ELSE 0 END) AS returns_value, "
            "SUM(CASE WHEN th.TransactionTypeID = 2 THEN ABS(td.Quantity) ELSE 0 END) AS returns_qty "
            "FROM t.TransactionsHeaders th "
            + _detail_join()
            + base_where
            + ") agg "
            "CROSS APPLY ("
            "SELECT TOP 1 td.ItemCode AS top_qty_item_code, i.Name AS top_qty_item_name, "
            "SUM(ABS(td.Quantity)) AS top_qty "
            "FROM t.TransactionsHeaders th "
            + _detail_join()
            + item_join
            + "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th", "td", "i")
            + day_filter
            + " GROUP BY td.ItemCode, i.Name ORDER BY SUM(ABS(td.Quantity)) DESC"
            + ") top_qty "
            "CROSS APPLY ("
            "SELECT TOP 1 td.ItemCode AS top_val_item_code, i.Name AS top_val_item_name, "
            f"SUM({line_amount_sql('td')}) AS top_val "
            "FROM t.TransactionsHeaders th "
            + _detail_join()
            + item_join
            + "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th", "td", "i")
            + day_filter
            + f" GROUP BY td.ItemCode, i.Name ORDER BY SUM({line_amount_sql('td')}) DESC"
            + ") top_val"
        )
    raise ValueError(f"unknown metric {metric!r}")


def run_metric(
    metric_name: str,
    company_id: int,
    client: str,
    allowed_procs=None,
    filters: dict | None = None,
) -> dict:
    if allowed_procs is None:
        allowed_procs = gate.DEFAULT_ALLOWED_PROCS
    canonical = resolve_metric(metric_name)
    if not canonical:
        known = ", ".join(sorted(METRICS))
        return {"error": f"unknown metric {metric_name!r}. Known: {known}"}
    filters = dict(filters or {})
    if canonical == "sales":
        try:
            tax, returns = _sales_filter_basis(filters)
        except ValueError as exc:
            return {"error": str(exc)}
        sql_text = build_sales_sql(company_id, filters)
        rows = sql.run_select(sql_text, company_id, client, allowed_procs=allowed_procs)
        primary_measure = "net_of_returns" if returns == "net" else "gross_sales"
        return {
            "metric": "sales",
            "sql": sql_text,
            "rows": rows,
            "basis": {"tax": tax, "returns": returns},
            "primary_measure": primary_measure,
        }
    if canonical == "daily_sales_pack" and not _safe_date(
        filters.get("date") or filters.get("from_date") or filters.get("to_date")
    ):
        rows = sql.run_select(
            "SELECT MAX(TransactionDate) AS d FROM t.TransactionsHeaders "
            "WHERE TransactionTypeID = 1 AND ISNULL(IsVoid, 0) = 0",
            company_id,
            client,
            allowed_procs=allowed_procs,
        )
        if rows and rows[0].get("d") is not None:
            filters["date"] = str(rows[0]["d"])[:10]
    sql_text = build_sql(canonical, filters, company_id=company_id)
    rows = sql.run_select(sql_text, company_id, client, allowed_procs=allowed_procs)
    return {"metric": canonical, "sql": sql_text, "rows": rows}
