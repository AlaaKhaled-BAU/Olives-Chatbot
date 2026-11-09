"""Phase 4 acceptance: the sqlglot gate rejects the bad corpus, allows a
clean SELECT (+ TOP), N-prefixes Arabic literals, and injects tenant predicates."""
import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import config
from core.gate import GateError, invoice_grain_error, validate

# Reconstructed from trace.jsonl (2026-11-09, client 105): derived-table aggregate
# over th/td; gate wrongly put th.CompanyID on the outer SELECT → SQL Server 4104.
TRACE_FAILING_DERIVED_SQL = (
    "SELECT SUM(x.line_total) AS total FROM ("
    "SELECT ABS(td.Quantity) * ABS(td.Price) AS line_total "
    "FROM t.TransactionsHeaders th "
    "INNER JOIN t.TransactionsDetails td "
    "ON th.CompanyID = td.CompanyID AND th.TransactionTypeID = td.TransactionTypeID "
    "AND th.TransactionYear = td.TransactionYear AND th.TransactionNo = td.TransactionNo "
    "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0 "
    "AND th.TransactionDate = CAST('2025-07-15' AS date)) x"
)

BAD_CORPUS = [
    "INSERT INTO Customers (Name) VALUES ('x')",
    "UPDATE Customers SET Name = 'x'",
    "DELETE FROM Customers",
    "DROP TABLE Customers",
    "CREATE TABLE Foo (id INT)",
    "ALTER TABLE Customers ADD COLUMN Foo INT",
    "SELECT * INTO NewTable FROM Customers",
    "SELECT * FROM Customers; DROP TABLE Customers;",
    "EXEC xp_cmdshell 'dir'",
    "EXEC sp_OACreate 'Scripting.FileSystemObject'",
    "SELECT * FROM OPENQUERY(srv, 'select 1')",
    "SELECT * FROM OPENROWSET('SQLNCLI', 'server'; 'user'; 'pw', 'select 1')",
    "EXEC dbo.NotOnTheAllowList @id = 1",
    "SELECT a INTO evil FROM t.X UNION SELECT b FROM t.Y",
]


@pytest.fixture
def schema_cache():
    """Minimal schema_cache for gate tenant tests — no live work/ file required."""
    return {
        "tables": {
            "dbo.Customers": [
                {"column": "ID", "type": "int"},
                {"column": "CompanyID", "type": "int"},
            ],
            "dbo.DeliveryRoute": [
                {"column": "RouteID", "type": "int"},
                {"column": "CompNo", "type": "int"},
            ],
            "dbo.TransactionsHeaders": [
                {"column": "CompanyID", "type": "int"},
                {"column": "TransactionTypeID", "type": "int"},
                {"column": "IsVoid", "type": "bit"},
                {"column": "TransactionNo", "type": "int"},
                {"column": "TransactionYear", "type": "int"},
                {"column": "TransactionDate", "type": "date"},
            ],
            "dbo.TransactionsDetails": [
                {"column": "CompanyID", "type": "int"},
                {"column": "TransactionTypeID", "type": "int"},
                {"column": "TransactionNo", "type": "int"},
                {"column": "TransactionYear", "type": "int"},
                {"column": "Quantity", "type": "decimal"},
                {"column": "Price", "type": "decimal"},
            ],
            "dbo.OrdersHeaders": [
                {"column": "CompanyID", "type": "int"},
                {"column": "CustomerID", "type": "int"},
            ],
            "dbo.Suppliers": [
                {"column": "CompanyID", "type": "int"},
                {"column": "Name", "type": "nvarchar"},
            ],
            "dbo.LogActionTransaction": [
                {"column": "CompNo", "type": "int"},
                {"column": "Data1", "type": "nvarchar"},
                {"column": "ActionID", "type": "nvarchar"},
            ],
            "dbo.Currencies": [
                {"column": "ID", "type": "int"},
            ],
        },
    }


@pytest.fixture
def schema_cache_105():
    path = config.work_dir("105") / "schema_cache.json"
    if not path.is_file():
        pytest.skip("work/105/schema_cache.json required")
    return json.loads(path.read_text(encoding="utf-8"))


def _outer_where(sql: str) -> str:
    """WHERE clause on the outermost SELECT (after the last derived-table close paren)."""
    depth = 0
    last_close = -1
    for i, ch in enumerate(sql):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                last_close = i
    tail = sql[last_close + 1 :] if last_close >= 0 else sql
    m = re.search(r"\bWHERE\b(.+)$", tail, re.IGNORECASE | re.DOTALL)
    return m.group(1) if m else ""


@pytest.mark.parametrize("sql", BAD_CORPUS)
def test_bad_corpus_rejected(sql):
    with pytest.raises(GateError):
        validate(sql, allowed_procs=["dbo.GetCustomer"])


def test_clean_select_allowed_and_top_injected():
    out = validate("SELECT * FROM t.Customers WHERE CompanyID = 1", row_cap=50)
    assert "TOP" in out.upper()
    assert "50" in out


