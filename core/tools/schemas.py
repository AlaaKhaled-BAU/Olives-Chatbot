"""Tool definitions and schemas for the Olives Chatbot agent.

Provides JSON schema tool specifications for LLM tool calling.
"""

from __future__ import annotations

from typing import Any

TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "introspect_schema",
            "description": (
                "Look up columns for a table, or parameters for an allow-listed "
                "procedure, by name (case-insensitive)."
            ),
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_select",
            "description": "Run exactly one read-only SELECT against the t. (tenant-scoped) views.",
            "parameters": {
                "type": "object",
                "properties": {"sql": {"type": "string"}},
                "required": ["sql"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "ask_user",
            "description": (
                "Block only for identity/policy that is NOT company: "
                "which of several hot-cache people/items, EXEC/proc body, or كل الشركات. "
                "CompanyID is already pinned by the UI — never ask which company, never list companies. "
                "Do NOT block for grain ambiguity (best salesman, sales vs orders, cash vs credit) — "
                "state one Arabic assumption, run run_metric/run_select, then offer an alternate "
                "('إذا تقصد عدد الفواتير أو زبائن المنطقة، قل.')."
            ),
            "parameters": {
                "type": "object",
                "properties": {"question": {"type": "string"}},
                "required": ["question"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "analyze",
            "description": (
                "Exact computation offload. Arithmetic: percent_change, difference, ratio "
                "(before/after). Trend analysis for forecasts: trend_direction (pass 'series' "
                "= oldest-to-newest weekly/monthly numbers from ONE grouped query; returns "
                "direction, slope %/step, and projected_next_bucket_estimate labeled ESTIMATE), "
                "growth_compare (before/after), top_movers ({label:value} dicts for current vs "
                "previous period). Never touches the database, never counts against the query "
                "budget. Use this instead of computing in prose -- it's exact and the forecast "
                "numbers it emits are honest estimates with stated basis."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "percent_change",
                            "difference",
                            "ratio",
                            "trend_direction",
                            "growth_compare",
                            "top_movers",
                        ],
                    },
                    "series": {"type": "array", "items": {"type": "number"}},
                    "current": {"type": "object", "additionalProperties": {"type": "number"}},
                    "previous": {"type": "object", "additionalProperties": {"type": "number"}},
                    "before": {"type": "number"},
                    "after": {"type": "number"},
                },
                "required": ["operation"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": (
                "Search the Olives user/system documentation for how a feature, screen, or system "
                "option works -- conceptual/how-to questions, not this client's own numbers. Returns "
                "the best-matching excerpts with their source. Never counts against the query budget. "
                "Bilingual search: when answering an Arabic question, pass English UI/ERP equivalent "
                "terms alongside Arabic keywords (e.g. query=\"customer type add new screen نوع زبون\") "
                "because the user guides are predominantly English."
            ),
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_schema_notes",
            "description": (
                "Regex search over vault schema notes (tables, procedures metadata, relations) in Olives_BO. "
                "Never returns procedure bodies. Does not count against query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"type": "string"},
                    "type": {"type": "string", "description": "Optional: table, procedure, or relation"},
                },
                "required": ["pattern"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_schema_note",
            "description": (
                "Read a vault schema note by name or path. Procedures return metadata only (params, tables read) — "
                "never CREATE PROCEDURE text. Does not count against query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "path": {"type": "string"},
                    "type": {"type": "string"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_joins",
            "description": (
                "Get FK relation notes and graph dependencies for a BO table name. "
                "Does not count against query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {"table": {"type": "string"}},
                "required": ["table"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_metric",
            "description": (
                "Run a named business metric with the correct grain — prefer over run_select for "
                "sales, salesperson rank, returns, orders, van stock, or customer-to-salesperson "
                "assignment. Counts against the query budget. "
                "Ranked questions over any dimension (best/worst/top/bottom salesman, customer, item, day): "
                "metric=sales with group_by + order (desc for best, asc for worst) + limit, so the database ranks. "
                "For worst/bottom items also call unsold_items for the same period."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "metric": {
                        "type": "string",
                        "description": (
                            "Prefer sales (مبيعات) as primary with filters tax and returns. "
                            "Also: net_sales_by_salesperson (أفضل مندوب), "
                            "daily_sales_pack (محصلة يومية), returns (مرتجعات), orders (طلبات), "
                            "van_stock (رصيد السيارة), cfd_assignment (عملاء المندوب), "
                            "unsold_items (مواد راكدة: active items with no sales in the period). "
                            "net_sales is legacy for old plans only -- use sales instead."
                        ),
                    },
                    "filters": {
                        "type": "object",
                        "properties": {
                            "from_date": {"type": "string", "description": "YYYY-MM-DD"},
                            "to_date": {"type": "string", "description": "YYYY-MM-DD (half-open end)"},
                            "tax": {
                                "type": "string",
                                "enum": ["incl", "excl"],
                                "description": "incl=charged total (default); excl=before tax (قبل الضريبة)",
                            },
                            "returns": {
                                "type": "string",
                                "enum": ["gross", "net"],
                                "description": "gross=sales only (default); net=gross minus returns (بعد المرتجعات)",
                            },
                            "group_by": {
                                "type": "string",
                                "enum": ["salesperson", "customer", "item", "day"],
                            },
                            "order": {
                                "type": "string",
                                "enum": ["asc", "desc"],
                                "description": "With group_by: rank by the primary measure (asc = lowest first).",
                            },
                            "limit": {
                                "type": "integer",
                                "description": (
                                    "Only with group_by and order: top N rows, 1-50 (default 10). "
                                    "Ignored or rejected if order is omitted."
                                ),
                            },
                            "sales_person_id": {"type": "integer"},
                            "undelivered_only": {"type": "boolean"},
                        },
                    },
                },
                "required": ["metric"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_report",
            "description": (
                "Run a named Olives BO report from the catalog. Uses a certified SELECT template on "
                "t. when available; otherwise returns catalog purpose and a not-certified notice. "
                "Never EXEC stored procedures in this release. Counts against the query budget when "
                "a SELECT template runs."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Catalog report name, e.g. Rpt_SalesmanSalesSummary",
                    },
                    "params": {
                        "type": "object",
                        "description": "Optional filters: from_date, to_date, sales_person_id, customer_id, item_code",
                        "properties": {
                            "from_date": {"type": "string"},
                            "to_date": {"type": "string"},
                            "sales_person_id": {"type": "integer"},
                            "customer_id": {"type": "integer"},
                            "item_code": {"type": "string"},
                        },
                    },
                },
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "lookup_hot",
            "description": (
                "Load an L1 master snapshot (SalesPersons, SalesPersonsDevicePermissions, "
                "DeliveryCars, items, routes, LogActions ActionID codebook). "
                "Pass LogActionTransaction for the same codebook (the fact log is not cached). "
                "Never for invoices/orders/receipts/balances. Free — does not count against query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {"table": {"type": "string"}},
                "required": ["table"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "recall_turns",
            "description": (
                "Search earlier questions in this session (beyond the last 4 turns). "
                "Returns question text and SQL to rewrite for the NEW dates/grain. "
                "Retrieved answer snippets are not numbers to copy — re-run SQL. "
                "Does not count against the query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Follow-up text or search terms (names, dates, tables).",
                    },
                },
                "required": ["query"],
            },
        },
    },
]
