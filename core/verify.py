"""Line vs header COUNT detection and optional header recount SQL (Phase 2 / L2).

Wired into the agent in I1; this module has no DB or network dependencies."""
from __future__ import annotations

import sqlglot
from sqlglot import exp

# Tool-result field (I1). English in JSON; user-facing copy lives in locale table.
COUNT_NOTE = "counts lines, not invoice headers"

_HEADER_TABLES = frozenset({"transactionsheaders", "ordersheaders"})
_DETAIL_TABLES = frozenset({"transactionsdetails", "ordersdetails"})
_HEADER_BARE = "TransactionsHeaders"
_ORDERS_HEADER_BARE = "OrdersHeaders"

_ALLOWED_PREDICATE_COLS = frozenset(
    {"companyid", "transactiontypeid", "isvoid", "transactiondate"}
)
_SALES_PERSON_COLS = frozenset({"salespersonid"})
_FORBIDDEN_DATE_FUNCS = frozenset({"getdate", "dateadd", "eomonth", "datefromparts"})


def _table_bare(tbl: exp.Table) -> str:
    return (tbl.name or "").split(".")[-1].lower()


def _from_clause(select: exp.Select):
    return select.args.get("from_") or select.args.get("from")


def _select_scope_tables(select: exp.Select) -> set[str]:
    tables: set[str] = set()
    from_ = _from_clause(select)
    if from_ and from_.this and isinstance(from_.this, exp.Table):
        tables.add(_table_bare(from_.this))
    for join in select.args.get("joins") or []:
        if isinstance(join.this, exp.Table):
            tables.add(_table_bare(join.this))
    return tables


def _has_count_excluding_subqueries(expr: exp.Expression) -> bool:
    if isinstance(expr, exp.Subquery):
        return False
    if isinstance(expr, exp.Count):
        return True
    for key, child in expr.args.items():
        if isinstance(child, exp.Expression):
            if _has_count_excluding_subqueries(child):
                return True
        elif isinstance(child, list):
            for item in child:
                if isinstance(item, exp.Expression) and _has_count_excluding_subqueries(item):
                    return True
    return False


def _select_has_count(select: exp.Select) -> bool:
    for expr in select.expressions:
        if _has_count_excluding_subqueries(expr):
            return True
    return False


def _count_kind_for_select(select: exp.Select) -> str | None:
    if not _select_has_count(select):
        return None
    tables = _select_scope_tables(select)
    if not tables:
        return "other"
    if tables & _DETAIL_TABLES:
        return "lines"
    if tables <= _HEADER_TABLES:
        return "header"
    return "other"


def count_scopes(sql: str) -> list[dict[str, str]]:
    """List COUNT scopes in SQL: {kind: header|lines|other, func: count}."""
    raw = (sql or "").strip()
    if not raw:
        return []
    scopes: list[dict[str, str]] = []
    for stmt in sqlglot.parse(raw, read="tsql"):
        if stmt is None:
            continue
        for select in stmt.find_all(exp.Select):
            kind = _count_kind_for_select(select)
            if kind is not None:
                scopes.append({"kind": kind, "func": "count"})
    return scopes


def _header_columns(schema_cache: dict, bare: str) -> set[str]:
    cols = schema_cache.get("tables", {}).get(f"dbo.{bare}") or []
    return {c["column"].lower() for c in cols if c.get("column")}


def _alias_to_header(select: exp.Select) -> dict[str, str]:
    mapping: dict[str, str] = {}
    from_ = _from_clause(select)
    if from_ and isinstance(from_.this, exp.Table):
        bare = _table_bare(from_.this)
        if bare in _HEADER_TABLES:
            alias = (from_.this.alias or from_.this.name or bare).lower()
            mapping[alias] = bare
    for join in select.args.get("joins") or []:
        if isinstance(join.this, exp.Table):
            bare = _table_bare(join.this)
            if bare in _HEADER_TABLES:
                alias = (join.this.alias or join.this.name or bare).lower()
                mapping[alias] = bare
    return mapping


def _detail_aliases(select: exp.Select) -> set[str]:
    aliases: set[str] = set()
    from_ = _from_clause(select)
    if from_ and isinstance(from_.this, exp.Table):
        if _table_bare(from_.this) in _DETAIL_TABLES:
            aliases.add((from_.this.alias or from_.this.name or "").lower())
    for join in select.args.get("joins") or []:
        if isinstance(join.this, exp.Table) and _table_bare(join.this) in _DETAIL_TABLES:
            aliases.add((join.this.alias or join.this.name or "").lower())
    return aliases


def _column_bare(col: exp.Column) -> str:
    return (col.name or "").lower()


def _column_table_alias(col: exp.Column) -> str:
    if col.table:
        return str(col.table).lower()
    return ""


