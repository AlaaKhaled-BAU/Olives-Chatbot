"""Unit tests for setup/audit_rpt_readonly.py — offline definition checks."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from setup.audit_rpt_readonly import audit_procedure


def test_audit_rejects_insert_keyword():
    reasons = audit_procedure("CREATE PROC dbo.Rpt_X AS INSERT INTO t VALUES (1)", "dbo.Rpt_X", set())
    assert any(r.startswith("keyword:INSERT") for r in reasons)


def test_audit_rejects_xp():
    reasons = audit_procedure("CREATE PROC dbo.Rpt_X AS EXEC xp_cmdshell 'dir'", "dbo.Rpt_X", set())
    assert "xp_or_sp_oa" in reasons


def test_audit_rejects_exec_of_unsigned_callee():
    reasons = audit_procedure(
        "CREATE PROC dbo.Rpt_X AS EXEC dbo.SomeHelper @x=1",
        "dbo.Rpt_X",
        set(),
    )
    assert "exec_callee:SomeHelper" in reasons


def test_audit_allows_select_only_body():
    reasons = audit_procedure(
        "CREATE PROC dbo.Rpt_X AS SELECT * FROM Customers WHERE CompanyID = @CompanyID",
        "dbo.Rpt_X",
        set(),
    )
    assert "keyword:CREATE" in reasons  # CREATE in definition is still flagged
    assert "exec_callee" not in " ".join(reasons)
