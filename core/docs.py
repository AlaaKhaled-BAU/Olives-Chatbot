"""C5: documentation Q&A via SQLite FTS5 (stdlib sqlite3 -- no embeddings, no
vector DB, no new dependency). Corpus is docs_corpus/ (setup/04_assemble_
docs_corpus.py's symlinked view over the real markdown docs), chunked by
heading, indexed once per client at setup time (setup/05_index_docs.py)
into work/<client>/docs.sqlite.

Tokenizer: trigram, not unicode61 -- it does substring matching, not word
matching. Measured on this box (SQLite 3.45.1) and directional, not the
symmetric "absorbs prefixes" it first looks like: query 'نظام' (bare) DOES
match corpus text containing 'النظام' (prefixed) -- the bare form is a
substring of the prefixed one -- but query 'النظام' (prefixed) does NOT
match corpus text containing only 'نظام' (bare), since the longer string
can never be a substring of the shorter one. Since a real Arabic question
usually carries the definite article ("ما هو النظام") while corpus prose
may or may not, _fts_query strips a leading 'ال' from each word (keeping
both forms in the OR) so a prefixed query can still find bare-form corpus
text -- without this, the more common real direction would silently lose
recall. This still does NOT handle root morphology: a corpus row with
'فاتورة' will not match a query for 'الفواتير' (different root-derived
forms, not a prefix/substring relationship at all). That is a real recall
ceiling -- report Arabic-vs-English retrieval recall separately in evals
rather than implying full Arabic search. Also confirmed case-insensitive
by default (GPS/gps/Gps all match the same row) -- no manual folding needed.

Short numeric anchors rank poorly. Measured live: "what does system option
3 control" found the right row (system_options_guide.md's "`3` | Login To
Cust GPS Check" table row) but ranked #54 among 953 matches, invisible at
any reasonable `limit` -- a 1-2 digit query term is a substring of huge
swaths of unrelated content (any price, date, or other option's ID), so
rank (matched-term density) doesn't favor the row where it's the
meaningful whole ID. A 3+ digit ID (e.g. "157", "211") ranks first
reliably -- there just isn't enough unrelated content sharing a 3-digit
substring to compete. No query-side fix attempted (boosting numeric-ID
matches would be real complexity for one content shape); documented here
and reflected in which option numbers evals/docs_accuracy.jsonl uses.

Confidentiality: identical reasoning to core/catalog.py's proc entitlement
(same CLIENT_NAME_TOKENS + per-deployment client-name universe) applied to
free-text chunks instead of a proc-name tail. Applied at INDEX time, one
docs.sqlite per client, so a client's index physically never contains a
chunk naming another client's customization -- there is no query-time
filter to accidentally bypass.
"""
import os
import re
import sqlite3
import unicodedata
from pathlib import Path

from . import catalog, config

BASE_DIR = Path(__file__).resolve().parent.parent
CORPUS_DIR = BASE_DIR / "docs_corpus"

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
_PARAGRAPH_RE = re.compile(r"\n\s*\n+")
_TABLE_SEP_RE = re.compile(r"^\|?[\s:|-]+\|?$")
_WORD_RE = re.compile(r"\w+", re.UNICODE)


def _split_table_rows(paragraph: str):
    """A markdown table (header + |---|---| separator + data rows) with no
    blank lines between rows survives _PARAGRAPH_RE as ONE paragraph --
    measured on system_options_guide.md, where this collapsed entire
    ~100-400-option categories (Pricing & Discounts, Invoicing & Sales
    Orders) into a single chunk each, so ONE option row naming another
    client excluded the other ~99% of that category along with it. Splits
    into one chunk per data row, each still prefixed with the header row
    so the column meaning ("Option ID | Description | ...") survives
    standalone -- and so entitlement filtering runs per-row instead of
    per-table."""
    lines = paragraph.splitlines()
    header = lines[0]
    for row in lines[2:]:
        if row.strip():
            yield header + "\n" + row


