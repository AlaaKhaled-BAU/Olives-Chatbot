"""L1 hot-cache queries must project identity columns explicitly."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import hot_cache


def test_customers_and_salespersons_have_no_select_star():
    for table in ("Customers", "SalesPersons"):
        sql = hot_cache.L1_QUERIES[table]
        assert "SELECT *" not in sql.upper(), sql
        assert "FROM" in sql.upper()


def test_customers_and_salespersons_include_foreignname_and_issuspended():
    for table in ("Customers", "SalesPersons"):
        sql = hot_cache.L1_QUERIES[table]
        assert "ForeignName" in sql
        assert "IsSuspended" in sql


def test_salespersons_includes_position_and_group_ids():
    sql = hot_cache.L1_QUERIES["SalesPersons"]
    assert "PositionID" in sql
    assert "GroupID" in sql


def test_l1_sql_customers_adds_code_only_when_introspected(monkeypatch):
    monkeypatch.setattr(
        hot_cache,
        "_table_columns",
        lambda client, table: {"ID", "Name", "ForeignName", "IsSuspended", "Code"},
    )
    sql = hot_cache.l1_sql("Customers", client="morec")
    assert "Code" in sql
    assert "SELECT *" not in sql.upper()


def test_l1_sql_customers_omits_code_when_absent(monkeypatch):
    monkeypatch.setattr(
        hot_cache,
        "_table_columns",
        lambda client, table: {"ID", "Name", "ForeignName", "IsSuspended"},
    )
    sql = hot_cache.l1_sql("Customers", client="morec")
    assert "Code" not in sql


def test_logactions_is_l1_identity_projection():
    sql = hot_cache.L1_QUERIES["LogActions"]
    assert "SELECT *" not in sql.upper()
    assert "ActionId" in sql and "ActionDesc" in sql
    assert hot_cache.l1_sql("LogActionTransaction") == hot_cache.L1_QUERIES["LogActions"]
    assert "LogActionTransaction" in hot_cache.L1_TABLES
