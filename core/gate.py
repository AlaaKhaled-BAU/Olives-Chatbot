"""sqlglot safety gate (PLAN.md Phase 4). Defense-in-depth on top of the
server-side wall (db/02_tenant_views.sql + core/sql.py) -- never the only
check. Allows exactly one SELECT or one allow-listed EXEC; rewrites the
SELECT to inject a row cap, N-prefix any Arabic string literal, and inject
session CompanyID/CompNo predicates on t. views."""
import re

import sqlglot
from sqlglot import exp

DEFAULT_ROW_CAP = 200
# T0: no signed Rpt_* EXEC allow-list yet — callers must pass this until Grok signs audit output.
DEFAULT_ALLOWED_PROCS: tuple[str, ...] = ()

_DANGEROUS_CALL_RE = re.compile(r"\b(xp_\w+|sp_oa\w+)\b", re.IGNORECASE)
_OPENROWSET_RE = re.compile(r"\b(OPENROWSET|OPENQUERY|OPENDATASOURCE)\b", re.IGNORECASE)
_ARABIC_RE = re.compile(r"[؀-ۿ]")
_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_WRITE_TYPES = (exp.Insert, exp.Update, exp.Delete, exp.Create, exp.Drop, exp.Alter, exp.Merge)

# Keep in sync with setup/02_introspect.py — unscoped reference tables.
_REFERENCE_TABLES = {
    "ActivityList", "CustomerLoginActions", "Currencies", "DeviceReportsList",
    "ExcelReports", "Language", "LanguageDictionary", "LogActions", "Menu",
    "MIMETypes", "MMS_MaintenanceTechnicianPermissions_Def", "MMS_OrderStatus",
    "OlivesMenu", "OlivesPages", "PromotionTypes", "SystemCodes",
    "TargetsTypes", "TransactionsTypes", "WF_Functions",
}

_COMPNO_VARIANTS = ("compno",)

_INVOICE_HEADER_RE = re.compile(r"\bt\.TransactionsHeaders\b", re.IGNORECASE)
_COUNT_RE = re.compile(r"\bCOUNT\s*\(", re.IGNORECASE)
_TYPE_GRAIN_OK_RE = re.compile(
    r"TransactionTypeID\s*=\s*1\b|TransactionTypeID\s*=\s*2\b",
    re.IGNORECASE,
)
_VOID_FILTER_RE = re.compile(r"\bIsVoid\b", re.IGNORECASE)

_INVOICE_GRAIN_ERROR = (
    "use run_metric — TransactionsHeaders COUNT needs "
    "TransactionTypeID=1 (or 2 for returns) and ISNULL(IsVoid,0)=0"
)


class GateError(Exception):
    pass


def invoice_grain_error(sql: str) -> str | None:
    """Return a tool error message when SQL counts TransactionsHeaders without invoice grain."""
    raw = (sql or "").strip()
    if not _INVOICE_HEADER_RE.search(raw):
        return None
    if not _COUNT_RE.search(raw):
        return None
    if _VOID_FILTER_RE.search(raw) and _TYPE_GRAIN_OK_RE.search(raw):
        return None
    return _INVOICE_GRAIN_ERROR


def _prefix_arabic_literals(tree):
    for lit in list(tree.find_all(exp.Literal)):
        if lit.is_string and _ARABIC_RE.search(lit.this or ""):
            lit.replace(exp.National(this=lit.this))


def _ensure_top(select, row_cap):
    if select.args.get("limit") is None:
        select.set("limit", exp.Limit(expression=exp.Literal.number(row_cap)))


def _schema_columns(schema_cache: dict, bare_name: str) -> list | None:
    return schema_cache.get("tables", {}).get(f"dbo.{bare_name}")


def _tenant_column_names(bare_name: str, columns: list | None) -> list[str]:
    if not columns or bare_name in _REFERENCE_TABLES:
        return []
    col_map = {c["column"].lower(): c["column"] for c in columns}
    if bare_name == "Companies":
        return [col_map["id"]] if "id" in col_map else []
    names: list[str] = []
    if "companyid" in col_map:
        names.append(col_map["companyid"])
    for variant in _COMPNO_VARIANTS:
        if variant in col_map:
            names.append(col_map[variant])
    return names


def _tables_in_from(select: exp.Select) -> list[exp.Table]:
    tables: list[exp.Table] = []
    from_ = select.args.get("from_")
    if from_:
        for node in from_.walk():
            if isinstance(node, exp.Table) and (node.db or "").lower() == "t":
                tables.append(node)
    for join in select.args.get("joins") or []:
        for node in join.walk():
            if isinstance(node, exp.Table) and (node.db or "").lower() == "t":
                tables.append(node)
    return tables