def _split_paragraphs(text: str):
    """Fallback chunking unit for a span with no heading to split on --
    measured on the real corpus: most of it (back-office/*.md,
    front-office/*.md, user_guide.md -- 31 of 33 files) is a hand-converted
    PDF/DOCX with NO markdown heading syntax at all, only blank-line
    paragraphs. Without this, those files would each index as a single
    multi-hundred-line chunk (user_guide.md alone would be one 206KB row),
    which still technically searches but cites as "user_guide.md › " for
    ANY match anywhere in it -- useless for the "cite your source" rule.
    A paragraph that is itself a markdown table is exploded further, one
    chunk per row (see _split_table_rows)."""
    chunks = []
    for p in (p.strip() for p in _PARAGRAPH_RE.split(text)):
        if not p:
            continue
        lines = p.splitlines()
        if len(lines) >= 3 and lines[0].lstrip().startswith("|") and _TABLE_SEP_RE.match(lines[1].strip()):
            chunks.extend(_split_table_rows(p))
        else:
            chunks.append(p)
    return chunks


def _chunks(text: str):
    """Yield (heading_path, body) for a markdown document. heading_path is
    a ' › '-joined breadcrumb of every ancestor heading currently open
    (e.g. "System Options Guide › GPS / Geofencing / Map"); body is one
    paragraph from that span (see _split_paragraphs). A span with no
    heading at all (or the preamble before the first heading) yields
    heading_path=""."""
    stack = []  # [(level, title), ...] -- innermost currently-open heading last
    matches = list(_HEADING_RE.finditer(text))
    if not matches:
        for para in _split_paragraphs(text):
            yield "", para
        return
    if matches[0].start() > 0:
        for para in _split_paragraphs(text[: matches[0].start()]):
            yield "", para
    for i, m in enumerate(matches):
        level, title = len(m.group(1)), m.group(2).strip()
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        heading_path = " › ".join(t for _, t in stack)
        for para in _split_paragraphs(text[m.end() : end]):
            yield heading_path, para


def _iter_corpus_md_files(corpus_dir: Path):
    """Yield every ``.md`` file under corpus_dir, following symlinked subdirs.

    ``docs_corpus/back-office`` is a symlink to ``knowledge/guide-headed/…``;
    ``Path.rglob`` does not descend into symlinked directories on Python 3.13."""
    for root, _dirs, files in os.walk(corpus_dir, followlinks=True):
        root_path = Path(root)
        for name in sorted(files):
            if name.lower().endswith(".md"):
                yield root_path / name


def iter_corpus_chunks(corpus_dir: Path = CORPUS_DIR):
    """(source_file, heading_path, text) for every .md file under
    corpus_dir -- walks symlinked back-office/front-office trees set up by
    04_assemble_docs_corpus.py."""
    for path in sorted(_iter_corpus_md_files(corpus_dir)):
        text = path.read_text(errors="replace")
        rel = path.relative_to(corpus_dir)
        for heading_path, body in _chunks(text):
            yield str(rel), heading_path, body


def _mentions_other_client(text: str, own_tokens: set, all_tokens: set) -> bool:
    """Same rule as catalog._entitled: a chunk is excluded unless every
    client-name token it contains is also one of this client's own names.
    catalog._SEGMENT_RE splits on non-[a-z0-9], so a run of Arabic prose
    around a Latin client name (e.g. "...مرحبا Kaylani توزيع...") still
    isolates "kaylani" as its own segment -- every real name in
    CLIENT_NAME_TOKENS is Latin-script, so this reuses catalog's
    tokenization unchanged rather than needing an Arabic-aware variant."""
    words = set(catalog._SEGMENT_RE.split(text.lower()))
    hit = words & all_tokens
    return bool(hit - own_tokens)


def db_path(client: str) -> Path:
    return config.work_dir(client) / "docs.sqlite"


def build_index(client: str, corpus_dir: Path = CORPUS_DIR) -> dict:
    """Rebuild work/<client>/docs.sqlite from scratch. Returns
    {"indexed": n, "excluded": n} -- run at setup time
    (setup/05_index_docs.py), never per-query."""
    client_config = config.load_client(client)
    own_tokens = {a.lower() for a in client_config.get("name_aliases", [client])}
    all_tokens = catalog.CLIENT_NAME_TOKENS | catalog._registered_client_tokens()

    path = db_path(client)
    path.unlink(missing_ok=True)
    conn = sqlite3.connect(path)
    try:
        conn.execute(
            "CREATE VIRTUAL TABLE docs USING fts5(source_file, heading_path, text, tokenize='trigram')"
        )
        indexed = excluded = 0
        for source_file, heading_path, text in iter_corpus_chunks(corpus_dir):
            if _mentions_other_client(text, own_tokens, all_tokens) or \
               _mentions_other_client(heading_path, own_tokens, all_tokens):
                excluded += 1
                continue
            conn.execute(
                "INSERT INTO docs (source_file, heading_path, text) VALUES (?, ?, ?)",
                (source_file, heading_path, text),
            )
            indexed += 1
        conn.commit()
    finally:
        conn.close()
    return {"indexed": indexed, "excluded": excluded}


