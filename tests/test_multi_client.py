"""Phase 9 acceptance: two real, independently-restored client databases
(morec = chatbot_db, rukn = chatbot_db2) never cross, and their catalogs
differ. The full agent-level proof (asking each client a real question and
getting back its own, correctly-scoped answer) is exercised live -- see the
Phase 9 commit message -- not duplicated here as an automated test (each
run would cost a live LLM call per client)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import catalog, config, sql

CLIENTS = {
    "morec": {"company_id": 1, "name_fragment": "مورك"},
    "rukn": {"company_id": 290, "name_fragment": "الالماس"},
}


def test_clients_resolve_to_different_databases():
    assert config.load_client("morec")["db_name"] != config.load_client("rukn")["db_name"]


def test_each_client_sees_only_its_own_company():
    for client, expected in CLIENTS.items():
        conn = sql.get_conn(client)
        sql.set_tenant(conn, expected["company_id"])
        cur = conn.cursor(as_dict=True)
        cur.execute("SELECT ID, Name FROM t.Companies")
        rows = cur.fetchall()
        conn.close()
        assert len(rows) == 1
        assert rows[0]["ID"] == expected["company_id"]
        assert expected["name_fragment"] in rows[0]["Name"]


def test_a_client_never_sees_the_others_companyid():
    """Querying client A's own database with client B's CompanyID must
    return zero rows -- proves isolation isn't just "different database",
    it's also that a wrong/foreign CompanyID can't accidentally match
    something in the wrong DB."""
    for client, other in [("morec", CLIENTS["rukn"]), ("rukn", CLIENTS["morec"])]:
        conn = sql.get_conn(client)
        sql.set_tenant(conn, other["company_id"])
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM t.Companies")
        count = cur.fetchone()[0]
        conn.close()
        assert count == 0, f"{client}'s DB leaked a row for the other client's CompanyID"


def test_catalogs_differ_per_client():
    morec_cfg = config.load_client("morec")
    rukn_cfg = config.load_client("rukn")
    morec_procs = set(catalog.for_client("morec", morec_cfg["name_aliases"]).keys())
    rukn_procs = set(catalog.for_client("rukn", rukn_cfg["name_aliases"]).keys())
    assert morec_procs != rukn_procs
