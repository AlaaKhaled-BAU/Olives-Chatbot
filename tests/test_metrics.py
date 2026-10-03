"""Unit tests for core/metrics.py — mocked sql.run_select, no live DB."""
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import metrics

COMPANY_ID = 2


def test_resolve_metric_aliases():
    assert metrics.resolve_metric("net_sales") == "net_sales"
    assert metrics.resolve_metric("مبيعات") == "sales"
    assert metrics.resolve_metric("إجمالي المبيعات") == "sales"
    assert metrics.resolve_metric("أفضل مندوب") == "net_sales_by_salesperson"
    assert metrics.resolve_metric("أعلى مندوب") == "net_sales_by_salesperson"
    assert metrics.resolve_metric("أعلى المناديب") == "net_sales_by_salesperson"
    assert metrics.resolve_metric("best salesman") == "net_sales_by_salesperson"
    assert metrics.resolve_metric("محصلة يومية") == "daily_sales_pack"
    assert metrics.resolve_metric("daily sales") == "daily_sales_pack"
    assert metrics.resolve_metric("returns") == "returns"
    assert metrics.resolve_metric("مرتجعات") == "returns"
    assert metrics.resolve_metric("طلبات") == "orders"
    assert metrics.resolve_metric("van_stock") == "van_stock"
    assert metrics.resolve_metric("بضاعة سيارات") == "van_stock"
    assert metrics.resolve_metric("رصيد السيارات") == "van_stock"
    assert metrics.resolve_metric("عملاء المندوب") == "cfd_assignment"
    assert metrics.resolve_metric("unknown_metric") is None


def test_net_sales_uses_charged_line_not_quantity_times_price():
    sql_text = metrics.build_sql("net_sales", company_id=COMPANY_ID)
    assert "ABS(td.Price)" in sql_text
    assert "ABS(td.DiscountAmount)" in sql_text
    assert "ABS(td.VoucherDiscount)" in sql_text
    assert "CustomerDiscountAmount" in sql_text
    assert "Quantity *" not in sql_text
    for name in ("net_sales_by_salesperson", "sales_pipeline"):
        other = metrics.build_sql(name, company_id=COMPANY_ID)
        assert "Quantity *" not in other
        assert "ABS(td.Price)" in other
    pack = metrics.build_sql(
        "daily_sales_pack", {"date": "2025-07-15"}, company_id=COMPANY_ID
    )
    assert "Quantity * td.Price" not in pack
    assert pack.count("ABS(td.Price)") >= 3


def test_net_sales_sql_has_type_and_void_filters():
    sql_text = metrics.build_sql("net_sales", company_id=COMPANY_ID)
    assert "TransactionTypeID = 1" in sql_text
    assert "ISNULL(th.IsVoid, 0) = 0" in sql_text
    assert "TransactionsDetails" in sql_text
    assert f"th.CompanyID = {COMPANY_ID}" in sql_text
    assert f"td.CompanyID = {COMPANY_ID}" in sql_text
    assert "COUNT(DISTINCT th.TransactionNo)" not in sql_text
    assert "COUNT(*)" in sql_text


def test_net_sales_by_salesperson_groups_and_filters():
    sql_text = metrics.build_sql("net_sales_by_salesperson", company_id=COMPANY_ID)
    assert "GROUP BY th.SalesPersonID, sp.Name" in sql_text
    assert "SalesPersons sp" in sql_text
    assert "TransactionTypeID = 1" in sql_text
    assert f"sp.CompanyID = {COMPANY_ID}" in sql_text
    assert "COUNT(DISTINCT th.TransactionNo)" not in sql_text
    assert "COUNT(*) AS invoice_count" in sql_text


def test_returns_sql_has_type_2_and_void_filter():
    sql_text = metrics.build_sql("returns", company_id=COMPANY_ID)
    assert "TransactionTypeID = 2" in sql_text
    assert "ISNULL(th.IsVoid, 0) = 0" in sql_text
    assert f"th.CompanyID = {COMPANY_ID}" in sql_text


def test_orders_sql_counts_undelivered():
    sql_text = metrics.build_sql("orders", company_id=COMPANY_ID)
    assert "OrdersHeaders" in sql_text
    assert "IsDelivered" in sql_text
    assert "undelivered_orders" in sql_text
    assert f"oh.CompanyID = {COMPANY_ID}" in sql_text


def test_cfd_assignment_joins_positions_id_not_customer_id_to_sp():
    sql_text = metrics.build_sql("cfd_assignment", company_id=COMPANY_ID)
    assert "CustomersFinancialDetails" in sql_text
    assert "PositionsID" in sql_text
    assert "sp.PositionID = cfd.PositionsID" in sql_text
    assert "cfd.CustomerID = sp.ID" not in sql_text.replace(" ", "")
    assert f"c.CompanyID = {COMPANY_ID}" in sql_text


def test_run_metric_calls_run_select_and_returns_sql():
    fake_rows = [{"invoice_count": 238, "gross_amount": 1000.0}]
    with patch.object(metrics.sql, "run_select", return_value=fake_rows) as mock_run:
        result = metrics.run_metric("net_sales", COMPANY_ID, "105", allowed_procs=[])
    mock_run.assert_called_once()
    assert result["metric"] == "net_sales"
    assert result["rows"] == fake_rows
    assert "TransactionTypeID = 1" in result["sql"]
    assert f"CompanyID = {COMPANY_ID}" in result["sql"]


