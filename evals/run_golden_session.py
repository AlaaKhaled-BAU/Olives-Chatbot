#!/usr/bin/env python3.13
"""Golden one-session eval for client 105 / CompanyID 1. Reference values
come from live SQL through core.sql.run_select (same gate as the bot), so
expectations follow the data. Requires the API running on :8100.
For --baseline regression, compare against pass_final when present, else pass."""
import argparse
import json
import math
import re
from collections import Counter
import sys
import time
import urllib.request
import uuid
from datetime import date, datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import metrics, sql  # noqa: E402

CLIENT, COMPANY = "105", 1
TRACE = BASE_DIR / "work" / "trace.jsonl"
CASES_PATH = BASE_DIR / "evals" / "golden_session_105.jsonl"
OFFPEAK = {"hit": 0.003, "miss": 0.15, "out": 0.60}   # USD per 1M, deepseek-flash
PEAK = {"hit": 0.006, "miss": 0.30, "out": 1.20}
NET = metrics.line_amount_sql("td")
JOIN = ("FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td ON th.CompanyID = td.CompanyID "
        "AND th.TransactionTypeID = td.TransactionTypeID AND th.TransactionYear = td.TransactionYear "
        "AND th.TransactionNo = td.TransactionNo")
INVOICE_HEADER_KEY = (
    "CAST(th.TransactionYear AS varchar(4)) + '-' + CAST(th.TransactionNo AS varchar(20))"
)
_MONTH_EN = (
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)
_MONTH_AR: dict[int, tuple[str, ...]] = {
    1: ("يناير",), 2: ("فبراير",), 3: ("مارس",), 4: ("أبريل",), 5: ("مايو",),
    6: ("يونيو",), 7: ("يوليو", "تموز"), 8: ("أغسطس",), 9: ("سبتمبر",),
    10: ("أكتوبر", "تشرين الأول"), 11: ("نوفمبر", "تشرين الثاني"),
    12: ("ديسمبر", "كانون الأول"),
}

_ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_NUM_RE = re.compile(
    r"(?<![\d.,])\d{1,3}(?:,\d{3})+(?:\.\d+)?(?![\d.,])"
    r"|(?<![\d.,])\d+(?:\.\d+)?(?![\d.,])"
)


def _norm(text: str) -> str:
    t = (text or "").translate(_ARABIC_DIGITS)
    return t.replace("\u066c", ",").replace("\u066b", ".")


def num_tokens(text: str) -> set[str]:
    return {m.replace(",", "") for m in _NUM_RE.findall(_norm(text))}


def amount_matches(x: float, text: str) -> bool:
    target = f"{x:.2f}"
    for tok in num_tokens(text):
        if "." in tok and tok == target:
            return True
        try:
            if abs(float(tok) - x) < 0.006:
                return True
        except ValueError:
            continue
    return False


def number_variants(x: float) -> set[str]:
    return {f"{x:,.2f}", f"{x:.2f}", f"{round(x):,}", str(round(x))}


def cost_usd(call: dict, rates: dict) -> float:
    return ((call.get("cache_hit") or 0) * rates["hit"]
            + (call.get("cache_miss") or 0) * rates["miss"]
            + (call.get("completion") or 0) * rates["out"]) / 1e6


def baseline_passes(results: dict) -> dict[str, bool]:
    out: dict[str, bool] = {}
    for row in results.get("cases") or []:
        if "pass_final" in row:
            out[row["name"]] = bool(row["pass_final"])
        else:
            out[row["name"]] = bool(row["pass"])
    return out


def regressions(
    baseline_pass: dict[str, bool],
    run1: dict[str, bool],
    run2: dict[str, bool] | None,
) -> tuple[list[str], list[str]]:
    if run2 is None:
        return [], []
    regressed, flaky = [], []
    for name, base_ok in baseline_pass.items():
        if not base_ok:
            continue
        if not run1.get(name) and not run2.get(name):
            regressed.append(name)
        elif not run1.get(name) and run2.get(name):
            flaky.append(name)
    return regressed, flaky


def _q(text: str) -> list[dict]:
    return sql.run_select(text, company_id=COMPANY, client=CLIENT)


def _last_month() -> tuple[str, str]:
    mx = _q("SELECT MAX(TransactionDate) AS mx FROM t.TransactionsHeaders "
            "WHERE TransactionTypeID = 1 AND ISNULL(IsVoid, 0) = 0")[0]["mx"]
    first_cur = date(mx.year, mx.month, 1)
    prev = date(first_cur.year - (first_cur.month == 1), (first_cur.month - 2) % 12 + 1, 1)
    return prev.isoformat(), first_cur.isoformat()


