"""In-process vault access for schema notes, joins, and procedure metadata.
Extracted from obsidian-mcp-server.py — no stdio MCP per chat turn.
Procedure bodies are NEVER returned to the model or user."""
import json
import os
import re
import sqlite3
from pathlib import Path

import yaml

from . import config

BASE_DIR = Path(__file__).resolve().parent.parent
VAULT = BASE_DIR / "obsidian" / "olives"
GRAPH_PATH = BASE_DIR / "db" / "vault_graph.json"

_PROC_BODY_MARKERS = re.compile(
    r"(CREATE\s+PROCEDURE|ALTER\s+PROCEDURE|CREATE\s+PROC\b|##\s*Procedure\s+Body)",
    re.IGNORECASE,
)
_ALLOWED_PROC_SECTIONS = (
    "Purpose", "Parameters", "Tables Read", "Tables Written",
    "When to Run This", "When to Run", "Related", "Impact / Dependencies",
)


def _split_flow(s):
    items, depth, cur = [], 0, ""
    for ch in s:
        if ch == "[":
            depth += 1
            cur += ch
        elif ch == "]":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            items.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        items.append(cur.strip())
    return items


def _parse_yaml_block(block):
    lines = block.split("\n")
    result = {}
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        mm = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not mm:
            i += 1
            continue
        key, val = mm.group(1), mm.group(2).strip()
        if val == "":
            j = i + 1
            items = []
            while j < n and re.match(r"^\s*-\s*(.*)$", lines[j]):
                items.append(re.match(r"^\s*-\s*(.*)$", lines[j]).group(1).strip())
                j += 1
            result[key] = items if items else ""
            i = j
        elif val.startswith("["):
            buf, j = val, i
            while not buf.rstrip().endswith("]") and j + 1 < n:
                j += 1
                buf += " " + lines[j].strip()
            inner = buf.strip()[1:-1] if buf.strip().endswith("]") else buf.strip()[1:]
            result[key] = _split_flow(inner)
            i = j + 1
        else:
            result[key] = val
            i += 1
    return result


