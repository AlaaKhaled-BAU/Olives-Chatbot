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


def test_count_note_tells_the_model_what_to_do():
    assert "line_count_columns" in verify.COUNT_NOTE
    assert "CAST(TransactionYear AS varchar(4))" in verify.COUNT_NOTE


def test_line_count_columns_names_the_offending_alias():
    s = (
        "SELECT th.CustomerID, COUNT(*) AS InvCount, COUNT(DISTINCT th.CustomerID) AS Buyers "
        "FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
        "ON td.TransactionNo = th.TransactionNo GROUP BY th.CustomerID"
    )
    assert verify.line_count_columns(s) == ["invcount"]


def test_line_count_columns_follow_reaggregation_through_cte():
    s = (
        "WITH inv AS (SELECT th.CustomerID, COUNT(*) AS InvCount "
        "FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
        "ON td.TransactionNo = th.TransactionNo GROUP BY th.CustomerID) "
        "SELECT (SELECT COUNT(*) FROM inv) AS BoughtCustomers, "
        "(SELECT ISNULL(SUM(InvCount),0) FROM inv) AS InvoiceCount"
    )
    assert verify.line_count_columns(s) == ["invcount", "invoicecount"]


def test_header_key_count_is_not_a_line_count_column():
    s = (
        "SELECT COUNT(DISTINCT CAST(th.TransactionYear AS varchar(4)) + '-' + "
        "CAST(th.TransactionNo AS varchar(20))) AS invoices "
        "FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
        "ON td.TransactionNo = th.TransactionNo"
    )
    assert verify.line_count_columns(s) == []


def test_plain_count_star_over_detail_join_is_still_lines():
    s = (
        "SELECT COUNT(*) AS n FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
        "ON td.TransactionNo = th.TransactionNo"
    )
    assert verify.count_scopes(s) == [{"kind": "lines", "func": "count"}]


def test_metrics_build_sales_sql_is_header_grain():
    s = metrics.build_sales_sql(1, {"from_date": "2026-10-01", "to_date": "2026-11-01"})
    kinds = {x["kind"] for x in verify.count_scopes(s)}
    assert "lines" not in kinds
    assert "header" in kinds


def test_metrics_net_sales_by_salesperson_is_header_grain():
    s = metrics.build_sql(
        "net_sales_by_salesperson",
        company_id=1,
        filters={"from_date": "2026-10-01", "to_date": "2026-11-01"},
    )
    kinds = {x["kind"] for x in verify.count_scopes(s)}
    assert kinds == {"header"}


@pytest.mark.parametrize(
    "sql,kind",
    [
        (
            "SELECT COUNT(DISTINCT th.TransactionNo) AS n FROM t.TransactionsHeaders th "
            "JOIN t.TransactionsDetails td ON td.TransactionNo = th.TransactionNo",
            "header",
        ),
        (
            "SELECT COUNT(DISTINCT CASE WHEN th.TransactionTypeID = 1 THEN th.TransactionNo END) AS n "
            "FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
            "ON td.TransactionNo = th.TransactionNo",
            "header",
        ),
        (
            "SELECT COUNT(DISTINCT CONCAT(th.TransactionYear, '-', th.TransactionNo)) AS n "
            "FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
            "ON td.TransactionNo = th.TransactionNo",
            "header",
        ),
        (
            "SELECT COUNT(DISTINCT CAST(th.TransactionYear AS varchar(4)) + '-' + "
            "CAST(th.TransactionNo AS varchar(20))) AS n "
            "FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
            "ON td.TransactionNo = th.TransactionNo",
            "header",
        ),
        (
            "SELECT COUNT(DISTINCT th.CustomerID) AS n FROM t.TransactionsHeaders th "
            "JOIN t.TransactionsDetails td ON td.TransactionNo = th.TransactionNo",
            "other",
        ),
        (
            "SELECT COUNT(DISTINCT td.ItemCode) AS n FROM t.TransactionsHeaders th "
            "JOIN t.TransactionsDetails td ON td.TransactionNo = th.TransactionNo",
            "lines",
        ),
        (
            "SELECT COUNT(*) AS n FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
            "ON td.TransactionNo = th.TransactionNo",
            "lines",
        ),
        (
            "SELECT COUNT(DISTINCT th.TransactionYear) AS n FROM t.TransactionsHeaders th "
            "JOIN t.TransactionsDetails td ON td.TransactionNo = th.TransactionNo",
            "other",
        ),
        (
            "SELECT COUNT(*) AS a, COUNT(DISTINCT th.TransactionNo) AS b "
            "FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
            "ON td.TransactionNo = th.TransactionNo",
            "lines",
        ),
        (
            "SELECT COUNT(*) AS n FROM (SELECT 1 AS x) sq JOIN t.TransactionsDetails td ON 1=1",
            "lines",
        ),
    ],
)
def test_detail_join_count_grain_table(sql, kind):
    scopes = verify.count_scopes(sql)
    assert scopes and scopes[0]["kind"] == kind


def test_sales_metric_with_customer_count_is_header_grain():
    sql = metrics.build_sales_sql(1, {"from_date": "2026-10-01", "to_date": "2026-11-01"})
    assert "customer_count" in sql
    assert [s["kind"] for s in verify.count_scopes(sql)] == ["header"]


def test_distinct_header_attribute_alone_is_not_a_line_count():
    sql = ("SELECT COUNT(DISTINCT th.CustomerID) AS custs FROM t.TransactionsHeaders th "
           "JOIN t.TransactionsDetails td ON th.TransactionNo = td.TransactionNo")
    assert [s["kind"] for s in verify.count_scopes(sql)] == ["other"]


def test_distinct_detail_column_still_counts_lines():
    sql = ("SELECT COUNT(DISTINCT td.ItemCode) AS n FROM t.TransactionsHeaders th "
           "JOIN t.TransactionsDetails td ON th.TransactionNo = td.TransactionNo")
    assert [s["kind"] for s in verify.count_scopes(sql)] == ["lines"]
