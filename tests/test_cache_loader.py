import json
from pathlib import Path
import sqlite3
import time
from unittest.mock import MagicMock

import pytest

from core import cache_loader, config, hot_cache, memory


def test_load_schema_cache_mtime_invalidation(tmp_path, monkeypatch):
    client_dir = tmp_path / "morec"
    client_dir.mkdir(parents=True)
    schema_file = client_dir / "schema_cache.json"
    schema_file.write_text(json.dumps({"tables": {"t1": []}}), encoding="utf-8")
    monkeypatch.setattr(config, "work_dir", lambda c: client_dir)

    data1 = cache_loader.load_schema_cache("morec")
    assert data1 == {"tables": {"t1": []}}

    # Modify file
    time.sleep(0.01)
    schema_file.write_text(json.dumps({"tables": {"t1": [], "t2": []}}), encoding="utf-8")

    data2 = cache_loader.load_schema_cache("morec")
    assert data2 == {"tables": {"t1": [], "t2": []}}


def test_load_templates_mtime_invalidation(tmp_path, monkeypatch):
    tmpl_dir = tmp_path / "knowledge" / "report_templates"
    tmpl_dir.mkdir(parents=True)
    tmpl_file = tmpl_dir / "templates.json"
    monkeypatch.setattr(cache_loader, "app_root", lambda: tmp_path)

    assert cache_loader.load_templates() == []

    tmpl_file.write_text(json.dumps([{"name": "sales_summary"}]), encoding="utf-8")
    data1 = cache_loader.load_templates()
    assert len(data1) == 1
    assert data1[0]["name"] == "sales_summary"

    time.sleep(0.01)
    tmpl_file.write_text(json.dumps([{"name": "sales_summary"}, {"name": "tax_report"}]), encoding="utf-8")
    data2 = cache_loader.load_templates()
    assert len(data2) == 2


def test_load_prompt_mtime_invalidation(tmp_path, monkeypatch):
    prompt_dir = tmp_path / "prompts"
    prompt_dir.mkdir(parents=True)
    prompt_file = prompt_dir / "system.md"
    monkeypatch.setattr(cache_loader, "app_root", lambda: tmp_path)

    prompt_file.write_text("Hello Prompt v1", encoding="utf-8")
    assert cache_loader.load_prompt("system.md") == "Hello Prompt v1"

    time.sleep(0.01)
    prompt_file.write_text("Hello Prompt v2", encoding="utf-8")
    assert cache_loader.load_prompt("system.md") == "Hello Prompt v2"


def test_load_vault_cards_mtime_invalidation(tmp_path, monkeypatch):
    client_dir = tmp_path / "morec"
    client_dir.mkdir(parents=True)
    db_path = client_dir / "vault_cards.sqlite"
    monkeypatch.setattr(config, "work_dir", lambda c: client_dir)

    assert cache_loader.load_vault_cards("morec") == []

    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE cards (table_name TEXT PRIMARY KEY, card_json TEXT)")
    conn.execute("INSERT INTO cards VALUES ('Customers', '{\"table\": \"Customers\"}')")
    conn.commit()
    conn.close()

    cards1 = cache_loader.load_vault_cards("morec")
    assert len(cards1) == 1
    assert cards1[0]["table"] == "Customers"

    time.sleep(0.01)
    conn = sqlite3.connect(db_path)
    conn.execute("INSERT INTO cards VALUES ('Items', '{\"table\": \"Items\"}')")
    conn.commit()
    conn.close()

    cards2 = cache_loader.load_vault_cards("morec")
    assert len(cards2) == 2


def test_load_client_config_mtime_invalidation(tmp_path, monkeypatch):
    clients_dir = tmp_path / "clients"
    clients_dir.mkdir(parents=True)
    monkeypatch.setattr(config, "CLIENTS_DIR", clients_dir)

    with pytest.raises(FileNotFoundError):
        cache_loader.load_client_config("morec")

    client_file = clients_dir / "morec.yaml"
    client_file.write_text("db_name: Olives_BO\nlocale: ar\n", encoding="utf-8")

    cfg1 = cache_loader.load_client_config("morec")
    assert cfg1["db_name"] == "Olives_BO"

    time.sleep(0.01)
    client_file.write_text("db_name: Olives_BO_V2\nlocale: en\n", encoding="utf-8")

    cfg2 = cache_loader.load_client_config("morec")
    assert cfg2["db_name"] == "Olives_BO_V2"
    assert cfg2["locale"] == "en"


