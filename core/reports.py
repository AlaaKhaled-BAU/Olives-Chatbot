"""Report catalog matcher and in-repo SELECT templates — metadata only, never EXEC."""
import json
import re
from pathlib import Path

from . import config, gate, sql

_BASE_DIR = Path(__file__).resolve().parent.parent
_TEMPLATES_PATH = _BASE_DIR / "knowledge" / "report_templates" / "templates.json"
_TOKEN_RE = re.compile(r"[a-zA-Z\u0600-\u06FF]{3,}")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def catalog_path(client: str) -> Path:
    return config.work_dir(client) / "report_catalog.json"


def load_catalog(client: str) -> list:
    path = catalog_path(client)
    if not path.exists():
        return []
    return json.loads(path.read_text())


def load_templates() -> list[dict]:
    if not _TEMPLATES_PATH.exists():
        return []
    return json.loads(_TEMPLATES_PATH.read_text(encoding="utf-8"))


def templates_by_name() -> dict[str, dict]:
    return {t["name"]: t for t in load_templates()}


def _tokens(text: str) -> set:
    return {t.lower() for t in _TOKEN_RE.findall(text)}


def _safe_date(value) -> str | None:
    if not value or not _DATE_RE.match(str(value)):
        return None
    return str(value)


def _safe_int(value) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _date_filters(params: dict, *, th_alias: str = "th") -> str:
    parts = []
    from_date = _safe_date(params.get("from_date"))
    to_date = _safe_date(params.get("to_date"))
    if from_date:
        parts.append(f"{th_alias}.TransactionDate >= '{from_date}'")
    if to_date:
        parts.append(f"{th_alias}.TransactionDate <= '{to_date}'")
    if parts:
        return " AND " + " AND ".join(parts)
    return ""


def _receipt_date_filters(params: dict, *, alias: str = "r") -> str:
    parts = []
    from_date = _safe_date(params.get("from_date"))
    to_date = _safe_date(params.get("to_date"))
    if from_date:
        parts.append(f"{alias}.TransactionDate >= '{from_date}'")
    if to_date:
        parts.append(f"{alias}.TransactionDate <= '{to_date}'")
    if parts:
        return " AND " + " AND ".join(parts)
    return ""


def _order_date_filters(params: dict, *, alias: str = "oh") -> str:
    parts = []
    from_date = _safe_date(params.get("from_date"))
    to_date = _safe_date(params.get("to_date"))
    if from_date:
        parts.append(f"{alias}.OrderDate >= '{from_date}'")
    if to_date:
        parts.append(f"{alias}.OrderDate <= '{to_date}'")
    if parts:
        return " AND " + " AND ".join(parts)
    return ""


def _invoice_date_filters(params: dict, *, alias: str = "th") -> str:
    return _date_filters(params, th_alias=alias)


def _exists_date_filters(params: dict, *, th_alias: str = "th") -> str:
    return _date_filters(params, th_alias=th_alias)


def build_report_sql(report_name: str, params: dict | None = None) -> str | None:
    """Materialize an in-repo SELECT template. Returns None if no template exists."""
    tmpl = templates_by_name().get(report_name)
    if not tmpl:
        return None
    params = dict(params or {})
    sql_text = tmpl["sql"]
    replacements = {
        "{date_filter}": _date_filters(params),
        "{date_filter_th2}": _date_filters(params, th_alias="th2"),
        "{receipt_date_filter}": _receipt_date_filters(params),
        "{order_date_filter}": _order_date_filters(params),
        "{invoice_date_filter}": _invoice_date_filters(params),
        "{date_filter_on_th}": _date_filters(params),
        "{date_filter_exists}": _exists_date_filters(params),
        "{salesperson_filter}": (
            f" AND th.SalesPersonID = {_safe_int(params['sales_person_id'])}"
            if _safe_int(params.get("sales_person_id")) is not None
            else ""
        ),
        "{salesperson_filter_th2}": (
            f" AND th2.SalesPersonID = {_safe_int(params['sales_person_id'])}"
            if _safe_int(params.get("sales_person_id")) is not None
            else ""
        ),
        "{customer_filter}": (
            f" AND th.CustomerID = {_safe_int(params['customer_id'])}"
            if _safe_int(params.get("customer_id")) is not None
            else ""
        ),
        "{item_filter}": (
            f" AND td.ItemCode = '{str(params['item_code']).replace(chr(39), chr(39) * 2)}'"
            if params.get("item_code")
            else ""
        ),
    }
    for key, value in replacements.items():
        sql_text = sql_text.replace(key, value)
    if "EXEC" in sql_text.upper():
        raise gate.GateError("report templates must be SELECT-only")
    return sql_text


