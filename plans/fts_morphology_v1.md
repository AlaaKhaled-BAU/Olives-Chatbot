# Junior execution plan: FTS morphology (docs recall)

Status: READY TO IMPLEMENT (literal executor)
Python: **python3.13 only**. Never `python3`.
Branch: `deepseek-swap`
Depends on: nothing in `plans/transcript_timing_v1.md` — can run in parallel.

If a test fails, stop. Do not add Chroma, embeddings, Redis, or a full Arabic NLP stack.

---

## Goal (one sentence)

Improve **how-to docs** recall for Arabic noun inflections (فاتورة ↔ فواتير ↔ الفاتورة, زيارة ↔ زيارات, …) without touching SQL totals or adding vector search.

## What morphology means here

SQLite FTS5 with `tokenize='trigram'` does **substring** matching, not Arabic grammar.

| Direction | Works? | Example |
|-----------|--------|---------|
| Bare query → prefixed corpus | Yes | Query `نظام` hits chunk containing `النظام` (shorter inside longer) |
| Prefixed query → bare corpus | Partially | `_fts_query` strips leading `ال` and ORs both forms |
| Different inflections (not substrings) | **No** | Corpus `فاتورة` does **not** match query `الفواتير` unless we expand one side |

`normalize_ar()` + `ال` strip in `_fts_query` is **not** a stemmer. Root morphology (فاتورة/فواتير/الفاتورة) is a separate recall ceiling — see module docstring in `core/docs.py`.

**Scope boundary:** morphology fixes **search_docs / how-to** only. Invoice **SQL totals** are not a docs problem — do not index money tables or add embeddings “for Arabic.”

## What already exists (do not re-invent)

| Piece | Where |
|-------|--------|
| Query-time synonym OR (`locale=="ar"`) | `_SYNONYM_GROUPS`, `_AR_EN_BRIDGE`, `_fts_query()` |
| Alef/diacritic norm (env-gated) | `DOCS_AR_NORM`, `normalize_ar()` |
| Client locale → search | `_search_docs()` in `core/agent.py` |
| Tests for query expansion | `tests/test_docs.py` (`test_fts_query_ar_synonym_*`) |

Query expansion helps when the **question** contains a group member (e.g. `الفواتير` → also searches `فاتورة`). It does **not** help when the corpus chunk has only `فواتير` and the user asks `فاتورة` without firing the group, or when `locale` is not `ar`. **Index-time aliases** fix the corpus→query direction for a curated noun list.

---

## Locked strategy (cheap → expensive)

1. **Do nothing for invoice SQL.** No agent prompt changes for “مبيعات الفواتير” style totals.
2. **Index-time extra tokens** for a short list of high-traffic Arabic nouns (reuse `_SYNONYM_GROUPS` Arabic members). Not a full morphology engine.
3. **Only if evals still fail after (2):** ISRI-style stem on **query only**; index stays as-is. Measure before/after on `evals/docs_accuracy.jsonl` + `evals/docs_105_ar.jsonl`.
4. **Never** add Chroma or embeddings “to fix Arabic.” Embeddings miss inflections unless you invest in Arabic models — and you still must not embed money/tenant data.

---

## Lane 0 — index-time alias injection (implement this)

### Files

- `core/docs.py` (primary)
- `tests/test_docs.py`
- Rebuild index after merge: `python3.13 setup/05_index_docs.py --client morec`

### Step 0.1 — shared morphology map

Add a constant **next to** `_SYNONYM_GROUPS` (do not duplicate unrelated English assign-customer keys in the index pass):

```python
# Arabic noun forms only — appended to indexed text so trigram sees every variant.
# Keep in sync with the Arabic members of _SYNONYM_GROUPS (invoice, order, visit, salesman).
_MORPHOLOGY_ALIASES: tuple[tuple[str, ...], ...] = (
    ("فاتورة", "فواتير", "الفاتورة", "الفواتير", "فاتورتي"),
    ("طلب", "طلبات", "الطلب", "الطلبات"),
    ("زيارة", "زيارات", "الزيارة", "الزيارات"),
    ("مندوب", "مناديب", "مندوبين", "المندوب"),
)
```

Junior rule: when you add a row to `_SYNONYM_GROUPS` for a new Arabic noun family, add the same family here with definite-article forms.

### Step 0.2 — `_index_text_with_morphology(body: str) -> str`

```python
def _index_text_with_morphology(body: str) -> str:
    """Append alias tokens for any morphology group hit in the chunk."""
    norm = normalize_ar(body)
    extras: list[str] = []
    for group in _MORPHOLOGY_ALIASES:
        group_lower = {g.lower() for g in group}
        if not any(g in norm for g in group):  # substring on normalized text
            continue
        for alias in group:
            if alias not in extras and alias not in norm:
                extras.append(alias)
    if not extras:
        return norm
    return norm + "\n" + " ".join(extras)
```

