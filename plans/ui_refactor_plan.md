# UI Refactor Plan — «Data Cockpit» reskin (UI/UX only)

Hard constraint: **zero backend/API changes**. Touches ONLY `static/` —
`style.css` (rewrite), `index.html` (restructure, all IDs preserved),
`app.js` (surgical: rich renderer + skeleton + empty-state hide),
`static/fonts/` (new, self-hosted). Every selector app.js depends on stays.

Decisions locked: **D1=A** auto both themes, dark default · **D2=B** self-hosted woff2.

---

## Lanes (parallel; ▸ = depends on)

```
L1 tokens+fonts   ─────────────┐
L2 index.html shell────────────┤
L3 style.css components ───────┼──► L5 verify gate (browser+mobile+pytest+qa loop)
L4 app.js surgical (renderer,  │
   skeleton, empty-state) ─────┘
```
L1–L4 are independent file scopes; only L5 is a join point.

## L1 — Foundation
- `:root` dark tokens: bg #0b1220, surface #111a2b, surface-2 #182338, border
  #ffffff14, text #e6edf6 / dim #9aa7ba, accent emerald #10b981, accent-2 cyan
  #06b6d4, danger/warn; radii 8/12/16; shadows ×2; fonts vars.
- Light theme via `[data-theme="light"]` overrides; tiny JS in app.js:
  `matchMedia('(prefers-color-scheme: light)')` sets attr + listens (auto, dark
  default; attribute override enables QA force-testing).
- Fonts: download IBM Plex Sans Arabic 400/500/700 + IBM Plex Mono 400/600
  woff2 → `static/fonts/`; `@font-face` with `font-display: swap`;
  fallback stacks kept so air-gapped missing-file case degrades gracefully.

## L2 — index.html shell
- `data-theme="dark"` on <html>; keep `lang=ar dir=rtl`, title, «مساعد بيانات»
  string (pytest asserts it), ALL existing IDs (`company-label`,
  `company-select`, `client-label`, `as-of-label`, `db-*`, `messages`,
  `ask-form`, `question`).
- Header → brand block (inline SVG mark) + consolidated status chips.
- New `#empty-state` hero: mark, one-liner, 4 starter-question chips
  (`data-q`), hidden by JS on first message.
- Composer stays a form#ask-form; visual only.

## L3 — style.css rewrite (~600 lines, token-driven)
- Glass sticky header; 760px column; composer as pinned glass footer.
- Assistant answers: flat surface cards with accent rail (no gray bubble);
  user: compact accent-tinted bubble aligned end.
- Markdown targets: `.md pre/code` (terminal block, dir=ltr), `.md-table`
  (sticky header, zebra, numeric cells `font-mono` + LTR), lists, bold,
  inline-code.
- `.sql-panel` terminal restyle (keep class + copy button behavior).
- Sources → chips; followups → pills w/ hover lift; feedback → ghost icon
  buttons; `.msg.en` keeps LTR hint; `unicode-bidi` rules retained.
- db-console: keep animated-border identity, retint via tokens, unify input
  heights.
- States: `.typing` three-dot skeleton, streaming caret, `.error-banner`.
- Empty-state hero styles; starter chips reuse `.chip` look.
- A11y: contrast ≥4.5 both themes, `:focus-visible` rings,
  `prefers-reduced-motion` kills orb/shake/spin animations.

## L4 — app.js surgical edits
1. `renderRich(text)`: HTML-escape → transform fenced code → inline code →
   bold → pipe-tables (with `---` separator detection) → lists → <br>.
   Applied to assistant messages only; user messages keep textContent.
2. Typing skeleton: inserted in `ask()` before fetch, removed on first
   chunk/done/error (guard all exits).
3. Empty-state hide on first `addMessage`; starter chips fill+submit.
4. Theme attr setter (6 lines, L1).
Nothing else — no API, no fetch-shape changes, no class renames used by logic.

## L5 — Verify gate
1. Browser: dark + forced-light screenshots (desktop + 375px).
2. Flow: ask → rich answer (code block + table + bold) → SQL panel →
   followups → sources → CSV button present; db-console connect flow intact.
3. Console error-free; bidi spot («25 زبونًا»); ISSUE-002 confirmed dead.
4. `pytest tests -q` → 353 passed / 7 pre-existing env failures unchanged
   (static index assertion intact).
5. /qa-style fix-verify loop on anything found; update
   `.gstack/qa-reports/baseline.json` visual scores.
