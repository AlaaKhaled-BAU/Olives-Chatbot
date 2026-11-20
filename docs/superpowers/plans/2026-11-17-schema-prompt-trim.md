# Schema prompt trim

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Shrink the standing DeepSeek prefix by sending full columns only for everyday tables, a short column list for the rest, names only for logs, and no dump of every vault card.

**Architecture:** A new `core/schema_prompt.py` decides which columns of a table appear in `_schema_block`. `core/agent.py` keeps building the block and stops appending `_all_cards_block` to the cached prefix. Vault cards stay on disk and are still fetched per question by `retrieve_cards`, `get_joins`, `search_schema_notes`, and `read_schema_note`. `introspect_schema` still returns every column. The gate is unchanged.

**Tech Stack:** Python 3.13 (`py -3.13`), pytest, existing `work/105/schema_cache.json` only as a fixture the tests may skip if absent.

## Global Constraints

- Python 3.13 only. Test command is `py -3.13 -m pytest`, never `python3`.
- Do not delete `work/105/*`, `obsidian/olives/`, or `vault_cards.sqlite`.
- Do not change `core/gate.py` or `core/sql.py`.
- Do not put `UserPWD` or any column whose name is `password` into the prompt.
- `CompanyID` stays omitted, as it is today.
- The prefix must stay byte-stable for a given `schema_cache.json` (no dates, no row counts).
- Do not start the chatbot server.

---

## File structure

- Create: `core/schema_prompt.py` — full-table set, name-only rule, trim regex, `columns_for_prompt`.
- Modify: `core/agent.py` — `_schema_block` calls `columns_for_prompt`; `_static_prefix` does not append the all-cards block; header sentence tells the model to call `introspect_schema` when the needed column is absent.
- Modify: `prompts/system.md` — one sentence in Schema grounding that matches the new header.
- Test: `tests/test_agent.py` — extend the schema-block test; add a prefix test that the vault dump is absent.

`_all_cards_block` stays defined so `test_cards_block_omits_primary_key` still passes. It is no longer part of the prefix.

---

### Task 1: Column policy module

**Files:**
- Create: `core/schema_prompt.py`
- Test: `tests/test_schema_prompt.py`

**Interfaces:**
- Consumes: nothing
- Produces: `columns_for_prompt(table_key: str, columns: list) -> list[str] | None`. `None` means emit the table name with no parentheses. A list is the column names to print, `CompanyID` and passwords already removed.

- [ ] **Step 1: Write the failing test**

```python
from core.schema_prompt import columns_for_prompt

def test_everyday_table_keeps_business_columns():
    cols = [
        {"column": "CompanyID"},
        {"column": "ItemCode"},
        {"column": "Name"},
        {"column": "ItemImage"},
    ]
    assert columns_for_prompt("dbo.Items", cols) == ["ItemCode", "Name", "ItemImage"]

def test_log_table_is_name_only():
    cols = [{"column": "ID"}, {"column": "Message"}]
    assert columns_for_prompt("dbo.ErrorLog", cols) is None

def test_rare_table_keeps_only_key_like_columns():
    cols = [
        {"column": "ID"},
        {"column": "Name"},
        {"column": "LogoBlob"},
        {"column": "UserPWD"},
    ]
    assert columns_for_prompt("dbo.ReprintReasons", cols) == ["ID", "Name"]

def test_password_never_in_prompt_even_on_a_full_table():
    cols = [{"column": "UserID"}, {"column": "UserPWD"}, {"column": "UserName"}]
    assert columns_for_prompt("dbo.Users", cols) == ["UserID", "UserName"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `py -3.13 -m pytest tests/test_schema_prompt.py -v`
Expected: FAIL with `ModuleNotFoundError` or `ImportError` for `core.schema_prompt`.

- [ ] **Step 3: Write minimal implementation**

```python
"""Which columns of a table are worth putting in the standing schema prompt.

Everyday tables keep every business column. Logs and staging tables contribute
a name only. Everything else keeps key, name, date, amount, and status columns.
introspect_schema still returns the full column list.
"""
import re

