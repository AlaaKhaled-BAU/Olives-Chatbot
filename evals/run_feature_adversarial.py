#!/usr/bin/env python3.13
"""Live adversarial battery for transcript + morphology + feedback + tools_ms.

Runs against a live uvicorn on :8100. Uses real LLM + real DB/docs.
"""
from __future__ import annotations

import json
import sys
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path

import httpx

BASE = "http://127.0.0.1:8100"
COMPANY_ID = 2
TIMEOUT = 180.0
DENIAL_PHRASES = (
    "لم أجد",
    "لا يوجد",
    "لم يكن في سياق",
    "غير موجود في المحادثة",
    "لا أتذكر",
    "لم يكن هناك",
    "لا أملك",
)

_EMPTY_SESSION_ADMIT_PHRASES = (
    "لا يوجد",
    "لم يكن",
    "لم أسأل",
    "لا أسئلة",
    "جديدة",
    "لم يسبق",
    "أول سؤال",
    "هذه المحادثة",
    "لا ذاكرة",
    "empty",
)


def _admits_empty_session(ans: str) -> bool:
    return any(p in ans for p in _EMPTY_SESSION_ADMIT_PHRASES)


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
        out.update({k: v for k, v in data.items() if v is not None})
    return out


@dataclass
class CaseResult:
    id: str
    category: str
    difficulty: str
    verdict: str
    reasons: list[str] = field(default_factory=list)
    elapsed_s: float = 0.0
    detail: dict = field(default_factory=dict)


