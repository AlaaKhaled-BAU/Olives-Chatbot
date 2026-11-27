"""Unit tests for core.postprocess module."""

import pytest
from core.postprocess import (
    DEFAULT_FOLLOWUPS,
    ROW_DISPLAY_CAP,
    SOURCE_TABLE_RE,
    TABLE_ROW_CAP,
    TIME_LIKE_COLUMN_RE,
    UNRESOLVED_TOKEN_RE,
    answer_sql,
    apply_count_backstop,
    build_arabic_stub,
    build_chart,
    build_sources,
    build_table,
    cap_for_context,
    evidence_confidence,
    fence_body_looks_like_sql,
    format_doc_sources,
    format_stub_number,
    is_blank,
    parse_delimited_followups,
    prose_mentions_count,
    strip_sql_fences,
)


def test_default_followups_clean_msa():
    """Verify DEFAULT_FOLLOWUPS is clean Modern Standard Arabic without colloquial Gulf words."""
    assert len(DEFAULT_FOLLOWUPS) == 3
    expected = [
        "توزيع هذا الرقم حسب المندوبين",
        "المقارنة مع الفترة السابقة",
        "ما أكثر الأصناف المساهمة في هذا الرقم؟",
    ]
    assert DEFAULT_FOLLOWUPS == expected

    colloquial_words = ["وش", "ايش", "شو", "حق ايش", "ليه", "وين"]
    for followup in DEFAULT_FOLLOWUPS:
        for word in colloquial_words:
            assert word not in followup, f"Colloquial word '{word}' found in followup: {followup}"


def test_regexes_and_caps():
    """Verify constants and regular expressions."""
    assert ROW_DISPLAY_CAP == 50
    assert TABLE_ROW_CAP == 100

    # UNRESOLVED_TOKEN_RE
    assert UNRESOLVED_TOKEN_RE.search("<company_id>")
    assert UNRESOLVED_TOKEN_RE.search("<date_from>")
    assert not UNRESOLVED_TOKEN_RE.search("<abc>")  # less than 4 chars
    assert not UNRESOLVED_TOKEN_RE.search("normal text")

    # SOURCE_TABLE_RE
    tables = [m.group(1) for m in SOURCE_TABLE_RE.finditer("SELECT * FROM t.Invoices JOIN t.Customers")]
    assert tables == ["Invoices", "Customers"]

    # TIME_LIKE_COLUMN_RE
    for col in ["invoice_date", "month_num", "day_name", "fiscal_year", "week_no"]:
        assert TIME_LIKE_COLUMN_RE.search(col), f"Failed to match time-like column {col}"
    assert not TIME_LIKE_COLUMN_RE.search("customer_name")


def test_cap_for_context():
    """Test cap_for_context behavior."""
    # Non-list passes through
    assert cap_for_context("error") == "error"
    assert cap_for_context({"key": "val"}) == {"key": "val"}

    # Under or equal cap
    rows_30 = [{"id": i} for i in range(30)]
    assert cap_for_context(rows_30) == rows_30

    rows_50 = [{"id": i} for i in range(50)]
    assert cap_for_context(rows_50) == rows_50

    # Over cap
    rows_60 = [{"id": i} for i in range(60)]
    capped = cap_for_context(rows_60)
    assert isinstance(capped, dict)
    assert capped["shown"] == 50
    assert capped["total_rows_returned"] == 60
    assert len(capped["rows"]) == 50
    assert "Only the first 50 of 60 returned rows" in capped["note"]


def test_is_blank():
    """Test is_blank helper."""
    assert is_blank(None) is True
    assert is_blank("") is True
    assert is_blank("   \n\t") is True
    assert is_blank("hello") is False
    assert is_blank("  مرحبا  ") is False


def test_format_stub_number():
    """Test number formatting in stubs."""
    assert format_stub_number(42) == "42"
    assert format_stub_number(42.0) == "42"
    assert format_stub_number(42.5) == "42.5"
    assert format_stub_number("100") == "100"