def references() -> dict:
    f, t = _last_month()
    W = f"th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0 AND th.TransactionDate >= '{f}' AND th.TransactionDate < '{t}'"
    reps = _q(f"SELECT th.SalesPersonID AS id, sp.Name AS name, SUM({NET}) AS net {JOIN} "
              f"JOIN t.SalesPersons sp ON sp.ID = th.SalesPersonID AND sp.CompanyID = th.CompanyID "
              f"WHERE {W} GROUP BY th.SalesPersonID, sp.Name ORDER BY net DESC")
    items = _q(f"SELECT td.ItemCode AS code, SUM({NET}) AS net {JOIN} WHERE {W} GROUP BY td.ItemCode ORDER BY net DESC")
    summary = _q(f"SELECT SUM({NET}) AS net, COUNT(DISTINCT {INVOICE_HEADER_KEY}) AS inv, "
                 f"COUNT(DISTINCT th.CustomerID) AS custs {JOIN} WHERE {W}")[0]
    unsold = _q("SELECT COUNT(*) AS n FROM t.Items i WHERE ISNULL(i.IsSuspended, 0) = 0 AND NOT EXISTS ("
                f"SELECT 1 {JOIN} WHERE {W} AND td.ItemCode = i.ItemCode)")[0]["n"]
    top = reps[0]
    days = _q("SELECT TOP 2 CAST(TimeStamp AS date) AS d, COUNT(DISTINCT TRY_CAST(Data1 AS bigint)) AS visited "
              f"FROM t.LogActionTransaction WHERE ActionID = N'0' AND TRY_CAST(SalesmanID AS int) = {int(top['id'])} "
              "GROUP BY CAST(TimeStamp AS date) ORDER BY d DESC")
    visit_days = []
    for d in days:
        nxt = date.fromordinal(d["d"].toordinal() + 1).isoformat()
        s = _q("SELECT COUNT(*) AS inv, COUNT(DISTINCT CustomerID) AS sold FROM t.TransactionsHeaders "
               f"WHERE TransactionTypeID = 1 AND ISNULL(IsVoid, 0) = 0 AND SalesPersonID = {int(top['id'])} "
               f"AND TransactionDate >= '{d['d'].isoformat()}' AND TransactionDate < '{nxt}'")[0]
        visit_days.append({"visited": d["visited"], "sold": s["sold"], "inv": s["inv"]})
    return {"reps": reps, "items": items, "summary": summary, "visit_days": visit_days, "unsold": unsold}


def _line_token_counts(line: str) -> Counter:
    return Counter(m.replace(",", "") for m in _NUM_RE.findall(_norm(line)))


def _line_visit_match(line: str, d: dict) -> bool:
    need = Counter([str(d["visited"]), str(d["sold"]), str(d["inv"])])
    have = _line_token_counts(line)
    return all(have[t] >= need[t] for t in need)


def _visits_pass(answer: str, ref: dict) -> bool:
    a = _norm(answer)
    top_name = ref["reps"][0]["name"].strip()
    if top_name not in a:
        return False
    return any(
        _line_visit_match(line, d)
        for d in ref["visit_days"]
        for line in a.splitlines()
    )


def check(kind: str, answer: str, ref: dict) -> bool:
    if "```" in (answer or ""):
        return False
    a = _norm(answer)
    if kind == "top_rep":
        top = ref["reps"][0]
        return top["name"].strip() in a and amount_matches(float(top["net"]), answer)
    if kind == "top_item":
        top = ref["items"][0]
        return top["code"] in a and amount_matches(float(top["net"]), answer)
    if kind == "bottom10":
        bottom = [r["code"] for r in ref["items"][-10:]]
        unsold_tok = str(int(ref["unsold"]))
        return sum(code in a for code in bottom) >= 5 and unsold_tok in num_tokens(a)
    if kind == "visits":
        return _visits_pass(answer, ref)
    if kind == "summary":
        s = ref["summary"]
        toks = num_tokens(a)
        return (
            amount_matches(float(s["net"]), answer)
            and str(s["inv"]) in toks
            and str(s["custs"]) in toks
        )
    if kind == "howto":
        return any(k in a for k in ("MakeOrderTaking", "طلب بيع", "الموقف الوظيفي", "وظيف"))
    raise ValueError(kind)


def render_ref_sql(text: str, f: str, t: str) -> str:
    w = (f"th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0 "
         f"AND th.TransactionDate >= '{f}' AND th.TransactionDate < '{t}'")
    return text.format(f=f, t=t, JOIN=JOIN, NET=NET, W=w, INV_KEY=INVOICE_HEADER_KEY)


def _as_date(val) -> date:
    if isinstance(val, datetime):
        return val.date()
    if isinstance(val, date):
        return val
    return date.fromisoformat(str(val).strip()[:10])


def _day_forms(day: int) -> list[str]:
    return list(dict.fromkeys((str(day), f"{day:02d}")))