_AL_PREFIX = "ال"
_TOC_RE = re.compile(r"(?i)table of contents|^toc$")
_PAGE_NUM_RE = re.compile(r"^\d{1,4}$")
_SYNONYM_GROUPS = (
    ("فاتورة", "فواتير", "فاتورتي"),
    ("طلب", "طلبات"),
    ("مندوب", "مناديب", "مندوبين", "salesman", "salesperson"),
    ("معلق", "suspended", "IsSuspended"),
    (
        "assign", "customers", "salesman", "4.8",
        "تعيين", "أسند", "اسند", "تسند", "إسناد", "سند",
        "زبائن", "زبون", "مندوب",
    ),
)
# Arabic UI terms → English corpus glosses (docs index is mostly English).
_AR_EN_BRIDGE = {
    "خيار": ("option",),
    "نظام": ("system",),
    "فواتير": ("invoice", "Invoicing"),
    "فاتورة": ("invoice",),
    "فاتورتي": ("invoice",),
    "تابلت": ("tablet",),
    "معلق": ("suspended",),
    "زبون": ("customer",),
    "زبائن": ("customer", "customers"),
    "عميل": ("customer",),
    "سند": ("assign",),
    "تسند": ("assign",),
    "إسناد": ("assign",),
    "تعيين": ("assign",),
    "أسند": ("assign",),
    "اسند": ("assign",),
    "مندوب": ("salesman", "salesperson"),
    "مندوبين": ("salesman", "salesperson"),
    "للمندوب": ("salesman", "salesperson"),
    "باك": ("back-office",),
    "أوفيس": ("office",),
    "اعتماد": ("approve", "approval"),
}
_ASSIGN_HEADING_RE = re.compile(
    r"(?i)4\.8|assign customers for salesman",
)


def _strip_ar_diacritics(text: str) -> str:
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


def _path_priority(source_file: str) -> int:
    sf = source_file.replace("\\", "/").lower()
    if "back-office/" in sf:
        return 0
    if "support-agent/" in sf or "system_options" in sf:
        return 1
    return 2


def _assignment_boost(heading: str, excerpt: str) -> int:
    """Prefer customers.md §4.8 (Assign Customers for Salesman) over generic
    assign-customer prose elsewhere in the corpus."""
    text = f"{heading}\n{excerpt}"
    if _ASSIGN_HEADING_RE.search(heading):
        return 2
    if _ASSIGN_HEADING_RE.search(text):
        return 1
    return 0


def _synthetic_heading(text: str) -> str:
    return text.replace("\n", " ").strip()[:80]


def _is_noise_chunk(heading_path: str, text: str) -> bool:
    """Drop TOC rows and headingless PDF conversion debris (page numbers, stubs)."""
    hp = heading_path.strip()
    if hp and _TOC_RE.match(hp):
        return True
    body = text.strip()
    if not body:
        return True
    if not hp:
        if _TOC_RE.search(body[:240]):
            return True
        if _PAGE_NUM_RE.match(body):
            return True
        if len(body) < 20:
            return True
    return False


def _question_tokens(question: str) -> set[str]:
    tokens: set[str] = set()
    for w in _WORD_RE.findall(_strip_ar_diacritics(question)):
        tokens.add(w.lower())
        if w.startswith(_AL_PREFIX) and len(w) >= 4:
            tokens.add(w[len(_AL_PREFIX) :].lower())
    return tokens


