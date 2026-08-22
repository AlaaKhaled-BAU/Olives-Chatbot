"""SA one-shot audit for Rpt_* procedures — candidate allow-list + reject reasons.

Inspects sys.sql_modules definitions and live sys.dm_sql_referenced_entities.
Does NOT GRANT EXECUTE. Grok signs candidates before any grant in a later PR.
Never prints procedure bodies to stdout.
"""
import argparse
import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import config  # noqa: E402
from setup.db_connect import sa_connect  # noqa: E402

_WRITE_KEYWORDS_RE = re.compile(
    r"\b(INSERT|UPDATE|DELETE|MERGE|TRUNCATE|DROP|CREATE|ALTER)\b",
    re.IGNORECASE,
)
_DANGEROUS_CALL_RE = re.compile(r"\b(xp_\w+|sp_oa\w+)\b", re.IGNORECASE)
_OPENROWSET_RE = re.compile(r"\b(OPENROWSET|OPENQUERY|OPENDATASOURCE)\b", re.IGNORECASE)
_EXEC_RE = re.compile(
    r"\bEXEC(?:UTE)?\s+(?:dbo\.)?([A-Za-z_][A-Za-z0-9_]*)",
    re.IGNORECASE,
)


def _load_signed_allowlist(client: str) -> set[str]:
    path = config.work_dir(client) / "rpt_exec_allowlist.json"
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    names = data.get("allowed") or data.get("procedures") or data
    if isinstance(names, dict):
        names = list(names.keys())
    return {str(n).lower() for n in names}


def _list_rpt_procedures(conn, db_name: str) -> list[str]:
    cur = conn.cursor()
    cur.execute(
        """
        SELECT QUOTENAME(SCHEMA_NAME(schema_id)) + '.' + QUOTENAME(name) AS full_name
        FROM sys.procedures
        WHERE name LIKE 'Rpt[_]%' OR name LIKE 'RPT[_]%'
        ORDER BY name
        """,
    )
    return [row[0] for row in cur.fetchall()]


def _module_definition(conn, full_name: str) -> str | None:
    cur = conn.cursor()
    cur.execute(
        """
        SELECT m.definition
        FROM sys.sql_modules m
        INNER JOIN sys.objects o ON o.object_id = m.object_id
        WHERE QUOTENAME(SCHEMA_NAME(o.schema_id)) + '.' + QUOTENAME(o.name) = %s
        """,
        (full_name,),
    )
    row = cur.fetchone()
    if not row:
        return None
    return row[0] or ""


def _referenced_writes(conn, full_name: str) -> list[str]:
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT DISTINCT referenced_entity_name
            FROM sys.dm_sql_referenced_entities(%s, 'OBJECT')
            WHERE is_updated = 1 OR is_deleted = 1 OR is_inserted = 1
            """,
            (full_name,),
        )
    except Exception:
        return ["dm_sql_referenced_entities_failed"]
    return sorted({row[0] for row in cur.fetchall() if row[0]})


def audit_procedure(defn: str, full_name: str, signed_allowlist: set[str]) -> list[str]:
    reasons: list[str] = []
    if not defn:
        reasons.append("missing_definition")
        return reasons
    for match in _WRITE_KEYWORDS_RE.finditer(defn):
        reasons.append(f"keyword:{match.group(1).upper()}")
    if _DANGEROUS_CALL_RE.search(defn):
        reasons.append("xp_or_sp_oa")
    if _OPENROWSET_RE.search(defn):
        reasons.append("openrowset")
    for callee in _EXEC_RE.findall(defn):
        callee_key = callee.lower()
        full_callee = f"dbo.{callee}".lower()
        if callee_key not in signed_allowlist and full_callee not in signed_allowlist:
            reasons.append(f"exec_callee:{callee}")
    return sorted(set(reasons))


def run_audit(client: str, db_name: str | None = None) -> dict:
    cfg = config.load_client(client)
    database = db_name or cfg["db_name"]
    signed = _load_signed_allowlist(client)
    conn = sa_connect(database=database)
    try:
        procedures = _list_rpt_procedures(conn, database)
        candidates = []
        rejected = []
        for full_name in procedures:
            defn = _module_definition(conn, full_name)
            keyword_reasons = audit_procedure(defn or "", full_name, signed)
            write_targets = _referenced_writes(conn, full_name)
            reasons = list(keyword_reasons)
            if write_targets:
                reasons.extend(f"writes_to:{t}" for t in write_targets)
            entry = {"name": full_name, "reasons": sorted(set(reasons))}
            if reasons:
                rejected.append(entry)
            else:
                candidates.append({"name": full_name})
    finally:
        conn.close()
    return {
        "client": client,
        "database": database,
        "signed_allowlist_count": len(signed),
        "candidates": candidates,
        "rejected": rejected,
    }


def main():
    parser = argparse.ArgumentParser(description="Audit Rpt_* procs for read-only EXEC candidates")
    parser.add_argument("--client", required=True)
    parser.add_argument("--db-name", default=None, help="Override database name from client yaml")
    args = parser.parse_args()
    result = run_audit(args.client, args.db_name)
    out_dir = config.work_dir(args.client)
    out_dir.mkdir(parents=True, exist_ok=True)
    candidates_path = out_dir / "rpt_exec_allowlist_candidates.json"
    rejects_path = out_dir / "rpt_exec_rejects.json"
    candidates_path.write_text(
        json.dumps(result["candidates"], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    rejects_path.write_text(
        json.dumps(result["rejected"], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(
        f"Audited {len(result['candidates']) + len(result['rejected'])} Rpt_* procedures: "
        f"{len(result['candidates'])} candidates, {len(result['rejected'])} rejected"
    )
    print(f"Wrote {candidates_path}")
    print(f"Wrote {rejects_path}")


if __name__ == "__main__":
    main()
