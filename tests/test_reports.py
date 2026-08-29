"""Unit tests for core/reports.py — matcher, aliases, SELECT templates (no EXEC)."""
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import gate, reports
from tests.report_template_schema import invalid_column_refs, load_schema_tables


@pytest.fixture(scope="module")
def schema_tables():
    return load_schema_tables()


def test_match_reports_visits_question_skips_sales_summary():
    hits = reports.match_reports("اعطيني زيارات المندوب اخر اسبوع", "105")
    names = [h["name"] for h in hits]
    assert "Rpt_SalesmanSalesSummary" not in names
    hits = reports.match_reports("تقرير مبيعات المندوب", "105")
    assert hits
    assert hits[0]["name"] == "Rpt_SalesmanSalesSummary"


def test_match_reports_english_alias():
    hits = reports.match_reports("show me salesman sales summary report", "105")
    assert hits
    assert hits[0]["name"] == "Rpt_SalesmanSalesSummary"


def test_match_reports_alias_boost_over_unrelated():
    hits = reports.match_reports("تقرير ملخص النقدية", "105")
    assert hits
    assert hits[0]["name"] == "Rpt_CashSummary"


def test_match_reports_coverage_alias_still_hits():
    hits = reports.match_reports("تقرير التغطية", "105")
    assert hits
    assert hits[0]["name"] == "Rpt_Coverage"


def test_list_template_names_has_eleven():
    names = reports.list_template_names()
    assert len(names) == 11
    assert "Rpt_SalesmanSalesSummary" in names
    assert "Rpt_RouteSummaryBySalesman" in names


def test_build_report_sql_is_select_only():
    sql_text = reports.build_report_sql("Rpt_SalesmanSalesSummary", {})
    assert sql_text is not None
    assert "EXEC" not in sql_text.upper()
    assert "t.TransactionsHeaders" in sql_text
    assert "COUNT(DISTINCT th.TransactionNo)" not in sql_text
    assert "COUNT(*) AS invoice_count" in sql_text


def test_build_report_sql_unknown_returns_none():
    assert reports.build_report_sql("Rpt_DoesNotExist", {}) is None


def test_receipt_templates_use_collections_grain_type_3():
    params = {"from_date": "2025-01-01", "to_date": "2025-07-15"}
    for name in ("Rpt_DailyReceiptsDetails", "Rpt_CollectedReceipts", "Rpt_CashSummary"):
        sql_text = reports.build_report_sql(name, params)
        assert "TransactionTypeID = 3" in sql_text
        assert "ReceiptDate" not in sql_text


def test_receipt_templates_use_transaction_date_not_receipt_date():
    params = {"from_date": "2025-01-01", "to_date": "2025-07-15"}
    for name in ("Rpt_DailyReceiptsDetails", "Rpt_CollectedReceipts", "Rpt_CashSummary"):
        sql_text = reports.build_report_sql(name, params)
        assert "ReceiptDate" not in sql_text
        assert "ReceiptNo" not in sql_text
        assert "TransactionDate" in sql_text


def test_coverage_template_uses_live_delivery_route_columns():
    sql_text = reports.build_report_sql("Rpt_Coverage", {})
    assert "RouteName" not in sql_text
    assert "dr.RouteID" not in sql_text
    assert "cfd.RouteID" in sql_text
    assert "dr.CompNo" in sql_text
    assert "dr.CustomerID" in sql_text


def test_run_report_select_never_calls_exec():
    with patch.object(reports.sql, "run_select", return_value=[{"n": 1}]) as mock_run:
        result = reports.run_report_select("Rpt_CashSummary", 2, "105", allowed_procs=[])
    assert result["rows"] == [{"n": 1}]
    assert "EXEC" not in mock_run.call_args[0][0].upper()
    mock_run.assert_called_once()
    assert mock_run.call_args.kwargs.get("allowed_procs") == []


def test_run_report_select_uses_empty_allowlist_by_default():
    with patch.object(reports.sql, "run_select", return_value=[]) as mock_run:
        reports.run_report_select("Rpt_Coverage", 2, "105")
    assert mock_run.call_args.kwargs.get("allowed_procs") == gate.DEFAULT_ALLOWED_PROCS


def test_run_report_path3_returns_not_certified_without_template():
    with patch.object(reports, "build_report_sql", return_value=None), \
         patch.object(reports, "_catalog_card", return_value={"name": "Rpt_Unknown", "purpose": "Legacy report"}):
        result = reports.run_report("Rpt_Unknown", 2, "105", allowed_procs=[])
    assert result["status"] == "not_certified"
    assert result["message"] == "equivalent SELECT not certified yet"
    assert result["purpose"] == "Legacy report"


