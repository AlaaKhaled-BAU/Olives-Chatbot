"""Post-processing module for client chatbot.

Extracts, hardens, and standardizes post-processing utilities:
- Clean Modern Standard Arabic (MSA) follow-up suggestions
- Context capping and formatting stubs
- SQL fence stripping and count backstops
- Table and chart builders
- Evidence confidence and source citations
- Delimited follow-ups parser
"""

from __future__ import annotations

import json
import re
from typing import Any

try:
    from . import locale_ar
except ImportError:
    from core import locale_ar

# 1. Clean Modern Standard Arabic follow-ups (NO colloquial Gulf words like "وش")
DEFAULT_FOLLOWUPS: list[str] = [
    "توزيع هذا الرقم حسب المندوبين",
    "المقارنة مع الفترة السابقة",
    "ما أكثر الأصناف المساهمة في هذا الرقم؟",
]

# 2. Constants and Regexes
UNRESOLVED_TOKEN_RE = re.compile(r"<[a-z_][a-z_0-9]{3,}>", re.IGNORECASE)
SOURCE_TABLE_RE = re.compile(r"\bt\.(\w+)", re.IGNORECASE)
TIME_LIKE_COLUMN_RE = re.compile(r"month|date|day|year|week", re.IGNORECASE)
ROW_DISPLAY_CAP: int = 50
TABLE_ROW_CAP: int = 100

_INVOICE_WORD_RE = re.compile(r"فاتور|فواتير|invoice", re.IGNORECASE)
_LINES_WORD_RE = re.compile(r"بنود|سطور|\blines\b", re.IGNORECASE)
_CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_FENCE_OPEN_RE = re.compile(r"```(\w*)\s*\n")
_SQL_LEAD_RE = re.compile(
    r"^\s*(?:--[^\n]*\n\s*)*(?:SELECT|WITH)\b",
    re.IGNORECASE | re.DOTALL,
)
_NON_SQL_FENCE_LANGS = frozenset({"python", "json", "yaml", "yml", "md", "markdown", "text"})

FOLLOWUPS_DELIMITER_RE = re.compile(r"---+\s*FOLLOWUPS\s*---+", re.IGNORECASE)
BULLET_PREFIX_RE = re.compile(r"^\s*(?:[-*•–—]|\(?\d+[\.\)\-:]|\(\d+\))\s*(.+)$")


# 3. Context capping, blank checking, and stub formatting
def cap_for_context(result: Any) -> Any:
    """Caps result rows for model context to ROW_DISPLAY_CAP (50).

    result is whatever sql.run_select() returned -- a list of row dicts
    (or occasionally a non-list for an edge-case query shape; passed
    through unchanged if so, nothing to cap).
    """
    if not isinstance(result, list) or len(result) <= ROW_DISPLAY_CAP:
        return result
    return {
        "rows": result[:ROW_DISPLAY_CAP],
        "shown": ROW_DISPLAY_CAP,
        "total_rows_returned": len(result),
        "note": (
            f"Only the first {ROW_DISPLAY_CAP} of {len(result)} returned rows are shown "
            f"above. Never infer a count/sum/average from this partial list -- if you need "
            f"one, write a dedicated aggregate query (COUNT/SUM/AVG) instead."
        ),
    }


def is_blank(text: str | None) -> bool:
    """Returns True if text is None, empty, or whitespace-only."""
    return not text or not str(text).strip()


def format_stub_number(val: Any) -> str:
    """Formats a number for Arabic stubs, displaying whole floats without trailing zeros."""
    if isinstance(val, float) and val == int(val):
        return str(int(val))
    return str(val)


def build_arabic_stub(state: dict) -> str:
    """Deterministic Arabic fallback when the model returns empty after tools."""
    rows = state.get("last_rows")
    if isinstance(rows, list) and rows:
        row = rows[0]
        if len(rows) == 1:
            if len(row) == 1:
                val = next(iter(row.values()))
                if isinstance(val, (int, float)) and not isinstance(val, bool):
                    return f"النتيجة: {format_stub_number(val)}."
            nums = [
                (k, v)
                for k, v in row.items()
                if isinstance(v, (int, float)) and not isinstance(v, bool)
            ]
            if nums:
                parts = [f"{k}: {format_stub_number(v)}" for k, v in nums[:3]]
                return "النتيجة: " + "، ".join(parts) + "."
        return "النتيجة في الجدول أدناه."
    if state.get("doc_source_pairs"):
        return "الإجابة في المصادر أدناه."
    return "تعذر صياغة الإجابة من البيانات المتاحة."


