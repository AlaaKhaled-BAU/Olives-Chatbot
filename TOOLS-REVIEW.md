# Tool Review — Grilled Against the client-chatbot Plan

> Standalone cleanup removed the raw research archive; decisions live here and in `PLAN.md`. Each tool judged on one question:

---

## TL;DR

**Keep the PoC plan as-is.** Nothing here is worth rebuilding a read-only SQL Q&A PoC around. Most of these tools optimize a different axis than ours (user personalization, web scraping, generic text-to-SQL) — and generic text-to-SQL is the exact thing our catalog-first design exists to avoid.

**Three finds that map to real, already-named phases (not the PoC core):**
1. **Metabase** — evaluate for the **reports / dashboard / push-report surface** (the deferred "80% of value, 5% of complexity" channel). **Not** the chatbot core: its Metabot NL→SQL undercuts our accuracy moat, and it doesn't know our 1,450 procs.
2. **OmniRoute** — a concrete implementation of the **central LLM gateway / key broker** the plan already defers. Adopt at gateway phase; pin Claude as primary, use fallback only for outages (never load-balance an accuracy-critical path across 290 providers).
3. **MinerU** — **Arabic-capable** document parsing for the 50MB `OLIVES USER GUIDE.pdf` + `Olives SQL_Documentation.docx` → clean markdown for the docs corpus. Cheap, one-time, later.

**One concept worth stealing now (accuracy win, no framework):** *procedural memory* = a flat file of verified question→proc/SQL mappings used as few-shots. Upgrade to a memory framework only if the eval shows repeat-question value.

**General-experience freebies (low risk, not architecture):** `claude-code-setup` (run it on this repo), `archify` (keep the architecture diagrams in sync), `obsidian-skills` (vault authoring later).

**Everything else:** wrong axis for a read-only SQL Q&A PoC.

---

## Baseline — what we already have (the thing each tool must beat)

- **Runtime:** plain Anthropic tool-use loop (`agent.py`), Flask+SSE chat, `python3.13`.
- **SQL:** `pymssql` + `sqlglot` gate + read-only login + Docker SQL Server (reused from drift-tool).
- **Knowledge:** live schema introspection (accurate, no drift) + the existing 12-tool **obsidian vault MCP** (docs path).
- **Memory:** conversation context (native) + a per-client **param profile** JSON (compno / ClientActive).
- **Accuracy moat:** catalog-first — run one of 1,450 tested **procedures** before generating any SQL.
- **Already built and reusable:** the **drift-tool** (Docker restore, schema introspection, dependency graph from `sys.sql_expression_dependencies`).

---

## Verdict table (all 23)

