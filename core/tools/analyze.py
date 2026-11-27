"""Exact arithmetic/trend computation tool.

Offloads deterministic calculations so the model doesn't compute them
in prose. Never accesses the database or state, so it never counts
against query budgets.
"""

from __future__ import annotations

from typing import Any


def analyze(args: dict[str, Any]) -> dict[str, Any]:
    """Exact arithmetic/trend computation the model can offload instead of
    computing (and potentially getting slightly wrong) in prose -- no DB access,
    doesn't touch state, so it never counts against MAX_QUERIES. Trend ops are
    DETERMINISTIC helpers; any number they emit is labeled an estimate by the
    analyst pack, never a promise."""
    op = args.get("operation")
    if op == "trend_direction":
        series = args.get("series")
        if not isinstance(series, list) or len(series) < 2:
            return {"error": "series must be a list of >=2 numbers (oldest to newest)"}
        try:
            values = [float(v) for v in series]
        except (TypeError, ValueError):
            return {"error": "series must contain only numbers"}
        n = len(values)
        # Least-squares slope on bucket index -> % of mean per step.
        mean = sum(values) / n
        if mean == 0:
            return {
                "direction": "flat",
                "slope_pct_per_step": 0.0,
                "note": "mean is 0 -- no trend computable",
            }
        denom = sum((i - (n - 1) / 2) ** 2 for i in range(n))
        slope = sum((i - (n - 1) / 2) * (v - mean) for i, v in enumerate(values)) / denom
        slope_pct = slope / mean * 100
        window = min(3, n)
        moving_avg = sum(values[-window:]) / window
        projected = max(0.0, moving_avg * (1 + slope_pct / 100))
        direction = "up" if slope_pct > 1 else ("down" if slope_pct < -1 else "flat")
        return {
            "direction": direction,
            "slope_pct_per_step": round(slope_pct, 2),
            "last_value": values[-1],
            "moving_average_last3": round(moving_avg, 4),
            "projected_next_bucket_estimate": round(projected, 4),
            "basis_buckets": n,
            "estimate_label": "ESTIMATE -- not a guarantee",
        }

    if op == "growth_compare":
        try:
            before, after = float(args["before"]), float(args["after"])
        except (KeyError, TypeError, ValueError):
            return {"error": "before/after must both be numbers"}
        if before == 0:
            return {"error": "before is 0 -- growth is undefined"}
        pct = (after - before) / before * 100
        return {"delta": after - before, "growth_pct": round(pct, 2)}

    if op == "top_movers":
        current, previous = args.get("current"), args.get("previous")
        if not isinstance(current, dict) or not isinstance(previous, dict):
            return {"error": "current/previous must be {label: number} dicts"}
        movers = []
        for label, val in current.items():
            try:
                v = float(val)
                p = float(previous.get(label, 0))
            except (TypeError, ValueError):
                continue
            delta = v - p
            pct = (delta / p * 100) if p else None
            movers.append({
                "label": label,
                "value": v,
                "previous": p,
                "delta": round(delta, 4),
                "pct_change": round(pct, 2) if pct is not None else "new",
            })
        movers.sort(key=lambda m: -abs(m["delta"]))
        return {"movers": movers[:10]}

    try:
        before, after = float(args["before"]), float(args["after"])
    except (KeyError, TypeError, ValueError):
        return {"error": "before/after must both be numbers"}

    if op == "difference":
        return {"result": after - before}
    if op == "ratio":
        if not before:
            return {"error": "before is 0 -- ratio is undefined"}
        return {"result": after / before}
    if op == "percent_change":
        if not before:
            return {"error": "before is 0 -- percent change is undefined"}
        return {"result": (after - before) / before * 100}

    return {
        "error": (
            f"unknown operation {op!r} -- use percent_change, difference, ratio, "
            f"trend_direction, growth_compare, or top_movers"
        )
    }


_analyze = analyze