# 4. SQL fence detection and count backstops
def fence_body_looks_like_sql(body: str) -> bool:
    """Checks whether code block body looks like SQL."""
    raw = body.strip()
    if not raw:
        return False
    if _SQL_LEAD_RE.match(raw):
        return True
    try:
        import sqlglot
        from sqlglot import exp

        for stmt in sqlglot.parse(raw, read="tsql") or []:
            if stmt is None or isinstance(stmt, exp.Command):
                continue
            if isinstance(stmt, exp.Select) or stmt.find(exp.Select):
                return True
    except Exception:
        pass
    return False


def strip_sql_fences(text: str | None) -> str | None:
    """Remove SQL code fences from model prose; answer_sql is shown separately."""
    if not text:
        return text
    parts: list[str] = []
    pos = 0
    while True:
        m = _FENCE_OPEN_RE.search(text, pos)
        if not m:
            parts.append(text[pos:])
            break
        parts.append(text[pos : m.start()])
        lang = (m.group(1) or "").lower()
        body_start = m.end()
        close = text.find("```", body_start)
        if close == -1:
            body = text[body_start:]
            fence_end = len(text)
        else:
            body = text[body_start:close]
            fence_end = close + 3
        strip_fence = lang in ("sql", "tsql") or (
            lang not in _NON_SQL_FENCE_LANGS and fence_body_looks_like_sql(body)
        )
        if strip_fence:
            parts.append("\n\n")
        else:
            parts.append(text[m.start() : fence_end])
        pos = fence_end
    out = re.sub(r"\n{3,}", "\n\n", "".join(parts))
    return out.strip()


def prose_mentions_count(prose: str, v: int) -> bool:
    """Checks if integer v (formatted or unformatted) is mentioned in prose."""
    return bool(
        re.search(rf"(?<![\d.,]){re.escape(f'{v:,}')}(?![\d]|[.,]\d)", prose)
        or re.search(rf"(?<![\d.,]){v}(?![\d]|[.,]\d)", prose)
    )


def apply_count_backstop(final_text: str | None, state: dict) -> str:
    """Append header recount or line-grain warning when prose treats lines as invoices."""
    text = (final_text or "").strip()
    if not text or not state.get("had_lines_count"):
        return text
    prose = _CODE_FENCE_RE.sub("", text)
    if _LINES_WORD_RE.search(prose):
        return text
    if not _INVOICE_WORD_RE.search(prose):
        return text
    line_values = state.get("line_count_values")
    line_sum = state.get("line_count_sum")
    # Ignore 1–9: they collide with type ids, dates, and one-line invoices.
    # The summed total is the number a wrong answer states as «فواتير».
    candidates: set[int] = set()
    if line_sum is not None and int(line_sum) >= 3:
        candidates.add(int(line_sum))
    for v in line_values or ():
        if int(v) >= 10:
            candidates.add(int(v))
    hc_now = state.get("header_count")
    if hc_now is not None:
        candidates.discard(int(hc_now))
    quoted = any(prose_mentions_count(prose, v) for v in candidates)
    if (
        line_values is not None
        and not state.get("line_count_unresolved")
        and not quoted
    ):
        return text
    hc = state.get("header_count")
    if hc is not None:
        suffix = locale_ar.HEADER_COUNT_SUFFIX.format(n=hc)
        if suffix not in text:
            return f"{text}\n{suffix}"
    elif locale_ar.COUNT_NOTE_USER not in text:
        return f"{text}\n{locale_ar.COUNT_NOTE_USER}"
    return text


# 5. Table, chart, sources, and evidence confidence
def build_table(rows: list | None) -> dict | None:
    """Builds {columns, rows} from query results, capped at TABLE_ROW_CAP."""
    if not rows or (len(rows) == 1 and len(rows[0]) <= 1):
        return None
    columns = list(rows[0].keys())
    return {
        "columns": columns,
        "rows": [[row.get(c) for c in columns] for row in rows[:TABLE_ROW_CAP]],
    }


def build_chart(table: dict | None) -> dict | None:
    """Heuristic chart builder: offers a chart for 1 label + 1 numeric column with 2-20 rows."""
    if not table or len(table["columns"]) != 2 or not (1 < len(table["rows"]) <= 20):
        return None
    label, value = table["rows"][0]
    if not (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and not isinstance(label, (int, float))
    ):
        return None
    kind = "line" if TIME_LIKE_COLUMN_RE.search(table["columns"][0]) else "bar"
    return {"kind": kind, "x": table["columns"][0], "y": table["columns"][1]}


def format_doc_sources(doc_source_pairs: list[tuple[str, str]]) -> list[str]:
    """Formats (source, heading) pairs into human-readable citations."""
    formatted = []
    for source, heading in doc_source_pairs:
        formatted.append(f"{source} › {heading}" if heading else source)
    return formatted