| # | Tool | Job it does | vs. what we have | Verdict |
|---|------|-------------|------------------|---------|
| 1 | Memory Types (concept) | Cognitive framework | Names the *procedural memory* idea we can use | **Steal 1 idea** |
| 2 | supermemory | User-memory graph | Wrong axis (personalization, not query reuse) | Skip PoC |
| 3 | mem0 | User/session memory | Same; a JSON file beats it for PoC | Hold |
| 4 | TencentDB-Agent-Memory | Team memory hub (L0–L3) | OpenClaw/Hermes-tied; heavy | Skip |
| 5 | turbovec | Rust vector index | We use no embeddings in the PoC | Skip PoC |
| 6 | OpenViking | Context DB / skills FS | Overkill; wrong axis | Skip |
| 7 | LangGraph | Agent orchestration | Its own docs say "overkill for MVP Q&A" | Hold → Idea 2 |
| 8 | Hermes-Agent | Self-improving multi-platform agent | Huge; buries a simple PoC | Hold → platform |
| 9 | **OmniRoute** | Local-first LLM gateway | **Implements our deferred gateway** | **Adopt @ gateway phase** |
| 10 | Gemini API | Model provider | Claude wins on accuracy + Arabic | Skip (maybe fallback) |
| 11 | freellmapi | Free-tier aggregator | Free = unreliable + data-leak risk | Skip (client data) |
| 12 | OpenWiki | Auto codebase wiki | Our drift→vault regen is the SQL-native equivalent | Skip |
| 13 | **MinerU** | Doc → markdown, Arabic OCR | **Ingests the PDF/docx guides** | **Adopt later (docs)** |
| 14 | Hyper-Extract | Text → knowledge graph | DB catalog beats LLM extraction for schema | Skip |
| 15 | qmd | On-device hybrid note search | Upgrade to the docs path *if* regex proves weak | Hold (pocket) |
| 16 | Cloud Run Sandboxes | Untrusted-code sandbox | We run no untrusted code; cloud ≠ on-prem | Skip |
| 17 | awesome-mcp-servers | MCP directory | Reference only | Reference |
| 18 | obsidian-skills | Native vault read/write | Useful when we build vault drafting | Hold → later |
| 19 | free-for-dev | Free-tier SaaS list | Meta reference | Reference |
| 20 | archify | Auto architecture diagrams | Automates the SVGs I hand-draw | Nice-to-have |
| 21 | **Metabase** | Open-source BI + Agent API + MCP | **Could own the reports/push surface** | **Evaluate (plan-relevant)** |
| 22 | Obscura | Rust headless browser | We query a DB, not the web | Skip |
| 23 | claude-code-setup | Repo → automation recommender | Free dev-experience win | **Run it** |

---

## The decision-worthy ones — grilled

### 21 · Metabase — the only real "should we change the plan?" candidate

**For (steelman):** self-hosted BI with a SQL Server driver, granular **row-level permissions + sandboxing**, **Metabot** (NL→SQL), an **Agent API** built for LLMs (capped 200-row results, typed schemas, tool-calling), a **built-in MCP server**, an **embedding SDK** with a ready AI-chat component, and **dashboards + subscriptions** (email/Slack/webhook). On paper it already does 80% of the surface we're hand-building.

