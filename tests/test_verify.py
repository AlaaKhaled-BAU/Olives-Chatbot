"""L2: count scope detection and header recount SQL (SQL strings only)."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import metrics, verify


@pytest.fixture
def schema_cache():
    return {
        "tables": {
            "dbo.TransactionsHeaders": [
                {"column": "CompanyID", "type": "int"},
                {"column": "TransactionTypeID", "type": "int"},
                {"column": "TransactionYear", "type": "int"},
                {"column": "TransactionNo", "type": "int"},
                {"column": "IsVoid", "type": "bit"},
                {"column": "TransactionDate", "type": "datetime"},
            ],
        },
    }


JULY_LINES_COUNT = """
SELECT COUNT(*) AS line_count
FROM t.TransactionsHeaders th
INNER JOIN t.TransactionsDetails td
  ON th.CompanyID = td.CompanyID
 AND th.TransactionTypeID = td.TransactionTypeID
 AND th.TransactionYear = td.TransactionYear
 AND th.TransactionNo = td.TransactionNo
WHERE th.CompanyID = 2
  AND th.TransactionTypeID = 1
  AND ISNULL(th.IsVoid, 0) = 0
  AND th.TransactionDate >= '2025-07-01'
  AND th.TransactionDate < '2025-08-01'
"""


def test_net_sales_has_header_count_not_lines(schema_cache):
    sql = metrics.build_sql("net_sales", company_id=2, filters={"from_date": "2025-07-01", "to_date": "2025-07-31"})
    scopes = verify.count_scopes(sql)
    kinds = {s["kind"] for s in scopes}
    assert "lines" not in kinds
    assert "header" in kinds
    assert not verify.needs_header_recount(sql, schema_cache)


def test_lines_join_count_scope():
    scopes = verify.count_scopes(JULY_LINES_COUNT)
    assert scopes == [{"kind": "lines", "func": "count"}]


def test_needs_header_recount_july_shape(schema_cache):
    assert verify.needs_header_recount(JULY_LINES_COUNT, schema_cache)


def test_needs_header_recount_skips_getdate(schema_cache):
    sql = JULY_LINES_COUNT.replace(
        "th.TransactionDate < '2025-08-01'",
        "th.TransactionDate < DATEADD(month, 1, '2025-07-01')",
    )
    assert not verify.needs_header_recount(sql, schema_cache)


def test_needs_header_recount_skips_salesperson(schema_cache):
    sql = JULY_LINES_COUNT.replace(
        "AND th.TransactionTypeID = 1",
        "AND th.TransactionTypeID = 1 AND th.SalesPersonID = 5",
    )
    assert not verify.needs_header_recount(sql, schema_cache)


def test_needs_header_recount_skips_detail_predicate(schema_cache):
    sql = JULY_LINES_COUNT + " AND td.ItemID = 99"
    assert not verify.needs_header_recount(sql, schema_cache)


def test_header_recount_sql_distinct_headers():
    out = verify.header_recount_sql(JULY_LINES_COUNT)
    assert out is not None
    upper = out.upper()
    assert "COUNT(*)" in upper
    assert "DISTINCT" in upper
    assert "TRANSACTIONSHEADERS" in upper
    assert "TRANSACTIONDATE" in upper
    assert "TRANSACTIONSDETAILS" not in upper


def test_header_only_count_is_not_lines():
    sql = (
        "SELECT COUNT(*) AS invoice_count FROM t.TransactionsHeaders th "
        "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid,0)=0 AND th.CompanyID = 2"
    )
    assert verify.count_scopes(sql) == [{"kind": "header", "func": "count"}]


def test_count_note_constant():
    assert verify.COUNT_NOTE == "counts lines, not invoice headers"
