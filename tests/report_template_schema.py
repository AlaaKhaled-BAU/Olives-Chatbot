"""Validate report template SQL column references against schema_cache tables."""
import json
import re
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
_SCHEMA_PATH = _REPO / "work" / "105" / "schema_cache.json"
_FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "report_template_schema_105.json"

_FROM_JOIN_RE = re.compile(
    r"(?:FROM|(?:INNER|LEFT|RIGHT|CROSS)\s+JOIN|JOIN)\s+t\.(\w+)\s+(?:AS\s+)?(\w+)\b",
    re.IGNORECASE,
)
_QUALIFIED_COL_RE = re.compile(r"\b([a-zA-Z_][\w]*)\.([a-zA-Z_][\w]*)\b")
_SQL_KEYWORDS = frozenset(
    {
        "select", "from", "where", "join", "inner", "left", "right", "cross",
        "on", "and", "or", "not", "null", "isnull", "case", "when", "then",
        "else", "end", "as", "by", "group", "order", "asc", "desc", "top",
        "distinct", "count", "sum", "max", "min", "cast", "date", "in",
        "exists", "between", "like", "having", "union", "except", "intersect",
    }
)


def load_schema_tables() -> dict[str, set[str]]:
    path = _SCHEMA_PATH if _SCHEMA_PATH.exists() else _FIXTURE_PATH
    data = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, set[str]] = {}
    for full_name, cols in data.get("tables", {}).items():
        bare = full_name.split(".")[-1]
        out[bare.lower()] = {c["column"].lower() for c in cols}
    return out


def alias_map(sql: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for table, alias in _FROM_JOIN_RE.findall(sql):
        mapping[alias.lower()] = table
    return mapping


def invalid_column_refs(sql: str, schema_tables: dict[str, set[str]]) -> list[str]:
    aliases = alias_map(sql)
    errors: list[str] = []
    for alias, column in _QUALIFIED_COL_RE.findall(sql):
        alias_l = alias.lower()
        col_l = column.lower()
        if alias_l in _SQL_KEYWORDS or col_l in _SQL_KEYWORDS:
            continue
        if alias_l not in aliases:
            continue
        table = aliases[alias_l]
        table_cols = schema_tables.get(table.lower())
        if table_cols is None:
            errors.append(f"unknown table t.{table} (alias {alias})")
            continue
        if col_l not in table_cols:
            errors.append(f"{alias}.{column} not on dbo.{table}")
    return errors
