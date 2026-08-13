"""Phase 5 acceptance: param resolution order + multi-value guard, cache-key
tenant isolation, and a verified query feeding a few-shot."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import memory, params


def test_conversation_value_wins_first():
    profile = {"CompanyID": 1}
    assert params.resolve("CompanyID", {"CompanyID": 99}, profile) == 99


def test_profile_used_when_no_conversation_value():
    profile = {"CompanyID": 1}
    assert params.resolve("CompanyID", {}, profile) == 1


def test_multi_valued_param_asks_never_guesses():
    profile = {"CompanyID": params.MULTI}
    assert params.resolve("CompanyID", {}, profile) == params.NEEDS_ASK


def test_missing_param_asks():
    assert params.resolve("SomeParam", {}, {}) == params.NEEDS_ASK


def test_discover_profile_from_live_schema_cache():
    profile = params.discover_profile("morec")
    # morec is single-company (Phase 1 finding: Companies.ID=1) -- a real
    # int, never MULTI, since the distinct-count probe proved it singular.
    assert profile["CompanyID"] == 1
    assert profile["ClientActive"] == 122


def test_cache_key_isolation_same_question_different_client():
    key_a = memory.cache_key("morec", 1, "manager", "chatbot", "how many customers?")
    key_b = memory.cache_key("otherclient", 1, "manager", "chatbot", "how many customers?")
    assert key_a != key_b


def test_cache_key_isolation_same_client_different_company():
    key_1 = memory.cache_key("morec", 1, "manager", "chatbot", "how many customers?")
    key_2 = memory.cache_key("morec", 2, "manager", "chatbot", "how many customers?")
    assert key_1 != key_2


def test_verified_query_feeds_few_shot(tmp_path, monkeypatch):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "test_cache.sqlite")
    memory.promote_verified_query("morec", "How many customers?", "SELECT COUNT(*) FROM t.Customers", source="user_feedback")
    shots = memory.few_shots("morec")
    assert len(shots) == 1
    assert shots[0]["proc_or_sql"] == "SELECT COUNT(*) FROM t.Customers"


def test_unpromoted_source_never_feeds_few_shot(tmp_path, monkeypatch):
    """C3: the exact regression this fix closes -- an entry with no real
    correctness signal behind it (source not in the trusted set, e.g. a
    legacy row from before this fix) must never be fed to the model as a
    verified exemplar, no matter how high its ok_count."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "test_cache2.sqlite")
    conn = memory._conn()
    conn.execute(
        "INSERT INTO verified_queries (client, question_norm, proc_or_sql, ok_count, source) "
        "VALUES ('morec', 'a wrong query asked many times', 'SELECT 1', 50, 'unknown')"
    )
    conn.commit()
    conn.close()
    assert memory.few_shots("morec") == []
