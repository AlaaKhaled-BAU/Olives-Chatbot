#!/usr/bin/env python3.13
"""Supplementary hole-finding probes after main battery."""
from __future__ import annotations

import json
import sys
import time
import uuid
from pathlib import Path

import httpx

BASE = "http://127.0.0.1:8100"
COMPANY_ID = 2
DENIAL_PHRASES = (
    "لم أجد",
    "لا يوجد",
    "لم يكن",
    "غير موجود",
    "لا أتذكر",
)


def parse_sse(raw: str) -> dict:
    out: dict = {}
    for block in raw.split("\n\n"):
        if not block.startswith("data: "):
            continue
        p = block[6:].strip()
        if p == "[DONE]":
            continue
        try:
            out.update(json.loads(p))
        except json.JSONDecodeError:
            pass
    return out


def _verdict(pass_cond: bool, *, warn: bool = False) -> str:
    if pass_cond:
        return "PASS"
    return "WARN" if warn else "FAIL"


def main() -> int:
    c = httpx.Client(timeout=180)
    findings: list[dict] = []
    t0 = time.time()

    if c.get(f"{BASE}/health").status_code != 200:
        print("ERROR: server not running on :8100", file=sys.stderr)
        return 2

    # --- 8-turn index recall (history rolled off) ---
    sid = f"sup-{uuid.uuid4().hex[:8]}"
    c.post(f"{BASE}/context", json={"session_id": sid, "company_id": COMPANY_ID})
    script = [
        "ما هو خيار النظام رقم 157؟",
        "وماذا عن رقم 211؟",
        "كيف أُسند الزبائن للمندوب؟",
        "ما الفرق بين الطلب والفاتورة؟",
        "كم عدد المسارات؟",
        "كم عدد سندات القبض؟",
        "ما معنى IsSuspended؟",
        "شكراً",
    ]
    for q in script:
        c.post(
            f"{BASE}/ask",
            json={"question": q, "session_id": sid, "company_id": COMPANY_ID},
            headers={"Accept": "text/event-stream"},
        )
        time.sleep(1.0)

    r = c.post(
        f"{BASE}/ask",
        json={
            "question": "في سؤالي الأول عن خيار النظام، ما رقم الخيار وما وظيفته؟",
            "session_id": sid,
            "company_id": COMPANY_ID,
        },
        headers={"Accept": "text/event-stream"},
    )
    p = parse_sse(r.text)
    ans = p.get("answer") or ""
    denies = any(x in ans[:300] for x in DENIAL_PHRASES)
    has_fact = "157" in ans and ("gps" in ans.lower() or "check" in ans.lower() or "خيار" in ans)
    findings.append(
        {
            "test": "history_amnesia_after_8",
            "category": "transcript_index",
            "verdict": _verdict(has_fact and not denies),
            "denies_memory": denies,
            "has_correct_fact": has_fact,
            "answer_snip": ans[:400],
        }
    )

    r1b = c.post(
        f"{BASE}/ask",
        json={
            "question": "ارجع لسؤالي الثاني عن 211",
            "session_id": sid,
            "company_id": COMPANY_ID,
        },
        headers={"Accept": "text/event-stream"},
    )
    p1b = parse_sse(r1b.text)
    ans1b = p1b.get("answer") or ""
    denies1b = any(x in ans1b[:300] for x in DENIAL_PHRASES)
    has_211 = "211" in ans1b
    findings.append(
        {
            "test": "index_second_question_211",
            "category": "transcript_index",
            "verdict": _verdict(has_211 and not denies1b),
            "denies_memory": denies1b,
            "has_211": has_211,
            "answer_snip": ans1b[:400],
        }
    )

    # --- tools_ms on docs ask ---
    r2 = c.post(
        f"{BASE}/ask",
        json={
            "question": "كيف أُسند الزبائن للمندوب؟",
            "session_id": sid,
            "company_id": COMPANY_ID,
        },
        headers={"Accept": "text/event-stream"},
    )
    p2 = parse_sse(r2.text)
    tools_ms = p2.get("tools_ms")
    tools_ok = (
        isinstance(tools_ms, dict)
        and bool(tools_ms)
        and not all(v == 0 for v in tools_ms.values())
        and tools_ms.get("search_docs", 0) > 0
    )
    findings.append(
        {
            "test": "tools_ms_in_sse",
            "category": "tools_ms",
            "verdict": _verdict(tools_ok),
            "tools_ms": tools_ms,
            "keys": sorted(p2.keys()),
        }
    )

    # --- morphology + new corpus ---
    sid_m = f"morph-{uuid.uuid4().hex[:8]}"
    c.post(f"{BASE}/context", json={"session_id": sid_m, "company_id": COMPANY_ID})
    r_m = c.post(
        f"{BASE}/ask",
        json={
            "question": "كيف أنشئ فاتورة مبيعات؟",
            "session_id": sid_m,
            "company_id": COMPANY_ID,
        },
        headers={"Accept": "text/event-stream"},
    )
    p_m = parse_sse(r_m.text)
    ans_m = (p_m.get("answer") or "").lower()
    src_m = json.dumps(p_m.get("sources") or [], ensure_ascii=False).lower()
    blob_m = ans_m + src_m
    tablet_hits = sum(
        1 for n in ("تابلت", "tablet", "new invoice", "1.5.4", "view customers", "create")
        if n in blob_m
    )
    findings.append(
        {
            "test": "morphology_invoice_create_tablet",
            "category": "morphology",
            "verdict": _verdict(tablet_hits >= 1 and bool(ans_m.strip())),
            "tablet_hits": tablet_hits,
            "sources_count": len(p_m.get("sources") or []),
            "answer_snip": (p_m.get("answer") or "")[:350],
        }
    )

    # --- BO-from-zero gap honesty ---
    r3 = c.post(
        f"{BASE}/ask",
        json={
            "question": "اشرح خطوة بخطوة كيف أنشئ فاتورة مبيعات من الصفر في الباك أوفيس",
            "session_id": sid_m,
            "company_id": COMPANY_ID,
        },
        headers={"Accept": "text/event-stream"},
    )
    p3 = parse_sse(r3.text)
    ans3 = p3.get("answer") or ""
    gap_phrases = ("لا يوجد", "لم يعثر", "لم أجد", "لا يشرح", "غير متوفر")
    admits_gap = any(x in ans3 for x in gap_phrases)
    ans3_lower = ans3.lower()
    honest_routing = any(n in ans3_lower for n in ("تابلت", "tablet", "new invoice", "1.5.4")) and any(
        n in ans3_lower for n in ("اعتماد", "approve", "7.3", "عرض", "void")
    )
    findings.append(
        {
            "test": "missing_corpus_create_invoice",
            "category": "docs_gap",
            "verdict": _verdict(admits_gap or honest_routing),
            "admits_gap": admits_gap,
            "honest_routing": honest_routing,
            "sources": len(p3.get("sources") or []),
            "answer_snip": ans3[:300],
        }
    )

    # --- whitespace guard ---
    sid_ws = f"ws-{uuid.uuid4().hex[:8]}"
    c.post(f"{BASE}/context", json={"session_id": sid_ws, "company_id": COMPANY_ID})
    ctx_before = c.get(f"{BASE}/context", params={"session_id": sid_ws}).json()
    len_before = len(ctx_before.get("transcript") or [])
    for ws_q in ("   ", "\n\t"):
        c.post(
            f"{BASE}/ask",
            json={"question": ws_q, "session_id": sid_ws, "company_id": COMPANY_ID},
            headers={"Accept": "text/event-stream"},
        )
    ctx_after = c.get(f"{BASE}/context", params={"session_id": sid_ws}).json()
    len_after = len(ctx_after.get("transcript") or [])
    findings.append(
        {
            "test": "whitespace_no_transcript_growth",
            "category": "break",
            "verdict": _verdict(len_after == len_before),
            "transcript_before": len_before,
            "transcript_after": len_after,
        }
    )

    # --- company switch index leak ---
    sid_co = f"co-{uuid.uuid4().hex[:8]}"
    c.post(f"{BASE}/context", json={"session_id": sid_co, "company_id": COMPANY_ID})
    c.post(
        f"{BASE}/ask",
        json={"question": "كم عدد المسارات؟", "session_id": sid_co, "company_id": COMPANY_ID},
        headers={"Accept": "text/event-stream"},
    )
    c.post(f"{BASE}/context", json={"session_id": sid_co, "company_id": 3})
    ctx_cleared = c.get(f"{BASE}/context", params={"session_id": sid_co}).json()
    cleared_ok = not ctx_cleared.get("transcript")
    r_co = c.post(
        f"{BASE}/ask",
        json={
            "question": "ما كان سؤالي الأول؟",
            "session_id": sid_co,
            "company_id": 3,
        },
        headers={"Accept": "text/event-stream"},
    )
    p_co = parse_sse(r_co.text)
    ans_co = p_co.get("answer") or ""
    leaked = "المسارات" in ans_co or "كم عدد المسارات" in ans_co
    ctx_co = c.get(f"{BASE}/context", params={"session_id": sid_co}).json()
    findings.append(
        {
            "test": "company_switch_no_index_leak",
            "category": "session",
            "verdict": _verdict(cleared_ok and not leaked),
            "transcript_cleared_on_switch": cleared_ok,
            "transcript_after_recall": len(ctx_co.get("transcript") or []),
            "leaked_prior_question": leaked,
            "answer_snip": ans_co[:300],
        }
    )

    # --- rate limit info ---
    sid2 = f"rl-{uuid.uuid4().hex[:8]}"
    c.post(f"{BASE}/context", json={"session_id": sid2, "company_id": COMPANY_ID})
    statuses = []
    for i in range(35):
        r = c.post(
            f"{BASE}/ask",
            json={"question": f"ping {i}", "session_id": sid2, "company_id": COMPANY_ID},
            headers={"Accept": "text/event-stream"},
        )
        statuses.append(r.status_code)
    ctx = c.get(f"{BASE}/context", params={"session_id": sid2}).json()
    findings.append(
        {
            "test": "rate_limit_30_per_min",
            "category": "rate_limit",
            "verdict": "INFO",
            "status_counts": {str(s): statuses.count(s) for s in set(statuses)},
            "transcript_len": len(ctx.get("transcript") or []),
            "note": "429s mean transcript stops growing even if user keeps typing",
        }
    )

    c.close()

    by_cat: dict[str, dict[str, int]] = {}
    for f in findings:
        cat = f.get("category", "other")
        v = f.get("verdict", "INFO")
        by_cat.setdefault(cat, {"PASS": 0, "WARN": 0, "FAIL": 0, "SKIP": 0, "INFO": 0})
        by_cat[cat][v] = by_cat[cat].get(v, 0) + 1

    payload = {
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "elapsed_s": round(time.time() - t0, 1),
        "summary": {
            v: sum(1 for f in findings if f.get("verdict") == v)
            for v in ("PASS", "WARN", "FAIL", "SKIP", "INFO")
        },
        "by_category": by_cat,
        "findings": findings,
    }

    out = Path(__file__).parent / f"feature_supplementary_results_{time.strftime('%Y%m%d_%H%M%S')}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    # Also write stable symlink path for convenience
    stable = Path(__file__).parent / "run_feature_supplementary_results.json"
    stable.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"out": str(out), **payload["summary"]}, ensure_ascii=False))
    return 0 if payload["summary"].get("FAIL", 0) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
