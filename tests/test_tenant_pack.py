"""Tenant pack live facts and calendar_today injection."""
import datetime
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import tenant_pack


def test_build_includes_calendar_today():
    with patch.object(tenant_pack, "_live_facts", return_value={}):
        pack = tenant_pack.build("morec", company_id=2)
    today = datetime.date.today().isoformat()
    assert f"calendar_today: {today}" in pack


def test_live_facts_batches_max_dates_in_one_select(monkeypatch):
    import importlib

    import core.tenant_pack as tp

    importlib.reload(tp)
    captured = []

    def fake_run_select(query, company_id, client):
        captured.append(query)
        if "max_invoice_date" in query:
            return [{"max_invoice_date": "2025-07-15", "max_order_date": "2025-07-10"}]
        return []

    monkeypatch.setattr(tp.sql, "run_select", fake_run_select)
    facts = tp._live_facts(2, "105")

    assert len(captured) == 3
    max_dates_query = captured[1]
    assert "max_invoice_date" in max_dates_query
    assert "max_order_date" in max_dates_query
    assert "TransactionsHeaders" in max_dates_query
    assert "OrdersHeaders" in max_dates_query
    assert facts["max_dates"][0]["max_invoice_date"] == "2025-07-15"
    assert facts["max_dates"][0]["max_order_date"] == "2025-07-10"


def test_build_labels_max_invoice_and_order_dates():
    facts = {
        "max_dates": [{"max_invoice_date": "2025-07-15", "max_order_date": "2025-07-10"}],
    }
    with patch.object(tenant_pack, "_live_facts", return_value=facts):
        pack = tenant_pack.build("105", company_id=2)
    assert "max_invoice_date: 2025-07-15" in pack
    assert "max_order_date: 2025-07-10" in pack
    assert "Max TransactionDate" not in pack
