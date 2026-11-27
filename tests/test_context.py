"""Unit tests for core/context.py — KV-cache friendly context builder."""
import datetime
from pathlib import Path
import pytest

from core import context, gate, cache_loader, sql, config


def test_core_tables_spec():
    """Verify CORE_TABLES contains exactly 45 lowercase ASCII bare table names."""
    assert isinstance(context.CORE_TABLES, frozenset)
    assert len(context.CORE_TABLES) == 45
    for table in context.CORE_TABLES:
        assert table.islower(), f"Table {table} is not lowercase"
        assert table.isascii(), f"Table {table} is not ASCII"
        assert "." not in table, f"Table {table} has schema prefix"

    # Spot-check critical business tables
    expected_samples = [
        "transactionsheaders", "transactionsdetails", "transactionstypes",
        "ordersheaders", "ordersdetails", "receipts", "checks", "bankdeposithf",
        "customers", "customersfinancialdetails", "positions", "salespersons",
        "salespersonsdevicepermissions", "salespersonsroutes", "salespersonroutebydate",
        "routesinformation", "deliveryroute", "items", "itemsunits", "itemscategories",
        "pricelists", "pricelistdetails", "logactiontransaction", "logactions",
        "salespersonitemsbalance", "storesbalances", "salespersonstocktacking",
        "transfersordersheaders", "transfersordersdetails", "deliverycars",
        "companies", "clientsactive", "currencies", "systemoptions", "systemcodes",
        "customertargets", "promotions", "promotiontypes",
        "requesttoadddiscount", "requestsalesmanwillnotvisit", "requesttovisitcustomernotinroute",
        "ot_storeitemsqty", "ot_storeitemsqty_main", "ot_itemsmf",
    ]
    for s in expected_samples:
        assert s in context.CORE_TABLES, f"Missing expected core table: {s}"


def test_strip_wiki():
    """Verify _strip_wiki removes [[...]] and |alias correctly."""
    assert context._strip_wiki("[[Customers]]") == "Customers"
    assert context._strip_wiki("[[Customers|Cust]]") == "Customers"
    assert context._strip_wiki("[[dbo.Customers|Cust]]") == "dbo.Customers"
    assert context._strip_wiki("Customers") == "Customers"
    assert context._strip_wiki("[[  Items  |  Alias  ]]") == "Items"
    assert context._strip_wiki("[[TransactionsHeaders]]") == "TransactionsHeaders"
    assert context._strip_wiki("[[Positions|]]") == "Positions"
    assert context._strip_wiki("") == ""
    assert context._strip_wiki(None) == ""