def test_build_arabic_stub():
    """Test deterministic Arabic stub builder."""
    # Single row, single scalar number
    state_scalar = {"last_rows": [{"total": 1500}]}
    assert build_arabic_stub(state_scalar) == "النتيجة: 1500."

    state_float_int = {"last_rows": [{"count": 25.0}]}
    assert build_arabic_stub(state_float_int) == "النتيجة: 25."

    # Single row, multiple numbers
    state_multi_nums = {"last_rows": [{"total": 100, "tax": 15, "net": 115, "extra": 999}]}
    stub_nums = build_arabic_stub(state_multi_nums)
    assert stub_nums.startswith("النتيجة: ")
    assert "total: 100" in stub_nums
    assert "tax: 15" in stub_nums
    assert "net: 115" in stub_nums
    assert "extra: 999" not in stub_nums  # capped at 3 parts

    # Multiple rows
    state_multi_rows = {"last_rows": [{"a": 1}, {"a": 2}]}
    assert build_arabic_stub(state_multi_rows) == "النتيجة في الجدول أدناه."

    # Doc source pairs without rows
    state_docs = {"doc_source_pairs": [("guide", "intro")]}
    assert build_arabic_stub(state_docs) == "الإجابة في المصادر أدناه."

    # Empty state
    assert build_arabic_stub({}) == "تعذر صياغة الإجابة من البيانات المتاحة."


def test_fence_body_looks_like_sql():
    """Test SQL detection in code fence body."""
    assert fence_body_looks_like_sql("SELECT * FROM t.Invoices") is True
    assert fence_body_looks_like_sql("   -- comment\nSELECT 1") is True
    assert fence_body_looks_like_sql("WITH q AS (SELECT 1) SELECT * FROM q") is True
    assert fence_body_looks_like_sql("def my_func():\n    return 42") is False
    assert fence_body_looks_like_sql("") is False
    assert fence_body_looks_like_sql("   ") is False


def test_strip_sql_fences():
    """Test stripping SQL code fences while preserving other fences."""
    assert strip_sql_fences(None) is None
    assert strip_sql_fences("") == ""

    # Explicit sql/tsql fence
    text_sql = "هذه النتيجة:\n```sql\nSELECT * FROM t.Invoices;\n```\nانتهى الشرح."
    assert strip_sql_fences(text_sql) == "هذه النتيجة:\n\nانتهى الشرح."

    text_tsql = "شاهد الاستعلام:\n```tsql\nSELECT 1;\n```"
    assert strip_sql_fences(text_tsql) == "شاهد الاستعلام:"

    # Unspecified language fence that contains SQL
    text_unspecified_sql = "ملاحظة:\n```\nSELECT col FROM t.Table\n```\nتم."
    assert strip_sql_fences(text_unspecified_sql) == "ملاحظة:\n\nتم."

    # Non-sql fence preserved
    text_python = "كود بايثون:\n```python\nprint('hello')\n```\nمع التقدير."
    assert strip_sql_fences(text_python) == text_python

    # Text that is only a SQL fence
    assert strip_sql_fences("```sql\nSELECT 1;\n```") == ""


def test_prose_mentions_count():
    """Test checking if count is mentioned in prose."""
    assert prose_mentions_count("إجمالي 1,234 فاتورة", 1234) is True
    assert prose_mentions_count("إجمالي 1234 فاتورة", 1234) is True
    assert prose_mentions_count("إجمالي 12345 فاتورة", 1234) is False
    assert prose_mentions_count("إجمالي 50 بند", 50) is True


def test_apply_count_backstop():
    """Test backstop appending when line counts are confused for invoices."""
    state_no_lines = {"had_lines_count": False}
    assert apply_count_backstop("يوجد 10 فواتير", state_no_lines) == "يوجد 10 فواتير"

    # Already mentions lines (بنود)
    state_lines = {
        "had_lines_count": True,
        "line_count_sum": 15,
        "header_count": 3,
    }
    text_with_lines = "يوجد 15 من بنود الفواتير"
    assert apply_count_backstop(text_with_lines, state_lines) == text_with_lines

    # Doesn't mention invoices
    text_no_invoice = "المبلغ الإجمالي هو 1500 ريال"
    assert apply_count_backstop(text_no_invoice, state_lines) == text_no_invoice

    # Treats lines as invoices, header_count available
    text_wrong = "يوجد 15 فاتورة مسجلة"
    backstopped = apply_count_backstop(text_wrong, state_lines)
    assert "عدد الفواتير: 3" in backstopped
    # Running again doesn't duplicate
    assert apply_count_backstop(backstopped, state_lines) == backstopped

    # Treats lines as invoices, no header_count -> warning note
    state_no_hc = {
        "had_lines_count": True,
        "line_count_sum": 15,
        "header_count": None,
    }
    backstopped_no_hc = apply_count_backstop(text_wrong, state_no_hc)
    assert "تنبيه: العدد المذكور كفواتير هو عدد البنود، وليس عدد رؤوس الفواتير." in backstopped_no_hc


