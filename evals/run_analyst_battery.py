#!/usr/bin/env python3.13
"""Run analyst_realworld battery, logical eval, merge into combined corpus."""
from __future__ import annotations

import hashlib
import json
import re
import time
import uuid
from datetime import UTC, datetime
from pathlib import Path

import httpx

BASE = "http://127.0.0.1:8100"
COMPANY_ID = 2
EVALS = Path(__file__).resolve().parent
CORPUS = EVALS / "analyst_realworld_ar_105.jsonl"
COMBINED = EVALS / "all_test_questions_combined.json"
OUT_RUN = EVALS / "analyst_realworld_ar_105_results.json"


def _norm_q(text: str) -> str:
    t = re.sub(r"\s+", " ", (text or "").strip().lower())
    return hashlib.sha256(t.encode()).hexdigest()[:16]


def parse_sse(raw: str) -> dict:
    out: dict = {}
    for block in raw.split("\n\n"):
        if not block.startswith("data: "):
            continue
        payload = block[6:].strip()
        if payload == "[DONE]":
            continue
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            continue
        if data.get("answer"):
            out["answer"] = data["answer"]
        if data.get("answer_sql"):
            out["answer_sql"] = data["answer_sql"]
        if data.get("needs_ask"):
            out["needs_ask"] = data["needs_ask"]
        if data.get("error"):
            out["error"] = data["error"]
        if data.get("sources"):
            out["sources"] = data["sources"]
    return out


def logical_eval(case: dict, parsed: dict) -> dict:
    """Heuristic analyst-quality review — not numeric gold scoring."""
    answer = (parsed.get("answer") or parsed.get("needs_ask") or parsed.get("error") or "").strip()
    sql = (parsed.get("answer_sql") or "").lower()
    a = answer.lower()
    score = 5  # start neutral
    notes: list[str] = []
    verdict = "logical"

    if not answer:
        return {"verdict": "fail", "logic_score": 1, "notes": ["empty answer"]}

    if parsed.get("needs_ask") and "شركة" in answer:
        return {"verdict": "fail", "logic_score": 2, "notes": ["re-asked company instead of analyzing"]}

    # Analyst behaviors that raise score
    if "isvoid" in sql or "isnull(isvoid" in sql or "غير ملغ" in a or "non-void" in a:
        score += 1
        notes.append("respects void filter")
    if "transactiontypeid" in sql and "1" in sql:
        score += 1
        notes.append("uses sales invoice type")
    if any(w in a for w in ("افترض", "assume", "أفترض", "يعني", "ملاحظة", "note")):
        score += 1
        notes.append("states assumptions or interpretation")
    if "ordersheaders" in sql or "طلب" in a:
        if case.get("angle") in ("backlog", "pipeline"):
            score += 1
            notes.append("distinguishes orders from invoices")
    if "receipts" in sql or "قبض" in a or "تحصيل" in a:
        if case.get("angle") in ("cash_vs_sales", "reconciliation", "timing"):
            score += 1
            notes.append("addresses receipts/collections")
    if re.search(r"\d", answer):
        score += 1
        notes.append("gives quantitative answer")
    if parsed.get("answer_sql"):
        score += 1
        notes.append("shows SQL evidence")

    # Red flags
    if "261" in answer and case.get("angle") not in ("reconciliation",):
        if "بدون" in case.get("question", "") or "كل الرؤوس" in case.get("question", ""):
            pass
        elif "238" not in answer and "مبيعات" in case.get("question", "").lower():
            score -= 1
            notes.append("possible grain confusion (261 vs sales)")
    if "dbo." in sql and "users" not in sql:
        score -= 2
        notes.append("queries base schema")
    if len(answer) < 40 and case.get("angle") == "summary":
        score -= 2
        notes.append("too thin for executive summary")

    score = max(1, min(10, score))
    if score >= 8:
        verdict = "strong"
    elif score >= 6:
        verdict = "logical"
    elif score >= 4:
        verdict = "weak"
    else:
        verdict = "fail"

    return {"verdict": verdict, "logic_score": score, "notes": notes}