class Harness:
    def __init__(self) -> None:
        self.client = httpx.Client(timeout=TIMEOUT)
        self.results: list[CaseResult] = []

    def close(self) -> None:
        self.client.close()

    def health(self) -> bool:
        try:
            r = self.client.get(f"{BASE}/health")
            return r.status_code == 200
        except httpx.ConnectError:
            return False

    def pin_company(self, session_id: str, company_id: int = COMPANY_ID) -> None:
        r = self.client.post(
            f"{BASE}/context",
            json={"session_id": session_id, "company_id": company_id},
        )
        r.raise_for_status()

    def ask(
        self,
        session_id: str,
        question: str,
        *,
        company_id: int | None = COMPANY_ID,
    ) -> dict:
        t0 = time.perf_counter()
        r = self.client.post(
            f"{BASE}/ask",
            json={
                "question": question,
                "session_id": session_id,
                "company_id": company_id,
            },
            headers={"Accept": "text/event-stream"},
        )
        elapsed = round(time.perf_counter() - t0, 2)
        parsed = parse_sse(r.text)
        parsed["_elapsed_s"] = elapsed
        parsed["_http_status"] = r.status_code
        return parsed

    def context(self, session_id: str) -> dict:
        r = self.client.get(f"{BASE}/context", params={"session_id": session_id})
        r.raise_for_status()
        return r.json()

    def feedback(self, session_id: str, turn_id: str | None, helpful: bool) -> int:
        body = {"session_id": session_id, "helpful": helpful}
        if turn_id:
            body["turn_id"] = turn_id
        r = self.client.post(f"{BASE}/feedback", json=body)
        return r.status_code

    def record(self, case_id: str, category: str, difficulty: str, verdict: str, reasons: list[str], **detail) -> None:
        self.results.append(
            CaseResult(
                id=case_id,
                category=category,
                difficulty= str(difficulty),
                verdict=verdict,
                reasons=reasons,
                elapsed_s=float(detail.pop("elapsed_s", 0)),
                detail=detail,
            )
        )

    # --- scenario groups ---

    def run_transcript_scenarios(self) -> None:
        sid = f"tx-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)

        # T1 easy: single ask → transcript has 1 row with turn_id
        p = self.ask(sid, "ما هو خيار النظام رقم 157؟")
        ctx = self.context(sid)
        reasons = []
        if len(ctx.get("transcript") or []) != 1:
            reasons.append(f"transcript_len={len(ctx.get('transcript') or [])} want 1")
        if not p.get("turn_id"):
            reasons.append("missing turn_id on done")
        if not (p.get("answer") or "").strip():
            reasons.append("empty answer")
        row = (ctx.get("transcript") or [{}])[0]
        if row.get("a") != p.get("answer"):
            reasons.append("transcript.a != full answer")
        self.record(
            "T1-single-transcript",
            "transcript",
            "easy",
            "PASS" if not reasons else "FAIL",
            reasons,
            turn_id=p.get("turn_id"),
            answer_len=len(p.get("answer") or ""),
            transcript_a_len=len(row.get("a") or ""),
        )

        # T2 medium: 6 asks → split plumbing (transcript len) vs memory (follow-up)
        sid6 = f"tx6-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid6)
        questions = [
            "ما هو خيار النظام رقم 157؟",
            "وماذا عن رقم 211؟",
            "كيف أُسند الزبائن للمندوب؟",
            "ما الفرق بين الطلب والفاتورة؟",
            "كم عدد المسارات المسجلة؟",
            "اشكرك، هذا كل شيء",
        ]
        turn_ids = []
        for q in questions:
            p = self.ask(sid6, q)
            if p.get("turn_id"):
                turn_ids.append(p["turn_id"])
            time.sleep(0.3)
        ctx6 = self.context(sid6)
        tr = ctx6.get("transcript") or []
        plumbing_reasons = []
        if len(tr) != 6:
            plumbing_reasons.append(f"transcript_len={len(tr)} want 6")
        if tr and len(tr[0].get("a") or "") < 10:
            plumbing_reasons.append("first answer suspiciously short")
        self.record(
            "T2-plumbing-six-transcript",
            "transcript",
            "medium",
            "PASS" if not plumbing_reasons else "FAIL",
            plumbing_reasons,
            transcript_len=len(tr),
            turn_ids=len(turn_ids),
        )

        # 7th ask references earlier topic — model only has 4 history turns
        p7 = self.ask(sid6, "ارجع لسؤالي الأول عن خيار 157، ما كان رقم الخيار؟")
        ans7 = p7.get("answer") or ""
        ans7_lower = ans7.lower()
        prefix250 = ans7[:250]
        memory_reasons = []
        has_denial = any(p in prefix250 for p in DENIAL_PHRASES)
        has_157 = "157" in ans7_lower
        has_needle = has_157 or "gps" in ans7_lower or "cust" in ans7_lower
        if has_denial:
            memory_reasons.append("denial_phrase_in_first_250_chars")
        if not has_157 and not has_needle:
            memory_reasons.append("157/GPS/Cust LogOut absent from answer")
        memory_pass = has_157 and not has_denial
        self.record(
            "T2-memory-first-question-157",
            "transcript",
            "medium",
            "PASS" if memory_pass else "FAIL",
            memory_reasons,
            transcript_len=len(tr),
            followup_answer=ans7[:300],
            followup_elapsed=p7.get("_elapsed_s"),
            has_denial=has_denial,
            has_157=has_157,
        )

        # T3 hard: long answer preserved in transcript (docs question)
        sid_long = f"txl-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid_long)
        p = self.ask(
            sid_long,
            "اشرح بالتفصيل كيف يعتمد مستخدم الباك أوفيس طلبات البيع خطوة بخطوة",
        )
        ctx_l = self.context(sid_long)
        tr_l = ctx_l.get("transcript") or []
        ans = p.get("answer") or ""
        reasons = []
        if tr_l and len(tr_l[0].get("a") or "") < len(ans):
            reasons.append("transcript truncated vs live answer")
        if len(ans) < 80:
            reasons.append("answer shorter than expected for detail question")
        self.record(
            "T3-long-answer-full-transcript",
            "transcript",
            "hard",
            "PASS" if not reasons else "WARN",
            reasons,
            answer_len=len(ans),
            transcript_len=len(tr_l[0].get("a") or "") if tr_l else 0,
        )

    def run_transcript_index_scenarios(self) -> None:
        """8+ turns: history[-4] rolled off — index must resolve Q1/Q2."""
        sid = f"idx-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)
        questions = [
            "ما هو خيار النظام رقم 157؟",
            "وماذا عن رقم 211؟",
            "كيف أُسند الزبائن للمندوب؟",
            "ما الفرق بين الطلب والفاتورة؟",
            "كم عدد المسارات المسجلة؟",
            "كم عدد سندات القبض غير الملغاة؟",
            "ما معنى IsSuspended للزبون؟",
            "شكراً جزيلاً",
        ]
        for q in questions:
            self.ask(sid, q)
            time.sleep(0.35)
        ctx = self.context(sid)
        tr_len = len(ctx.get("transcript") or [])
        if tr_len < 8:
            self.record(
                "TI0-index-setup",
                "transcript_index",
                "hard",
                "SKIP",
                [f"transcript_len={tr_len} want 8"],
            )
            return

        p1 = self.ask(sid, "ما كان سؤالي الأول؟")
        ans1 = p1.get("answer") or ""
        reasons1 = []
        has_denial1 = any(p in ans1[:300] for p in DENIAL_PHRASES)
        has_157 = "157" in ans1
        if has_denial1:
            reasons1.append("denial_on_first_question_recall")
        if not has_157:
            reasons1.append("157_absent_from_first_question_recall")
        self.record(
            "TI1-index-first-question-ar",
            "transcript_index",
            "hard",
            "PASS" if has_157 and not has_denial1 else "FAIL",
            reasons1,
            transcript_len=tr_len,
            followup_answer=ans1[:350],
            has_denial=has_denial1,
            has_157=has_157,
            elapsed_s=p1.get("_elapsed_s"),
        )

        p2 = self.ask(sid, "ارجع لسؤالي الثاني عن 211، ما كان رقم الخيار وما وظيفته؟")
        ans2 = p2.get("answer") or ""
        reasons2 = []
        has_denial2 = any(p in ans2[:300] for p in DENIAL_PHRASES)
        has_211 = "211" in ans2
        if has_denial2:
            reasons2.append("denial_on_second_question_recall")
        if not has_211:
            reasons2.append("211_absent_from_second_question_recall")
        self.record(
            "TI2-index-second-question-211",
            "transcript_index",
            "hard",
            "PASS" if has_211 and not has_denial2 else "FAIL",
            reasons2,
            followup_answer=ans2[:350],
            has_denial=has_denial2,
            has_211=has_211,
            elapsed_s=p2.get("_elapsed_s"),
        )

    def run_feedback_scenarios(self) -> None:
        sid = f"fb-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)
        self.ask(sid, "كم عدد المسارات المسجلة؟")
        p2 = self.ask(sid, "كم عدد سندات القبض غير الملغاة؟")
        ctx = self.context(sid)
        tr = ctx.get("transcript") or []
        reasons = []
        if len(tr) < 2:
            self.record("F1-feedback-turn-id", "feedback", "medium", "SKIP", ["need 2 turns"])
            return
        first_id = tr[0]["id"]
        last_id = tr[-1]["id"]
        st = self.feedback(sid, first_id, True)
        if st != 200:
            reasons.append(f"feedback first turn status={st}")
        st_bad = self.feedback(sid, "deadbeef" * 4, True)
        if st_bad != 404:
            reasons.append(f"bogus turn_id status={st_bad} want 404")
        st_last = self.feedback(sid, last_id, False)
        if st_last != 200:
            reasons.append(f"feedback last turn status={st_last}")
        self.record(
            "F1-feedback-turn-id",
            "feedback",
            "medium",
            "PASS" if not reasons else "FAIL",
            reasons,
            first_turn_q=tr[0].get("q"),
            second_turn_q=tr[1].get("q"),
            last_sql_snip=(p2.get("answer_sql") or "")[:120],
        )

    def run_feedback_middle_turn_promote(self) -> None:
        """3 SQL turns — thumbs-up on middle must promote middle SQL only."""
        import os
        import sys
        from pathlib import Path

        sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
        from core import memory

        client = os.environ.get("CHATBOT_CLIENT", "105")
        sid = f"fb3-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)
        tag = uuid.uuid4().hex[:6]
        q1 = f"كم عدد المسارات المسجلة؟ ({tag}-a)"
        q2 = f"كم عدد العملاء في الشركة؟ ({tag}-b)"
        q3 = f"كم عدد مندوبي المبيعات؟ ({tag}-c)"
        before_q1 = memory.get_verified_query(client, COMPANY_ID, q1)
        before_q2 = memory.get_verified_query(client, COMPANY_ID, q2)
        before_q3 = memory.get_verified_query(client, COMPANY_ID, q3)
        self.ask(sid, q1)
        p2 = self.ask(sid, q2)
        self.ask(sid, q3)
        ctx = self.context(sid)
        tr = ctx.get("transcript") or []
        if len(tr) < 3:
            self.record(
                "F2-feedback-middle-turn-promote",
                "feedback",
                "hard",
                "SKIP",
                [f"transcript_len={len(tr)} want 3"],
            )
            return
        middle_id = tr[1]["id"]
        middle_sql = (tr[1].get("sql") or p2.get("answer_sql") or "").strip()
        st = self.feedback(sid, middle_id, True)
        reasons = []
        if st != 200:
            reasons.append(f"feedback_status={st}")
        stored = memory.get_verified_query(client, COMPANY_ID, q2)
        if not stored and not before_q2:
            reasons.append("middle_turn_not_promoted")
        elif middle_sql and stored and stored.get("proc_or_sql", "").strip() != middle_sql:
            reasons.append(
                f"promoted_sql_mismatch got={stored.get('proc_or_sql', '')[:80]!r} "
                f"want={middle_sql[:80]!r}"
            )
        after_q1 = memory.get_verified_query(client, COMPANY_ID, q1)
        after_q3 = memory.get_verified_query(client, COMPANY_ID, q3)
        if not before_q1 and after_q1:
            reasons.append("q1_erroneously_promoted")
        if not before_q3 and after_q3:
            reasons.append("q3_erroneously_promoted")
        self.record(
            "F2-feedback-middle-turn-promote",
            "feedback",
            "hard",
            "PASS" if not reasons else "FAIL",
            reasons,
            middle_turn_q=q2,
            middle_sql_snip=middle_sql[:120],
            promoted=bool(stored),
        )

    def run_company_switch(self) -> None:
        sid = f"co-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid, COMPANY_ID)
        self.ask(sid, "كم عدد المسارات؟")
        self.ask(sid, "وشكراً")
        ctx_before = self.context(sid)
        if len(ctx_before.get("transcript") or []) < 2:
            self.record("C1-company-clears-transcript", "session", "medium", "SKIP", ["asks failed"])
            return
        # switch to company 3
        self.pin_company(sid, 3)
        ctx_after = self.context(sid)
        reasons = []
        if ctx_after.get("transcript"):
            reasons.append(f"transcript not cleared len={len(ctx_after.get('transcript') or [])}")
        self.record(
            "C1-company-clears-transcript",
            "session",
            "medium",
            "PASS" if not reasons else "FAIL",
            reasons,
            before_len=len(ctx_before.get("transcript") or []),
            after_len=len(ctx_after.get("transcript") or []),
        )

        p_recall = self.ask(sid, "ما كان سؤالي الأول في هذه المحادثة؟")
        ans_recall = p_recall.get("answer") or ""
        leak_reasons = []
        if "كم عدد المسارات" in ans_recall:
            leak_reasons.append("prior_company_question_leaked_after_switch")
        if "157" in ans_recall or "211" in ans_recall:
            leak_reasons.append("index_leaked_cleared_transcript")
        admits_empty = _admits_empty_session(ans_recall)
        self.record(
            "C2-company-switch-no-index-leak",
            "session",
            "hard",
            "PASS" if not leak_reasons else "FAIL",
            leak_reasons,
            recall_answer=ans_recall[:350],
            admits_empty=admits_empty,
        )

    def run_morphology_docs(self) -> None:
        """Docs/how-to questions with inflected Arabic — real user phrasing."""
        pairs = [
            (
                "M1-invoice-create-tablet",
                "easy",
                "كيف أنشئ فاتورة مبيعات؟",
                ["تابلت", "tablet", "new invoice", "1.5.4", "view customers", "create", "فاتورة"],
            ),
            ("M1b-invoice-plural", "easy", "كيف أنشئ فاتورة مبيعات جديدة؟", ["فاتورة", "invoice", "إنشاء", "create", "بيع", "تابلت", "tablet"]),
            ("M2-invoice-def-plural", "medium", "أين أجد شاشة الفواتير في الباك أوفيس؟", ["فاتورة", "invoice", "فواتير", "back", "باك"]),
            ("M3-visit-singular", "medium", "كيف أسجل زيارة مندوب على التابلت؟", ["زيارة", "visit", "tablet", "تابلت", "مندوب"]),
            ("M4-visit-plural", "hard", "أين أرى الزيارات المسجلة للمندوب؟", ["زيارة", "visit", "زيارات", "LogAction", "مندوب"]),
            ("M5-order-forms", "hard", "ما الفرق بين الطلبات والفواتير عند الاعتماد؟", ["طلب", "فاتورة", "order", "invoice", "اعتماد"]),
            ("M6-typo-invoice", "hard", "كيف اصدر فاتوره مبيعات؟", ["فاتورة", "invoice", "بيع", "إصدار"]),
        ]
        sid = f"morph-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)
        for case_id, diff, question, needles in pairs:
            p = self.ask(sid, question)
            ans = (p.get("answer") or "").lower()
            srcs = json.dumps(p.get("sources") or [], ensure_ascii=False).lower()
            blob = ans + srcs
            hits = sum(1 for n in needles if n.lower() in blob)
            tablet_hits = sum(
                1 for n in ("تابلت", "tablet", "new invoice", "1.5.4", "view customers")
                if n.lower() in blob
            )
            reasons = []
            if not ans.strip():
                reasons.append("empty_answer")
            elif hits < 1:
                reasons.append(f"no_needle_match hits={hits}/{len(needles)}")
            if "invoice-create" in case_id and tablet_hits < 1:
                reasons.append("missing_tablet_create_reference")
            if not p.get("sources") and "docs" in case_id:
                pass  # sources optional
            min_hits = 2 if "invoice-create" in case_id else 1
            self.record(
                case_id,
                "morphology",
                diff,
                "PASS" if not reasons and hits >= min_hits else "WARN" if hits >= 1 else "FAIL",
                reasons,
                question=question,
                elapsed_s=p.get("_elapsed_s"),
                answer_preview=(p.get("answer") or "")[:400],
                sources_count=len(p.get("sources") or []),
                needle_hits=hits,
            )
            time.sleep(0.4)

    def run_docs_gap_scenarios(self) -> None:
        """BO create-from-zero is not in the user guide — PASS on honest gap admission."""
        sid = f"gap-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)
        question = "اشرح خطوة بخطوة كيف أنشئ فاتورة مبيعات من الصفر في الباك أوفيس"
        p = self.ask(sid, question)
        ans = p.get("answer") or ""
        gap_phrases = ("لا يوجد", "لم يعثر", "لا يشرح", "لم أجد", "لا يغطي", "غير متوفر")
        admits_gap = any(phrase in ans for phrase in gap_phrases)
        # Correct routing (tablet creates, BO views/approves) also counts as honest.
        ans_lower = ans.lower()
        routes_to_tablet = any(
            n in ans_lower for n in ("تابلت", "tablet", "new invoice", "view customers", "1.5.4")
        )
        clarifies_bo_limit = any(
            n in ans_lower for n in ("اعتماد", "approve", "7.3", "void", "إلغاء", "عرض")
        )
        honest_routing = routes_to_tablet and clarifies_bo_limit
        reasons = []
        if not ans.strip():
            reasons.append("empty_answer")
        elif not admits_gap and not honest_routing:
            reasons.append("neither_gap_admission_nor_tablet_vs_bo_routing")
        self.record(
            "docs_create_invoice_gap",
            "docs_gap",
            "medium",
            "PASS" if not reasons else "FAIL",
            reasons,
            question=question,
            admits_gap=admits_gap,
            honest_routing=honest_routing,
            elapsed_s=p.get("_elapsed_s"),
            answer_preview=ans[:400],
            sources_count=len(p.get("sources") or []),
        )
    def run_tools_ms(self) -> None:
        sid = f"tm-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)
        p = self.ask(sid, "كيف أُسند الزبائن للمندوب في دليل المستخدم؟")
        reasons = []
        tools_ms = p.get("tools_ms")
        if tools_ms is None:
            reasons.append("tools_ms_missing_from_sse")
        elif not isinstance(tools_ms, dict):
            reasons.append(f"tools_ms_not_dict type={type(tools_ms).__name__}")
        elif not tools_ms:
            reasons.append("tools_ms_empty_dict")
        elif all(v == 0 for v in tools_ms.values()):
            reasons.append("tools_ms_all_zeros")
        elif "search_docs" not in tools_ms:
            reasons.append("search_docs_missing_from_tools_ms")
        elif tools_ms.get("search_docs", 0) <= 0:
            reasons.append("search_docs_zero_ms")
        if not (p.get("answer") or "").strip():
            reasons.append("empty_answer")
        self.record(
            "TM2-tools-ms-sse",
            "tools_ms",
            "medium",
            "PASS" if not reasons else "FAIL",
            reasons,
            elapsed_s=p.get("_elapsed_s"),
            tools_ms=tools_ms,
            has_sources=bool(p.get("sources")),
        )

    def run_break_attempts(self) -> None:
        sid = f"brk-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)

        # No session_id — should not crash, no transcript server-side
        r = self.client.post(
            f"{BASE}/ask",
            json={"question": "مرحبا", "company_id": COMPANY_ID},
            headers={"Accept": "text/event-stream"},
        )
        p = parse_sse(r.text)
        reasons = []
        if r.status_code != 200:
            reasons.append(f"status={r.status_code}")
        self.record(
            "B1-no-session-id",
            "break",
            "easy",
            "PASS" if r.status_code == 200 else "FAIL",
            reasons,
            has_answer=bool(p.get("answer")),
        )

        # Whitespace-only questions must not grow transcript
        sid_ws = f"ws-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid_ws)
        len_before = len(self.context(sid_ws).get("transcript") or [])
        for ws_q in ("   ", "\n\t", "  \n  "):
            p_ws = self.ask(sid_ws, ws_q)
            if p_ws.get("_http_status") != 200:
                reasons2 = [f"non-200 for {ws_q!r}"]
                break
        else:
            reasons2 = []
        len_after = len(self.context(sid_ws).get("transcript") or [])
        if len_after > len_before:
            reasons2.append(f"transcript_grew {len_before}->{len_after}")
        self.record(
            "B2-whitespace-question",
            "break",
            "medium",
            "PASS" if not reasons2 else "FAIL",
            reasons2,
            transcript_before=len_before,
            transcript_after=len_after,
        )

        # Rapid fire 3 asks
        sid_rf = f"rf-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid_rf)
        for i in range(3):
            self.ask(sid_rf, f"سؤال سريع رقم {i+1}: ما هو النظام؟")
        ctx_rf = self.context(sid_rf)
        reasons3 = []
        if len(ctx_rf.get("transcript") or []) != 3:
            reasons3.append(f"transcript={len(ctx_rf.get('transcript') or [])}")
        self.record(
            "B3-rapid-fire",
            "break",
            "medium",
            "PASS" if not reasons3 else "FAIL",
            reasons3,
        )

        # Context without session
        r_ctx = self.client.get(f"{BASE}/context")
        reasons4 = []
        if r_ctx.json().get("transcript") != []:
            reasons4.append("transcript should be []")
        self.record(
            "B4-context-no-session",
            "break",
            "easy",
            "PASS" if not reasons4 else "FAIL",
            reasons4,
        )

    def run_user_conversation(self) -> None:
        """Simulate a real back-office user session."""
        sid = f"user-{uuid.uuid4().hex[:10]}"
        self.pin_company(sid)
        script = [
            ("مرحبا، أنا جديد على النظام", "greet", "easy"),
            ("كيف أُسند الزبائن للمندوب؟", "howto", "medium"),
            ("طيب وكيف أعتمد الطلبات؟", "followup", "medium"),
            ("كم عدد فواتير المبيعات في يونيو 2025 غير الملغاة؟", "sql", "hard"),
            ("هل هذا العدد يشمل الطلبات أم الفواتير فقط؟", "clarify", "hard"),
        ]
        transcript_lens = []
        for q, tag, diff in script:
            p = self.ask(sid, q)
            ctx = self.context(sid)
            transcript_lens.append(len(ctx.get("transcript") or []))
            time.sleep(0.5)
        reasons = []
        if transcript_lens[-1] != len(script):
            reasons.append(f"final_transcript={transcript_lens[-1]} want {len(script)}")
        # re-fetch context (simulate refresh)
        ctx_final = self.context(sid)
        tr = ctx_final.get("transcript") or []
        if len(tr) != len(script):
            reasons.append("refresh lost transcript")
        if tr and tr[0].get("q") != script[0][0]:
            reasons.append("first question mismatch after refresh")
        self.record(
            "U1-real-user-session",
            "conversation",
            "hard",
            "PASS" if not reasons else "FAIL",
            reasons,
            transcript_lens=transcript_lens,
            questions=[s[0][:40] for s in script],
        )