def test_build_table():
    """Test table extraction from query rows."""
    assert build_table(None) is None
    assert build_table([]) is None
    # 1 row, 1 col -> None (scalar)
    assert build_table([{"count": 5}]) is None

    # 1 row, multiple cols
    rows_one = [{"id": 1, "name": "Alice"}]
    assert build_table(rows_one) == {
        "columns": ["id", "name"],
        "rows": [[1, "Alice"]],
    }

    # Multiple rows capped at TABLE_ROW_CAP (100)
    rows_120 = [{"id": i, "val": i * 2} for i in range(120)]
    tbl = build_table(rows_120)
    assert tbl is not None
    assert len(tbl["rows"]) == 100
    assert tbl["columns"] == ["id", "val"]


def test_build_chart():
    """Test heuristic chart generation."""
    assert build_chart(None) is None

    # Not 2 columns
    table_3cols = {"columns": ["a", "b", "c"], "rows": [[1, 2, 3], [4, 5, 6]]}
    assert build_chart(table_3cols) is None

    # Only 1 row -> None
    table_1row = {"columns": ["month", "amount"], "rows": [["Jan", 100]]}
    assert build_chart(table_1row) is None

    # More than 20 rows -> None
    table_25rows = {"columns": ["month", "amount"], "rows": [[f"m{i}", i] for i in range(25)]}
    assert build_chart(table_25rows) is None

    # Line chart for time-like column
    table_time = {
        "columns": ["invoice_date", "total_sales"],
        "rows": [["2024-01", 1000], ["2024-02", 1500]],
    }
    chart_line = build_chart(table_time)
    assert chart_line == {"kind": "line", "x": "invoice_date", "y": "total_sales"}

    # Bar chart for categorical column
    table_cat = {
        "columns": ["rep_name", "total_sales"],
        "rows": [["Ahmed", 1000], ["Sara", 1500]],
    }
    chart_bar = build_chart(table_cat)
    assert chart_bar == {"kind": "bar", "x": "rep_name", "y": "total_sales"}

    # Non-numeric second column -> None
    table_invalid = {
        "columns": ["rep_name", "status"],
        "rows": [["Ahmed", "active"], ["Sara", "inactive"]],
    }
    assert build_chart(table_invalid) is None


def test_format_doc_sources_and_build_sources():
    """Test doc sources formatting and full sources building."""
    pairs = [("دليل_المستخدم.md", "فواتير المبيعات"), ("المصطلحات.md", "")]
    formatted = format_doc_sources(pairs)
    assert formatted == ["دليل_المستخدم.md › فواتير المبيعات", "المصطلحات.md"]

    queries = [
        "SELECT * FROM t.Invoices WHERE CompanyID = 1",
        "SELECT * FROM t.Customers JOIN t.Invoices ON ...",
    ]
    sources = build_sources(queries, pairs)
    assert sources == ["Customers", "Invoices", "دليل_المستخدم.md › فواتير المبيعات", "المصطلحات.md"]


def test_answer_sql():
    """Test SQL concatenation from queries and hot_sql."""
    assert answer_sql({}) is None
    state = {
        "queries": ["SELECT * FROM t.Invoices", "SELECT 1"],
        "hot_sql": ["SELECT * FROM t.Customers"],
    }
    assert answer_sql(state) == "SELECT * FROM t.Invoices; SELECT 1; SELECT * FROM t.Customers"


def test_evidence_confidence():
    """Test evidence confidence calculations."""
    assert evidence_confidence({"tool_errors": ["syntax error"]}) == "medium"
    assert evidence_confidence({"last_rows": [{"id": 1}]}) == "high"
    assert evidence_confidence({"doc_source_pairs": [("doc", "h1")]}) == "medium"
    assert evidence_confidence({}) == "low"