def test_schema_block_core_filtering_and_compact_directory():
    """Verify schema_block filters core tables and outputs compact other-tables list."""
    cache = {
        "has_tenant_view": {
            "dbo.TransactionsHeaders": True,
            "dbo.Customers": True,
            "dbo.OtherTable1": True,
            "dbo.OtherTable2": True,
            "dbo.SecretInternal": False,  # No tenant view -> should be excluded
            "dbo.SalesmanVisitsSummary": True,  # In HIDDEN_TABLES -> should be excluded
            "dbo.Customers_Old": True,  # Junk suffix -> excluded
            "dbo.Items_temp": True,  # Junk suffix -> excluded
            "dbo.Orders_": True,  # Junk suffix -> excluded
        },
        "tables": {
            "dbo.TransactionsHeaders": [
                {"column": "CompanyID", "type": "int"},
                {"column": "TransactionDate", "type": "datetime"},
                {"column": "TotalNet", "type": "decimal"},
            ],
            "dbo.Customers": [
                {"column": "companyid", "type": "int"},
                {"column": "CustomerID", "type": "bigint"},
                {"column": "Name", "type": "nvarchar"},
            ],
            "dbo.OtherTable1": [
                {"column": "CompanyID", "type": "int"},
                {"column": "ColA", "type": "nvarchar"},
            ],
            "dbo.OtherTable2": [
                {"column": "CompanyID", "type": "int"},
                {"column": "ColB", "type": "int"},
            ],
            "dbo.SecretInternal": [{"column": "ID", "type": "int"}],
            "dbo.SalesmanVisitsSummary": [{"column": "ID", "type": "int"}],
            "dbo.Customers_Old": [{"column": "ID", "type": "int"}],
            "dbo.Items_temp": [{"column": "ID", "type": "int"}],
            "dbo.Orders_": [{"column": "ID", "type": "int"}],
        },
    }

    # Test core_only=True
    text_core = context.schema_block(cache, core_only=True)
    assert "- dbo.TransactionsHeaders(TransactionDate, TotalNet)" in text_core
    assert "- dbo.Customers(CustomerID, Name)" in text_core
    # Verify CompanyID is dropped from column lists (case-insensitive)
    assert "(CompanyID" not in text_core and ", CompanyID" not in text_core
    assert "(companyid" not in text_core and ", companyid" not in text_core
    assert "- dbo.OtherTable1(" not in text_core
    assert "- dbo.OtherTable2(" not in text_core
    assert "## Other queryable tenant views (names only — use introspect_schema for columns)" in text_core
    assert "dbo.OtherTable1, dbo.OtherTable2" in text_core
    assert "SecretInternal" not in text_core
    assert "SalesmanVisitsSummary" not in text_core
    assert "Customers_Old" not in text_core
    assert "Items_temp" not in text_core
    assert "Orders_" not in text_core

    # Test core_only=False (legacy behavior)
    text_all = context.schema_block(cache, core_only=False)
    assert "- dbo.TransactionsHeaders(TransactionDate, TotalNet)" in text_all
    assert "- dbo.Customers(CustomerID, Name)" in text_all
    assert "- dbo.OtherTable1(ColA)" in text_all
    assert "- dbo.OtherTable2(ColB)" in text_all
    assert "## Other queryable tenant views" not in text_all
    assert "SecretInternal" not in text_all
    assert "SalesmanVisitsSummary" not in text_all


def test_schema_block_no_other_tables():
    """When all queryable tables are core tables, other-tables section is omitted."""
    cache = {
        "has_tenant_view": {"dbo.Customers": True},
        "tables": {
            "dbo.Customers": [{"column": "CustomerID", "type": "bigint"}],
        },
    }
    text = context.schema_block(cache, core_only=True)
    assert "- dbo.Customers(CustomerID)" in text
    assert "## Other queryable tenant views" not in text


def test_all_cards_block_filtering_and_strip_wiki(monkeypatch):
    """Verify all_cards_block respects CORE_TABLES, HIDDEN_TABLES, and _strip_wiki."""
    mock_cards = [
        {"kind": "table", "name": "Customers", "purpose": "Customer accounts", "foreign_keys": "CityID"},
        {"kind": "table", "name": "CustomInternalTable", "purpose": "internal", "foreign_keys": "ID"},
        {"kind": "table", "name": "SalesmanVisitsSummary", "purpose": "hidden", "foreign_keys": "ID"},
        {
            "kind": "relation",
            "parent": "[[Customers|Cust]]",
            "referenced": "[[Positions]]",
            "columns": "PositionID",
            "business_meaning": "Customer primary position",
        },
        {
            "kind": "relation",
            "parent": "[[CustomInternalTable]]",
            "referenced": "[[AnotherInternalTable]]",
            "columns": "InternalID",
            "business_meaning": "Internal join",
        },
    ]
    monkeypatch.setattr(cache_loader, "load_vault_cards", lambda client: mock_cards)

    # With core_only=True
    text_core = context.all_cards_block("morec", core_only=True)
    assert "- TBL Customers — Customer accounts | FK CityID" in text_core
    assert "REL [[Customers|Cust]]→[[Positions]]: PositionID — Customer primary position" in text_core
    assert "CustomInternalTable" not in text_core
    assert "AnotherInternalTable" not in text_core
    assert "SalesmanVisitsSummary" not in text_core

    # With core_only=False
    text_all = context.all_cards_block("morec", core_only=False)
    assert "TBL Customers" in text_all
    assert "TBL CustomInternalTable" in text_all
    assert "REL [[CustomInternalTable]]→[[AnotherInternalTable]]" in text_all
    assert "SalesmanVisitsSummary" not in text_all