def run_report_select(
    report_name: str,
    company_id: int,
    client: str,
    params: dict | None = None,
    allowed_procs=None,
) -> dict:
    """Run a certified SELECT template through the gate. Never calls EXEC."""
    sql_text = build_report_sql(report_name, params)
    if sql_text is None:
        return {"error": f"no SELECT template for {report_name!r}"}
    rows = sql.run_select(
        sql_text,
        company_id,
        client,
        allowed_procs=allowed_procs if allowed_procs is not None else gate.DEFAULT_ALLOWED_PROCS,
    )
    return {"report": report_name, "sql": sql_text, "rows": rows}


def _catalog_card(client: str, report_name: str) -> dict | None:
    name = (report_name or "").strip()
    if not name:
        return None
    for card in load_catalog(client):
        if card.get("name") == name:
            return card
    tmpl = templates_by_name().get(name)
    if tmpl:
        return {"name": name, "purpose": tmpl.get("purpose", "")}
    return None


def run_report(
    report_name: str,
    company_id: int,
    client: str,
    params: dict | None = None,
    allowed_procs=None,
) -> dict:
    """Path 1: certified SELECT template via run_select. Path 3: catalog purpose only."""
    allowed = allowed_procs if allowed_procs is not None else gate.DEFAULT_ALLOWED_PROCS
    if build_report_sql(report_name, params):
        return run_report_select(
            report_name, company_id, client, params=params, allowed_procs=allowed,
        )
    card = _catalog_card(client, report_name)
    purpose = (card or {}).get("purpose", "")
    return {
        "report": report_name,
        "status": "not_certified",
        "purpose": purpose,
        "message": "equivalent SELECT not certified yet",
    }


def _score_card(question_tokens: set, card: dict, aliases: list[str]) -> int:
    blob = " ".join(
        str(card.get(k, "")) for k in ("name", "purpose", "tables", "params", "when_to_run")
    )
    blob += " " + " ".join(aliases)
    card_tokens = _tokens(blob)
    overlap = len(question_tokens & card_tokens)
    q_lower = " ".join(sorted(question_tokens))
    for alias in aliases:
        alias_tokens = _tokens(alias)
        if alias_tokens and alias_tokens <= question_tokens:
            overlap += len(alias_tokens) + 2
        alias_lower = alias.lower()
        if len(alias_lower) >= 6 and alias_lower in q_lower:
            overlap += 5
    return overlap


def match_reports(question: str, client: str, limit: int = 3) -> list:
    """Keyword overlap match against catalog cards plus in-repo template aliases."""
    catalog = load_catalog(client)
    templates = templates_by_name()
    known = {c.get("name") for c in catalog}
    for name, tmpl in templates.items():
        if name not in known:
            catalog.append({
                "name": name,
                "purpose": tmpl.get("purpose", ""),
                "params": ", ".join(tmpl.get("params") or []),
                "tables": [],
                "when_to_run": "",
                "aliases": tmpl.get("aliases", []),
            })
    q_tokens = _tokens(question)
    if not q_tokens:
        return []
    scored = []
    for card in catalog:
        name = card.get("name", "")
        aliases = list(card.get("aliases") or templates.get(name, {}).get("aliases") or [])
        overlap = _score_card(q_tokens, card, aliases)
        if overlap:
            out = dict(card)
            out["aliases"] = aliases
            scored.append((overlap, out))
    scored.sort(key=lambda x: (-x[0], x[1].get("name", "")))
    return [c for _, c in scored[:limit]]


def list_template_names() -> list[str]:
    return [t["name"] for t in load_templates()]
