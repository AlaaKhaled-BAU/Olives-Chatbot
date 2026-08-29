"""run_proc must pass through gate allow-list."""
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import gate, sql


def test_run_proc_rejects_disallowed():
    with pytest.raises(gate.GateError):
        sql.run_proc("Rpt_Foo", {}, 2, "105", allowed_procs=())


def test_run_proc_allowed_passes_gate():
    with patch.object(sql, "get_conn") as mock_conn, \
         patch.object(sql, "set_tenant"), \
         patch.object(sql, "_schema_cache", return_value={}):
        cur = MagicMock()
        cur.fetchall.return_value = []
        mock_conn.return_value.__enter__ = MagicMock(return_value=mock_conn.return_value)
        mock_conn.return_value.cursor.return_value = cur
        sql.run_proc("Rpt_Allowed", {}, 2, "105", allowed_procs=["Rpt_Allowed"])
    cur.execute.assert_called_once()
