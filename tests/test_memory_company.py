"""company_id isolation for few-shots and negatives."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import memory


def test_few_shots_never_cross_company(tmp_path, monkeypatch):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "iso.sqlite")
    memory.promote_verified_query("morec", 1, "sales total", "SELECT 1", source="eval")
    memory.promote_verified_query("morec", 2, "sales total", "SELECT 2", source="eval")
    shots_a = memory.few_shots("morec", 1, "sales")
    shots_b = memory.few_shots("morec", 2, "sales")
    assert shots_a[0]["proc_or_sql"] == "SELECT 1"
    assert shots_b[0]["proc_or_sql"] == "SELECT 2"
