"""Tests for core.tools (schemas and analyze tool)."""

from __future__ import annotations

import pytest

from core.tools import TOOLS, analyze, _analyze


# ---------------------------------------------------------------------------
# Test analyze() function
# ---------------------------------------------------------------------------

def test_analyze_percent_change_success():
    res = analyze({"operation": "percent_change", "before": 100, "after": 125})
    assert res == {"result": 25.0}

    res_neg = analyze({"operation": "percent_change", "before": 200, "after": 100})
    assert res_neg == {"result": -50.0}


def test_analyze_percent_change_zero_before():
    res = analyze({"operation": "percent_change", "before": 0, "after": 50})
    assert "error" in res
    assert "percent change is undefined" in res["error"]


def test_analyze_difference_success():
    res = analyze({"operation": "difference", "before": 45.5, "after": 100})
    assert res == {"result": 54.5}

    res_neg = analyze({"operation": "difference", "before": 100, "after": 40})
    assert res_neg == {"result": -60.0}


def test_analyze_ratio_success():
    res = analyze({"operation": "ratio", "before": 25, "after": 75})
    assert res == {"result": 3.0}


def test_analyze_ratio_zero_before():
    res = analyze({"operation": "ratio", "before": 0, "after": 100})
    assert "error" in res
    assert "ratio is undefined" in res["error"]


def test_analyze_missing_before_after_arithmetic():
    for op in ["percent_change", "difference", "ratio"]:
        res_missing = analyze({"operation": op, "before": 10})
        assert "error" in res_missing
        assert "before/after must both be numbers" in res_missing["error"]

        res_invalid = analyze({"operation": op, "before": "not_a_num", "after": 10})
        assert "error" in res_invalid
        assert "before/after must both be numbers" in res_invalid["error"]


def test_analyze_growth_compare_success():
    res = analyze({"operation": "growth_compare", "before": 200, "after": 250})
    assert res == {"delta": 50.0, "growth_pct": 25.0}


def test_analyze_growth_compare_zero_before():
    res = analyze({"operation": "growth_compare", "before": 0, "after": 100})
    assert "error" in res
    assert "growth is undefined" in res["error"]


def test_analyze_growth_compare_invalid_inputs():
    res = analyze({"operation": "growth_compare", "before": "abc", "after": 10})
    assert "error" in res
    assert "before/after must both be numbers" in res["error"]


def test_analyze_trend_direction_up():
    series = [10.0, 20.0, 30.0, 40.0]
    res = analyze({"operation": "trend_direction", "series": series})
    assert res["direction"] == "up"
    assert res["slope_pct_per_step"] > 0
    assert res["basis_buckets"] == 4
    assert res["last_value"] == 40.0
    assert "ESTIMATE" in res["estimate_label"]
    assert res["projected_next_bucket_estimate"] > 40.0


def test_analyze_trend_direction_down():
    series = [100.0, 80.0, 60.0, 40.0]
    res = analyze({"operation": "trend_direction", "series": series})
    assert res["direction"] == "down"
    assert res["slope_pct_per_step"] < 0
    assert res["basis_buckets"] == 4
    assert res["last_value"] == 40.0


def test_analyze_trend_direction_flat():
    series = [50.0, 50.0, 50.0, 50.0]
    res = analyze({"operation": "trend_direction", "series": series})
    assert res["direction"] == "flat"
    assert res["slope_pct_per_step"] == 0.0


def test_analyze_trend_direction_zero_mean():
    series = [0.0, 0.0, 0.0]
    res = analyze({"operation": "trend_direction", "series": series})
    assert res["direction"] == "flat"
    assert res["slope_pct_per_step"] == 0.0
    assert "mean is 0" in res["note"]


def test_analyze_trend_direction_invalid_series():
    res_short = analyze({"operation": "trend_direction", "series": [10.0]})
    assert "error" in res_short
    assert ">=2 numbers" in res_short["error"]

    res_not_list = analyze({"operation": "trend_direction", "series": "invalid"})
    assert "error" in res_not_list
    assert ">=2 numbers" in res_not_list["error"]

    res_non_numeric = analyze({"operation": "trend_direction", "series": [10.0, "abc"]})
    assert "error" in res_non_numeric
    assert "contain only numbers" in res_non_numeric["error"]


def test_analyze_top_movers_success():
    current = {"ItemA": 100, "ItemB": 20, "ItemC": 50, "ItemD": 10}
    previous = {"ItemA": 80, "ItemB": 50, "ItemC": 50}  # ItemB delta = -30, ItemA delta = +20, ItemD is new
    res = analyze({"operation": "top_movers", "current": current, "previous": previous})
    assert "movers" in res
    movers = res["movers"]
    # Sorted by abs(delta) desc: ItemB (| -30 | = 30), ItemA (| 20 | = 20), ItemD (| 10 | = 10), ItemC (| 0 | = 0)
    assert movers[0]["label"] == "ItemB"
    assert movers[0]["delta"] == -30.0
    assert movers[0]["pct_change"] == -60.0

    assert movers[1]["label"] == "ItemA"
    assert movers[1]["delta"] == 20.0
    assert movers[1]["pct_change"] == 25.0

    assert movers[2]["label"] == "ItemD"
    assert movers[2]["delta"] == 10.0
    assert movers[2]["pct_change"] == "new"


def test_analyze_top_movers_invalid_inputs():
    res = analyze({"operation": "top_movers", "current": "not_a_dict", "previous": {}})
    assert "error" in res
    assert "dict" in res["error"]


def test_analyze_unknown_operation():
    res = analyze({"operation": "unsupported_op", "before": 1, "after": 2})
    assert "error" in res
    assert "unknown operation 'unsupported_op'" in res["error"]


def test_analyze_alias():
    assert _analyze is analyze


# ---------------------------------------------------------------------------
# Test TOOLS schemas
# ---------------------------------------------------------------------------

def test_tools_count_and_names():
    names = [t["function"]["name"] for t in TOOLS]
    assert len(TOOLS) >= 11
    expected_names = {
        "introspect_schema",
        "run_select",
        "ask_user",
        "analyze",
        "search_docs",
        "search_schema_notes",
        "read_schema_note",
        "get_joins",
        "run_metric",
        "run_report",
        "lookup_hot",
        "recall_turns",
    }
    assert set(names) == expected_names
    # run_proc must not be in tools
    assert "run_proc" not in names


def test_analyze_schema_required_only_operation():
    analyze_tool = next(t for t in TOOLS if t["function"]["name"] == "analyze")
    params = analyze_tool["function"]["parameters"]
    assert params["required"] == ["operation"]
    assert "before" not in params["required"]
    assert "after" not in params["required"]


def test_search_docs_description_bilingual():
    docs_tool = next(t for t in TOOLS if t["function"]["name"] == "search_docs")
    desc = docs_tool["function"]["description"]
    # Verify English + Arabic bilingual search instruction
    assert "English" in desc
    assert "Arabic" in desc
    assert "نوع زبون" in desc
    assert "customer type" in desc


def test_run_metric_sales_primary_net_sales_legacy():
    metric_tool = next(t for t in TOOLS if t["function"]["name"] == "run_metric")
    metric_prop = metric_tool["function"]["parameters"]["properties"]["metric"]
    desc = metric_prop["description"]
    assert "sales" in desc
    assert "primary" in desc
    assert "net_sales" in desc
    assert "legacy" in desc
