"""db/hot_tables.json — curated BO core tables."""
import json
from pathlib import Path

from core import hot_tables
from setup import compile_module_map

_REPO = Path(__file__).resolve().parent.parent


def test_hot_tables_json_loads():
    data = hot_tables.load()
    assert data["version"] == 1
    names = data["tables"]
    assert len(names) >= 35
    assert len(names) == len(set(names)), "duplicate table names in hot_tables.json"


def test_price_list_details_in_hot_set():
    names = hot_tables.table_names()
    assert "PriceListDetails" in names
    assert "PriceLists" in names
    assert "PriceListsDetails" not in names


def test_compile_module_map_cfd_includes_price_list_details():
    data = compile_module_map.compile_map()
    cfd_tables = set(data["domains"]["cfd"]["tables"])
    assert "PriceListDetails" in cfd_tables
    assert "PriceLists" in cfd_tables
    hints = " ".join(data["domains"]["cfd"]["hints"])
    assert "PriceListDetails" in hints