def _expr_has_forbidden_date_func(node: exp.Expression) -> bool:
    if isinstance(node, (exp.DateAdd, exp.CurrentDate, exp.CurrentTimestamp)):
        return True
    for fn in node.find_all(exp.Anonymous):
        name = (fn.this or "").lower() if isinstance(fn.this, str) else ""
        if name in _FORBIDDEN_DATE_FUNCS:
            return True
    for fn in node.find_all(exp.Func):
        if (fn.name or "").lower() in _FORBIDDEN_DATE_FUNCS:
            return True
    return bool(list(node.find_all(exp.DateAdd)))


def _is_date_literal(node: exp.Expression | None) -> bool:
    if node is None:
        return False
    if isinstance(node, exp.Literal):
        return True
    if isinstance(node, exp.Cast) and node.this:
        return _is_date_literal(node.this)
    return False


def _transaction_date_ok(node: exp.Expression) -> bool:
    """True when TransactionDate is only compared to literals (no dynamic dates)."""
    if _expr_has_forbidden_date_func(node):
        return False
    for col in node.find_all(exp.Column):
        if _column_bare(col) != "transactiondate":
            continue
        # Parent comparison should involve a literal on the other side
        found_literal = False
        for lit in node.find_all(exp.Literal):
            found_literal = True
        if not found_literal:
            return False
    return True


def _where_predicates_allowed(
    where_expr: exp.Expression,
    header_aliases: dict[str, str],
    detail_aliases: set[str],
    header_cols: set[str],
) -> bool:
    if _expr_has_forbidden_date_func(where_expr):
        return False
    if not _transaction_date_ok(where_expr):
        return False

    for col in where_expr.find_all(exp.Column):
        alias = _column_table_alias(col)
        bare = _column_bare(col)
        if alias in detail_aliases:
            return False
        if bare in _SALES_PERSON_COLS:
            return False
        if alias and alias not in header_aliases:
            return False
        if bare not in _ALLOWED_PREDICATE_COLS:
            return False
        if bare != "transactiondate" and bare not in header_cols:
            return False
    return True


def _lines_count_select(sql: str) -> exp.Select | None:
    raw = (sql or "").strip()
    if not raw:
        return None
    for stmt in sqlglot.parse(raw, read="tsql"):
        if stmt is None:
            continue
        for select in stmt.find_all(exp.Select):
            if _count_kind_for_select(select) == "lines":
                return select
    return None


def _primary_header_table(select: exp.Select) -> tuple[exp.Table, str] | None:
    from_ = _from_clause(select)
    if from_ and isinstance(from_.this, exp.Table):
        if _table_bare(from_.this) in _HEADER_TABLES:
            bare = _HEADER_BARE if _table_bare(from_.this) == "transactionsheaders" else _ORDERS_HEADER_BARE
            return from_.this, bare
    for join in select.args.get("joins") or []:
        if isinstance(join.this, exp.Table) and _table_bare(join.this) in _HEADER_TABLES:
            bare = _HEADER_BARE if _table_bare(join.this) == "transactionsheaders" else _ORDERS_HEADER_BARE
            return join.this, bare
    return None


def needs_header_recount(sql: str, schema_cache: dict) -> bool:
    """True when a lines-scope COUNT has only safe header WHERE predicates (per plan)."""
    select = _lines_count_select(sql)
    if select is None:
        return False

    header_aliases = _alias_to_header(select)
    if not header_aliases:
        return False

    bare_key = next(iter(header_aliases.values()))
    header_bare = _HEADER_BARE if bare_key == "transactionsheaders" else _ORDERS_HEADER_BARE
    header_cols = _header_columns(schema_cache, header_bare)
    for required in ("transactiontypeid", "isvoid", "companyid"):
        if required not in header_cols:
            return False

    detail_aliases = _detail_aliases(select)
    where = select.args.get("where")
    if where is None:
        return False
    return _where_predicates_allowed(where.this, header_aliases, detail_aliases, header_cols)


def header_recount_sql(sql: str) -> str | None:
    """COUNT(DISTINCT header keys) with WHERE copied from the lines-scope SELECT."""
    select = _lines_count_select(sql)
    if select is None:
        return None

    found = _primary_header_table(select)
    if found is None:
        return None
    th, table_bare = found
    alias = th.alias or "th"

    where = select.args.get("where")
    where_sql = f" WHERE {where.this.sql(dialect='tsql')}" if where else ""

    return (
        f"SELECT COUNT(*) AS header_count FROM ("
        f"SELECT DISTINCT {alias}.CompanyID, {alias}.TransactionTypeID, "
        f"{alias}.TransactionYear, {alias}.TransactionNo "
        f"FROM t.{table_bare} {alias}"
        f"{where_sql}"
        f") AS _hdr"
    )
