#!/usr/bin/env python3.13
"""Compile vault table/relation notes into small schema cards (Wave 6).

Walks obsidian/olives/Olives_BO/Tables and Relations — never procedure bodies
or Impact/Procedures lists. Output: work/<client>/vault_cards.sqlite
"""
import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import config, vault  # noqa: E402

VAULT_BO = BASE_DIR / "obsidian" / "olives" / "Olives_BO"
_SKIP_SECTIONS = frozenset({
    "Impact / Procedures Using This Table",
    "Impact / Dependencies",
    "Impact / Procedures",
    "Estimated Size / Volatility",
    "Related",
    "Columns",
    "Known Circular Dependencies",
})

_ARABIC_ALIASES = {
    "مبيعات": "TransactionsHeaders",
    "مرتجعات": "returns",
    "تحصيل": "Receipts",
    "طلبات": "OrdersHeaders",
    "رصيد السيارة": "SalesPersonItemsBalance",
    "عملاء المندوب": "CustomersFinancialDetails",
    "عملاء كل مندوب": "CustomersFinancialDetails",
}


def _section_until_next(content: str, section_names) -> str:
    body, _ = vault.extract_section(content, section_names)
    if not body:
        return ""
    # Stop at any skipped / heavy section that may have leaked in
    for skip in _SKIP_SECTIONS:
        marker = f"\n## {skip}"
        idx = body.find(marker)
        if idx != -1:
            body = body[:idx]
    if "Reads (" in body:
        body = body[: body.index("Reads (")]
    return body.strip()


def _compile_table(path: Path) -> dict | None:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return None
    fm = vault.parse_frontmatter(content)
    name = str(fm.get("name", path.stem))
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    purpose = _section_until_next(content, "Business Purpose")
    pk = _section_until_next(content, "Primary Key")
    fks = _section_until_next(content, "Foreign Keys")
    issues = _section_until_next(content, "Common Issues")
    return {
        "kind": "table",
        "name": name,
        "tags": tags,
        "purpose": purpose[:800] if purpose else "",
        "primary_key": pk[:400] if pk else "",
        "foreign_keys": fks[:600] if fks else "",
        "common_issues": issues[:500] if issues else "",
    }


def _wiki_field(raw) -> str:
    if isinstance(raw, list):
        raw = raw[0] if raw else ""
    return vault._wiki_name(str(raw))


def _compile_relation(path: Path) -> dict | None:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return None
    fm = vault.parse_frontmatter(content)
    meaning, _ = vault.extract_section(content, ["Business meaning", "Business Meaning"])
    parent = _wiki_field(fm.get("parent_table", ""))
    ref = _wiki_field(fm.get("referenced_table", ""))
    return {
        "kind": "relation",
        "name": str(fm.get("name", path.stem)),
        "parent": parent,
        "referenced": ref,
        "columns": str(fm.get("columns", ""))[:300],
        "business_meaning": (meaning or "")[:500],
        "support_relevance": str(fm.get("support_relevance", "")),
    }


def _search_text(card: dict) -> str:
    parts = [card.get("name", "")]
    if card["kind"] == "table":
        parts.extend([
            " ".join(card.get("tags") or []),
            card.get("purpose", ""),
            card.get("primary_key", ""),
            card.get("foreign_keys", ""),
            card.get("common_issues", ""),
        ])
    else:
        parts.extend([
            card.get("parent", ""),
            card.get("referenced", ""),
            card.get("columns", ""),
            card.get("business_meaning", ""),
        ])
    return " ".join(p for p in parts if p)


def compile_cards() -> list[dict]:
    cards: list[dict] = []
    tables_dir = VAULT_BO / "Tables"
    if tables_dir.is_dir():
        for path in sorted(tables_dir.glob("*.md")):
            card = _compile_table(path)
            if card:
                cards.append(card)
    rel_dir = VAULT_BO / "Relations"
    if rel_dir.is_dir():
        for path in sorted(rel_dir.glob("*.md")):
            card = _compile_relation(path)
            if card:
                cards.append(card)
    for alias, table in _ARABIC_ALIASES.items():
        cards.append({
            "kind": "alias",
            "name": alias,
            "maps_to": table,
            "arabic": alias,
        })
    return cards


def write_sqlite(client: str, cards: list[dict]) -> Path:
    out = config.work_dir(client) / "vault_cards.sqlite"
    conn = sqlite3.connect(out)
    conn.execute("DROP TABLE IF EXISTS cards")
    conn.execute(
        "CREATE TABLE cards ("
        "id INTEGER PRIMARY KEY, "
        "kind TEXT NOT NULL, "
        "name TEXT NOT NULL, "
        "card_json TEXT NOT NULL, "
        "search_text TEXT NOT NULL)"
    )
    for card in cards:
        st = _search_text(card) if card["kind"] != "alias" else f"{card['name']} {card['maps_to']}"
        conn.execute(
            "INSERT INTO cards (kind, name, card_json, search_text) VALUES (?, ?, ?, ?)",
            (card["kind"], card.get("name", ""), json.dumps(card, ensure_ascii=False), st),
        )
    conn.commit()
    conn.close()
    return out


def main():
    parser = argparse.ArgumentParser(description="Compile vault schema cards for a client")
    parser.add_argument("--client", required=True)
    args = parser.parse_args()
    cards = compile_cards()
    out = write_sqlite(args.client, cards)
    tables = sum(1 for c in cards if c["kind"] == "table")
    relations = sum(1 for c in cards if c["kind"] == "relation")
    aliases = sum(1 for c in cards if c["kind"] == "alias")
    print(f"Wrote {len(cards)} cards ({tables} tables, {relations} relations, {aliases} aliases) to {out}")


if __name__ == "__main__":
    main()
