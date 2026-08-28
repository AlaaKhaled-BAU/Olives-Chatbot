#!/usr/bin/env python3.13
"""Merge all eval / test question corpora into one JSON file."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
OUT = EVALS / "all_test_questions_combined.json"

QUESTION_CORPORA: list[tuple[str, str, dict]] = [
    ("comprehensive_ar_105.jsonl", "question", {"client": "105", "company_id": 2, "lang": "ar"}),
    ("comprehensive_ar_105_wave2.jsonl", "question", {"client": "105", "company_id": 2, "lang": "ar"}),
    ("adhoc_ar_105.jsonl", "question", {"client": "105", "company_id": 2, "lang": "ar"}),
    ("report_alias_ar_105.jsonl", "question", {"client": "105", "company_id": 2, "lang": "ar"}),
    ("docs_105_ar.jsonl", "question", {"client": "105", "company_id": 2, "lang": "ar"}),
    ("wave5_accuracy.jsonl", "question", {"client": "105", "company_id": 2, "lang": "ar"}),
    ("hard_en_regression.jsonl", "question", {"client": "105", "company_id": 2, "lang": "en"}),
    ("stress70.jsonl", "mixed", {"client": "105", "company_id": 2, "lang": "ar"}),
    ("accuracy.jsonl", "question", {"client": "morec", "lang": "mixed"}),
    ("docs_accuracy.jsonl", "question", {"client": "morec", "lang": "mixed"}),
    ("exec_golden.jsonl", "golden_sql", {"client": "105", "company_id": 2, "lang": "ar"}),
    ("isolation.jsonl", "isolation", {}),
]

RESULT_CORPORA = [
    "stress70_results.jsonl",
    "comprehensive_ar_105_results.json",
    "adhoc_ar_105_results.json",
    "report_alias_ar_105_results.json",
]

QA_RESULTS = ROOT / ".gstack/qa-reports/adversarial-results.json"
GROUND_TRUTH_MD = EVALS / "comprehensive_ar_105_ground_truth.md"


def _norm_q(text: str) -> str:
    t = re.sub(r"\s+", " ", (text or "").strip().lower())
    return hashlib.sha256(t.encode()).hexdigest()[:16]


def _load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def _base_id(row: dict, fallback: str) -> str:
    for k in ("id", "name"):
        if row.get(k):
            return str(row[k])
    return fallback


def _question_text(row: dict) -> str | None:
    return row.get("question") or row.get("q")


def _normalize_row(row: dict, source_file: str, defaults: dict, index: int) -> dict | list[dict]:
    src = f"evals/{source_file}"
    base = _base_id(row, f"line{index + 1}")
    uid = f"{source_file}:{base}"

    if row.get("turns"):
        return {
            "uid": uid,
            "kind": "multi_turn",
            "source_file": src,
            "source_id": base,
            "client": row.get("client") or defaults.get("client"),
            "company_id": row.get("company") or row.get("company_id") or defaults.get("company_id"),
            "lang": row.get("lang") or defaults.get("lang"),
            "category": row.get("cat") or row.get("category"),
            "turns": row["turns"],
            "note": row.get("note"),
            "raw": row,
        }

    if row.get("attack"):
        return {
            "uid": uid,
            "kind": "isolation",
            "source_file": src,
            "source_id": base,
            "attack": row.get("attack"),
            "client": row.get("client"),
            "company_id": row.get("company_id"),
            "sql": row.get("sql"),
            "proc": row.get("proc"),
            "query": row.get("query"),
            "raw": row,
        }

    q = _question_text(row)
    if not q and row.get("gold_sql"):
        return {
            "uid": uid,
            "kind": "golden_sql",
            "source_file": src,
            "source_id": base,
            "client": row.get("client") or defaults.get("client"),
            "company_id": row.get("company_id") or defaults.get("company_id"),
            "lang": row.get("lang") or defaults.get("lang"),
            "question": row.get("question"),
            "gold_sql": row.get("gold_sql"),
            "gold_rows": row.get("gold_rows"),
            "raw": row,
        }

    if not q:
        return None

    item = {
        "uid": uid,
        "kind": "question",
        "source_file": src,
        "source_id": base,
        "client": row.get("client") or defaults.get("client"),
        "company_id": row.get("company") or row.get("company_id") or defaults.get("company_id"),
        "lang": row.get("lang") or defaults.get("lang"),
        "category": row.get("cat") or row.get("category"),
        "purpose": row.get("purpose"),
        "question": q,
        "question_hash": _norm_q(q),
        "ground_truth": row.get("ground_truth"),
        "gold_sql": row.get("gold_sql"),
        "validation": row.get("validation"),
        "expect_contains": row.get("expect_contains"),
        "expect_contains_any": row.get("expect_contains_any"),
        "expect_not_contains": row.get("expect_not_contains"),
        "expect_refusal": row.get("expect_refusal"),
        "expect_refusal_or_ask": row.get("expect_refusal_or_ask"),
        "source_must_match": row.get("source_must_match"),
        "doc_must": row.get("doc_must"),
        "answer_sql_must_contain": row.get("answer_sql_must_contain"),
        "expect_report": row.get("expect_report"),
        "note": row.get("note"),
        "wave": row.get("wave"),
        "raw": row,
    }
    return {k: v for k, v in item.items() if v is not None}


def _attach_results(cases: list[dict]) -> None:
    by_uid: dict[str, dict] = {c["uid"]: c for c in cases if "uid" in c}

    stress = _load_jsonl(EVALS / "stress70_results.jsonl")
    stress_by_id = {r["id"]: r for r in stress}
    for c in cases:
        sid = c.get("source_id")
        if c.get("source_file") == "evals/stress70.jsonl" and sid in stress_by_id:
            c["last_run"] = {
                "answer": stress_by_id[sid].get("answer"),
                "answer_sql": stress_by_id[sid].get("answer_sql"),
                "elapsed_s": stress_by_id[sid].get("elapsed_s"),
                "validation": stress_by_id[sid].get("validation"),
            }

    for name in ("comprehensive_ar_105_results.json", "adhoc_ar_105_results.json", "report_alias_ar_105_results.json"):
        path = EVALS / name
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for r in data.get("results", data if isinstance(data, list) else []):
            rid = r.get("id")
            for c in cases:
                if c.get("source_id") == rid and name.startswith(c.get("source_file", "").replace(".jsonl", "")):
                    c.setdefault("last_run", {})
                    c["last_run"].update({
                        "verdict": r.get("verdict"),
                        "answer_excerpt": (r.get("answer") or "")[:500],
                        "answer_sql": r.get("answer_sql"),
                        "elapsed_s": r.get("elapsed_s"),
                    })


def _load_qa_adversarial() -> list[dict]:
    if not QA_RESULTS.exists():
        return []
    rows = json.loads(QA_RESULTS.read_text(encoding="utf-8"))
    out = []
    for r in rows:
        out.append({
            "uid": f"qa-adversarial:{r.get('id')}",
            "kind": "qa_session",
            "source_file": ".gstack/qa-reports/adversarial-results.json",
            "source_id": r.get("id"),
            "client": "105",
            "company_id": 2,
            "lang": "ar",
            "category": r.get("trap"),
            "question": r.get("question"),
            "question_hash": _norm_q(r.get("question", "")),
            "elapsed_s": r.get("elapsed_s"),
            "verdict_auto": r.get("verdict"),
            "verdict_reasons": r.get("reasons"),
            "answer": r.get("answer"),
            "answer_sql": r.get("answer_sql"),
            "sources": r.get("sources"),
            "note": r.get("note"),
        })
    return out


def main() -> None:
    cases: list[dict] = []
    source_counts: dict[str, int] = {}

    for filename, _mode, defaults in QUESTION_CORPORA:
        rows = _load_jsonl(EVALS / filename)
        n = 0
        for i, row in enumerate(rows):
            norm = _normalize_row(row, filename, defaults, i)
            if norm is None:
                continue
            if isinstance(norm, dict):
                cases.append(norm)
                n += 1
        source_counts[filename] = n

    cases.extend(_load_qa_adversarial())
    source_counts["qa-adversarial"] = len(_load_qa_adversarial())

    _attach_results(cases)

    # dedup index by question hash (single-turn only)
    hash_map: dict[str, list[str]] = {}
    for c in cases:
        if c.get("kind") == "question" and c.get("question_hash"):
            hash_map.setdefault(c["question_hash"], []).append(c["uid"])
    duplicates = {h: uids for h, uids in hash_map.items() if len(uids) > 1}

    by_kind: dict[str, int] = {}
    for c in cases:
        by_kind[c.get("kind", "unknown")] = by_kind.get(c.get("kind", "unknown"), 0) + 1

    payload = {
        "meta": {
            "generated_at": datetime.now(UTC).isoformat(),
            "repo": str(ROOT),
            "description": "Unified test-question corpus: eval JSONL files + QA adversarial session",
            "ground_truth_markdown": str(GROUND_TRUTH_MD.relative_to(ROOT)) if GROUND_TRUTH_MD.exists() else None,
            "source_files": list(source_counts.keys()),
            "counts_by_source": source_counts,
            "counts_by_kind": by_kind,
            "total_cases": len(cases),
            "unique_question_hashes": len(hash_map),
            "duplicate_question_groups": len(duplicates),
            "notes": [
                "comprehensive_ar_105_wave2.jsonl is a subset duplicate of q51-q69 in comprehensive_ar_105.jsonl",
                "stress70.jsonl includes multi_turn chains (E01-E05) and single questions",
                "isolation.jsonl entries are SQL/gate attacks, not NL questions",
                "qa_session entries from 2026-08-24 adversarial run include live answers",
            ],
        },
        "duplicate_index": duplicates,
        "cases": cases,
    }

    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "out": str(OUT),
        "total": len(cases),
        "by_kind": by_kind,
        "duplicate_groups": len(duplicates),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
