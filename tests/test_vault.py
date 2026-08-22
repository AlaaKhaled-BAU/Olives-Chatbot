"""Vault tools: procedure body stripping, schema search, live FK joins, module map (Lane B)."""
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import module_map, tenant_pack, vault
from setup import compile_module_map, compile_vault_cards


def _ensure_cards(client: str = "morec"):
    compile_vault_cards.write_sqlite(client, compile_vault_cards.compile_cards())


def _ensure_module_map(client: str = "morec"):
    compile_module_map.write(client, compile_module_map.compile_map())


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
    joins = vault.get_joins("Customers", client="morec")
    assert joins["table"] == "Customers"
    assert joins["relations"]
    assert joins["live_foreign_keys"]


def test_get_joins_live_fk_without_vault_relation_note():
    """SalesPersonItemsBalance has live FKs but no Relations/*.md note."""
    joins = vault.get_joins("SalesPersonItemsBalance", client="morec")
    assert joins["live_foreign_keys"], "expected live FKs from schema_cache"
    live_names = {fk["fk_name"] for fk in joins["live_foreign_keys"]}
    assert "FK_SalesPersonItemsBalance_SalesPersons" in live_names
    assert "FK_SalesPersonItemsBalance_Items" in live_names
    assert joins["relations"][0]["source"] == "live_schema_cache"
    vault_only = [r for r in joins["vault_relations"] if r.get("source") == "vault"]
    assert not vault_only


def test_get_joins_live_fk_preferred_over_vault_relation():
    """Customers--SalesPersons vault note exists; live FKs still listed first."""
    joins = vault.get_joins("Customers", client="morec")
    assert joins["live_foreign_keys"]
    assert joins["relations"][0]["source"] == "live_schema_cache"
    vault_names = {r.get("name") for r in joins["vault_relations"]}
    assert "Customers--SalesPersons" in vault_names
    # No live FK constraint for SalesPersonID — vault hint stays (playbook overrides apply elsewhere).
    sp_hint = next(r for r in joins["relations"] if r.get("name") == "Customers--SalesPersons")
    assert sp_hint["source"] == "vault"
    assert not sp_hint.get("superseded_by_live")


def test_get_joins_cfd_positions_live_fk_present():
    joins = vault.get_joins("CustomersFinancialDetails", client="morec")
    pairs = []
    for fk in joins["live_foreign_keys"]:
        if fk.get("referenced_table") == "Positions":
            pairs.extend(fk.get("column_pairs") or [])
    assert any(p.get("column") == "PositionsID" and p.get("ref_column") == "ID" for p in pairs)


def test_get_joins_source_precedence_documented():
    joins = vault.get_joins("OrdersHeaders", client="morec")
    assert "live_schema_cache" in joins["source_precedence"]