def _month_forms(month: int) -> list[str]:
    return list(dict.fromkeys((str(month), f"{month:02d}")))


def _date_token_pattern(literal: str) -> re.Pattern[str]:
    return re.compile(rf"(?<!\d){re.escape(literal)}(?!\d)")


def date_variants(val) -> list[str]:
    """Literal date strings matched by date_patterns (padded and unpadded)."""
    d = _as_date(val)
    day, month, year = d.day, d.month, d.year
    days, months = _day_forms(day), _month_forms(month)
    out = [d.isoformat()]
    for d_s in days:
        for m_s in months:
            for sep in ("/", "-"):
                out.append(f"{d_s}{sep}{m_s}{sep}{year}")
                out.append(f"{d_s}{sep}{m_s}")
            out.append(f"{year}/{m_s}/{d_s}")
    for d_s in days:
        out.append(f"{d_s} {_MONTH_EN[month]}")
        out.append(f"{_MONTH_EN[month][:3]} {d_s}")
        for ar in _MONTH_AR.get(month, ()):
            out.append(f"{d_s} {ar}")
    return out


def date_patterns(val) -> list[re.Pattern[str]]:
    return [_date_token_pattern(v) for v in date_variants(val)]


def date_matches(val, text: str) -> bool:
    a = _norm(text)
    return any(p.search(a) for p in date_patterns(val))


def _name_metric_cols(expect: list[str]) -> tuple[str | None, str | None, str | None]:
    name_col = amount_col = int_col = None
    for item in expect:
        kind, _, rest = item.partition(":")
        if kind == "name":
            name_col = rest
        elif kind == "amount":
            amount_col = rest
        elif kind == "int":
            int_col = rest
    if name_col and amount_col:
        return name_col, "amount", amount_col
    if name_col and int_col:
        return name_col, "int", int_col
    return None, None, None


def _same_line_name_metric(rows: list[dict], name_col: str, metric: str, metric_col: str,
                           answer: str) -> bool:
    if not rows:
        return False
    name = str(rows[0][name_col]).strip()
    lines = answer.splitlines() or [answer]
    for line in lines:
        if name not in _norm(line):
            continue
        if metric == "amount" and amount_matches(float(rows[0][metric_col]), line):
            return True
        if metric == "int" and str(int(rows[0][metric_col])) in num_tokens(line):
            return True
    return False


def expect_holds(expect: list[str], rows: list[dict], answer: str) -> bool:
    if "```" in (answer or ""):
        return False
    a = _norm(answer)
    toks = num_tokens(answer)
    name_col, metric, metric_col = _name_metric_cols(expect)
    paired = name_col is not None and metric is not None
    if paired and not _same_line_name_metric(rows, name_col, metric, metric_col, answer):
        return False
    for item in expect:
        kind, _, rest = item.partition(":")
        if paired and kind in ("name", "amount", "int"):
            continue
        if kind == "name":
            if not rows or str(rows[0][rest]).strip() not in a:
                return False
        elif kind == "amount":
            if not rows or not amount_matches(float(rows[0][rest]), answer):
                return False
        elif kind == "int":
            if not rows or str(int(rows[0][rest])) not in toks:
                return False
        elif kind == "date":
            if not rows or not date_matches(rows[0][rest], answer):
                return False
        elif kind == "rows":
            n_s, _, col = rest.partition(":")
            n, need = int(n_s), math.ceil(int(n_s) / 2)
            hit = sum(1 for i in range(min(n, len(rows))) if str(rows[i][col]).strip() in a)
            if hit < need:
                return False
        else:
            raise ValueError(item)
    return True


def load_cases(path: Path | None = None) -> list[dict]:
    p = path or CASES_PATH
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def ask(question: str, session_id: str) -> dict:
    body = json.dumps({"question": question, "session_id": session_id, "company_id": COMPANY}).encode()
    req = urllib.request.Request("http://127.0.0.1:8100/ask", data=body,
                                 headers={"Content-Type": "application/json"})
    final = {}
    with urllib.request.urlopen(req, timeout=600) as resp:
        for raw in resp.read().decode("utf-8").split("\n\n"):
            if raw.startswith("data: ") and raw[6:] != "[DONE]":
                ev = json.loads(raw[6:])
                if "answer" in ev or "error" in ev or "needs_ask" in ev:
                    final = ev
    return final


def trace_for(question: str, since: float) -> dict:
    for line in reversed(TRACE.read_text(encoding="utf-8").splitlines()):
        rec = json.loads(line)
        if rec.get("ts", 0) >= since and rec.get("question") == question:
            return rec
    return {}