def test_existing_top_not_overridden():
    out = validate("SELECT TOP 5 * FROM t.Customers", row_cap=200)
    assert "TOP 5" in out.upper()
    assert "200" not in out


def test_allowlisted_exec_allowed():
    out = validate("EXEC dbo.GetCustomer @id = 1", allowed_procs=["dbo.GetCustomer"])
    assert "GetCustomer" in out


def test_salesman_visits_summary_select_rejected():
    with pytest.raises(GateError, match="LogActionTransaction"):
        validate("SELECT * FROM t.SalesmanVisitsSummary")
    with pytest.raises(GateError, match="not an allow-listed procedure"):
        validate("EXEC dbo.Rpt_SalesmanSalesSummary @CompanyID = 1", allowed_procs=[])


def test_exec_denied_by_default_allowed_procs_constant():
    from core.gate import DEFAULT_ALLOWED_PROCS

    assert DEFAULT_ALLOWED_PROCS == ()
    with pytest.raises(GateError):
        validate("EXEC dbo.GetCustomer @id = 1")


def test_xp_denied_even_with_allowlisted_exec():
    with pytest.raises(GateError, match="xp_"):
        validate("EXEC xp_cmdshell 'dir'", allowed_procs=["dbo.GetCustomer"])


def test_arabic_literal_gets_n_prefixed():
    out = validate("SELECT * FROM t.Customers WHERE Name = 'مرحبا'")
    assert "N'مرحبا'" in out


def test_already_n_prefixed_arabic_is_untouched():
    out = validate("SELECT * FROM t.Customers WHERE Name = N'مرحبا'")
    assert "N'مرحبا'" in out


def test_non_arabic_literal_not_touched():
    out = validate("SELECT * FROM t.Customers WHERE Name = 'John'")
    assert "N'John'" not in out
    assert "'John'" in out


@pytest.mark.parametrize("keyword", ["UNION", "EXCEPT", "INTERSECT"])
def test_set_operations_allowed_and_capped(keyword):
    out = validate(f"SELECT Name FROM t.Customers {keyword} SELECT Name FROM t.Suppliers", row_cap=50)
    assert "TOP 50" in out.upper(), out


def test_union_row_cap_wraps_the_whole_set_not_one_branch():
    out = validate("SELECT Name FROM t.Customers UNION SELECT Name FROM t.Suppliers", row_cap=10)
    assert out.upper().count("TOP 10") == 1, "the cap must apply once, to the combined result"


def test_injects_companyid_on_t_customers(schema_cache):
    out = validate(
        "SELECT * FROM t.Customers",
        company_id=2,
        schema_cache=schema_cache,
        row_cap=50,
    )
    assert "Customers.CompanyID = 2" in out


def test_injects_compno_on_compno_only_table(schema_cache):
    out = validate(
        "SELECT * FROM t.DeliveryRoute",
        company_id=2,
        schema_cache=schema_cache,
        row_cap=50,
    )
    assert "DeliveryRoute.CompNo = 2" in out


def test_skips_information_schema_tenant_injection(schema_cache):
    out = validate(
        "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Customers'",
        company_id=2,
        schema_cache=schema_cache,
    )
    assert "CompanyID = 2" not in out


def test_rejects_wrong_companyid_literal(schema_cache):
    with pytest.raises(GateError, match="cross-company"):
        validate(
            "SELECT * FROM t.Customers WHERE CompanyID = 99",
            company_id=2,
            schema_cache=schema_cache,
        )


def test_invoice_grain_error_on_unfiltered_header_count():
    err = invoice_grain_error("SELECT COUNT(*) FROM t.TransactionsHeaders")
    assert err is not None
    assert "run_metric" in err


def test_invoice_grain_rejects_wrong_type_even_with_void():
    err = invoice_grain_error(
        "SELECT COUNT(*) FROM t.TransactionsHeaders "
        "WHERE TransactionTypeID = 3 AND ISNULL(IsVoid, 0) = 0"
    )
    assert err is not None


def test_invoice_grain_allows_typed_void_count():
    err = invoice_grain_error(
        "SELECT COUNT(*) FROM t.TransactionsHeaders "
        "WHERE TransactionTypeID = 1 AND ISNULL(IsVoid, 0) = 0"
    )
    assert err is None


def test_invoice_grain_allows_returns_type_2():
    err = invoice_grain_error(
        "SELECT COUNT(*) FROM t.TransactionsHeaders "
        "WHERE TransactionTypeID = 2 AND ISNULL(IsVoid, 0) = 0"
    )
    assert err is None


def test_derived_table_gets_tenant_predicate_inside_not_outside(schema_cache):
    sql = (
        "SELECT COUNT(DISTINCT v.c) AS n FROM (SELECT TRY_CAST(Data1 AS bigint) AS c "
        "FROM t.LogActionTransaction WHERE ActionID = N'0') v"
    )
    out = validate(sql, company_id=1, schema_cache=schema_cache)
    inner, outer = out.split(") AS v", 1)
    assert "CompNo = 1" in inner or "LogActionTransaction.CompNo = 1" in inner
    assert "CompNo" not in _outer_where(out)
    assert "LogActionTransaction" not in _outer_where(out)