Use **substring** presence (`g in norm`) not token equality — corpus may say `الفواتير` inside a sentence.

Cap appended aliases at **20 tokens per chunk** (safety). If over cap, truncate extras list.

### Step 0.3 — wire into `build_index`

Replace:

```python
(source_file, heading_path, normalize_ar(text)),
```

with:

```python
(source_file, heading_path, _index_text_with_morphology(text)),
```

`heading_path` is **not** aliased (headings are short; body carries the terms).

### Step 0.4 — tests (hermetic, tmp corpus)

Add to `tests/test_docs.py`:

**test_index_morphology_appends_invoice_aliases**

- Corpus chunk body: `شرح إنشاء فاتورة جديدة` (only singular).
- Build index, search `morec` with query `الفواتير`, `locale="ar"`.
- Assert at least one hit whose excerpt still contains `فاتورة` (user-visible text unchanged; aliases are on the indexed copy only — excerpt returns stored text which includes appended line).

Actually: stored text **includes** appended aliases at end. That is OK — excerpt may show trailing alias tokens. Alternative: store aliases after `\x1e` separator and strip in `search()` before returning excerpt. **Prefer simpler:** append on new line; accept that excerpt may end with alias words. Document in test comment.

**test_index_morphology_no_alias_when_no_group_hit**

- Body about GPS only → indexed text equals `normalize_ar(body)` (no extra line).

**test_morphology_roundtrip_fawateer_finds_fatura_chunk**

- Body: `خطوات فاتورة` only.
- `search(..., "ما هي الفواتير", locale="ar")` returns ≥1 hit.

Run:

```bash
python3.13 -m pytest tests/test_docs.py -q -k morphology
```

### Step 0.5 — rebuild + smoke

```bash
python3.13 setup/05_index_docs.py --client morec
python3.13 -m pytest tests/test_docs.py -q
```

---

## Lane 1 — eval gate (after Lane 0 green)

### Before/after harness

Add `evals/run_docs_morphology_ab.py` (or extend existing docs eval runner if one exists):

1. Build tmp index from a fixed tiny corpus (2–3 md files) with morphology on.
2. Run probe questions:

| Probe | Corpus contains | Query | Must hit |
|-------|-----------------|-------|----------|
| inv-sg-pl | `فاتورة` only | `الفواتير` | yes |
| visit-pl-sg | `زيارات` only | `زيارة` | yes |
| no-false | English GPS chunk | `فاتورة` | no |

3. Run full suite (if `work/morec/docs.sqlite` exists):

```bash
# Document in script header — needs DEEPSEEK only if agent-backed; pure FTS can call docs.search directly
python3.13 evals/run_docs_morphology_ab.py --client morec
```

Record recall@5 on `evals/docs_accuracy.jsonl` and `evals/docs_105_ar.jsonl` **before** and **after** reindex. Commit a one-line result in the PR description, not a new golden file, unless recall regresses.

**Merge rule:** Lane 0 merges if unit tests pass and probe table is green. Full 105-ar battery is **nightly / pre-client-drop**, not CI blocker (same as other accuracy evals).

---

## Lane 2 — ISRI query stem (ONLY if Lane 1 shows regressions or probes still fail)

**Do not start Lane 2 unless Lane 0 + 1 are merged and a human flags failing probes.**

### Approach

- Add optional dependency or vendored ~50-line ISRI stemmer (query side only).
- Behind env `DOCS_AR_STEM=1` (default off).
- In `_fts_query`, after `normalize_ar`, stem each Arabic token **in addition to** literal + synonym expansion (OR all forms).
- **Never** stem index text.
- A/B again on the same probe set; adopt only if recall strictly improves with zero new false positives on English-only queries.

**Explicit skip:** snowball-ar, CAMeL Tools, full morphological analyzers — out of scope unless product owner expands scope.

---

## NOT in scope

- Chroma / sqlite-vec / embeddings for docs
- Morphology for SQL / `run_select` / vault cards
- Changing `MAX_HISTORY_TURNS`, transcript, widget, login, EXEC allow-list
- Folding ة→ه or aggressive stemmers at index time
- Synonym expansion when `locale != "ar"` (separate ticket if needed)

---

## Acceptance

```bash
python3.13 -m pytest tests/test_docs.py -q
python3.13 setup/05_index_docs.py --client morec
python3.13 evals/run_docs_morphology_ab.py --client morec   # after script exists
```

---

## GSTACK REVIEW REPORT

| Review | Status |
|--------|--------|
| Product | morphology = docs/how-to only; SQL totals untouched |
| Eng | index-time aliases reuse `_SYNONYM_GROUPS` noun families |
| Risk | trailing alias tokens in excerpt — acceptable v1 |

NO UNRESOLVED DECISIONS