def main() -> int:
    h = Harness()
    if not h.health():
        print("ERROR: server not running on :8100", file=sys.stderr)
        return 2
    print("Running feature adversarial battery...", file=sys.stderr)

    h.run_transcript_scenarios()
    h.run_transcript_index_scenarios()
    h.run_feedback_scenarios()
    h.run_feedback_middle_turn_promote()
    h.run_company_switch()
    h.run_morphology_docs()
    h.run_docs_gap_scenarios()
    h.run_tools_ms()
    h.run_break_attempts()
    h.run_user_conversation()
    h.close()

    out = Path(__file__).parent / f"feature_adversarial_results_{time.strftime('%Y%m%d_%H%M%S')}.json"
    payload = {
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": {},
        "by_category": {},
        "results": [
            {
                "id": r.id,
                "category": r.category,
                "difficulty": r.difficulty,
                "verdict": r.verdict,
                "reasons": r.reasons,
                "elapsed_s": r.elapsed_s,
                **r.detail,
            }
            for r in h.results
        ],
    }
    by_v: dict[str, int] = {}
    by_cat: dict[str, dict[str, int]] = {}
    for r in h.results:
        by_v[r.verdict] = by_v.get(r.verdict, 0) + 1
        cat = by_cat.setdefault(r.category, {"PASS": 0, "WARN": 0, "FAIL": 0, "SKIP": 0})
        cat[r.verdict] = cat.get(r.verdict, 0) + 1
    payload["summary"] = by_v
    payload["by_category"] = by_cat
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    stable = Path(__file__).parent / "feature_adversarial_results.json"
    stable.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    total = len(h.results)
    passed = sum(1 for r in h.results if r.verdict == "PASS")
    warn = sum(1 for r in h.results if r.verdict == "WARN")
    fail = sum(1 for r in h.results if r.verdict == "FAIL")
    print(
        json.dumps(
            {
                "pass": passed,
                "warn": warn,
                "fail": fail,
                "skip": by_v.get("SKIP", 0),
                "total": total,
                "out": str(out),
            },
            ensure_ascii=False,
        )
    )
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
