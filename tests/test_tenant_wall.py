"""Phase 2 acceptance: the server-side tenant wall isolates and fails closed.
Requires chatbot_db up with the wall applied (setup/01_db_up.py, setup/03_apply_db_sql.py).
Assumes the morec pilot fixture: CompanyID 1 exists with Customers rows; a non-existent
CompanyID (99) must see zero rows. CompanyID 2 may exist on morec (105 snapshot drift)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import sql


def test_correct_tenant_sees_its_rows():
    conn = sql.get_conn("morec")
    sql.set_tenant(conn, 1)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM t.Customers")
    count = cur.fetchone()[0]
    conn.close()
    assert count > 0, "company 1 (morec) should see its own Customers rows"


def test_wrong_tenant_sees_zero_rows():
    conn = sql.get_conn("morec")
    sql.set_tenant(conn, 99)  # non-existent CompanyID — must not see company 1's rows
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM t.Customers")
    count = cur.fetchone()[0]
    conn.close()
    assert count == 0, "a non-existent CompanyID must never see another tenant's rows"


def test_no_session_context_fails_closed():
    conn = sql.get_conn("morec")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM t.Customers")
    count = cur.fetchone()[0]
    conn.close()
    assert count == 0, "no SESSION_CONTEXT set must return zero rows, not everything"


def test_write_denied():
    conn = sql.get_conn("morec")
    sql.set_tenant(conn, 1)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO t.Customers DEFAULT VALUES")
        raise AssertionError("chatbot_ro must not be able to write")
    except AssertionError:
        raise
    except Exception as e:
        assert "permission" in str(e).lower() or "denied" in str(e).lower()
    finally:
        conn.close()


def test_base_table_denied():
    conn = sql.get_conn("morec")
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) FROM dbo.Customers")
        raise AssertionError("chatbot_ro must not have base-table access, only t. views")
    except AssertionError:
        raise
    except Exception as e:
        assert "permission" in str(e).lower() or "denied" in str(e).lower()
    finally:
        conn.close()


def test_cross_client_directory_tables_have_no_view():
    """C0: Clients/Users must never get a t. view -- Clients lists every
    OTHER client (cross-tenant leak), Users has UserPWD (credentials).
    This is a stronger guarantee than "wrong tenant sees zero rows": there
    is no view to query at all, not even one that would fail closed."""
    conn = sql.get_conn("morec")
    sql.set_tenant(conn, 1)
    cur = conn.cursor()
    for table in ("Clients", "Users"):
        try:
            cur.execute(f"SELECT COUNT(*) FROM t.{table}")
            raise AssertionError(f"t.{table} must not exist as a view at all")
        except AssertionError:
            raise
        except Exception as e:
            assert "invalid object name" in str(e).lower(), f"unexpected error for t.{table}: {e}"
    conn.close()


def test_reference_table_ignores_tenant_scoping():
    """C0: Currencies has no tenant-varying data -- its t. view must return
    the identical row count regardless of which CompanyID (or none at all)
    is in SESSION_CONTEXT. This is the opposite property from every other
    test in this file, and that's the point: it's genuinely global data,
    not a wall bypass."""
    conn_a = sql.get_conn("morec")
    sql.set_tenant(conn_a, 1)
    cur_a = conn_a.cursor()
    cur_a.execute("SELECT COUNT(*) FROM t.Currencies")
    count_tenant_1 = cur_a.fetchone()[0]
    conn_a.close()

    conn_b = sql.get_conn("morec")  # no set_tenant call at all
    cur_b = conn_b.cursor()
    cur_b.execute("SELECT COUNT(*) FROM t.Currencies")
    count_no_tenant = cur_b.fetchone()[0]
    conn_b.close()

    assert count_tenant_1 > 0, "Currencies should have real rows"
    assert count_tenant_1 == count_no_tenant, "reference data must not vary by tenant at all"


def test_company_col_table_isolates_by_tenant():
    """C0: a table scoped via the older CompNo column (not literal
    CompanyID) must isolate exactly like the CompanyID-column tables
    already do -- same fail-closed guarantee, different underlying
    column name. LogActionTransaction is real, large (millions of rows on
    morec), not a toy fixture."""
    conn_right = sql.get_conn("morec")
    sql.set_tenant(conn_right, 1)
    cur_right = conn_right.cursor()
    cur_right.execute("SELECT COUNT(*) FROM t.LogActionTransaction")
    count_right = cur_right.fetchone()[0]
    conn_right.close()

    conn_wrong = sql.get_conn("morec")
    sql.set_tenant(conn_wrong, 999)
    cur_wrong = conn_wrong.cursor()
    cur_wrong.execute("SELECT COUNT(*) FROM t.LogActionTransaction")
    count_wrong = cur_wrong.fetchone()[0]
    conn_wrong.close()

    assert count_right > 0, "expected real rows for the correct tenant"
    assert count_wrong == 0, "a different tenant must see zero rows via the CompNo-scoped view too"
