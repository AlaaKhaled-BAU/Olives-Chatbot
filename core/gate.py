"""sqlglot safety gate (PLAN.md Phase 4). Defense-in-depth on top of the
server-side wall (db/02_tenant_views.sql + core/sql.py) -- never the only
check. Allows exactly one SELECT or one allow-listed EXEC; rewrites the
SELECT to inject a row cap and N-prefix any Arabic string literal."""
import re

import sqlglot
from sqlglot import exp

DEFAULT_ROW_CAP = 200

_DANGEROUS_CALL_RE = re.compile(r"\b(xp_\w+|sp_oa\w+)\b", re.IGNORECASE)
_OPENROWSET_RE = re.compile(r"\b(OPENROWSET|OPENQUERY|OPENDATASOURCE)\b", re.IGNORECASE)
_ARABIC_RE = re.compile(r"[؀-ۿ]")
_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_WRITE_TYPES = (exp.Insert, exp.Update, exp.Delete, exp.Create, exp.Drop, exp.Alter, exp.Merge)


class GateError(Exception):
    pass


def _prefix_arabic_literals(tree):
    for lit in list(tree.find_all(exp.Literal)):
        if lit.is_string and _ARABIC_RE.search(lit.this or ""):
            lit.replace(exp.National(this=lit.this))


def _ensure_top(select, row_cap):
    if select.args.get("limit") is None:
        select.set("limit", exp.Limit(expression=exp.Literal.number(row_cap)))


def validate(sql: str, allowed_procs=None, row_cap: int = DEFAULT_ROW_CAP) -> str:
    """Raise GateError unless sql is exactly one safe SELECT or one
    allow-listed EXEC. Returns the SQL text to actually run (TOP injected,
    Arabic literals N-prefixed)."""
    allowed_procs = {p.lower() for p in (allowed_procs or ())}
    raw = sql.strip()
    if not raw:
        raise GateError("empty query")
    if _DANGEROUS_CALL_RE.search(raw):
        raise GateError("extended stored procedures (xp_/sp_OA*) are never allowed")
    if _OPENROWSET_RE.search(raw):
        raise GateError("OPENROWSET/OPENQUERY/OPENDATASOURCE are never allowed")

    try:
        statements = [s for s in sqlglot.parse(raw, read="tsql") if s is not None]
    except Exception as e:
        raise GateError(f"unparseable SQL: {e}") from e

    if len(statements) != 1:
        raise GateError(f"exactly one statement is allowed, got {len(statements)}")
    stmt = statements[0]

    if isinstance(stmt, exp.Execute):
        proc_name = stmt.this.sql(dialect="tsql").lower()
        if proc_name not in allowed_procs:
            raise GateError(f"{proc_name} is not an allow-listed procedure")
        return stmt.sql(dialect="tsql")

    # C6b: UNION/EXCEPT/INTERSECT are read-only and common for the
    # comparative questions ("this month vs last month") the multi-query
    # budget (C4) exists to answer -- CTE/subquery/GROUP BY already passed
    # through the old exp.Select-only check, there was no reason for these
    # three to be singled out and rejected.
    if not isinstance(stmt, (exp.Select, exp.Union, exp.Except, exp.Intersect)):
        raise GateError(
            f"only SELECT or allow-listed EXEC is permitted, got {type(stmt).__name__}"
        )
    # Checked on every nested exp.Select, not just the top-level node --
    # verified live that sqlglot parses "SELECT a INTO evil FROM t.X UNION
    # SELECT b FROM t.Y" without complaint, and the top-level Union node's
    # OWN "into" arg is None even though a real Into node sits on the
    # first branch. Widening the isinstance check above without this would
    # have opened exactly that bypass.
    if any(sel.args.get("into") for sel in stmt.find_all(exp.Select)):
        raise GateError("SELECT ... INTO is not allowed (creates a table)")
    if next(stmt.find_all(_WRITE_TYPES), None) is not None:
        raise GateError("write/DDL is not allowed inside a SELECT")

    _ensure_top(stmt, row_cap)
    _prefix_arabic_literals(stmt)
    return stmt.sql(dialect="tsql")


def safe_identifier(name: str) -> str:
    """Guards proc-arg key names before they're interpolated into `@name=` --
    values themselves go through pymssql parameter substitution, but the
    parameter NAME can't be, so it's restricted to a plain identifier shape."""
    if not _IDENTIFIER_RE.match(name):
        raise GateError(f"{name!r} is not a valid parameter name")
    return name