def test_run_metric_unknown_returns_error():
    with patch.object(metrics.sql, "run_select"):
        result = metrics.run_metric("not_a_metric", COMPANY_ID, "105")
    assert "error" in result


def test_run_metric_date_and_salesperson_filters():
    sql_text = metrics.build_sql(
        "net_sales",
        {"from_date": "2025-06-01", "to_date": "2025-06-30", "sales_person_id": 3},
        company_id=COMPANY_ID,
    )
    assert "TransactionDate >= '2025-06-01'" in sql_text
    assert "TransactionDate <= '2025-06-30'" in sql_text
    assert "SalesPersonID = 3" in sql_text


def test_van_stock_optional_salesperson_filter():
    sql_all = metrics.build_sql("van_stock", company_id=COMPANY_ID)
    assert "SalesPersonItemsBalance" in sql_all
    assert f"CompanyID = {COMPANY_ID}" in sql_all
    sql_sp = metrics.build_sql("van_stock", {"sales_person_id": 5}, company_id=COMPANY_ID)
    assert "SalesPersonID = 5" in sql_sp


def test_daily_sales_pack_sql_has_grain_and_top_items():
    sql_text = metrics.build_sql(
        "daily_sales_pack",
        {"date": "2025-07-15"},
        company_id=COMPANY_ID,
    )
    assert "TransactionTypeID IN (1, 2)" in sql_text
    assert "ISNULL(th.IsVoid, 0) = 0" in sql_text
    assert "ABS(td.Quantity)" in sql_text
    assert "top_qty_item_code" in sql_text
    assert "top_val_item_code" in sql_text
    assert "TransactionDate = '2025-07-15'" in sql_text
    assert f"th.CompanyID = {COMPANY_ID}" in sql_text


def test_daily_sales_pack_defaults_last_posting_day():
    with patch.object(metrics.sql, "run_select") as mock_run:
        mock_run.side_effect = [
            [{"d": "2025-07-15"}],
            [{"sales_value": 100}],
        ]
        result = metrics.run_metric("daily_sales_pack", COMPANY_ID, "105")
    assert mock_run.call_count == 2
    assert "TransactionDate = '2025-07-15'" in result["sql"]
    assert result["metric"] == "daily_sales_pack"


def test_build_sales_sql_has_isnull_and_types_one_and_two():
    sql_text = metrics.build_sales_sql(
        COMPANY_ID,
        {"from_date": "2025-06-01", "to_date": "2025-07-01"},
    )
    assert "ISNULL(" in sql_text
    assert "TransactionTypeID IN (1, 2)" in sql_text
    assert "ISNULL(th.IsVoid, 0) = 0" in sql_text
    assert "TransactionDate >= '2025-06-01'" in sql_text
    assert "TransactionDate < '2025-07-01'" in sql_text
    assert "TransactionDate <=" not in sql_text


def test_build_sales_sql_excl_subtracts_tax_amount():
    sql_text = metrics.build_sales_sql(COMPANY_ID, {"tax": "excl"})
    assert "TaxAmount" in sql_text
    incl = metrics.build_sales_sql(COMPANY_ID, {"tax": "incl"})
    assert "TaxAmount" not in incl


def test_build_sales_sql_net_of_returns_subtracts_type_two():
    sql_text = metrics.build_sales_sql(COMPANY_ID, {"returns": "net"})
    assert "TransactionTypeID = 2" in sql_text
    assert "net_of_returns" in sql_text
    assert "ISNULL(SUM(CASE WHEN th.TransactionTypeID = 1" in sql_text
    assert "- ISNULL(SUM(CASE WHEN th.TransactionTypeID = 2" in sql_text


def test_build_sales_sql_group_by_salesperson():
    sql_text = metrics.build_sales_sql(
        COMPANY_ID,
        {"group_by": "salesperson", "from_date": "2025-06-01", "to_date": "2025-07-01"},
    )
    assert "SalesPersonName" in sql_text
    assert "GROUP BY th.SalesPersonID, sp.Name" in sql_text
    assert "SalesPersons sp" in sql_text


def test_run_metric_sales_returns_basis_and_primary_measure():
    fake_rows = [
        {
            "gross_sales": 1000.0,
            "returns": 50.0,
            "net_of_returns": 950.0,
            "invoice_count": 10,
            "return_count": 2,
        }
    ]
    with patch.object(metrics.sql, "run_select", return_value=fake_rows) as mock_run:
        gross = metrics.run_metric(
            "sales",
            COMPANY_ID,
            "105",
            allowed_procs=[],
            filters={"tax": "incl", "returns": "gross"},
        )
        net = metrics.run_metric(
            "sales",
            COMPANY_ID,
            "105",
            allowed_procs=[],
            filters={"returns": "net"},
        )
    assert mock_run.call_count == 2
    assert gross["metric"] == "sales"
    assert gross["basis"] == {"tax": "incl", "returns": "gross"}
    assert gross["primary_measure"] == "gross_sales"
    assert net["basis"]["returns"] == "net"
    assert net["primary_measure"] == "net_of_returns"
    assert "TransactionTypeID IN (1, 2)" in gross["sql"]
