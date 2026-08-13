"""Phase 4 acceptance: the sqlglot gate rejects the bad corpus, allows a
clean SELECT (+ TOP), and N-prefixes Arabic literals."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core.gate import GateError, validate

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
    # C6b: verified live that sqlglot parses this without complaint, and the
    # top-level Union node's OWN "into" arg is None even though a real Into
    # node sits on the first branch -- widening the allowed-statement-types
    # check to include Union/Except/Intersect without ALSO checking every
    # nested exp.Select would have opened exactly this bypass.
    "SELECT a INTO evil FROM t.X UNION SELECT b FROM t.Y",
]


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
    """C6b: these are read-only and common for the comparative questions
    ("this month vs last month") C4's multi-query budget exists to
    answer -- CTE/subquery/GROUP BY already passed through the gate,
    there was no reason these three were singled out and rejected."""
    out = validate(f"SELECT Name FROM t.Customers {keyword} SELECT Name FROM t.Suppliers", row_cap=50)
    assert "TOP 50" in out.upper(), out


def test_union_row_cap_wraps_the_whole_set_not_one_branch():
    out = validate("SELECT Name FROM t.Customers UNION SELECT Name FROM t.Suppliers", row_cap=10)
    assert out.upper().count("TOP 10") == 1, "the cap must apply once, to the combined result"