def test_get_joins_does_not_write_vault_files(tmp_path, monkeypatch):
    """Runtime get_joins must be read-only — never patch obsidian notes."""
    from core import config

    cache_path = tmp_path / "schema_cache.json"
    cache_path.write_text(json.dumps({
        "tables": {
            "dbo.DemoTable": [
                {"column": "CompanyID", "type": "smallint", "nullable": False},
                {"column": "ID", "type": "int", "nullable": False},
            ],
        },
        "foreign_keys": [],
    }))
    monkeypatch.setattr(config, "work_dir", lambda _client: tmp_path)

    vault_dir = tmp_path / "vault" / "Olives_BO" / "Tables"
    vault_dir.mkdir(parents=True)
    note = vault_dir / "DemoTable.md"
    note.write_text(
        "---\ntype: table\nname: DemoTable\n---\n# DemoTable\n\n## Columns\n| Column | Type |\n| OldCol | int |\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(vault, "VAULT", tmp_path / "vault")

    writes: list[str] = []
    original_write_text = Path.write_text

    def tracking_write_text(self, data, *args, **kwargs):
        writes.append(str(self))
        return original_write_text(self, data, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", tracking_write_text)

    joins = vault.get_joins("DemoTable", client="morec", database="Olives_BO")
    assert joins["table"] == "DemoTable"
    assert not writes, f"get_joins must not write vault files, wrote: {writes}"


def test_setup_sync_vault_table_from_cache_patches_columns(tmp_path, monkeypatch):
    from core import config

    cache_path = tmp_path / "schema_cache.json"
    cache_path.write_text(json.dumps({
        "tables": {
            "dbo.DemoTable": [
                {"column": "CompanyID", "type": "smallint", "nullable": False, "is_pk": True},
                {"column": "ID", "type": "int", "nullable": False, "is_pk": True},
            ],
        },
        "foreign_keys": [
            {
                "fk_name": "FK_DemoTable_Companies",
                "table_name": "dbo.DemoTable",
                "column_name": "CompanyID",
                "ref_table": "dbo.Companies",
                "ref_column": "ID",
            },
        ],
    }))
    monkeypatch.setattr(config, "work_dir", lambda _client: tmp_path)

    vault_dir = tmp_path / "vault" / "Olives_BO" / "Tables"
    vault_dir.mkdir(parents=True)
    note = vault_dir / "DemoTable.md"
    note.write_text(
        "---\ntype: table\ndatabase: Olives_BO\nname: DemoTable\nforeign_keys:\n  - [[OldRef]]\n---\n"
        "# DemoTable\n\n## Columns\n| Column | Type | Nullable | PK | FK | References |\n"
        "| CompanyID | int | NO | ✓ |  |  |\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(vault, "VAULT", tmp_path / "vault")
    monkeypatch.setattr(vault, "_table_note_path", lambda name, db="Olives_BO": note if name == "DemoTable" else None)

    first = vault.sync_vault_table_from_cache("DemoTable", "morec")
    assert first["status"] == "patched"
    patched = note.read_text(encoding="utf-8")
    assert "[[Companies]]" in patched
    assert "| ID | int |" in patched

    second = vault.sync_vault_table_from_cache("DemoTable", "morec")
    assert second.get("patched") is False


def test_setup_sync_vault_from_cache_script_finds_drift(tmp_path, monkeypatch):
    from core import config
    from setup import sync_vault_from_cache

    cache_path = tmp_path / "schema_cache.json"
    cache_path.write_text(json.dumps({
        "tables": {
            "dbo.DemoTable": [
                {"column": "CompanyID", "type": "smallint", "nullable": False, "is_pk": True},
                {"column": "ID", "type": "int", "nullable": False, "is_pk": True},
            ],
        },
        "foreign_keys": [],
    }))
    monkeypatch.setattr(config, "work_dir", lambda _client: tmp_path)

    vault_dir = tmp_path / "vault" / "Olives_BO" / "Tables"
    vault_dir.mkdir(parents=True)
    note = vault_dir / "DemoTable.md"
    note.write_text(
        "---\ntype: table\ndatabase: Olives_BO\nname: DemoTable\n---\n"
        "# DemoTable\n\n## Columns\n| Column | Type | Nullable | PK | FK | References |\n"
        "| CompanyID | int | NO | ✓ |  |  |\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(vault, "VAULT", tmp_path / "vault")
    monkeypatch.setattr(vault, "_table_note_path", lambda name, db="Olives_BO": note if name == "DemoTable" else None)

    drifted = sync_vault_from_cache._tables_with_drift("morec")
    assert "DemoTable" in drifted

    results = sync_vault_from_cache.sync_client("morec", table="DemoTable")
    assert any(r.get("status") == "patched" for r in results)
    assert "| ID | int |" in note.read_text(encoding="utf-8")


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
    assert "Customers--SalesPersons" in formatted


def test_retrieve_arabic_sales_alias():
    _ensure_cards()
    hits = vault.retrieve_cards("كم مبيعات الشهر", "morec", limit=3)
    names = {c["name"] for c in hits if c["kind"] == "table"}
    assert "TransactionsHeaders" in names


def test_module_map_match_and_tenant_pack_injection():
    _ensure_module_map("morec")
    assert module_map.match_domain("كم مبيعات هذا الشهر", "morec") == "sales"
    assert module_map.match_domain("رصيد السيارة للمندوب", "morec") == "van"
    with patch.object(tenant_pack, "_live_facts", return_value={}):
        pack = tenant_pack.build("morec", company_id=2, question="كم طلبات اليوم")
    assert "## Module:" in pack
    assert "OrdersHeaders" in pack


def test_module_map_cfd_domain():
    _ensure_module_map("morec")
    domain = module_map.match_domain("عملاء المندوب أسامة", "morec")
    assert domain == "cfd"
    card = module_map.format_card("cfd", "morec")
    assert "CustomersFinancialDetails" in card
    assert "PositionsID" in card or "Positions" in card


def test_compile_module_map_writes_all_domains():
    _ensure_module_map("morec")
    data = module_map.load("morec")
    for domain_id in ("sales", "orders", "receipts", "cfd", "van", "items", "routes", "system_options"):
        assert domain_id in data["domains"]
        assert data["domains"][domain_id]["tables"]