FULL_TABLES = frozenset({
    "transactionsheaders", "transactionsdetails", "ordersheaders", "ordersdetails",
    "customers", "customersfinancialdetails", "positions", "salespersons",
    "salespersonsroutes", "routesinformation", "logactiontransaction", "logactions",
    "salespersonsdevicepermissions", "customerstypes", "customersclasses",
    "customersgroups", "items", "itemsunits", "itemsbarcodes",
    "salespersonitemsbalance", "storesbalances", "transfersordersdetails",
    "receipts", "checks", "customerchqlist", "promotionsheaders",
    "wf_masterlog", "wf_sublog", "companyparameters", "targetsreferences",
    "wieghttargets", "users",
})

_SECRET = frozenset({"userpwd", "password"})
_TRIM_COL = re.compile(
    r"(?i)(id|no|code|name|date|time|amount|amt|qty|quantity|price|"
    r"status|state|void|suspend|approv|type|due|paid|balance)$"
)

def _bare(table_key: str) -> str:
    return table_key.split(".")[-1].casefold()

def _name_only(bare: str) -> bool:
    if bare in FULL_TABLES:
        return False
    if bare.endswith("log") or bare.startswith("mms_"):
        return True
    return bare in {
        "table_1", "excel", "excel2", "forupdateonly", "promptembeddings",
    }

def _col_names(columns: list) -> list[str]:
    out = []
    for col in columns or []:
        if not isinstance(col, dict):
            continue
        name = col.get("column")
        if not name:
            continue
        if str(name).casefold() in _SECRET or str(name).casefold() == "companyid":
            continue
        out.append(str(name))
    return out

def columns_for_prompt(table_key: str, columns: list) -> list[str] | None:
    bare = _bare(table_key)
    names = _col_names(columns)
    if _name_only(bare):
        return None
    if bare in FULL_TABLES:
        return names
    return [n for n in names if _TRIM_COL.search(n)]
```

Fix the set if a test fails because `TransactionsHeaders` was misspelled: the bare form is `transactionsheaders`.

- [ ] **Step 4: Run test to verify it passes**

Run: `py -3.13 -m pytest tests/test_schema_prompt.py -v`
Expected: PASS, 4 tests.

- [ ] **Step 5: Commit**

```bash
git add core/schema_prompt.py tests/test_schema_prompt.py
git commit -m "feat: decide which schema columns belong in the prompt"
```

---

### Task 2: Use the policy in the schema block and drop the card dump

**Files:**
- Modify: `core/agent.py` (`_schema_block`, `_static_prefix`)
- Modify: `prompts/system.md` (Schema grounding bullet)
- Test: `tests/test_agent.py`

**Interfaces:**
- Consumes: `columns_for_prompt(table_key, columns) -> list[str] | None` from Task 1
- Produces: `_schema_block` lines `- dbo.Items(ItemCode, Name)` for a full or trimmed table, and `- dbo.ErrorLog` when the policy returns `None`. `_static_prefix` has two system messages (rules+playbook, schema), not three.

- [ ] **Step 1: Write the failing test**

Add to `tests/test_agent.py`:

```python
def test_schema_block_name_only_and_lookup_hint():
    cache = {
        "has_tenant_view": {"dbo.ErrorLog": True, "dbo.Items": True},
        "tables": {
            "dbo.ErrorLog": [{"column": "ID"}, {"column": "Message"}],
            "dbo.Items": [
                {"column": "ItemCode"},
                {"column": "Name"},
                {"column": "ItemImage"},
            ],
        },
    }
    text = agent._schema_block(cache)
    assert "- dbo.ErrorLog\n" in text or text.endswith("- dbo.ErrorLog")
    assert "ErrorLog(" not in text
    assert "dbo.Items(ItemCode, Name, ItemImage)" in text
    assert "introspect_schema" in text
    assert "NOT listed here" not in text

def test_static_prefix_omits_vault_card_dump(monkeypatch):
    monkeypatch.setattr(agent, "_all_cards_block", lambda client: "VAULT DUMP MUST NOT APPEAR")
    msgs = agent._static_prefix("105", {"tables": {}, "has_tenant_view": {}})
    blob = "\n".join(m["content"] for m in msgs)
    assert "VAULT DUMP MUST NOT APPEAR" not in blob
