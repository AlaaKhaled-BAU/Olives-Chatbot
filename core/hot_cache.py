"""L1 master-table snapshots — names/IDs/routes change slowly; never snapshot fact tables."""
import hashlib
import json
import time

from . import config, memory, sql

TTL_SECONDS = 600  # 10 minutes

# Identity-only projections — no SELECT * on Customers/SalesPersons.
# Customers may gain Code when schema_cache shows that column (see l1_sql).
L1_QUERIES = {
    "SalesPersons": (
        "SELECT ID, Name, ForeignName, PositionID, IsSuspended, GroupID, CarID, VehicleId FROM t.SalesPersons"
    ),
    "SalesPersonsDevicePermissions": (
        "SELECT PositionsID, MakeSalesInvoice, MakeOrderTaking, "
        "AllowVanTransfer, AllowUnloadOrder, MakeReturnSales, AllowReturnOrder "
        "FROM t.SalesPersonsDevicePermissions"
    ),
    "DeliveryCars": "SELECT ID, Name, CarType, Barcode FROM t.DeliveryCars",
    "Positions": "SELECT ID, Name FROM t.Positions",
    "Customers": "SELECT ID, Name, ForeignName, IsSuspended FROM t.Customers",
    "Items": "SELECT ItemCode, Name, ForeignName FROM t.Items",
    "ItemsUnits": "SELECT ID, Name FROM t.ItemsUnits",
    "ItemsCategories": "SELECT CategCode, Name, ForeignName FROM t.ItemsCategories",
    "RoutesInformation": "SELECT ID, Name FROM t.RoutesInformation",
    "Companies": "SELECT ID, Name FROM t.Companies",
    "ClientsActive": "SELECT ClientID FROM t.ClientsActive",
    "DocumentsTypes": "SELECT ID, Name, TransactionTypeID FROM t.DocumentsTypes",
    "TransactionsTypes": "SELECT ID, Name FROM t.TransactionsTypes",
    "LogActions": "SELECT ActionId, ActionDesc FROM t.LogActions",
    "PriceLists": "SELECT ID, Name, IsSuspended FROM t.PriceLists",
}

# Fact log is too large to snapshot. lookup_hot("LogActionTransaction") serves
# the ActionID codebook (same rows as LogActions) plus a grain note.
L1_ALIASES = {
    "LogActionTransaction": "LogActions",
    "Permissions": "SalesPersonsDevicePermissions",
    "DevicePermissions": "SalesPersonsDevicePermissions",
}

L1_TABLES = frozenset(L1_QUERIES.keys()) | frozenset(L1_ALIASES)

_CUSTOMERS_BASE_COLS = ("ID", "Name", "ForeignName", "IsSuspended")


def _schema_cache(client: str) -> dict:
    return json.loads((config.work_dir(client) / "schema_cache.json").read_text())


def _table_columns(client: str, table: str) -> set[str]:
    cols = _schema_cache(client).get("tables", {}).get(f"dbo.{table}", [])
    return {c["column"] for c in cols}


def l1_sql(table: str, client: str | None = None) -> str | None:
    """Return the L1 SELECT for a master table. Customers may include Code
    when introspection shows that column on dbo.Customers."""
    base = table.strip().split(".")[-1]
    base = L1_ALIASES.get(base, base)
    if base not in L1_QUERIES:
        return None
    if base == "Customers" and client:
        cols = list(_CUSTOMERS_BASE_COLS)
        if "Code" in _table_columns(client, "Customers"):
            cols.insert(2, "Code")
        return f"SELECT {', '.join(cols)} FROM t.Customers"
    return L1_QUERIES[base]


def _schema_version(client: str) -> str:
    cache = _schema_cache(client)
    payload = json.dumps({"tables": cache.get("tables", {})}, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def cache_key(client: str, company_id: int, table: str, schema_version: str) -> str:
    raw = f"l1|{client}|{company_id}|{table}|{schema_version}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def lookup(table_name: str, company_id: int, client: str) -> dict:
    """Return cached L1 master rows or fetch live. Free — does not spend MAX_QUERIES."""
    table = table_name.strip()
    base = table.split(".")[-1]
    requested = base
    codebook_alias = base in L1_ALIASES
    base = L1_ALIASES.get(base, base)
    if base not in L1_QUERIES:
        return {"error": f"{table!r} is not an L1 master table. Use run_select for fact data."}
    schema_version = _schema_version(client)
    key = cache_key(client, company_id, base, schema_version)
    cached = memory.get_result(key, ttl_seconds=TTL_SECONDS)
    source = "l1_cache"
    if cached is not None:
        rows = cached
    else:
        sql_text = l1_sql(base, client)
        rows = sql.run_select(sql_text, company_id, client)
        memory.set_result(key, rows)
        source = "live"
    out = {"table": base, "rows": rows, "source": source}
    if codebook_alias:
        out["requested"] = requested
        out["note"] = (
            "LogActionTransaction is a high-volume fact log and is not snapshotted. "
            "These rows are t.LogActions (ActionID codebook). "
            "Customer visits: ActionID N'0' CustEntry / N'3' CustLeave, Data1=customer. "
            "Do not count ActionID 7 SystemLogin. Document actions 4/5/9/12 use Data1=year, Data2=doc no. "
            "Query facts with run_select on t.LogActionTransaction."
        )
    return out