**Against (why it doesn't replace the core):**
- **Metabot is generic text-to-SQL — the exact trap we designed around.** It doesn't know Olives' 1,450 procedures, so it *generates* SQL where our plan *runs a tested proc*. Adopting it as the brain trades our #1 asset (procs-as-semantic-layer) for the 10–31%-accuracy problem. Bad trade for an accuracy-first system.
- **Its permission model is Metabase's, not Olives'.** The per-record permissions from `ticket_0004` live in BO tables/procs. We'd have to re-express Olives permission logic inside Metabase's sandboxing — not free, and now in two places.
- **It's query/dashboard-shaped, not proc-execution-shaped.** Running 1,450 parameterized business procs with our resolution order isn't its sweet spot. *(Verify proc-exec support before assuming.)*
- **No Arabic-in / reason-English / Arabic-out loop, no `N'…'` handling, no `@ClientActive` confidentiality.** All the hard, Olives-specific parts still fall to us.
- **A Clojure/JVM platform to run, learn, and bend** vs. a ~12-file Python PoC. Dropping it in is the opposite of "prove the concept simply."

**Honest verdict:** **not** the chatbot core — it would dilute the accuracy moat and add a heavy dependency. **But** it's a strong candidate for the **deferred reports/dashboard/push channel** (the CEO-voice "80% of value" alternative): self-hosted, SQL Server-native, subscriptions built in, real permissions. And its **Agent API design** (capped rows, typed schemas) is a good reference to copy into our `sql_tools`. **Plan touch-point:** when we reach the push-report decision, evaluate Metabase as the delivery surface **instead of** hand-building dashboards + a WhatsApp/email pusher. Keep the chatbot's proc-catalog brain ours.

### 9 · OmniRoute — the gateway we already said we need

**For:** local-first (runs on our servers — fits the hosting decision), OpenAI-compatible `/v1` (the chatbot just changes `base_url`), 4-tier fallback, circuit breakers + key cooldown, **AES-256 encrypted keys** (kills the "raw key on a box" risk the architecture plan flagged), audit trail, even RTK+Caveman compression (which this user already runs). This is almost exactly the "central LLM gateway / key broker" the plan lists as a pre-prod prerequisite.

**Against:** for the **PoC**, a router that can silently swap providers **destroys clean accuracy measurement** — you can't tell if a wrong answer is the pipeline or a substituted model. Adds a 5–50ms hop and one more process. *(Thin-ish repo — verify maturity before betting the prod path on it.)*

**Verdict:** **PoC = direct Anthropic** (deterministic, measurable). **Gateway phase = OmniRoute is a concrete, well-matched candidate** for the deferred gateway — but configure it to **pin Claude as primary and use fallback only on outage/ratelimit**, never load-balance the accuracy path across providers. This is a real plan-item match, just not now.

### 8 · Hermes-Agent — the "Hermes" you asked about originally

**For:** self-improving (skill generation = procedural memory), **multi-platform gateway including WhatsApp/Telegram/Signal** (the deferred push channel, again), model-agnostic, cron scheduling. If the platform vision becomes "one agent, many channels, gets better with use," this is the whole substrate.

**Against:** it's enormous (70+ tools, ~28 toolsets, 25k tests). Wrapping a read-only DB Q&A PoC in it means fighting its abstractions for zero PoC benefit. Its strengths (autonomy, self-improvement, 20+ chat platforms) are all things the PoC explicitly *doesn't* need yet.

**Verdict:** **Hold for the platform, not the PoC.** Revisit if/when we go multi-platform + self-improving (support-assistant territory). Adopting now would bury the thing we're trying to prove.

### 7 · LangGraph — correct to defer, by its own admission

The research's own "when to use" says: **overkill for basic Q&A with 1–3 tools, MVP stage, crash=restart acceptable** — that is precisely our PoC. Its real value (durable execution, human-in-the-loop interrupts, checkpointing, parallel fan-out) is the **support-assistant (Idea 2)** with its approval workflow. **Verdict:** hold → Idea 2. Our plain tool-use loop is the right call for Idea 1.

### 2/3/4/6 · Memory frameworks (supermemory, mem0, TencentDB, OpenViking)

**The key grill:** these are optimized for **user personalization** ("Alice prefers dark mode", cross-session recall of a person). Our chatbot's memory need is **not the user — it's the schema and the verified query patterns.** That's a different axis. The one piece that *would* help accuracy is **procedural memory** (concept #1): a library of question→proc/SQL that worked, retrieved as few-shots.

**Verdict:** don't add a memory framework to the PoC. **Steal the procedural-memory idea as a flat JSON file** of verified mappings (this doubles as the deferred "plan cache" and "learned memory" from the plan). If the eval later shows a high repeat-question rate, *then* evaluate **mem0** (most mature, Apache-2.0) to back it. Not before.

### 13 · MinerU — the quiet useful one

We have a **50MB `OLIVES USER GUIDE.pdf`** and a **1.6MB `Olives SQL_Documentation.docx`** sitting in the repo, currently not in the docs path. MinerU converts both to clean markdown, with **109-language OCR including Arabic** and a no-hallucination pipeline. **Verdict:** not PoC-critical (PoC uses live introspection + the existing vault), but the **right tool** to enrich the docs corpus later — especially the Arabic OCR. One-time batch, no runtime dependency, low risk.

### 15 · qmd — a clean upgrade held in the pocket

Our docs path currently uses the obsidian MCP's `search_notes` (regex/full-text). qmd is **on-device hybrid search** (BM25 + vector + rerank), MCP-native, AST-aware. If regex retrieval over ~2,300 notes proves weak for "why is X blocked" questions, qmd is the drop-in upgrade — on-device (fits on-prem), MCP-native (drops into the plan). **Verdict:** keep the obsidian MCP for PoC; **hold qmd as the upgrade** if docs-retrieval quality is the bottleneck. Don't add it speculatively.

### 10 / 11 · Gemini API / freellmapi — the accuracy + confidentiality filters

- **Gemini:** cheaper and huge context, but the research's own table shows **~50% hallucination vs Claude's ~36%**, weaker tool use, weaker SWE-bench. For a system whose whole point is *not returning a confident wrong number*, and which needs strong Arabic, **Claude stays.** Gemini could be a fallback tier inside OmniRoute later, nothing more.
- **freellmapi:** free-tier aggregation is **disqualified twice over** — (1) the drift-tool's own validation already proved free small models (Qwen/Gemma/Nemotron) rate-limit and leak reasoning; (2) routing **client DB data** through random free providers is a **confidentiality leak**. Fine for throwaway internal dev, never for the client-data path.

---

## Skips — one line each (wrong axis for a read-only SQL Q&A PoC)

- **5 · turbovec** — excellent Rust vector index, but the PoC uses **no embeddings** (catalog-first + live introspection, not RAG-over-schema). Revisit only if we build semantic search at scale.
- **12 · OpenWiki** — auto-wiki for **code repos** (scans package.json etc.); a SQL schema isn't that shape, and our drift-tool→vault regen is the SQL-native equivalent we already planned.
- **14 · Hyper-Extract** — LLM extraction of graphs from text; for **schema** relationships the DB's own `sys.sql_expression_dependencies` is authoritative and doesn't hallucinate. Wrong tool for a DB.
- **16 · Cloud Run Sandboxes** — we execute **no untrusted code** (gated read-only SQL only), and it's a **GCP cloud** service that contradicts on-prem/confidentiality.
- **22 · Obscura** — headless browser for **web scraping**; we query a database.
- **17 · awesome-mcp-servers / 19 · free-for-dev** — directories, not tools. Worth a browse (check if a mature MSSQL MCP exists), but our gate requirement means we build our own thin `sql_mcp.py` anyway.

---

## General-experience wins (not architecture — cheap, low-risk)

- **23 · claude-code-setup** — official Anthropic, read-only, scans the repo and recommends hooks/MCP/subagents/skills. **Run it on `client-chatbot/`** for tailored setup suggestions. Zero risk.
- **20 · archify** — generates + maintains interactive architecture diagrams with evidence-linked source. Could keep the plan's SVGs in sync with the code as it's built. Nice-to-have, not a blocker.
- **18 · obsidian-skills** — native vault read/write for the agent. Useful **when** we build the per-client vault drafting tool (deferred idea C), and for the user's own Obsidian workflow.

---

## Plan changes I'd actually make (and where)

| Change | Where in the plan | Confidence |
|--------|-------------------|-----------|
| Add a **verified-query JSON file** (procedural memory as few-shots) | `prompts/` + `agent.py` — feed matched examples into generation | **Do it in PoC** — cheap, direct accuracy win |
| Evaluate **Metabase** for the **reports/dashboard/push** surface | The deferred push-report decision, **not** the chatbot core | Evaluate at that phase |
| Name **OmniRoute** as the concrete **gateway** candidate | The deferred "central gateway/key broker" item | Adopt at gateway phase, Claude-pinned |
| Note **MinerU** as the doc-ingest tool (Arabic OCR) | When enriching the docs corpus from the PDF/docx | Later, low risk |
| Run **claude-code-setup** on the repo | One-time, now | Free win |

**Everything else stays exactly as PLAN.md has it.** The PoC core — catalog-first proc execution, `sqlglot` gate, read-only login, live introspection, plain Anthropic loop — beats every alternative here on the two things that matter: **accuracy** (tested procs > generated SQL) and **simplicity** (12 Python files > a BI platform or an agent framework). No dictator verdict: the door is genuinely open on Metabase-for-reports and OmniRoute-for-gateway — just not on the chatbot's brain.

---

# RECHECK — at pilot tier (between a bare MCP and production)

The target moved up (see [PLAN.md](PLAN.md) § "What pilot tier means"). At this bar, durability, observability, key custody, a real docs corpus, and multi-client config are now genuine needs — not gold-plating. Several PoC "defer/hold" verdicts flip. The ones that **don't** move are as informative as the ones that do.

## What moved, and why

| Tool | PoC verdict | Pilot verdict | Why it shifted (or didn't) |
|---|---|---|---|
| **OmniRoute** (9) | adopt @ gateway phase | **Adopt now** | A pilot serving real users needs key custody + outage fallback + audit **now**, not later. But weigh against **LiteLLM** (not in the list — the tried-and-true self-hosted OpenAI-compatible gateway). Pick LiteLLM for maturity/simplicity, OmniRoute if you want its compression/free-tier/dashboard extras. Either way: **Claude pinned primary, fallback only on outage.** |
| **MinerU** (13) | adopt later | **Adopt now** | The pilot has a real docs path, so the 50MB PDF + DOCX guides get ingested now. Arabic OCR is the clincher. One-time batch. |
| **qmd** (15) | pocket | **Adopt if regex is weak** | Docs retrieval is a first-class path now. Start on the vault MCP; wire qmd (on-device hybrid, MCP-native) the moment retrieval quality bites. |
| **Metabase** (21) | evaluate later | **Evaluate now — reports/push surface** | A pilot benefits from scheduled reports + permission-gated dashboards immediately. Adopt it as a **parallel delivery layer**, self-hosted, SQL Server-native. **Still not the chat brain** — Metabot NL→SQL is the accuracy trap; our proc-catalog stays the engine. |
| **Gemini** (10) | skip | **Fallback tier only** | Now that a gateway exists, Gemini is a reasonable outage-fallback model. Never primary (hallucination rate + weaker Arabic). |
| Memory concern (1/3) | param JSON only | **Real SQLite memory module** | Pilot builds `core/memory.py`: procedural (verified queries), plan cache, traces. **Still DIY, not mem0** — on-prem confidentiality + control, and our axis is query-pattern reuse, not user personalization. Re-evaluate **mem0** only if a SQLite table + FTS stops scaling. |
| **turbovec** (5) | skip | **Still skip** — prefer sqlite-vec/pgvector | If the memory/docs layer ever needs vectors, a **persistent** store (sqlite-vec or pgvector) fits ops better than turbovec (fast but no disk index, no HNSW). |
| **LangGraph** (7) | hold → Idea 2 | **Still hold → Idea 2** | Even at pilot, a **read-only single-agent** loop doesn't need durable execution / HITL / multi-agent. Its payoff is the support assistant (approvals, long-running), not this bot. Own structured tracing (`core/trace.py`) covers the observability need without the framework. |
| **Hermes-Agent** (8) | hold → platform | **Still hold → platform** | Pilot is one deployment, one channel. Its multi-platform gateway + self-improvement are a later-platform bet, not a pilot need. |
| **claude-code-setup** (23) | run it | **Run it** | Unchanged — free dev-experience win on the new repo layout. |
| **archify** (20) / **obsidian-skills** (18) | nice-to-have / later | **Mildly up** | A real pilot has real docs + (later) per-client vault projection; both help, still not blockers. |

## What did NOT move (and that's the signal)

The **core accuracy strategy is tier-independent**: catalog-first proc execution + `sqlglot` gate + read-only login + server-side scoping beats generic NL→SQL at **every** tier. So the tools that lose to it at PoC (Metabot-as-brain, memory frameworks for the wrong axis, free-tier aggregators, LangGraph-for-a-simple-loop) still lose at pilot. Moving up the tier adds **surrounding** machinery (gateway, memory store, docs corpus, observability, tenant views) — it does **not** change the brain.

**Net at pilot:** adopt a gateway (LiteLLM/OmniRoute), MinerU for docs, a SQLite memory module, tenant views, FastAPI + metrics, and evaluate Metabase for the report/push surface. Hold LangGraph/Hermes for the support-assistant. Keep the proc-catalog brain exactly as-is. The higher bar justified more scaffolding, not a different center.