def test_all_cards_block_fail_soft(monkeypatch):
    """When vault cards fail to load, return empty string."""
    def _raise(c):
        raise RuntimeError("db error")

    monkeypatch.setattr(cache_loader, "load_vault_cards", _raise)
    assert context.all_cards_block("morec") == ""

    monkeypatch.setattr(cache_loader, "load_vault_cards", lambda c: [])
    assert context.all_cards_block("morec") == ""


def test_static_prefix_and_prefix_hash_determinism(monkeypatch):
    """Verify static_prefix byte stability and prefix_hash determinism."""
    cache = {
        "tables": {
            "dbo.Customers": [{"column": "CustomerID", "type": "bigint"}],
            "dbo.OtherNonCore": [{"column": "ID", "type": "int"}],
        }
    }
    monkeypatch.setattr(cache_loader, "load_vault_cards", lambda c: [])

    msgs1 = context.static_prefix("morec", cache, max_queries=4, core_only=True)
    msgs2 = context.static_prefix("morec", cache, max_queries=4, core_only=True)
    assert msgs1 == msgs2

    h1 = context.prefix_hash("morec", cache, max_queries=4, core_only=True)
    h2 = context.prefix_hash("morec", cache, max_queries=4, core_only=True)
    assert h1 == h2
    assert len(h1) == 16

    # core_only=False produces different hash
    h_all = context.prefix_hash("morec", cache, max_queries=4, core_only=False)
    assert h1 != h_all
    # Different max_queries produces different hash
    h_q6 = context.prefix_hash("morec", cache, max_queries=6, core_only=True)
    assert h1 != h_q6


def test_tenant_freshness_operational_profile_and_caching(monkeypatch):
    """Verify tenant_freshness query logic, operational_profile calculation, and caching."""
    cache_loader.clear_all()
    calls = 0

    def mock_run_select(query, cid, client):
        nonlocal calls
        calls += 1
        assert "TransactionTypeID = 1 AND ISNULL(IsVoid,0) = 0" in query
        assert "OrdersHeaders WHERE ISNULL(IsVoid,0) = 0" in query
        return [{
            "max_invoice_date": datetime.date(2026, 5, 1),
            "invoice_count": 10,
            "max_order_date": datetime.date(2026, 5, 2),
            "order_count": 100,
        }]

    monkeypatch.setattr(sql, "run_select", mock_run_select)

    # 1. First call computes Pre-Sales Dominant (order_count 100 > 3 * 10)
    res1 = context.tenant_freshness("morec", 1, ttl_s=60.0)
    assert res1["operational_profile"] == "Pre-Sales Dominant"
    assert res1["max_invoice_date"] == "2026-05-01"
    assert res1["max_order_date"] == "2026-05-02"
    assert res1["invoice_count"] == 10
    assert res1["order_count"] == 100
    assert calls == 1

    # 2. Second call uses cache (ttl_cache)
    res2 = context.tenant_freshness("morec", 1, ttl_s=60.0)
    assert res2 == res1
    assert calls == 1

    # 3. Cash Van Dominant: invoice_count 100 > 3 * 10
    cache_loader.clear_all()
    monkeypatch.setattr(sql, "run_select", lambda q, cid, client: [{
        "max_invoice_date": "2026-05-01",
        "invoice_count": 100,
        "max_order_date": "2026-05-02",
        "order_count": 10,
    }])
    res_van = context.tenant_freshness("morec", 1)
    assert res_van["operational_profile"] == "Cash Van Dominant"

    # 4. Hybrid: invoice_count 100, order_count 80
    cache_loader.clear_all()
    monkeypatch.setattr(sql, "run_select", lambda q, cid, client: [{
        "max_invoice_date": "2026-05-01",
        "invoice_count": 100,
        "max_order_date": "2026-05-02",
        "order_count": 80,
    }])
    res_hybrid = context.tenant_freshness("morec", 1)
    assert res_hybrid["operational_profile"] == "Hybrid"


