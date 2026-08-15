"""C5: docs.py's heading chunker, FTS5 index/search, and the confidentiality
filter that reuses catalog.py's CLIENT_NAME_TOKENS. Synthetic corpus dirs
(tmp_path) throughout -- never touches the real docs_corpus/ or work/*/
docs.sqlite, but uses the real "morec" client config (its name_aliases are
a known, stable fixture) rather than fabricating a client.yaml too."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import config, docs


def test_chunks_splits_flat_text_with_no_headings():
    assert list(docs._chunks("just a paragraph, no headings at all")) == \
        [("", "just a paragraph, no headings at all")]


def test_chunks_builds_breadcrumb_for_nested_headings():
    text = (
        "# Guide\n"
        "intro text\n"
        "## Section A\n"
        "a text\n"
        "### Sub A1\n"
        "a1 text\n"
        "## Section B\n"
        "b text\n"
    )
    chunks = list(docs._chunks(text))
    assert chunks == [
        ("Guide", "intro text"),
        ("Guide › Section A", "a text"),
        ("Guide › Section A › Sub A1", "a1 text"),
        ("Guide › Section B", "b text"),
    ]


def test_chunks_pops_stack_back_to_sibling_level():
    """After a level-3 heading, a following level-2 heading must drop Sub A1
    from the breadcrumb, not append alongside it."""
    text = "# G\n## A\n### A1\nx\n## B\ny\n"
    chunks = list(docs._chunks(text))
    headings = [h for h, _ in chunks]
    assert "G › B" in headings
    assert not any("A1" in h and "B" in h for h in headings)


def test_markdown_table_splits_one_chunk_per_row():
    """A table with no blank lines between rows must not collapse into one
    chunk -- measured on system_options_guide.md, this previously excluded
    an entire ~100+ option category from a client just because ONE row in
    it named another client."""
    text = (
        "## Options\n"
        "| Option ID | Description |\n"
        "|---|---|\n"
        "| `3` | Login GPS Check |\n"
        "| `6` | Login GPS Delay |\n"
    )
    chunks = list(docs._chunks(text))
    assert len(chunks) == 2
    for heading, body in chunks:
        assert heading == "Options"
        assert body.startswith("| Option ID | Description |")
    assert "Login GPS Check" in chunks[0][1]
    assert "Login GPS Delay" in chunks[1][1]


def test_markdown_table_row_naming_another_client_does_not_exclude_sibling_rows(tmp_path, monkeypatch):
    (tmp_path / "corpus").mkdir()
    (tmp_path / "corpus" / "options.md").write_text(
        "## Options\n"
        "| Option ID | Description |\n"
        "|---|---|\n"
        "| `3` | Login GPS Check |\n"
        "| `317` | Enable Salbeshian Hospital Invoice |\n"
    )
    monkeypatch.setattr(config, "work_dir", lambda client: tmp_path / "work" / client)
    (tmp_path / "work" / "morec").mkdir(parents=True)

    result = docs.build_index("morec", corpus_dir=tmp_path / "corpus")
    assert result == {"indexed": 1, "excluded": 1}
    assert docs.search("morec", "Login GPS Check")
    assert docs.search("morec", "Salbeshian") == []


def _write_corpus(tmp_path):
    tmp_path.mkdir(parents=True, exist_ok=True)
    (tmp_path / "guide.md").write_text(
        "# User Guide\n"
        "## Price Lists\n"
        "خيارات نظام تتحكم في سلوك الفواتير. A price list controls item pricing.\n"
        "## Zumot Special Promo\n"
        "Use Promo 14 Input By Invoice Amount_Zumot is a client-specific option.\n"
    )
    return tmp_path


def test_build_index_excludes_other_client_chunk(tmp_path, monkeypatch):
    corpus = _write_corpus(tmp_path / "corpus")
    monkeypatch.setattr(config, "work_dir", lambda client: tmp_path / "work" / client)
    (tmp_path / "work" / "morec").mkdir(parents=True)

    result = docs.build_index("morec", corpus_dir=corpus)
    assert result == {"indexed": 1, "excluded": 1}


def test_search_finds_entitled_chunk_but_not_other_client_chunk(tmp_path, monkeypatch):
    corpus = _write_corpus(tmp_path / "corpus")
    monkeypatch.setattr(config, "work_dir", lambda client: tmp_path / "work" / client)
    (tmp_path / "work" / "morec").mkdir(parents=True)
    docs.build_index("morec", corpus_dir=corpus)

    hits = docs.search("morec", "price list")
    assert any("Price Lists" in h["heading"] for h in hits)
    assert not any("zumot" in (h["heading"] + h["excerpt"]).lower() for h in hits)

    # C5 isolation: a chunk naming another client must not be retrievable
    # by morec even when searched for directly by its own distinctive term.
    assert docs.search("morec", "Zumot promo") == []


def test_search_arabic_prefix_recall(tmp_path, monkeypatch):
    """Measured trigram property this module's docstring relies on:
    substring matching is directional. The corpus here has the bare form
    'نظام' (no definite article) -- a bare query still finds it (trivial
    substring), and a PREFIXED query ('النظام') must ALSO find it only
    because _fts_query strips the 'ال' and ORs in the bare form too. If
    this regression ever fails, the docstring's claim and _fts_query's
    stripping both need revisiting together."""
    corpus = _write_corpus(tmp_path / "corpus")
    monkeypatch.setattr(config, "work_dir", lambda client: tmp_path / "work" / client)
    (tmp_path / "work" / "morec").mkdir(parents=True)
    docs.build_index("morec", corpus_dir=corpus)

    assert docs.search("morec", "نظام")
    assert docs.search("morec", "النظام")


def test_fts_query_strips_al_prefix_but_keeps_original_term_too():
    q = docs._fts_query("النظام")
    assert q == '"النظام" OR "نظام"'


def test_fts_query_does_not_strip_short_words_starting_with_al():
    """'ال' + a 1-letter remainder isn't a real stripped word -- don't
    mangle it down to noise."""
    q = docs._fts_query("الو")
    assert q == '"الو"'


def test_search_returns_empty_list_when_no_index_built(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "work_dir", lambda client: tmp_path / "work" / "nobody")
    assert docs.search("nobody", "anything") == []


def test_fts_query_neutralizes_syntax_and_injection_characters():
    """An arbitrary user question must never be interpretable as FTS5 query
    syntax -- unbalanced quotes, boolean operators, a leading NOT-dash."""
    q = docs._fts_query('weird "quote -injection AND test')
    assert q == '"weird" OR "quote" OR "injection" OR "AND" OR "test"'


def test_fts_query_empty_input_is_a_valid_no_op_query():
    assert docs._fts_query("   ") == '""'


def _build_custom_index(tmp_path, monkeypatch, corpus_dir):
    monkeypatch.setattr(config, "work_dir", lambda client: tmp_path / "work" / client)
    (tmp_path / "work" / "morec").mkdir(parents=True)
    docs.build_index("morec", corpus_dir=corpus_dir)


def test_search_drops_toc_rows(tmp_path, monkeypatch):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "guide.md").write_text("## Real Section\ninvoice approval workflow here.\n")
    (corpus / "toc.md").write_text("## Table of Contents\ninvoice list of chapters.\n")
    _build_custom_index(tmp_path, monkeypatch, corpus)

    hits = docs.search("morec", "invoice", limit=5)
    assert hits
    assert all("table of contents" not in h["heading"].lower() for h in hits)
    assert any("Real Section" in h["heading"] for h in hits)


def test_search_synthetic_heading_for_headingless_chunks(tmp_path, monkeypatch):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    long_text = "A" * 50 + "\n" + "B" * 50
    (corpus / "user_guide.md").write_text(long_text + "\n")
    _build_custom_index(tmp_path, monkeypatch, corpus)

    hits = docs.search("morec", "AAAA", limit=1)
    assert len(hits) == 1
    assert hits[0]["heading"] == ("A" * 50 + " " + "B" * 29)


def test_search_prefers_back_office_path(tmp_path, monkeypatch):
    corpus = tmp_path / "corpus"
    (corpus / "back-office").mkdir(parents=True)
    (corpus / "back-office" / "sales.md").write_text("## BO Sales\nassign customers to salesperson route.\n")
    (corpus / "user_guide.md").write_text("assign customers to salesperson from generic guide.\n")
    _build_custom_index(tmp_path, monkeypatch, corpus)

    hits = docs.search("morec", "assign customers salesperson", limit=2)
    assert len(hits) >= 2
    assert hits[0]["source"].startswith("back-office/")


def test_fts_query_ar_synonym_expansion_for_invoice_group():
    q = docs._fts_query("ما هي الفاتورة", locale="ar")
    assert '"فاتورة"' in q
    assert '"فواتير"' in q
    assert '"فاتورتي"' in q


def test_fts_query_en_locale_does_not_expand_arabic_synonyms():
    q_ar = docs._fts_query("فاتورة", locale="ar")
    q_en = docs._fts_query("فاتورة", locale="en")
    assert q_en == '"فاتورة"'
    assert q_ar != q_en
    assert '"فواتير"' in q_ar


def test_fts_query_synonym_cap_at_original_plus_six():
    question = "فاتورة طلب مندوب extra1 extra2 extra3 extra4 extra5 extra6 extra7"
    q = docs._fts_query(question, locale="ar")
    terms = [part.strip('"') for part in q.split(" OR ")]
    original = len(docs._WORD_RE.findall(question))
    assert len(terms) <= original + 6


def test_fts_query_locale_none_skips_synonym_expansion():
    q = docs._fts_query("فاتورة", locale=None)
    assert q == '"فاتورة"'


def test_fts_query_ar_en_bridge_for_system_options():
    q = docs._fts_query("خيار نظام فواتير تابلت", locale="ar")
    assert '"system"' in q
    assert '"option"' in q
    assert '"invoice"' in q or '"Invoicing"' in q


def test_fts_query_strips_arabic_diacritics_before_tokenizing():
    q = docs._fts_query("كيف تُسند الزبائن", locale="ar")
    assert '"تسند"' in q
    assert '"assign"' in q


def test_fts_query_ar_assign_customers_salesman_synonyms():
    q = docs._fts_query("كيف تعيين الزبائن للمندوب", locale="ar")
    assert '"تعيين"' in q
    assert '"assign"' in q
    assert '"customers"' in q
    assert '"salesman"' in q or '"salesperson"' in q


def test_search_boosts_customers_48_assign_heading(tmp_path, monkeypatch):
    corpus = tmp_path / "corpus"
    (corpus / "back-office").mkdir(parents=True)
    (corpus / "back-office" / "customers.md").write_text(
        "4.8 Customers - Assign Customers for Salesman\n"
        "Choose salesman Position then check customers and press Update.\n"
    )
    (corpus / "user_guide.md").write_text(
        "assign customers to salesperson from generic guide without section number.\n"
    )
    _build_custom_index(tmp_path, monkeypatch, corpus)

    hits = docs.search("morec", "كيف تُسند الزبائن للمندوب", locale="ar", limit=2)
    assert hits
    assert "4.8" in hits[0]["heading"] or "Assign Customers" in hits[0]["excerpt"]
    assert hits[0]["source"].startswith("back-office/")