def build_sources(queries: list, doc_source_pairs: list[tuple[str, str]]) -> list:
    """Builds sources list combining SQL table names and doc search citations."""
    tables = sorted(set(m.group(1) for q in queries for m in SOURCE_TABLE_RE.finditer(q)))
    return tables + format_doc_sources(doc_source_pairs)


def answer_sql(state: dict) -> str | None:
    """Extracts executed SQL queries from state joined by semicolons."""
    parts = list(state.get("queries") or []) + list(state.get("hot_sql") or [])
    return "; ".join(parts) if parts else None


def evidence_confidence(state: dict) -> str:
    """Determines confidence level ('high', 'medium', 'low') based on executed evidence."""
    if state.get("tool_errors"):
        return "medium"
    if isinstance(state.get("last_rows"), list) and state["last_rows"]:
        return "high"
    return "medium" if state.get("doc_source_pairs") else "low"


# 6. Delimited follow-ups parsing
def parse_delimited_followups(text: str | None) -> tuple[str, list[str]]:
    """Supports optional trailing block delimited by `---FOLLOWUPS---`.

    The block can be either:
    1. A JSON array of question strings (optionally enclosed in code fences).
    2. Bulleted or numbered lines (-, *, •, 1., 1), etc.).

    Returns:
        (clean_prose, followups)
        followups contains up to 3 items, each capped at 120 characters.
        If no delimiter is present, returns (text or "", []).
    """
    if not text:
        return ("", [])

    m = FOLLOWUPS_DELIMITER_RE.search(text)
    if not m:
        return (text, [])

    clean_prose = text[: m.start()].strip()
    block = text[m.end() :].strip()
    if not block:
        return (clean_prose, [])

    # Try JSON array first
    json_candidate = block
    if json_candidate.startswith("```"):
        lines = json_candidate.splitlines()
        if len(lines) >= 2 and lines[-1].strip() == "```":
            json_candidate = "\n".join(lines[1:-1]).strip()
        else:
            json_candidate = re.sub(r"^```[a-zA-Z]*\n?|```$", "", json_candidate).strip()

    try:
        parsed = json.loads(json_candidate)
        if isinstance(parsed, dict) and "followups" in parsed and isinstance(parsed["followups"], list):
            parsed = parsed["followups"]
        if isinstance(parsed, list):
            followups = [str(x).strip()[:120] for x in parsed if str(x).strip()]
            return (clean_prose, followups[:3])
    except Exception:
        pass

    # Try bulleted or numbered lines
    items: list[str] = []
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("```"):
            continue
        bm = BULLET_PREFIX_RE.match(line)
        if bm:
            cleaned = bm.group(1).strip().strip('"\'')
            if cleaned:
                items.append(cleaned[:120])

    if items:
        return (clean_prose, items[:3])

    # Malformed block fallback
    return (clean_prose, [])


# Aliases for backward compatibility
_DEFAULT_FOLLOWUPS = DEFAULT_FOLLOWUPS
_UNRESOLVED_TOKEN_RE = UNRESOLVED_TOKEN_RE
_SOURCE_TABLE_RE = SOURCE_TABLE_RE
_TIME_LIKE_COLUMN_RE = TIME_LIKE_COLUMN_RE
_ROW_DISPLAY_CAP = ROW_DISPLAY_CAP
_TABLE_ROW_CAP = TABLE_ROW_CAP
_cap_for_context = cap_for_context
_is_blank = is_blank
_format_stub_number = format_stub_number
_build_arabic_stub = build_arabic_stub
_fence_body_looks_like_sql = fence_body_looks_like_sql
_strip_sql_fences = strip_sql_fences
_prose_mentions_count = prose_mentions_count
_apply_count_backstop = apply_count_backstop
_build_table = build_table
_build_chart = build_chart
_format_doc_sources = format_doc_sources
_build_sources = build_sources
_answer_sql = answer_sql
_evidence_confidence = evidence_confidence


__all__ = [
    "DEFAULT_FOLLOWUPS",
    "UNRESOLVED_TOKEN_RE",
    "SOURCE_TABLE_RE",
    "TIME_LIKE_COLUMN_RE",
    "ROW_DISPLAY_CAP",
    "TABLE_ROW_CAP",
    "cap_for_context",
    "is_blank",
    "format_stub_number",
    "build_arabic_stub",
    "fence_body_looks_like_sql",
    "strip_sql_fences",
    "prose_mentions_count",
    "apply_count_backstop",
    "build_table",
    "build_chart",
    "format_doc_sources",
    "build_sources",
    "answer_sql",
    "evidence_confidence",
    "parse_delimited_followups",
]