def test_run_report_path1_delegates_to_select():
    with patch.object(reports, "run_report_select", return_value={"report": "Rpt_Coverage", "sql": "SELECT 1", "rows": []}) as mock_select:
        reports.run_report("Rpt_Coverage", 2, "105", allowed_procs=[])
    mock_select.assert_called_once()
    assert mock_select.call_args.kwargs["allowed_procs"] == []


def test_sales_and_orders_template_gate_injects_companyid():
    """Scalar subqueries must get tenant predicates; outer WHERE must not bind oh/th."""
    fixture = Path(__file__).parent / "fixtures" / "report_template_schema_105.json"
    live = Path(__file__).parent.parent / "work" / "105" / "schema_cache.json"
    schema_cache = json.loads((live if live.exists() else fixture).read_text(encoding="utf-8"))
    raw = reports.build_report_sql("Rpt_SalesAndOrders", {})
    assert raw is not None
    safe = gate.validate(raw, company_id=2, schema_cache=schema_cache)
    assert "sp.CompanyID = 2" in safe
    assert "oh.CompanyID = 2" in safe
    assert "th.CompanyID = 2" in safe
    outer_tail = safe.split("ORDER BY")[0].split("FROM t.SalesPersons")[-1]
    assert "oh.CompanyID" not in outer_tail
    assert "th.CompanyID" not in outer_tail


def test_sales_and_orders_template_runs_live():
    """Flattened template executes after gate rewrite (live DB when reachable)."""
    try:
        result = reports.run_report_select("Rpt_SalesAndOrders", 2, "105", allowed_procs=[])
    except Exception as exc:
        if "connect" in str(exc).lower() or "login" in str(exc).lower():
            pytest.skip("SQL Server not reachable")
        raise
    if "error" in result:
        pytest.skip(f"live DB unavailable: {result['error']}")
    assert len(result["rows"]) > 0
    imad = next(r for r in result["rows"] if r.get("SalesPersonName") == "Imad")
    assert imad["invoice_count"] == 130


def test_templates_include_aliases_on_cards():
    hits = reports.match_reports("أصناف لم تباع", "105")
    assert hits
    assert hits[0]["name"] == "Rpt_ItemsNotSold"
    assert hits[0].get("aliases")


def test_all_templates_reject_exec_in_sql_field():
    for tmpl in reports.load_templates():
        assert "EXEC" not in tmpl["sql"].upper(), tmpl["name"]


@pytest.mark.parametrize("name", reports.list_template_names())
def test_build_report_sql_for_every_template(name):
    sql_text = reports.build_report_sql(name, {"from_date": "2025-01-01", "to_date": "2025-07-15"})
    assert sql_text
    assert "EXEC" not in sql_text.upper()


@pytest.mark.parametrize("name", reports.list_template_names())
def test_template_columns_exist_on_schema(name, schema_tables):
    params = {
        "from_date": "2025-01-01",
        "to_date": "2025-07-15",
        "sales_person_id": 1,
        "customer_id": 1,
        "item_code": "ITEM1",
    }
    sql_text = reports.build_report_sql(name, params)
    errors = invalid_column_refs(sql_text, schema_tables)
    assert not errors, f"{name}: {errors}"


def test_schema_fixture_has_delivery_route_without_route_name():
    fixture_path = Path(__file__).parent / "fixtures" / "report_template_schema_105.json"
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    dr_cols = {c["column"] for c in data["tables"]["dbo.DeliveryRoute"]}
    assert dr_cols == {"CompNo", "SalesmanNo", "CustomerID", "RouteDate"}
    rc_cols = {c["column"] for c in data["tables"]["dbo.Receipts"]}
    assert "TransactionDate" in rc_cols
    assert "ReceiptDate" not in rc_cols
    assert "ReceiptNo" not in rc_cols


def test_receipt_date_filter_placeholder_uses_transaction_date():
    sql_text = reports.build_report_sql(
        "Rpt_DailyReceiptsDetails",
        {"from_date": "2025-01-01", "to_date": "2025-07-15"},
    )
    assert "r.TransactionDate >=" in sql_text
    assert "ReceiptDate" not in sql_text



def test_match_reports_visit_skips_route_summary():
    hits = reports.match_reports("كم زيارة للمندوب أمس", "105")
    names = [h["name"] for h in hits]
    assert "Rpt_RouteSummaryBySalesman" not in names
    assert "Rpt_Coverage" not in names


def test_run_report_route_summary_needs_salesman():
    result = reports.run_report(
        "Rpt_RouteSummaryBySalesman",
        2,
        "105",
        params={"from_date": "2025-07-01"},
        allowed_procs=[],
        question="تقرير ملخص المسار ليوم أمس",
    )
    assert result.get("status") == "needs_ask"
    assert result.get("missing") == "sales_person_id"
