"""Minimal thread card (I1)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import thread


def test_make_card_sales_codes_only():
    row = {
        "gross_sales": 100.0,
        "returns": 0.0,
        "net_of_returns": 100.0,
        "invoice_count": 2,
        "return_count": 0,
    }
    args = {
        "metric": "sales",
        "filters": {"from_date": "2025-07-01", "to_date": "2025-08-01", "tax": "incl", "returns": "gross"},
    }
    card = thread.make_card("run_metric", args, row)
    assert card["tax"] == "incl"
    assert card["returns"] == "gross"
    assert card["period_label"] == "2025-07-01 .. 2025-08-01"
    assert card["primary_measure"] == "gross_sales"
    assert card["values"]["gross_sales"] == 100.0
    assert "شامل" not in str(card)


def test_card_followups_three_suggestions():
    card = thread.make_card(
        "run_metric",
        {"metric": "sales", "filters": {"from_date": "2025-07-01", "to_date": "2025-08-01"}},
        {"gross_sales": 1},
    )
    fu = thread.card_followups(card)
    assert len(fu) == 3
    assert any("الضريبة" in x for x in fu)