def parse_frontmatter(content: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    try:
        data = yaml.safe_load(block)
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    try:
        data = _parse_yaml_block(block)
        if data:
            return data
    except Exception:
        pass
    fm = {}
    for line in block.split("\n"):
        mm = re.match(r"^(\w+):\s*(.*)", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm


def _build_index():
    notes = []
    for root, _dirs, files in os.walk(VAULT):
        if ".obsidian" in root:
            continue
        for fname in files:
            if not fname.endswith(".md"):
                continue
            path = os.path.join(root, fname)
            rel = os.path.relpath(path, VAULT)
            parts = rel.split(os.sep)
            db_dir = parts[0] if len(parts) > 1 else "Shared"
            subdir = parts[1] if len(parts) > 2 else ""
            notes.append({"path": path, "rel": rel, "db": db_dir, "subdir": subdir, "fname": fname})
    return notes


NOTES_INDEX = _build_index()


def _load_graph():
    try:
        with open(GRAPH_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"tables": {}, "procedures": {}}


VAULT_GRAPH = _load_graph()


def _norm_value(v):
    v = str(v).strip()
    if v.startswith("[["):
        v = v[2:]
    if v.endswith("]]"):
        v = v[:-2]
    return v.split("|")[0].strip().lower()


def extract_section(content: str, section_names):
    names = section_names if isinstance(section_names, (list, tuple)) else [section_names]
    for sn in names:
        pattern = rf"## {re.escape(sn)}\s*\n(.*?)(?=\n## |\Z)"
        m = re.search(pattern, content, re.DOTALL)
        if m:
            return m.group(1).strip(), sn
    return "", None


def _sanitize_procedure_content(content: str, fm: dict) -> dict:
    """Return metadata-only card for a procedure — never the body."""
    if _PROC_BODY_MARKERS.search(content):
        pass  # expected for many notes; we strip by section extraction
    sections = {}
    for section in _ALLOWED_PROC_SECTIONS:
        body, matched = extract_section(content, section)
        if body and not _PROC_BODY_MARKERS.search(body):
            sections[matched or section] = body
    meta = {k: fm.get(k) for k in (
        "name", "type", "database", "tags", "reads_from", "writes_to",
        "called_by", "support_relevance", "parameters",
    ) if fm.get(k) is not None}
    return {
        "kind": "procedure",
        "metadata": meta,
        "sections": sections,
        "note": "Procedure body omitted — metadata only.",
    }


def _is_procedure_note(fm: dict, subdir: str) -> bool:
    note_type = str(fm.get("type", "")).lower()
    if note_type == "procedure":
        return True
    return subdir.lower() == "procedures"


def sanitize_note_content(content: str, fm: dict, subdir: str) -> dict | str:
    if _is_procedure_note(fm, subdir):
        if _PROC_BODY_MARKERS.search(content):
            return _sanitize_procedure_content(content, fm)
        return _sanitize_procedure_content(content, fm)
    return content


def search_schema_notes(
    pattern: str,
    database: str = "Olives_BO",
    type_filter: str | None = None,
    limit: int = 20,
) -> list:
    try:
        rx = re.compile(pattern, re.IGNORECASE)
    except re.error as e:
        return [{"error": f"Invalid regex: {e}"}]
    results = []
    for n in NOTES_INDEX:
        if database and n["db"] != database:
            continue
        try:
            with open(n["path"], "r", encoding="utf-8") as f:
                content = f.read()
        except OSError:
            continue
        fm = parse_frontmatter(content)
        note_type = fm.get("type", "")
        if type_filter and note_type.lower() != type_filter.lower():
            continue
        if n["subdir"] in ("Tables", "Procedures", "Relations") or note_type in ("table", "procedure", "relation"):
            if not rx.search(content):
                continue
            excerpt = content[max(0, rx.search(content).start() - 60):rx.search(content).start() + 80].replace("\n", " ")
            results.append({
                "path": n["rel"],
                "name": fm.get("name", n["fname"].replace(".md", "")),
                "type": note_type or n["subdir"].lower(),
                "database": n["db"],
                "excerpt": excerpt.strip(),
            })
        if len(results) >= limit:
            break
    return results


def read_schema_note(
    name: str | None = None,
    path: str | None = None,
    database: str | None = None,
    type_filter: str | None = None,
) -> dict:
    if path:
        cand = VAULT / path
        if not cand.exists() and not path.endswith(".md"):
            cand = VAULT / (path + ".md")
        if not cand.exists():
            return {"error": f"Note at path '{path}' not found."}
        with open(cand, "r", encoding="utf-8") as f:
            content = f.read()
        rel = os.path.relpath(cand, VAULT)
        parts = rel.split(os.sep)
        subdir = parts[1] if len(parts) > 2 else ""
        fm = parse_frontmatter(content)
        sanitized = sanitize_note_content(content, fm, subdir)
        return {"path": rel, "name": fm.get("name", cand.stem), "content": sanitized}
    target = (name or "").upper()
    for n in NOTES_INDEX:
        try:
            with open(n["path"], "r", encoding="utf-8") as f:
                content = f.read()
        except OSError:
            continue
        fm = parse_frontmatter(content)
        fm_name = str(fm.get("name", n["fname"].replace(".md", "")))
        if fm_name.upper() != target:
            continue
        if database and n["db"].upper() != database.upper():
            continue
        if type_filter and str(fm.get("type", "")).lower() != type_filter.lower():
            continue
        sanitized = sanitize_note_content(content, fm, n["subdir"])
        return {"path": n["rel"], "name": fm_name, "content": sanitized}
    return {"error": f"Note '{name}' not found."}


def _wiki_name(raw: str) -> str:
    return _norm_value(raw).split("/")[-1]


def get_joins(table_name: str, database: str = "Olives_BO") -> dict:
    target = table_name.upper()
    relations = []
    for n in NOTES_INDEX:
        if n["db"] != database or n["subdir"] != "Relations":
            continue
        try:
            with open(n["path"], "r", encoding="utf-8") as f:
                content = f.read()
        except OSError:
            continue
        fm = parse_frontmatter(content)
        parent = _wiki_name(fm.get("parent_table", ""))
        ref = _wiki_name(fm.get("referenced_table", ""))
        note_name = str(fm.get("name", n["fname"].replace(".md", "")))
        if target not in (parent.upper(), ref.upper(), note_name.upper().split("--")[0], note_name.upper().split("--")[-1]):
            if target not in content.upper():
                continue
        body, _ = extract_section(content, ["Business meaning", "FK"])
        relations.append({
            "name": note_name,
            "path": n["rel"],
            "parent_table": fm.get("parent_table"),
            "referenced_table": fm.get("referenced_table"),
            "columns": fm.get("columns"),
            "summary": body[:500] if body else None,
        })
    graph_matches = []
    for key, entry in VAULT_GRAPH.get("tables", {}).items():
        if entry.get("name", "").upper() == target:
            if database and entry.get("database", "").upper() != database.upper():
                continue
            graph_matches.append({
                "graph_key": key,
                "reads_by_procs": entry.get("reads_by", [])[:20],
                "writes_by_procs": entry.get("writes_by", [])[:20],
            })
    return {"table": table_name, "database": database, "relations": relations, "graph": graph_matches}


# Wave 6 — compiled vault cards (setup/compile_vault_cards.py)
_TOKEN_RE = re.compile(r"[a-zA-Z\u0600-\u06FF]{2,}")

ARABIC_ALIASES = {
    "مبيعات": ["TransactionsHeaders"],
    "مرتجعات": ["TransactionsHeaders"],
    "تحصيل": ["Receipts"],
    "طلبات": ["OrdersHeaders"],
    "رصيد السيارة": ["SalesPersonItemsBalance"],
    "عملاء المندوب": ["CustomersFinancialDetails", "Positions", "SalesPersons", "Customers"],
    "عملاء كل مندوب": ["CustomersFinancialDetails", "Positions", "SalesPersons", "Customers"],
}

PLAYBOOK_OVERRIDES = {
    "Customers--SalesPersons": {
        "override": "playbook",
        "reason": (
            "Territory / عملاء مندوب: join Customers → CustomersFinancialDetails → Positions "
            "→ SalesPersons via PositionsID → PositionID — not Customers.SalesPersonID alone."
        ),
        "boost_tables": ["CustomersFinancialDetails", "Positions", "SalesPersons", "Customers"],
    },
}

_TERRITORY_HINTS = re.compile(
    r"مندوب|عملاء|territory|salesperson\s+assign|customers?\s+per\s+sales",
    re.IGNORECASE,
)


def cards_db_path(client: str) -> Path:
    return config.work_dir(client) / "vault_cards.sqlite"


def _load_cards(client: str) -> list[dict]:
    path = cards_db_path(client)
    if not path.exists():
        return []
    conn = sqlite3.connect(path)
    try:
        rows = conn.execute("SELECT card_json FROM cards").fetchall()
    finally:
        conn.close()
    return [json.loads(r[0]) for r in rows]


def _tokens(text: str) -> set[str]:
    return {t.lower() for t in _TOKEN_RE.findall(text)}


def _alias_hits(question: str) -> list[str]:
    tables: list[str] = []
    for alias, targets in ARABIC_ALIASES.items():
        if alias in question:
            tables.extend(targets)
    return tables


def _format_table_card(card: dict) -> str:
    lines = [f"Table {card['name']}"]
    if card.get("tags"):
        lines.append(f"  tags: {', '.join(card['tags'])}")
    if card.get("purpose"):
        lines.append(f"  purpose: {card['purpose'][:300]}")
    if card.get("primary_key"):
        lines.append(f"  PK: {card['primary_key'][:200]}")
    if card.get("foreign_keys"):
        lines.append(f"  FK: {card['foreign_keys'][:300]}")
    if card.get("common_issues"):
        lines.append(f"  issues: {card['common_issues'][:200]}")
    return "\n".join(lines)


def _format_relation_card(card: dict, question: str) -> str:
    lines = [
        f"Relation {card['name']}: {card.get('parent')} → {card.get('referenced')}",
        f"  columns: {card.get('columns', '')}",
    ]
    if card.get("business_meaning"):
        lines.append(f"  meaning: {card['business_meaning'][:250]}")
    override = PLAYBOOK_OVERRIDES.get(card.get("name", ""))
    if override and _TERRITORY_HINTS.search(question):
        lines.append(f"  override: {override['override']} — {override['reason']}")
    return "\n".join(lines)


def retrieve_cards(question: str, client: str, limit: int = 3) -> list[dict]:
    """Token/alias overlap against compiled vault cards; attach related relations."""
    all_cards = _load_cards(client)
    if not all_cards:
        return []

    table_cards = [c for c in all_cards if c["kind"] == "table"]
    relation_cards = [c for c in all_cards if c["kind"] == "relation"]
    q_tokens = _tokens(question)
    alias_tables = {t.lower() for t in _alias_hits(question)}

    scored: list[tuple[int, dict]] = []
    for card in table_cards:
        blob = _tokens(card.get("name", "") + " " + _search_blob(card))
        overlap = len(q_tokens & blob)
        if card["name"].lower() in alias_tables:
            overlap += 5
        if overlap:
            scored.append((overlap, card))
    scored.sort(key=lambda x: (-x[0], x[1].get("name", "")))

    # Territory questions: boost playbook tables even if token overlap is weak
    if _TERRITORY_HINTS.search(question):
        boost = PLAYBOOK_OVERRIDES["Customers--SalesPersons"]["boost_tables"]
        picked_names = {c["name"] for _, c in scored[:limit]}
        for name in boost:
            if name not in picked_names:
                for card in table_cards:
                    if card["name"] == name:
                        scored.append((3, card))
                        break

    seen: set[str] = set()
    top_tables: list[dict] = []
    for _, card in sorted(scored, key=lambda x: (-x[0], x[1].get("name", ""))):
        if card["name"] in seen:
            continue
        seen.add(card["name"])
        top_tables.append(card)
        if len(top_tables) >= limit:
            break

    table_names = {c["name"] for c in top_tables}
    related: list[dict] = []
    for rel in relation_cards:
        if rel.get("parent") in table_names or rel.get("referenced") in table_names:
            related.append(rel)
        elif rel.get("name") == "Customers--SalesPersons" and _TERRITORY_HINTS.search(question):
            related.append(rel)

    return top_tables + related


def _search_blob(card: dict) -> str:
    if card["kind"] == "table":
        return " ".join(str(card.get(k, "")) for k in (
            "purpose", "primary_key", "foreign_keys", "common_issues", "tags"
        ))
    return " ".join(str(card.get(k, "")) for k in (
        "parent", "referenced", "columns", "business_meaning"
    ))


def format_retrieved_cards(question: str, cards: list[dict]) -> str:
    """Render retrieved cards for system-message injection."""
    if not cards:
        return ""
    lines = ["# Wave 6 vault cards", "Compiled schema memory (playbook overrides dirty FKs):"]
    for card in cards:
        if card["kind"] == "table":
            lines.append(_format_table_card(card))
        elif card["kind"] == "relation":
            lines.append(_format_relation_card(card, question))
    return "\n".join(lines)