```

- [ ] **Step 2: Run test to verify it fails**

Run: `py -3.13 -m pytest tests/test_agent.py::test_schema_block_name_only_and_lookup_hint tests/test_agent.py::test_static_prefix_omits_vault_card_dump -v`
Expected: FAIL. The current block prints `ErrorLog(ID, Message)` and the prefix includes the card dump when the function returns text. The monkeypatched dump will appear until `_static_prefix` stops calling it.

- [ ] **Step 3: Write minimal implementation**

In `core/agent.py` `_schema_block`, replace the header and the column loop:

```python
    lines = [
        "## Queryable tenant views",
        "Every table below is a `t.*` view scoped to this session's CompanyID.",
        "Columns in parentheses are the ones to use directly.",
        "If the column you need is not listed, call introspect_schema with the table name before writing SQL.",
        "A line with no parentheses is a name only. Call introspect_schema before using it.",
    ]
```

Inside the loop, after the existing `endswith` skips:

```python
        from core.schema_prompt import columns_for_prompt
        shown = columns_for_prompt(name, cols)
        if shown is None:
            lines.append(f"- {name}")
        elif shown:
            lines.append(f"- {name}({', '.join(shown)})")
```

Move that import to the top of `core/agent.py` with the other `core` imports. Do not import inside the function.

In `_static_prefix`, delete these two lines:

```python
    cards = _all_cards_block(client)
    if cards:
        msgs.append({"role": "system", "content": cards})
```

In `prompts/system.md`, in the Schema grounding bullet, replace the sentence that says introspect is for live column existence with:

```markdown
- If a column is missing from the schema list, call `introspect_schema` with the table name before writing SQL. Vault tools (`get_joins`, `search_schema_notes`, `read_schema_note`) explain joins and meaning. They do not replace the column list.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `py -3.13 -m pytest tests/test_agent.py::test_schema_block_drops_types_companyid_and_junk_views tests/test_agent.py::test_schema_block_name_only_and_lookup_hint tests/test_agent.py::test_static_prefix_omits_vault_card_dump tests/test_agent.py::test_cards_block_omits_primary_key tests/test_schema_prompt.py -v`
Expected: PASS. `test_schema_block_drops_types_companyid_and_junk_views` still sees `dbo.Items(ItemCode, Name)` because `Items` is a full table.

- [ ] **Step 5: Commit**

```bash
git add core/agent.py core/schema_prompt.py prompts/system.md tests/test_agent.py
git commit -m "feat: stop sending every column and every vault card on each turn"
```

---

### Task 3: Check the 105 prompt got smaller and everyday tables stayed fat

**Files:**
- Test: `tests/test_schema_prompt.py`

**Interfaces:**
- Consumes: `agent._schema_block` and `work/105/schema_cache.json`
- Produces: a skipped-or-passing size test. No production behavior beyond Task 2.

- [ ] **Step 1: Write the failing test**

```python
import json
from pathlib import Path

import core.agent as agent

def test_105_schema_block_shrinks_but_keeps_invoice_columns():
    path = Path("work/105/schema_cache.json")
    if not path.exists():
        import pytest
        pytest.skip("work/105 schema cache is not in this checkout")
    cache = json.loads(path.read_text(encoding="utf-8"))
    text = agent._schema_block(cache)
    assert "TransactionsHeaders(" in text
    assert "IsVoid" in text.split("TransactionsHeaders(", 1)[1].split(")", 1)[0]
    assert "ErrorLog(" not in text
    assert len(text) < 40_000
```

This fails on today's code because the untrimmed block is about 63,000 characters.

- [ ] **Step 2: Run test to verify it fails before Task 2, or passes after**

Run: `py -3.13 -m pytest tests/test_schema_prompt.py::test_105_schema_block_shrinks_but_keeps_invoice_columns -v`
Expected after Task 2: PASS, and `len(text)` is under 40,000. If `IsVoid` is not the invoice header column name in this cache, print the header's column names once and put the real void/status column in the assert. Do not weaken the length assert above 40,000.

- [ ] **Step 3: No extra production code**

Task 2 already implements the behavior. Only adjust `FULL_TABLES` spelling if the 105 cache uses a different bare name.

- [ ] **Step 4: Run the schema tests**

Run: `py -3.13 -m pytest tests/test_schema_prompt.py tests/test_agent.py::test_schema_block_drops_types_companyid_and_junk_views tests/test_deepseek_swap.py::test_static_prefix_is_byte_stable_across_calls -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add tests/test_schema_prompt.py core/schema_prompt.py
git commit -m "test: 105 schema prompt keeps invoice columns and drops the dump"
```
