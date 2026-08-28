"""Phase 4 acceptance: the sqlglot gate rejects the bad corpus, allows a
clean SELECT (+ TOP), N-prefixes Arabic literals, and injects tenant predicates."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core.gate import GateError, invoice_grain_error, validate

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
          ],
          "dbo.Currencies": [
              {"column": "ID", "type": "int"},
          ],
      },
  }


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
