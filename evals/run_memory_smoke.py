#!/usr/bin/env python3.13
"""Programmatic multi-turn memory smoke (thread card + company switch).

Uses fake LLM for prompt wiring; one optional live path when CHATBOT_MEMORY_LIVE=1.
"""
from __future__ import annotations

import json
import os
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core import agent, sessions  # noqa: E402
from core.sessions import record_session_turn  # noqa: E402
from api import server  # noqa: E402


def _chunk(text: str):
    delta = types.SimpleNamespace(content=text, tool_calls=None, reasoning_content=None)
    return types.SimpleNamespace(choices=[types.SimpleNamespace(delta=delta)])


def _plain(content: str):
    return types.SimpleNamespace(
        choices=[types.SimpleNamespace(message=types.SimpleNamespace(content=content))]
    )


def test_basis_followup_injects_card(monkeypatch_db: Path) -> dict:
    """Turn1 metric card; turn2 bare basis change must see card in messages."""
    import core.memory as memory

    memory.DB_PATH = monkeypatch_db / "cache.sqlite"
    captured_turns: list[list] = []

    def fake_complete(messages, **kwargs):
        if kwargs.get("stream"):
            captured_turns.append(list(messages))
            return iter([_chunk("إجابة.")])
        return _plain('{"followups": [], "confidence": null, "refusal": false}')

    agent.llm.complete = fake_complete  # type: ignore[method-assign]

    session: dict = {}
    card = {
        "metric": "sales",
        "tax": "incl",
        "returns": "gross",
        "period_label": "2025-07-01 .. 2025-08-01",
        "as_of": "2025-10-03",
        "primary_measure": "gross_sales",
        "values": {"gross_sales": 100.0},
    }
    session["thread_head"] = card
    session["conversation"] = {"CompanyID": 2}
    session["history"] = [
        {
            "q": "قديش مبيعات يوليو 2025؟",
            "a": "100 دينار شامل الضريبة.",
            "sql": "SELECT 1",
        }
    ]

    list(
        agent.ask_stream(
            "morec",
            "طيب قبل الضريبة",
            conversation=session["conversation"],
            history=session["history"],
            thread_head=session.get("thread_head"),
        )
    )
    blob = json.dumps(captured_turns[-1], ensure_ascii=False)
    has_card = "Thread card" in blob and "tax" in blob
    return {
        "name": "basis_followup_card_in_prompt",
        "pass": has_card,
        "evidence": "Thread card" if has_card else blob[:500],
    }


def test_company_switch_clears_thread_head() -> dict:
    session = {
        "conversation": {"CompanyID": 1},
        "history": [{"q": "x", "a": "y"}],
        "transcript": [{"id": "t1"}],
        "thread_head": {"tax": "incl", "returns": "gross"},
    }
    server._set_session_company(session, session["conversation"], 2)
    ok = (
        session.get("thread_head") is None
        and session.get("history") == []
        and session.get("transcript") == []
    )
    return {
        "name": "company_switch_clears_card",
        "pass": ok,
        "evidence": {k: session.get(k) for k in ("thread_head", "history", "transcript")},
    }


def test_record_session_stores_thread_head(tmp_path: Path) -> dict:
    sessions.DB_PATH = tmp_path / "sessions.sqlite"
    session: dict = {}
    result = {
        "answer": "ok",
        "thread_head": {"tax": "excl", "returns": "net", "metric": "sales"},
    }
    record_session_turn(
        session,
        question="q",
        result=result,
        client="morec",
        company_id=1,
        max_history=agent.MAX_HISTORY_TURNS,
    )
    ok = session.get("thread_head", {}).get("tax") == "excl"
    sessions.save("mem-smoke", session)
    loaded = sessions.load("mem-smoke")
    ok = ok and loaded and loaded.get("thread_head", {}).get("returns") == "net"
    return {
        "name": "record_session_persists_thread_head",
        "pass": bool(ok),
        "evidence": loaded.get("thread_head") if loaded else None,
    }


def main() -> int:
    tmp = Path(os.environ.get("TMPDIR", "/tmp")) / "chatbot_memory_smoke"
    tmp.mkdir(parents=True, exist_ok=True)
    tests = [
        test_company_switch_clears_thread_head(),
        test_record_session_stores_thread_head(tmp),
        test_basis_followup_injects_card(tmp),
    ]
    report = {"tests": tests, "all_pass": all(t["pass"] for t in tests)}
    out = ROOT / "evals" / "memory_smoke_results.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
