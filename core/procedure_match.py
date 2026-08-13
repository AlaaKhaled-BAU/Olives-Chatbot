"""Match user question to entitled procedures by keyword intent.
No embeddings, no new dependencies — pure TF-IDF-style word overlap
over heuristic descriptions derived from procedure names + params.

Golden rule 5: never reads proc bodies. Only uses name and params
(the same data catalog.py already exposes)."""

import math
import re
from collections import Counter

_SEGMENT_RE = re.compile(r"[^a-zA-Z0-9]+")
_CAMEL_RE = re.compile(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")

_STOP_WORDS = {
    "get", "set", "by", "from", "to", "with", "and", "for", "in", "on", "at",
    "of", "the", "a", "an", "is", "are", "was", "were", "has", "have", "had",
    "do", "does", "did", "not", "no", "or", "but", "if", "as", "per", "via",
    "into", "through", "during", "after", "before", "between", "over", "under",
    "all", "any", "each", "every", "some", "many", "much", "more", "most",
    "list", "show", "find", "search", "select", "fetch", "return", "update",
    "insert", "delete", "create", "drop", "alter", "add", "remove",
    "dbo", "proc", "sp",
}


def _tokenize(text: str) -> list[str]:
    """Split text into lowercase keyword tokens."""
    parts = _SEGMENT_RE.split(text)
    tokens = []
    for part in parts:
        sub = _CAMEL_RE.split(part)
        for s in sub:
            s = s.strip().lower()
            if s and len(s) > 1:
                tokens.append(s)
    return tokens


def _build_description(proc_name: str, params: list[dict]) -> str:
    """Generate a searchable text description from a procedure name + params.
    Never touches proc bodies (golden rule 5)."""
    tokens = _tokenize(proc_name.split(".")[-1])  # bare name only, no schema
    desc = " ".join(t for t in tokens if t not in _STOP_WORDS)
    if params:
        param_names = [p["param"].lstrip("@").lower() for p in params if not p.get("output")]
        param_keywords = " ".join(_tokenize(n) for n in param_names if n not in _STOP_WORDS)
        desc = f"{desc} {' '.join(param_keywords)}"
    return desc


def _build_index(procs: dict[str, list[dict]]) -> dict:
    """Build {proc_name: description} for all entitled procedures."""
    return {name: _build_description(name, params) for name, params in procs.items()}


def _compute_idf(descriptions: dict[str, str]) -> dict[str, float]:
    """Compute inverse document frequency for each keyword across all procs."""
    doc_count = len(descriptions)
    df: Counter = Counter()
    for desc in descriptions.values():
        words = set(desc.split())
        df.update(words)
    return {
        word: math.log((doc_count + 1) / (freq + 1)) + 1
        for word, freq in df.items()
    }


def _score_question(question_tokens: list[str], proc_tokens: set[str], idf: dict[str, float]) -> float:
    """TF-IDF-style relevance score: sum IDF of matched question keywords."""
    score = 0.0
    for qt in question_tokens:
        if qt in proc_tokens:
            score += idf.get(qt, 1.0)
    return score


def find_candidates(
    question: str,
    procs: dict[str, list[dict]],
    top_k: int = 5,
) -> list[dict]:
    """Return top-K procedures that best match the user's question intent.

    Returns list of dicts:
        {name, params, description, score}
    Sorted by descending score. Empty list if no match above threshold.
    """
    descriptions = _build_index(procs)
    if not descriptions:
        return []

    idf = _compute_idf(descriptions)

    question_tokens = [t for t in _tokenize(question) if t not in _STOP_WORDS]
    if not question_tokens:
        return []

    scored = []
    for name, desc in descriptions.items():
        proc_tokens = set(desc.split())
        score = _score_question(question_tokens, proc_tokens, idf)
        if score > 0:
            scored.append({
                "name": name,
                "params": procs[name],
                "description": desc,
                "score": round(score, 2),
            })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]


def format_candidates(candidates: list[dict]) -> str:
    """Format matched procedures as readable context for the system prompt."""
    if not candidates:
        return ""
    lines = ["## Suggested procedures matching this question"]
    for i, c in enumerate(candidates, 1):
        parts = [c["name"]]
        if c["params"]:
            sig = ", ".join(f"@{p['param']} {p['type']}" for p in c["params"])
            parts.append(f"({sig})")
        lines.append(f"{i}. {' '.join(parts)}")
    lines.append("Only use these if exactly relevant — otherwise generate SELECT as normal.\n")
    return "\n".join(lines)