def run_battery() -> list[dict]:
    cases = [json.loads(l) for l in CORPUS.read_text(encoding="utf-8").splitlines() if l.strip()]
    session_id = f"analyst-{uuid.uuid4().hex[:10]}"
    results = []
    with httpx.Client() as client:
        client.post(f"{BASE}/context", json={"session_id": session_id, "company_id": COMPANY_ID})
        for case in cases:
            print(f"Running {case['id']}...", flush=True)
            t0 = time.perf_counter()
            resp = client.post(
                f"{BASE}/ask",
                json={"question": case["question"], "session_id": session_id, "company_id": COMPANY_ID},
                headers={"Accept": "text/event-stream"},
                timeout=180.0,
            )
            elapsed = round(time.perf_counter() - t0, 2)
            parsed = parse_sse(resp.text)
            ev = logical_eval(case, parsed)
            results.append({
                **case,
                "client": "105",
                "company_id": COMPANY_ID,
                "lang": "ar",
                "elapsed_s": elapsed,
                "answer": (parsed.get("answer") or parsed.get("needs_ask") or parsed.get("error") or ""),
                "answer_sql": parsed.get("answer_sql") or "",
                "sources": parsed.get("sources"),
                "http_status": resp.status_code,
                "evaluation": ev,
            })
            time.sleep(0.3)
    OUT_RUN.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return results


def merge_into_combined(results: list[dict]) -> None:
    data = json.loads(COMBINED.read_text(encoding="utf-8"))
    existing_uids = {c["uid"] for c in data["cases"]}
    added = 0
    for r in results:
        uid = f"analyst_realworld_ar_105.jsonl:{r['id']}"
        if uid in existing_uids:
            continue
        entry = {
            "uid": uid,
            "kind": "analyst_session",
            "source_file": "evals/analyst_realworld_ar_105.jsonl",
            "source_id": r["id"],
            "client": "105",
            "company_id": 2,
            "lang": "ar",
            "persona": r.get("persona"),
            "angle": r.get("angle"),
            "category": r.get("angle"),
            "purpose": r.get("purpose"),
            "question": r["question"],
            "question_hash": _norm_q(r["question"]),
            "validation": r.get("validation"),
            "elapsed_s": r.get("elapsed_s"),
            "answer": r.get("answer"),
            "answer_sql": r.get("answer_sql"),
            "sources": r.get("sources"),
            "evaluation": r.get("evaluation"),
            "last_run": {
                "answer": r.get("answer"),
                "answer_sql": r.get("answer_sql"),
                "elapsed_s": r.get("elapsed_s"),
                "evaluation": r.get("evaluation"),
            },
            "raw": {k: r[k] for k in ("id", "persona", "angle", "purpose", "question", "validation") if k in r},
        }
        data["cases"].append(entry)
        added += 1

    meta = data["meta"]
    meta["generated_at"] = datetime.now(UTC).isoformat()
    meta["source_files"] = list(dict.fromkeys(meta.get("source_files", []) + ["analyst_realworld_ar_105.jsonl"]))
    meta["counts_by_source"] = meta.get("counts_by_source", {})
    meta["counts_by_source"]["analyst_realworld_ar_105.jsonl"] = 20
    meta["counts_by_kind"] = meta.get("counts_by_kind", {})
    meta["counts_by_kind"]["analyst_session"] = meta["counts_by_kind"].get("analyst_session", 0) + added
    meta["total_cases"] = len(data["cases"])
    notes = meta.get("notes", [])
    note = "analyst_realworld_ar_105.jsonl: 20 real-world analyst personas with logic_score evaluation"
    if note not in notes:
        notes.append(note)
    meta["notes"] = notes

    COMBINED.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"added": added, "total": len(data["cases"]), "out": str(COMBINED)}, ensure_ascii=False))


if __name__ == "__main__":
    res = run_battery()
    merge_into_combined(res)
    strong = sum(1 for r in res if r["evaluation"]["verdict"] == "strong")
    logical = sum(1 for r in res if r["evaluation"]["verdict"] == "logical")
    weak = sum(1 for r in res if r["evaluation"]["verdict"] == "weak")
    fail = sum(1 for r in res if r["evaluation"]["verdict"] == "fail")
    print(json.dumps({"strong": strong, "logical": logical, "weak": weak, "fail": fail, "avg_s": round(sum(r["elapsed_s"] for r in res)/len(res), 2)}))