def _col_matches(col: exp.Column, alias: str, col_name: str, bare: str = "") -> bool:
    if not col.name or col.name.lower() != col_name.lower():
        return False
    if col.table is None or str(col.table) == "":
        return True
    tbl = str(col.table).lower()
    return tbl in {alias.lower(), bare.lower()}


def _reject_cross_company_literals(stmt, company_id: int, schema_cache: dict):
    cid = int(company_id)
    for select in stmt.find_all(exp.Select):
        where = select.args.get("where")
        if where is None:
            continue
        refs = [(t, t.name, t.alias_or_name) for t in _tables_in_from(select)]
        for eq in where.this.find_all(exp.EQ):
            if not isinstance(eq.this, exp.Column):
                continue
            if not isinstance(eq.expression, exp.Literal) or not eq.expression.is_int:
                continue
            val = int(eq.expression.this)
            col = eq.this
            for _table, bare, alias in refs:
                columns = _schema_columns(schema_cache, bare)
                for tcol in _tenant_column_names(bare, columns):
                    if _col_matches(col, alias, tcol, bare):
                        if val != cid:
                            raise GateError(
                                f"cross-company filter {tcol} = {val} not allowed "
                                f"(session CompanyID is {cid})"
                            )


def _tenant_pred_satisfied(where_expr, alias: str, col_name: str, company_id: int, bare: str) -> bool:
    if where_expr is None:
        return False
    cid = int(company_id)
    for eq in where_expr.find_all(exp.EQ):
        if not isinstance(eq.this, exp.Column):
            continue
        if not isinstance(eq.expression, exp.Literal) or not eq.expression.is_int:
            continue
        if int(eq.expression.this) != cid:
            continue
        if _col_matches(eq.this, alias, col_name, bare):
            return True
    return False


def _eq_predicate(alias: str, col_name: str, company_id: int) -> exp.EQ:
    return exp.EQ(
        this=exp.Column(
            this=exp.to_identifier(col_name),
            table=exp.to_identifier(alias),
        ),
        expression=exp.Literal.number(int(company_id)),
    )


def _append_where(select: exp.Select, predicate: exp.Expression):
    where = select.args.get("where")
    if where is None:
        select.set("where", exp.Where(this=predicate))
    else:
        select.set("where", exp.Where(this=exp.And(this=where.this, expression=predicate)))


def _inject_tenant_on_select(select: exp.Select, company_id: int, schema_cache: dict):
    where = select.args.get("where")
    where_expr = where.this if where is not None else None
    missing: list[exp.Expression] = []
    for table in _tables_in_from(select):
        bare = table.name
        alias = table.alias_or_name
        columns = _schema_columns(schema_cache, bare)
        for tcol in _tenant_column_names(bare, columns):
            if not _tenant_pred_satisfied(where_expr, alias, tcol, company_id, bare):
                missing.append(_eq_predicate(alias, tcol, company_id))
    for pred in missing:
        _append_where(select, pred)


def _inject_tenant_predicates(stmt, company_id: int, schema_cache: dict):
    for select in stmt.find_all(exp.Select):
        _inject_tenant_on_select(select, company_id, schema_cache)


def _skip_tenant_rewrite(raw: str) -> bool:
    lower = raw.lower()
    return "information_schema" in lower or "sys." in lower


def validate(
    sql: str,
    allowed_procs=None,
    row_cap: int = DEFAULT_ROW_CAP,
    company_id: int | None = None,
    schema_cache: dict | None = None,
) -> str:
    """Raise GateError unless sql is exactly one safe SELECT or one
    allow-listed EXEC. Returns the SQL text to actually run (TOP injected,
    tenant predicates, Arabic literals N-prefixed)."""
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

    if not isinstance(stmt, (exp.Select, exp.Union, exp.Except, exp.Intersect)):
        raise GateError(
            f"only SELECT or allow-listed EXEC is permitted, got {type(stmt).__name__}"
        )
    if any(sel.args.get("into") for sel in stmt.find_all(exp.Select)):
        raise GateError("SELECT ... INTO is not allowed (creates a table)")
    if next(stmt.find_all(_WRITE_TYPES), None) is not None:
        raise GateError("write/DDL is not allowed inside a SELECT")

    if (
        company_id is not None
        and schema_cache is not None
        and not _skip_tenant_rewrite(raw)
    ):
        _reject_cross_company_literals(stmt, company_id, schema_cache)
        _inject_tenant_predicates(stmt, company_id, schema_cache)

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
