"""C3: core/memory.py's writer-gating and schema-version invalidation.
Isolated sqlite file per test (monkeypatched DB_PATH), never the real
work/cache.sqlite."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import memory


def test_cache_key_changes_with_schema_version():
    """A stale cached plan from before a schema change must never match a
    query issued after it -- different schema_version, different key,
    guaranteed miss rather than a wrong hit."""
    k1 = memory.cache_key("morec", 1, "manager", "chatbot", "how many customers?", schema_version="abc123")
    k2 = memory.cache_key("morec", 1, "manager", "chatbot", "how many customers?", schema_version="def456")
    assert k1 != k2


def test_cache_key_default_schema_version_is_stable():
    """Callers with no schema_version yet (schema_version="") must still
    get a deterministic key -- worst case is an unnecessary miss, never an
    inconsistent one."""
    k1 = memory.cache_key("morec", 1, "manager", "chatbot", "how many customers?")
    k2 = memory.cache_key("morec", 1, "manager", "chatbot", "how many customers?")
    assert k1 == k2


def test_promote_verified_query_requires_a_source(tmp_path, monkeypatch):
    """source is a required positional/keyword arg, not defaulted -- a
    future accidental agent-side call without stating why this is trusted
    must fail loudly, not silently reintroduce the bug this fix closes."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    try:
        memory.promote_verified_query("morec", 1, "q", "SELECT 1")
        assert False, "expected a missing-argument TypeError"
    except TypeError:
        pass


def test_set_plan_then_delete_plan(tmp_path, monkeypatch):
    """Thumbs-down: remove exactly the one cache entry, not the client's
    whole cache."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    key = memory.cache_key("morec", 1, "manager", "chatbot", "q1")
    other_key = memory.cache_key("morec", 1, "manager", "chatbot", "q2")
    memory.set_plan(key, "morec", {"sql": "SELECT 1"})
    memory.set_plan(other_key, "morec", {"sql": "SELECT 2"})
    memory.delete_plan(key)
    assert memory.get_plan(key) is None
    assert memory.get_plan(other_key) == {"sql": "SELECT 2"}


def test_clear_plan_cache_only_touches_that_client(tmp_path, monkeypatch):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    key_morec = memory.cache_key("morec", 1, "manager", "chatbot", "q")
    key_rukn = memory.cache_key("rukn", 1, "manager", "chatbot", "q")
    memory.set_plan(key_morec, "morec", {"sql": "SELECT 1"})
    memory.set_plan(key_rukn, "rukn", {"sql": "SELECT 2"})
    removed = memory.clear_plan_cache("morec")
    assert removed == 1
    assert memory.get_plan(key_morec) is None
    assert memory.get_plan(key_rukn) == {"sql": "SELECT 2"}


def test_migration_adds_columns_to_a_pre_c3_database(tmp_path, monkeypatch):
    """The real work/cache.sqlite predates C3 (client-less plan_cache,
    source-less verified_queries) -- _conn()'s additive migration must
    bring an old file up to the new shape without losing existing rows."""
    import sqlite3
    db_path = tmp_path / "legacy.sqlite"
    conn = sqlite3.connect(db_path)
    conn.executescript("""
        CREATE TABLE verified_queries (
            client TEXT NOT NULL, question_norm TEXT NOT NULL,
            proc_or_sql TEXT NOT NULL, ok_count INTEGER NOT NULL DEFAULT 1,
            PRIMARY KEY (client, question_norm)
        );
        CREATE TABLE plan_cache (key TEXT PRIMARY KEY, plan TEXT NOT NULL, ts REAL NOT NULL);
    """)
    conn.execute("INSERT INTO verified_queries VALUES ('morec', 'old q', 'SELECT 1', 7)")
    conn.commit()
    conn.close()

    monkeypatch.setattr(memory, "DB_PATH", db_path)
    row = memory.get_verified_query("morec", 0, "old q")
    assert row == {"proc_or_sql": "SELECT 1", "ok_count": 7}, "existing row must survive the migration"
    assert memory.few_shots("morec", 0) == []