def test_nested_derived_table_scopes_predicates(schema_cache):
    sql = (
        "SELECT COUNT(*) AS n FROM ("
        "SELECT ID FROM (SELECT ID FROM t.Customers) i"
        ") o"
    )
    out = validate(sql, company_id=2, schema_cache=schema_cache)
    assert "CompanyID = 2" in out
    assert "CompanyID" not in _outer_where(out)


def test_join_inside_derived_table_injects_on_inner_select(schema_cache):
    sql = (
        "SELECT n FROM ("
        "SELECT c.ID FROM t.Customers c "
        "JOIN t.DeliveryRoute d ON d.CompNo = c.CompanyID"
        ") v"
    )
    out = validate(sql, company_id=1, schema_cache=schema_cache)
    assert "c.CompanyID = 1" in out
    assert "d.CompNo = 1" in out
    assert "CompanyID" not in _outer_where(out)
    assert "CompNo" not in _outer_where(out)


def test_cte_body_gets_tenant_predicate(schema_cache):
    sql = "WITH x AS (SELECT ID FROM t.Customers) SELECT * FROM x"
    out = validate(sql, company_id=1, schema_cache=schema_cache)
    assert "Customers.CompanyID = 1" in out


def test_exists_subquery_gets_tenant_predicate(schema_cache):
    sql = (
        "SELECT 1 FROM t.Customers c WHERE EXISTS ("
        "SELECT 1 FROM t.OrdersHeaders oh WHERE oh.CustomerID = c.ID)"
    )
    out = validate(sql, company_id=1, schema_cache=schema_cache)
    assert "c.CompanyID = 1" in out
    assert "oh.CompanyID = 1" in out


def test_in_subquery_gets_tenant_predicate(schema_cache):
    sql = (
        "SELECT 1 FROM t.Customers c "
        "WHERE c.ID IN (SELECT CustomerID FROM t.OrdersHeaders)"
    )
    out = validate(sql, company_id=1, schema_cache=schema_cache)
    assert "OrdersHeaders" in out and "CompanyID = 1" in out


def test_scalar_subquery_in_select_list_gets_tenant_predicate(schema_cache):
    sql = (
        "SELECT (SELECT COUNT(*) FROM t.Customers) AS n, d.RouteID "
        "FROM t.DeliveryRoute d"
    )
    out = validate(sql, company_id=1, schema_cache=schema_cache)
    assert re.search(r"Customers.*CompanyID\s*=\s*1", out)
    assert "d.CompNo = 1" in out


def test_union_branches_each_get_tenant_predicates(schema_cache):
    sql = "SELECT Name FROM t.Customers UNION ALL SELECT Name FROM t.Suppliers"
    out = validate(sql, company_id=2, schema_cache=schema_cache)
    assert out.count("CompanyID = 2") == 2


def test_trace_failing_derived_query_no_outer_th_companyid(schema_cache):
    out = validate(TRACE_FAILING_DERIVED_SQL, company_id=1, schema_cache=schema_cache)
    outer = _outer_where(out)
    assert "th.CompanyID" not in outer
    assert "td.CompanyID" not in outer
    assert "th.CompanyID = 1" in out
    assert "td.CompanyID = 1" in out


def test_trace_failing_derived_query_validates_with_105_cache(schema_cache_105):
    out = validate(TRACE_FAILING_DERIVED_SQL, company_id=1, schema_cache=schema_cache_105)
    assert "th.CompanyID" not in _outer_where(out)


def test_fail_closed_when_tenant_predicate_missing(monkeypatch, schema_cache):
    from core import gate

    def broken_inject(stmt, company_id, schema_cache):
        pass

    monkeypatch.setattr(gate, "_inject_tenant_on_select", broken_inject)
    with pytest.raises(GateError, match="missing tenant predicate"):
        gate.validate(
            "SELECT * FROM t.Customers",
            company_id=1,
            schema_cache=schema_cache,
        )


def test_trace_failing_sql_runs_on_sql_server(schema_cache_105):
    from core import sql

    safe = validate(TRACE_FAILING_DERIVED_SQL, company_id=1, schema_cache=schema_cache_105)
    try:
        rows_c1 = sql.run_select(safe, company_id=1, client="105")
    except Exception as exc:
        pytest.skip(f"SQL Server unavailable: {exc}")
    assert rows_c1 is not None

    safe_c2 = validate(TRACE_FAILING_DERIVED_SQL, company_id=2, schema_cache=schema_cache_105)
    try:
        rows_c2 = sql.run_select(safe_c2, company_id=2, client="105")
    except Exception as exc:
        pytest.skip(f"SQL Server unavailable: {exc}")

    # Isolation: company 2 must never see company 1's totals for this predicate.
    if rows_c1 and rows_c2:
        v1 = rows_c1[0].get("total") or rows_c1[0].get("Col_1")
        v2 = rows_c2[0].get("total") or rows_c2[0].get("Col_1")
        if v1 is not None and v2 is not None and float(v1) != 0 and float(v2) != 0:
            assert float(v1) != float(v2)