def _fts_query(question: str, locale: str | None = None) -> str:
    """Every word double-quoted (embedded quotes doubled per FTS5 escaping)
    and OR'd together -- an arbitrary user question can never be read as
    FTS5 query syntax (AND/OR/NOT/NEAR, a leading '-', unbalanced quotes).

    A word starting with the Arabic definite article also contributes its
    bare form (module docstring: trigram substring matching means a
    prefixed query alone would miss bare-form corpus text). >= 4 chars
    before stripping so a 2-3 letter word that only coincidentally starts
    with the same two letters isn't mangled down to nothing useful.

    When locale is ``ar``, up to three synonym groups expand for tokens
    present in the question (after ``ال`` strip). Total quoted terms are
    capped at original term count + 6."""
    words = _WORD_RE.findall(_strip_ar_diacritics(question))
    if not words:
        return '""'
    terms, seen = [], set()
    for w in words:
        candidates = (w, w[len(_AL_PREFIX):]) if w.startswith(_AL_PREFIX) and len(w) >= 4 else (w,)
        for t in candidates:
            key = t.lower()
            if key not in seen:
                seen.add(key)
                terms.append(t)
    original_count = len(terms)
    max_terms = original_count + 6

    if locale == "ar":
        q_tokens = _question_tokens(question)
        groups_fired = 0
        for group in _SYNONYM_GROUPS:
            if groups_fired >= 3:
                break
            group_lower = {g.lower() for g in group}
            if not (q_tokens & group_lower):
                continue
            groups_fired += 1
            for syn in group:
                syn_key = syn.lower()
                if syn_key in seen:
                    continue
                if len(terms) >= max_terms:
                    break
                seen.add(syn_key)
                terms.append(syn)
        bridge_added = 0
        for ar_tok, en_terms in _AR_EN_BRIDGE.items():
            if bridge_added >= 4 or ar_tok not in q_tokens:
                continue
            for en in en_terms:
                if len(terms) >= max_terms:
                    break
                en_key = en.lower()
                if en_key in seen:
                    continue
                seen.add(en_key)
                terms.append(en)
                bridge_added += 1
    return " OR ".join('"' + t.replace('"', '""') + '"' for t in terms)


def search(client: str, query: str, limit: int = 5, locale: str | None = None) -> list:
    """[{source, heading, excerpt}, ...], best match first. Returns []
    (not an error) when this client has no docs index yet -- a missing
    setup/05_index_docs.py run should degrade the tool to 'no results',
    not crash the agent loop.

    Post-fetch: drop TOC rows, synthesize headings for headingless chunks,
    re-sort by back-office path priority, then take ``limit`` survivors.
    ``locale`` gates Arabic synonym expansion in ``_fts_query`` (``ar`` only).

    "excerpt" is the FULL chunk text, not FTS5's snippet(). Measured live:
    snippet()'s "best 30-token window" heuristic picks the window with the
    most raw term hits, which for a table-row chunk ("| Option ID |
    Description | ... |\\n| `157` | Cust LogOut GPS Check | ... |") is the
    generic HEADER line (2 hits for "option") -- not the data row with the
    answer (1 hit for "157") -- so it truncated to "| Option ID |
    Description | ... " and never showed the row at all. That produced a
    real end-to-end failure: the agent found the right chunk on the first
    search every time, was handed a snippet with no actual content, and
    burned its whole turn budget re-querying before giving up. Chunks here
    are already heading/paragraph/table-row-sized (measured: median 87
    chars, p99 935, max 3343 across the real corpus) -- small enough that
    returning the whole thing outright is both simpler and correct."""
    path = db_path(client)
    if not path.exists():
        return []
    conn = sqlite3.connect(path)
    try:
        rows = conn.execute(
            "SELECT source_file, heading_path, text "
            "FROM docs WHERE docs MATCH ? ORDER BY rank LIMIT ?",
            (_fts_query(query, locale=locale), limit * 4),
        ).fetchall()
    finally:
        conn.close()

    survivors = []
    for rank, (source_file, heading_path, text) in enumerate(rows):
        if _is_noise_chunk(heading_path, text):
            continue
        heading = heading_path.strip() or _synthetic_heading(text)
        survivors.append(
            {
                "source": source_file,
                "heading": heading,
                "excerpt": text,
                "_path_priority": _path_priority(source_file),
                "_assignment_boost": _assignment_boost(heading, text),
                "_original_rank": rank,
            }
        )

    survivors.sort(
        key=lambda row: (
            row["_path_priority"],
            -row["_assignment_boost"],
            row["_original_rank"],
        )
    )
    return [
        {"source": row["source"], "heading": row["heading"], "excerpt": row["excerpt"]}
        for row in survivors[:limit]
    ]