def _summary(rows: list[dict]) -> dict:
    n = len(rows)
    final_key = lambda r: r.get("pass_final", r["pass"])
    return {
        "accuracy": sum(r["pass"] for r in rows) / n,
        "accuracy_final": sum(final_key(r) for r in rows) / n,
        "usd_per_q_offpeak": round(sum(r["usd_offpeak"] for r in rows) / n, 5),
        "usd_per_q_peak": round(sum(r["usd_peak"] for r in rows) / n, 5),
        "p50_latency_ms": sorted(r["latency_ms"] or 0 for r in rows)[n // 2],
        "calls_per_q": round(sum(r["llm_calls"] for r in rows) / n, 2),
    }


def _print_rows(rows: list[dict]) -> None:
    for r in rows:
        print(f"{r['name']:<28} pass={r['pass']} {r['latency_ms']}ms "
              f"calls={r['llm_calls']} ${r['usd_offpeak']}", flush=True)


def _pass_case(c: dict, answer: str, ref: dict) -> bool:
    if c.get("ref_sql"):
        f, t = _last_month()
        ref_rows = _q(render_ref_sql(c["ref_sql"], f, t))
        return expect_holds(c["expect"], ref_rows, answer)
    return check(c["check"], answer, ref)


def run_session(cases: list[dict], ref: dict, session_id: str | None = None) -> list[dict]:
    sid = session_id or f"golden-{uuid.uuid4().hex[:8]}"
    rows = []
    for c in cases:
        use_sid = f"heldout-{c['name']}-{uuid.uuid4().hex[:8]}" if c.get("ref_sql") else sid
        t0 = time.time()
        res = ask(c["question"], use_sid)
        tr = trace_for(c["question"], t0 - 1)
        calls = tr.get("calls") or []
        rows.append({
            "name": c["name"],
            "pass": _pass_case(c, res.get("answer") or "", ref),
            "latency_ms": tr.get("latency_ms"),
            "ttft_ms": tr.get("ttft_ms"),
            "llm_calls": len(calls),
            "tool_errors": tr.get("tool_errors"),
            "usd_offpeak": round(sum(cost_usd(x, OFFPEAK) for x in calls), 5),
            "usd_peak": round(sum(cost_usd(x, PEAK) for x in calls), 5),
            "answer": res.get("answer"),
        })
    return rows


def rescore_results(src: Path, cases_path: Path | None = None) -> int:
    cases_path = cases_path or CASES_PATH
    data = json.loads(src.read_text(encoding="utf-8"))
    ref = references()
    by_name = {c["name"]: c for c in load_cases(cases_path)}
    rows = []
    for old in data["cases"]:
        c = by_name[old["name"]]
        row = dict(old)
        row["pass"] = _pass_case(c, old.get("answer") or "", ref)
        rows.append(row)
    summary = _summary(rows)
    _print_rows(rows)
    print(json.dumps(summary, indent=1))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = BASE_DIR / "evals" / f"{cases_path.stem}_results_{stamp}_rescored.json"
    payload = {
        "rescored_from": str(src),
        "summary": summary,
        "cases": rows,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default=str(CASES_PATH.relative_to(BASE_DIR)),
                    help="jsonl case file (default: evals/golden_session_105.jsonl)")
    ap.add_argument("--baseline", help="previous results json; fail if any baseline pass now fails")
    ap.add_argument("--rescore", metavar="RESULTS_JSON",
                    help="re-score stored answers with live references (no API)")
    args = ap.parse_args()

    cases_path = Path(args.cases)
    if not cases_path.is_absolute():
        cases_path = BASE_DIR / cases_path

    if args.rescore:
        rescore_results(Path(args.rescore), cases_path)
        return 0

    cases = load_cases(cases_path)
    ref = references()
    rows = run_session(cases, ref)
    for r in rows:
        r["pass_final"] = r["pass"]
    _print_rows(rows)

    regressed: list[str] = []
    if args.baseline:
        base = baseline_passes(json.loads(Path(args.baseline).read_text(encoding="utf-8")))
        run1 = {r["name"]: r["pass"] for r in rows}
        need_rerun = any(base.get(n) and not run1.get(n) for n in base)
        run2_map = None
        if need_rerun:
            rows2 = run_session(cases, ref)
            run2_map = {r["name"]: r["pass"] for r in rows2}
            for r, r2 in zip(rows, rows2, strict=True):
                r["pass_rerun"] = r2["pass"]
                r["answer_rerun"] = r2.get("answer")
                r["pass_final"] = r["pass"] or r2["pass"]
        regressed, flaky = regressions(base, run1, run2_map)
        if flaky:
            print("FLAKY:", flaky)
        if regressed:
            print("REGRESSED:", regressed)

    summary = _summary(rows)
    print(json.dumps(summary, indent=1))

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = BASE_DIR / "evals" / f"{cases_path.stem}_results_{stamp}.json"
    out.write_text(json.dumps({"summary": summary, "cases": rows}, ensure_ascii=False, indent=1, default=str),
                   encoding="utf-8")
    if regressed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