def test_tenant_freshness_fail_soft(monkeypatch):
    """Verify tenant_freshness fails soft to {} when DB is unavailable or empty."""
    cache_loader.clear_all()

    def mock_err(q, cid, client):
        raise ConnectionError("SQL Server unreachable")

    monkeypatch.setattr(sql, "run_select", mock_err)
    assert context.tenant_freshness("morec", 1) == {}

    cache_loader.clear_all()
    monkeypatch.setattr(sql, "run_select", lambda q, cid, client: [])
    assert context.tenant_freshness("morec", 1) == {}


def test_format_tenant_context():
    """Verify format_tenant_context generates concise 3-5 line block."""
    freshness = {
        "max_invoice_date": "2026-04-15",
        "max_order_date": "2026-04-20",
        "operational_profile": "Pre-Sales Dominant",
    }
    text = context.format_tenant_context("morec", 1, freshness)
    assert "CompanyID: 1 (pinned)" in text
    assert f"calendar_today: {datetime.date.today().isoformat()}" in text
    assert "max_invoice_date: 2026-04-15" in text
    assert "max_order_date: 2026-04-20" in text
    assert "operational_profile: Pre-Sales Dominant" in text

    # Verify fallback on empty freshness
    text_empty = context.format_tenant_context("morec", 2, {})
    assert "CompanyID: 2 (pinned)" in text_empty
    assert "max_invoice_date: none" in text_empty
    assert "max_order_date: none" in text_empty
    assert "operational_profile: none" in text_empty


def test_static_prefix_size_reduction():
    """Verify that core_only=True significantly reduces prefix size."""
    # Check if real work/morec/schema_cache.json exists
    real_path = Path("work/morec/schema_cache.json")
    if real_path.exists():
        import json
        cache = json.loads(real_path.read_text(encoding="utf-8"))
        msgs = context.static_prefix("morec", cache, core_only=True)
        total_chars = sum(len(m["content"]) for m in msgs)
        assert total_chars < 65000, f"Expected < 65,000 chars, got {total_chars}"

    # Also test on a large synthetic schema of 100 tables with 25 columns each
    synthetic_tables = {}
    has_views = {}
    for i in range(100):
        tname = f"dbo.Table_{i:03d}"
        synthetic_tables[tname] = [{"column": f"Column_{j:02d}", "type": "int"} for j in range(25)]
        has_views[tname] = True
    # Add a core table
    synthetic_tables["dbo.TransactionsHeaders"] = [{"column": f"Col_{j}", "type": "int"} for j in range(25)]
    has_views["dbo.TransactionsHeaders"] = True

    synthetic_cache = {"tables": synthetic_tables, "has_tenant_view": has_views}

    schema_full = context.schema_block(synthetic_cache, core_only=False)
    schema_core = context.schema_block(synthetic_cache, core_only=True)

    # Core schema block should be less than 10% of full schema block
    assert len(schema_core) < len(schema_full) * 0.1, (
        f"Core schema ({len(schema_core)}) should be < 10% of full schema ({len(schema_full)})"
    )

    prefix_full = context.static_prefix("morec", synthetic_cache, core_only=False)
    prefix_core = context.static_prefix("morec", synthetic_cache, core_only=True)

    len_full = sum(len(m["content"]) for m in prefix_full)
    len_core = sum(len(m["content"]) for m in prefix_core)

    # Total prefix (including system.md and playbook) should be reduced significantly
    assert len_core < len_full