def test_parse_delimited_followups_absent():
    """Test parse_delimited_followups when delimiter is absent or text is None/empty."""
    assert parse_delimited_followups(None) == ("", [])
    assert parse_delimited_followups("") == ("", [])
    assert parse_delimited_followups("الإجابة واضحة ومباشرة.") == ("الإجابة واضحة ومباشرة.", [])


def test_parse_delimited_followups_json():
    """Test parse_delimited_followups with JSON array."""
    text = (
        "النتيجة الإجمالية 500 ريال.\n\n"
        "---FOLLOWUPS---\n"
        '["توزيع حسب الفروع", "المقارنة مع العام الماضي", "أعلى الأصناف"]'
    )
    clean, followups = parse_delimited_followups(text)
    assert clean == "النتيجة الإجمالية 500 ريال."
    assert followups == ["توزيع حسب الفروع", "المقارنة مع العام الماضي", "أعلى الأصناف"]


def test_parse_delimited_followups_json_fenced_and_dict():
    """Test parse_delimited_followups with JSON array inside code fence or dict wrapper."""
    text = (
        "النتيجة.\n\n"
        "---FOLLOWUPS---\n"
        "```json\n"
        '{"followups": ["سؤال 1", "سؤال 2"]}\n'
        "```"
    )
    clean, followups = parse_delimited_followups(text)
    assert clean == "النتيجة."
    assert followups == ["سؤال 1", "سؤال 2"]


def test_parse_delimited_followups_bulleted_arabic():
    """Test parse_delimited_followups with bulleted Arabic lines."""
    text = (
        "إجمالي المبيعات لشهر مايو هو 25,000 ريال.\n\n"
        "---FOLLOWUPS---\n"
        "- توزيع هذا الرقم حسب المندوبين\n"
        "* المقارنة مع الفترة السابقة\n"
        "• ما أكثر الأصناف المساهمة في هذا الرقم؟"
    )
    clean, followups = parse_delimited_followups(text)
    assert clean == "إجمالي المبيعات لشهر مايو هو 25,000 ريال."
    assert followups == [
        "توزيع هذا الرقم حسب المندوبين",
        "المقارنة مع الفترة السابقة",
        "ما أكثر الأصناف المساهمة في هذا الرقم؟",
    ]


def test_parse_delimited_followups_numbered():
    """Test parse_delimited_followups with numbered lines."""
    text = (
        "البيانات مكتملة.\n\n"
        "---FOLLOWUPS---\n"
        "1. ما هي الأصناف الأكثر مبيعاً؟\n"
        "2) كيف توزع المبيعات حسب المناطق؟\n"
        "3- هل هناك فواتير مرتجعة؟\n"
        "4. سؤال إضافي زائد عن الثلاثة"
    )
    clean, followups = parse_delimited_followups(text)
    assert clean == "البيانات مكتملة."
    assert len(followups) == 3
    assert followups == [
        "ما هي الأصناف الأكثر مبيعاً؟",
        "كيف توزع المبيعات حسب المناطق؟",
        "هل هناك فواتير مرتجعة؟",
    ]


def test_parse_delimited_followups_length_cap():
    """Test capping each followup item at 120 characters."""
    long_question = "س" * 150
    text = f"إجابة.\n\n---FOLLOWUPS---\n- {long_question}"
    clean, followups = parse_delimited_followups(text)
    assert clean == "إجابة."
    assert len(followups) == 1
    assert len(followups[0]) == 120


def test_parse_delimited_followups_malformed_and_empty():
    """Test parse_delimited_followups with malformed block or empty delimiter."""
    # Malformed block: neither JSON array nor bulleted/numbered lines
    text_malformed = "نص الإجابة.\n\n---FOLLOWUPS---\n{not valid json or bullets"
    clean, followups = parse_delimited_followups(text_malformed)
    assert clean == "نص الإجابة."
    assert followups == []

    # Empty block after delimiter
    text_empty_block = "نص الإجابة.\n\n---FOLLOWUPS---\n   "
    clean_empty, followups_empty = parse_delimited_followups(text_empty_block)
    assert clean_empty == "نص الإجابة."
    assert followups_empty == []
