"""Vault tools: procedure body stripping, schema search, compiled cards (Wave 6)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import vault
from setup import compile_vault_cards


def _ensure_cards(client: str = "morec"):
    compile_vault_cards.write_sqlite(client, compile_vault_cards.compile_cards())


def test_read_schema_note_on_report_returns_metadata_not_body():
    note = vault.read_schema_note(name="Rpt_SalesmanSalesComparison", database="Olives_BO")
    assert "error" not in note
    content = note["content"]
    assert isinstance(content, dict)
    assert content["kind"] == "procedure"
    assert "CREATE PROCEDURE" not in str(content).upper()
    assert "metadata" in content
    assert content["metadata"].get("name") == "Rpt_SalesmanSalesComparison"


def test_search_schema_notes_finds_transactions():
    results = vault.search_schema_notes("TransactionsHeaders", type_filter="table")
    assert results
    assert any("TransactionsHeaders" in r["name"] for r in results)


def test_get_joins_for_customers():
    joins = vault.get_joins("Customers")
    assert joins["table"] == "Customers"
    assert joins["relations"]


def test_customers_card_has_purpose_not_reads_708():
    _ensure_cards()
    cards = vault._load_cards("morec")
    customers = next(c for c in cards if c["kind"] == "table" and c["name"] == "Customers")
    assert customers["purpose"]
    assert "Central registry" in customers["purpose"]
    blob = json.dumps(customers)
    assert "Reads (708)" not in blob
    assert "Impact / Procedures" not in blob


def test_retrieve_territory_question_includes_cfd_and_playbook_override():
    _ensure_cards()
    hits = vault.retrieve_cards("عملاء كل مندوب", "morec", limit=3)
    names = {c["name"] for c in hits if c["kind"] == "table"}
    assert "CustomersFinancialDetails" in names
    assert "Positions" in names
    formatted = vault.format_retrieved_cards("عملاء كل مندوب", hits)
    assert "override: playbook" in formatted
    assert "PositionsID" in formatted
    # Must not be only the naive SalesPersonID relation without override context
    assert "Customers--SalesPersons" in formatted


def test_retrieve_arabic_sales_alias():
    _ensure_cards()
    hits = vault.retrieve_cards("كم مبيعات الشهر", "morec", limit=3)
    names = {c["name"] for c in hits if c["kind"] == "table"}
    assert "TransactionsHeaders" in names