def test_ttl_cache_helper():
    called = 0

    def loader():
        nonlocal called
        called += 1
        return called

    val1 = cache_loader.ttl_cache("test_key", 0.05, loader)
    assert val1 == 1
    val2 = cache_loader.ttl_cache("test_key", 0.05, loader)
    assert val2 == 1
    assert called == 1

    time.sleep(0.06)
    val3 = cache_loader.ttl_cache("test_key", 0.05, loader)
    assert val3 == 2
    assert called == 2


def test_clear_all():
    cache_loader.ttl_cache("k", 100, lambda: 42)
    assert "k" in cache_loader._TTL_CACHE
    cache_loader.clear_all()
    assert len(cache_loader._TTL_CACHE) == 0


def test_hot_cache_permissions_alias_without_log_action_note(monkeypatch):
    monkeypatch.setattr(hot_cache.sql, "run_select", lambda sql_text, cid, client: [{"p": 1}])
    monkeypatch.setattr(hot_cache, "_schema_version", lambda client: "v1")

    # Permissions alias
    out_perm = hot_cache.lookup("Permissions", 1, "morec")
    assert out_perm["table"] == "SalesPersonsDevicePermissions"
    assert out_perm.get("requested") == "Permissions"
    assert "note" not in out_perm

    # DevicePermissions alias
    out_dev = hot_cache.lookup("DevicePermissions", 1, "morec")
    assert out_dev["table"] == "SalesPersonsDevicePermissions"
    assert out_dev.get("requested") == "DevicePermissions"
    assert "note" not in out_dev

    # LogActionTransaction alias MUST carry the note
    out_lat = hot_cache.lookup("LogActionTransaction", 1, "morec")
    assert out_lat["table"] == "LogActions"
    assert out_lat.get("requested") == "LogActionTransaction"
    assert "note" in out_lat
    assert "LogActionTransaction is a high-volume fact log" in out_lat["note"]


def test_memory_normalize_question_punctuation_and_alef_folding():
    q1 = "كم مبيعات يوليو؟"
    q2 = "كم مبيعات يوليو"
    assert memory.normalize_question(q1) == memory.normalize_question(q2)
    assert memory.normalize_question(q1) == "كم مبيعات يوليو"

    # Alef variants fold to ا
    assert memory.normalize_question("أحمد إبراهيم آمن") == "احمد ابراهيم امن"

    # Stripping punctuation: ؟ ? . ! ، ,
    assert memory.normalize_question("ماذا، حدث! هل تم؟ حقا, نعم.") == "ماذا حدث هل تم حقا نعم"

    # Same cache key
    k1 = memory.cache_key("morec", 1, "analyst", "m", q1)
    k2 = memory.cache_key("morec", 1, "analyst", "m", q2)
    assert k1 == k2


def test_memory_wal_and_schema_init_once(tmp_path, monkeypatch):
    db_file = tmp_path / "cache.sqlite"
    monkeypatch.setattr(memory, "DB_PATH", db_file)

    conn1 = memory._conn()
    mode = conn1.execute("PRAGMA journal_mode").fetchone()[0]
    assert mode.lower() == "wal"
    conn1.close()

    resolved_path_str = str(db_file.resolve())
    assert resolved_path_str in memory._INITIALIZED_PATHS

    # Second connection does not re-run DDL
    conn2 = memory._conn()
    conn2.close()


def test_memory_honors_chatbot_work_dir_when_default(tmp_path, monkeypatch):
    monkeypatch.setattr(memory, "DB_PATH", memory._DEFAULT_DB_PATH)
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path / "custom_work"))

    resolved = memory._resolve_db_path()
    assert resolved == tmp_path / "custom_work" / "cache.sqlite"

    # Respects monkeypatch when DB_PATH is not default
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "other.sqlite")
    assert memory._resolve_db_path() == tmp_path / "other.sqlite"
