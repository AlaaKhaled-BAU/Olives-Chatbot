# Raw Tool Research — client-chatbot Project

> Compiled July 24, 2026. No opinions or analysis — only facts from each tool's documentation, repository, and benchmarks.

---

## Table of Contents

1. [Memory Types (Cognitive Framework)](#1-memory-types)
2. [supermemory](#2-supermemory)
3. [mem0](#3-mem0)
4. [TencentDB-Agent-Memory](#4-tencentdb-agent-memory)
5. [turbovec](#5-turbovec)
6. [OpenViking](#6-openviking)
7. [LangGraph](#7-langgraph)
8. [Hermes-Agent](#8-hermes-agent)
9. [OmniRoute](#9-omniroute)
10. [Gemini API](#10-gemini-api)
11. [freellmapi](#11-freellmapi)
12. [OpenWiki](#12-openwiki)
13. [MinerU](#13-mineru)
14. [Hyper-Extract](#14-hyper-extract)
15. [qmd](#15-qmd)
16. [Cloud Run Sandboxes](#16-cloud-run-sandboxes)
17. [awesome-mcp-servers](#17-awesome-mcp-servers)
18. [obsidian-skills](#18-obsidian-skills)
19. [free-for-dev](#19-free-for-dev)
20. [archify](#20-archify)
21. [Metabase](#21-metabase)
22. [Obscura](#22-obscura)
23. [claude-code-setup](#23-claude-code-setup)

---

## 1. Memory Types

### Short-Term Memory (Working Memory)
- **Definition**: Active scratchpad holding information relevant to the current moment. In AI agents, this is the LLM context window plus ephemeral in-process state.
- **Scope**: Current conversation turns, user's latest query, intermediate reasoning steps, tool call results, temporary variables. Cleared when session ends.
- **Implementation approaches**: Raw context window (append every turn), sliding window (keep last N turns), token-budget truncation (drop oldest until under limit), summary compression (periodically summarize older turns), semantic cache (cache recent responses keyed by query embedding), hybrid window+summary.
- **Key insight**: Raw context window is simple but expensive. Summary-based STM reduces token costs 3-10x for long sessions.

### Long-Term Memory (LTM)
- **Definition**: Persistent storage that survives across sessions. Umbrella category for anything that outlives a single conversation. Subsumes episodic, semantic, and procedural memory.
- **Scope**: Enables agent to remember users across sessions, recall past conversations, accumulate knowledge over time.
- **Implementation layers**: Vector database (embedding vectors + metadata), key-value store (structured facts), relational DB (tables with schemas), graph DB (nodes + edges), hybrid (vector + structured).
- **Key insight**: LTM is three distinct stores (episodic, semantic, procedural) with different write/read patterns. Treating them as a single blob degrades retrieval quality.

### Episodic Memory
- **Definition**: Stores specific past experiences with temporal context — what happened, when, and what the outcome was. In AI agents, a log of past interactions, decisions, and results.
- **Content**: Specific events ("User X asked about Y on date Z"). Timestamped, ordered. Append-only. High volume (every interaction).
- **Retrieval**: "What happened when..."
- **Implementation**: Timestamped vector entries, event log, dated observations, checkpoints.
- **Key insight**: Episodic memory needs consolidation — raw logs are too noisy. Extract and promote important episodes to semantic memory using confidence thresholds, frequency analysis, or LLM-based summarization.

### Semantic Memory
- **Definition**: Stores generalized factual knowledge independent of specific experiences. Facts, concepts, rules, user preferences, domain knowledge, relationships. The "what is true" store.
- **Content**: Generalized facts ("User X prefers Y"). Timeless, overwritable. Low volume (only consolidated facts).
- **Retrieval**: "What is true about..."
- **Implementation**: Vector RAG, structured KV, knowledge graph, hybrid RAG, in-weight fine-tuning.
- **Key insight**: Most common LTM type in production. The hard problem is knowing when to retrieve and what is stale.

### Procedural Memory
- **Definition**: Encodes how to do things — workflows, skills, tool usage patterns, behavioral rules. In AI agents, knowledge of which tool to call, in what order, and under what conditions.
- **Examples**: "When user asks for refund, first verify order, then check policy, then process if eligible." "If DB query fails, retry with exponential backoff, then escalate."
- **Implementation**: System prompt instructions, few-shot examples, tool-use policies, fine-tuned model, dynamic few-shot (retrieve similar past successful trajectories at runtime), graph-based workflows, behavioral cloning.
- **Key insight**: Most underused memory type. A library of verified workflows (tool-call sequences that worked) is more reliable than hoping the LLM invents the right procedure each time.

### Shared Memory
- **Definition**: Memory that spans multiple agents, sessions, or users. Enables coordination, knowledge transfer, and consistent state across agents working on the same task.
- **Use cases**: Multi-agent coordination, cross-session continuity, team-wide knowledge, scoped isolation.
- **Architecture patterns**: Centralized (shared bus), distributed (per-agent with selective sync), hierarchical (global + role/team + private), blackboard (central workspace + coordinator), namespace isolation (single store with scoped prefixes).
- **Conflict resolution strategies**: Last-write-wins, reducer functions, LLM-assisted consolidation, event sourcing + replay, orchestrator-mediated serialization.
- **Key insight**: 36.9% of multi-agent system failures stem from inter-agent misalignment (Cemri et al., arXiv 2503.13657).

### Three-Tier Production Architecture
1. In-context working memory — raw message buffer, ephemeral (session lifetime)
2. Session-scoped compressed — summarized/extracted facts from current session
3. Long-term persistent store — vector + graph + structured, cross-session

### Memory Consolidation Pipeline
Raw interaction → Extract key info → Store as episodic (raw + timestamp) → Promote to semantic (if confidence > threshold) → Refine procedural (if tool-use pattern repeats)

---

## 2. supermemory

**Repo**: https://github.com/supermemoryai/supermemory
**Stars**: 28.6k | **License**: MIT | **Stack**: TypeScript, Bun, Cloudflare, Drizzle ORM, Postgres, Next.js

### Overview
Memory and context engine for AI agents. #1 on LongMemEval, LoCoMo, ConvoMem benchmarks. Achieves 95% Recall@15 with 99.4% context reduction (~720 tokens injected per query vs. raw history). User profiles resolve in ~50ms.

Three tiers: consumer app (app.supermemory.ai), API/SDK (npm/pip), self-hosted binary (fully offline with Ollama).

### Architecture
Monorepo with Bun workspaces + Turborepo. Components: Web App (Cloudflare Pages), MCP Server (Cloudflare Workers + Durable Objects), Browser Extension (Chrome/Firefox), Backend API (external), TS SDK, Python SDK, AI Tools middleware.

Core processing: App/AI Tool → Supermemory API Layer (/documents, /search, /profile, /memories) → Processing Pipeline (Extract → Chunk → Embed → Index → Build Relationships) → Knowledge Graph Storage (Vectors in HNSW + Graph Relationships).

### Memory Engine — Living Knowledge Graph
Content stored as fact-based knowledge graph with three relationship types:
- **Updates**: new info supersedes old (temporal versioning, isLatest flag)
- **Extends**: enriching context linked to existing facts
- **Derives**: inferred connections from pattern analysis

Enables: automatic contradiction resolution, temporal expiry, version history for every fact.

Container tag isolation for multi-tenant scoping.

### Key Features
1. `client.add()` — extract atomic facts from conversations, docs, URLs
2. `client.profile()` — auto-maintained dual-profile (static + dynamic), ~50ms
3. `client.search()` — hybrid RAG + Memory in single query with metadata filtering
4. Connectors: Google Drive, Gmail, Notion, OneDrive, GitHub (OAuth auto-sync)
5. Multi-modal extractors: PDFs, images (OCR), videos (transcription), code (AST-aware)
6. MCP Server: memory, recall, context tools
7. SMFS: virtual filesystem (NFSv3/FUSE) for agents
8. `withSupermemory()` middleware for Vercel AI SDK, LangChain, Mastra, OpenAI Agents SDK
9. Framework integrations: LangChain, LangGraph, CrewAI, Mastra, Agno, n8n, Zapier, Pipecat, Claude Memory Tool
10. MemoryBench: open-source benchmarking framework

### Architecture Principles
- Memory ≠ RAG: RAG retrieves document chunks (stateless). Memory tracks evolving facts about users (stateful, temporal).
- Graph-based, not blob store: facts are nodes; relationships enable reasoning.
- Automatic forgetting: temporary facts expire. Contradictions resolve automatically.
- Profile as summary: system distills all memories into compact user profile (~50ms).
- Container-scoped: all operations scoped by containerTag.

### Benchmarks
- LongMemEval: 95% Recall@15, 99.4% context reduction
- User profiles: ~50ms latency
- Search: sub-300ms p95

### Integration Options
1. MCP: add mcp.supermemory.ai/mcp to MCP config (5 min)
2. SDK middleware: wrap model with withSupermemory() (10 min)
3. REST API: direct calls (30 min)
4. Self-host: curl install + configure Ollama

---

## 3. mem0

**Repo**: https://github.com/mem0ai/mem0
**Stars**: 61.6k | **License**: Apache 2.0 | **Funding**: Y Combinator S24, $24M Series A

### Overview
Memory layer for AI agents that extracts durable facts from conversations, stores them, and retrieves relevant ones when needed. New algorithm (April 2026): single-pass ADD-only extraction, entity linking across memories, multi-signal retrieval (semantic + BM25 + entity matching), temporal reasoning.

### Benchmarks (New Algorithm)
- LoCoMo: 92.5 (old: 71.4) — 7.0K tokens, 0.88s latency
- LongMemEval: 94.4 (old: 67.8) — 6.8K tokens, 1.09s latency
- BEAM (1M): 64.1 — 6.7K tokens, 1.00s latency
- BEAM (10M): 48.6 — 6.9K tokens, 1.05s latency

### Key Features
- Multi-level memory: User, Session, and Agent state
- Cross-platform SDKs: Python (pip install mem0ai), TypeScript (npm install mem0ai), CLI (@mem0/cli)
- Deployment options: Library (local), Self-hosted Server (Docker), Cloud Platform
- Agent skills: Plugins for Claude Code, Codex, Cursor, Windsurf, OpenCode
- Integrations: LangGraph, CrewAI, ChatGPT, browser extension

### Architecture
Uses vector embeddings + BM25 keyword + entity matching for retrieval. Default LLM: gpt-5-mini (OpenAI). Default embedding: text-embedding-3-small. Supports Qwen 600M+ for hybrid search.

### Quickstart
```python
from mem0 import Memory
memory = Memory()
memory.add("Prefers dark mode", user_id="alice")
results = memory.search("What does Alice prefer?", user_id="alice")
```

**Paper**: Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (arXiv 2504.19413)

---

## 4. TencentDB-Agent-Memory

**Repo**: https://github.com/TencentCloud/TencentDB-Agent-Memory
**Stars**: ~9,300 | **License**: MIT | **Language**: TypeScript
**Published**: April 2026 by Tencent Cloud Database Team

### Overview
Team-level memory hub for AI Agents. Turns conversations, docs, and code into four reusable memory assets: Chat Memory, Skill, LLM-Wiki, and Code-Graph. Fully local long-term memory with zero external API dependencies. When integrated with OpenClaw, cuts token usage by up to 61.38%, improves pass rate by 51.52% (relative), raises PersonaMem accuracy from 48% to 76%.

### Architecture — Two Pillars
1. Memory Layering — progressive disclosure with heterogeneous storage
2. Symbolic Memory — context offloading into compact Mermaid symbol graphs

### L0–L3 Semantic Pyramid (Long-Term Personalization)
| Layer | Name | Content | Storage |
|-------|------|---------|---------|
| L0 | Conversation | Raw dialogue, unedited | JSONL files + SQLite |
| L1 | Atom | Atomic facts | Vector DB + JSONL |
| L2 | Scenario | Scene blocks grouping related atoms | Markdown files |
| L3 | Persona | User profile — preferences, style, patterns | Markdown (persona.md) |

Progressive disclosure: Agent normally uses only L3 Persona. Drills down to L2/L1/L0 only when specifics are needed.

### Short-Term Context Layering (In-Task)
| Layer | Content | Storage |
|-------|---------|---------|
| Top | Mermaid canvas (symbolic task graph) | In-context (~hundreds of tokens) |
| Middle | Step-level summaries | JSONL |
| Bottom | Raw tool outputs (search, code, errors) | refs/*.md files |

### Storage
- Bottom layers (facts, logs, traces) → databases (SQLite + sqlite-vec)
- Top layers (personas, scenes, canvases) → human-readable Markdown
- Full traceability: Persona → Scenario → Atom → Conversation

### Host Integration
- OpenClaw plugin: automatic capture, extraction, recall
- Hermes Gateway adapter: TdaiCore + HostAdapter
- Data under ~/.openclaw/memory-tdai/

### Features
- L0: Auto-captures every conversation turn, dual-writes
- L1: LLM extracts structured memories with vector dedup/conflict detection
- L2: LLM induces scene blocks from L1 memories
- L3: LLM generates/updates user persona from scene blocks
- Symbolic short-term memory via Mermaid canvas context offloading
- Hybrid retrieval: BM25 + vector + RRF fusion
- Auto-Recall before each conversation turn
- Local backend: SQLite + sqlite-vec
- Remote backend: Tencent Cloud Vector Database
- Agent tools: tdai_memory_search / tdai_conversation_search
- Session isolation, configurable retention days
- White-box debuggability: all artifacts human-readable

### Roadmap: Skill Generation from execution traces

---

## 5. turbovec

**Repo**: https://github.com/RyanCodrai/turbovec
**Stars**: ~14.1k | **License**: MIT | **Language**: Rust + Python bindings
**Paper**: TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate (ICLR 2026 oral)

### Overview
Rust vector index built on Google Research's TurboQuant algorithm — data-oblivious quantizer requiring no training pass, no codebook calibration, no index rebuild as corpus grows. Compresses embeddings to 2–4 bits per coordinate. Searches directly in compressed space using SIMD kernels (NEON, AVX-512BW, AVX2). A 10M-document corpus: ~31 GB f32 → ~4 GB.

### Core Components
| Component | Description |
|-----------|-------------|
| TurboQuantIndex | Positional index (fast, small, O(1) swap_remove) |
| IdMapIndex | Stable u64 external IDs (hash-table backed, O(1) remove) |
| Python bindings (PyO3/maturin) | pip-installable, numpy-native arrays |
| Rust crate | cargo add turbovec |

### Framework Integrations (drop-in)
- LangChain: turbovec[langchain] → InMemoryVectorStore
- LlamaIndex: turbovec[llama-index] → SimpleVectorStore
- Haystack: turbovec[haystack] → InMemoryDocumentStore
- Agno: turbovec[agno] → LanceDb

### TurboQuant Algorithm (6 steps)
1. Normalize — strip vector norm, store as f32
2. Random rotation — multiply by fixed random orthogonal matrix
3. TQ+ calibration (optional) — shift+scale scalars per coordinate
4. Lloyd-Max scalar quantization — precomputes optimal bucket boundaries from known Beta distribution
5. Bit-pack — each coordinate stored as 2–4 bit integer
6. Length-renormalized scoring — per-vector correction scalar

### Filtered Search
Pass id allowlist or slot bitmask — blocks with zero allowed slots short-circuited before scoring. Output shape always (nq, min(k, n_allowed)).

### Performance (100K vectors, 1K queries, k=64)
- ARM (M3 Max): 10–19% faster than FAISS IndexPQFastScan
- x86 (Sapphire Rapids): wins 4-bit configs (up to ~5%), trails FAISS on 2-bit (~8%)
- Recall @1 (d=1536): beats FAISS by 0.2–1.9pp at 2-bit and 4-bit
- Recall @1 (GloVe d=200): beats FAISS by 0.9pp at 4-bit, tied at 2-bit

### Comparison with Alternatives
| Feature | turbovec | FAISS | LanceDB/Chroma | pgvector |
|---------|----------|-------|----------------|----------|
| Training-free ingest | Yes | No | N/A | N/A |
| Online add O(1) | Yes | Retrain needed | Yes | Yes |
| Compression ratio | 8–16x | 4–8x | None (f32) | None (f32) |
| Kernel-level filtered search | Yes | Post-filter only | DB-backed | SQL WHERE |
| SIMD search kernels | NEON+AVX | FastScan | No | No |
| MMR | No | Yes | Yes | No |
| Persistent disk index | No (serialize/load) | Yes | Yes | Yes |
| GPU | No | Yes | No | No |
| Distributed | No | Yes | Yes | No |

### Limitations
- No MMR (raw vectors discarded after quantization)
- No HNSW/graph-based search (brute-force over compressed vectors)
- No persistent disk index (write/load is serialize/deserialize)
- No GPU kernels (CPU SIMD only)
- No distributed/sharded operation
- Recall degrades on low-dim embeddings (<200d) at 2-bit

### Python API
```python
index.add(vectors)
scores, ids = index.search(query, k=10, allowlist=allowed_ids)
```

---

## 6. OpenViking

**Repo**: https://github.com/volcengine/OpenViking
**Stars**: 27.2K | **License**: AGPLv3 (main), Apache 2.0 (CLI crate)
**Paper**: VikingMem published at VLDB 2026

### Overview
Self-evolving Context Database for AI Agents. Unifies agent memory, knowledge RAG, and skills. Virtual filesystem (viking:// protocol) with tiered loading. Reduces token costs.

### Architecture
- Virtual filesystem: Memories, resources, skills as browsable filesystem (ls, tree, find)
- Tiered loading: L0 (abstract ~100 tokens), L1 (overview ~2K tokens), L2 (details) — only load what the task needs
- Directory recursive retrieval: vector search locates highest-scoring directory, drills down layer by layer
- Session → memory: auto-extracts user preferences and agent experience asynchronously after session commit

### Benchmarks
- LoCoMo (user memory): accuracy 80-83% with OpenViking vs 24-57% native — input tokens drop 34-91%, latency drops 58-66%
- tau2-bench (agent experience): +6.87pp (retail), +11.87pp (airline) task success

### Integrations
Claude Code, Codex, OpenClaw, Hermes, Cursor, Trae, OpenCode, MCP clients, LangChain/LangGraph

### Includes
- VikingBot: Agent framework built on OpenViking
- OpenViking Helper (beta): desktop app for visual config, session trace inspection

---

## 7. LangGraph

**Repo**: https://github.com/langchain-ai/langgraph
**Stars**: 38k | **License**: MIT | **Current version**: 1.2.9 (July 2026)
**Used by**: Klarna, Uber, JP Morgan, Elastic, LinkedIn

### Overview
Low-level orchestration framework and runtime for building, managing, and deploying stateful, long-running AI agents. Independent library (not LangChain — can be used standalone). 34% enterprise agent framework market share (2026).

### Architecture
Models agent workflows as directed cyclic graphs (state machines), inspired by Google's Pregel and Apache Beam.

Three primitives:
1. **State** (TypedDict or Pydantic model) — shared data bucket flowing through graph. Uses channels and reducers (e.g., add_messages) to merge parallel writes.
2. **Nodes** — Python functions that process state and return updates.
3. **Edges** — define control flow: normal edges (static A→B), conditional edges (runtime function decides next node(s)), entry point routing. Multiple outgoing edges = parallel fan-out.

Execution model: nodes run in supersteps — all nodes in a given step execute in parallel across assigned channels, then synchronize. Cycles are natural (node can route back to itself or earlier nodes).

### Key Features
1. Durable execution — agents survive failures, resume from checkpoint
2. Human-in-the-loop — static interrupts (interrupt_before/interrupt_after) and dynamic interrupts
3. Comprehensive memory — short-term (graph state) + long-term (persistent)
4. Streaming — token-by-token LLM outputs and intermediate reasoning
5. Parallel execution — fan-out to N nodes, automatic join
6. Conditional routing — dynamic decision points
7. Observability via LangSmith — every transition is a trace event
8. LangSmith Deployment — platform for deploying stateful agents
9. Subgraphs — any node can be a compiled graph (composable nesting)

### Comparison with Simple ReAct Loop

| Dimension | Simple Loop | LangGraph |
|-----------|-------------|-----------|
| Flow control | LLM decides everything (implicit) | Programmer defines explicit graph |
| State | Linear conversation history | Rich typed state with channels & reducers |
| Error recovery | Stateless — crash loses context | Durable — resumes from checkpoint |
| HITL | Custom middleware required | Built-in interrupts |
| Parallelism | Sequential only | Native fan-out/fan-in |
| Long-running | Unreliable | Survives restarts |
| Debugging | Opaque | Full traceability via LangSmith |
| Boilerplate | ~20 lines | More upfront |
| Flexibility | Simple tool use | Complex branching, loops, multi-agent |

### When to Use
Overkill for: basic Q&A with 1-3 tools, no long-running sessions, no human approval, crash=restart acceptable, single agent, MVP stage.
Justified for: multi-step workflows, human approval, production reliability, long-running tasks, multi-agent, need observability, parallel tool execution.

Can coexist — wrap simple loops inside LangGraph nodes for gradual adoption.

---

## 8. Hermes-Agent

**Repo**: https://github.com/NousResearch/Hermes-Agent
**Stars**: ~220k | **License**: MIT | **Author**: Nous Research | **Release**: February 2026

### Overview
Self-improving, open-source AI agent framework. Persistent, autonomous agent runtime with closed learning loop — accumulates skills from experience, improves them during use, builds user models across sessions, searches own conversation history. Runs on $5 VPS to GPU cluster. Model-agnostic (OpenAI, Anthropic, OpenRouter, Nous Portal, local Ollama/vLLM). Communicates via 20+ platforms.

Core thesis: agent should get better the more you use it, not through fine-tuning but through experience accumulation.

### Architecture — Three-Tier
1. **Entry Points**: CLI, Gateway, ACP, Batch, API
2. **AIAgent orchestrator**: Prompt Builder, Provider Resolver, Tool Dispatch, Compression & Caching, 3 API modes
3. **Storage & Backends**: Session Storage (SQLite + FTS5, session lineage), Tool Backends (6 terminal backends, 5 browser backends, Web, MCP, File)

~25K tests across ~1,250 files.

### Key Features
1. **Closed Learning Loop**: Skill Generation (writes reusable skill markdown after complex tasks), Skill Self-Improvement, Agent-Curated Memory, FTS5 Cross-Session Search with LLM summarization, User Modeling (Honcho dialectic modeling), Skills Hub compatibility
2. **Multi-Platform Gateway**: 20+ adapters (CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, Weixin, QQ Bot, Yuanbao, BlueBubbles, Home Assistant, Microsoft Teams, Google Chat)
3. **Any-Model, Anywhere**: 18+ provider integrations, 6 terminal backends (local, Docker, SSH, Daytona, Modal, Singularity)
4. **Tool System**: 70+ tools across ~28 toolsets, self-registering, MCP integration with tool filtering
5. **Delegation & Parallelism**: spawn isolated subagents, execute_code via Python RPC
6. **Cron Scheduler**: first-class agent tasks with skill/script attachment, delivery to any platform
7. **Research Infrastructure**: batch trajectory generation, ShareGPT-format export, RL training integration

### Data Flow
CLI: User input → HermesCLI.process_input() → AIAgent.run_conversation() → prompt assembly → provider resolution → API call → tool dispatch loop → response → display → save to SQLite.

Gateway: Platform event → Adapter → GatewayRunner → authorize → resolve session → create AIAgent with history → run conversation → deliver response.

---

## 9. OmniRoute

**Repo**: https://github.com/diegosouzapw/OmniRoute
**Stars**: ~28k | **License**: MIT | **Language**: TypeScript (Next.js)

### Overview
Local-first AI API routing gateway. Unified access to 290+ model providers (500+ models) through single OpenAI-compatible endpoint (/v1). Aggregates ~1.53B free tokens/month across 90+ free tiers. Ships as npm package, Docker image, Electron desktop app, and PWA.

### Architecture
IDE/CLI Agent → localhost:20128/v1 → Smart Router → 4-Tier Fallback → Provider API

Four Tiers of Fallback:
1. Tier 1 — Subscription (Claude Code, Codex, Copilot)
2. Tier 2 — API Key (DeepSeek, Groq, xAI)
3. Tier 3 — Cheap (GLM $0.5, MiniMax $0.2)
4. Tier 4 — Free (Kiro, Qoder, Pollinations, OpenCode Free)

Falls through tiers automatically on rate-limit, quota exhaustion, or error.

### Key Components
| Path | Description |
|------|-------------|
| src/app/api/v1/ | OpenAI-compatible proxy endpoints |
| src/domain/ | Core business logic: policy engine, combo resolution, model availability |
| src/lib/db/ | SQLite database layer, schema, backup system |
| src/lib/a2a/ | Agent-to-Agent protocol (JSON-RPC 2.0 + SSE, 6 skills) |
| open-sse/mcp-server/ | Built-in MCP server (94 tools, 3 transports, 30 scopes) |
| bin/omniroute.mjs | Primary CLI entry point (80+ commands) |

### Smart Routing — 19 Strategies
priority, fill-first, weighted, round-robin, p2c, least-used, cost-optimized, headroom, quota-share, latency-optimized, context-relay, fusion

Zero-config auto variants: auto, auto/coding, auto/fast, auto/cheap, auto/offline, auto/smart

### Key Features
1. Token compression — RTK + Caveman (9 composable stages, 15-95% reduction, ~89% avg on tool-heavy)
2. Resilience — circuit breakers, key cooldown, model lockout, 3-level proxy (TLS stealth, JA3/JA4 fingerprint spoofing)
3. Built-in MCP — 94 tools, 3 transports, 30 scopes, full audit trail
4. A2A protocol — Agent-to-Agent JSON-RPC 2.0 + SSE
5. Dashboard — live free-tier budget tracker, per-provider usage, p95 latency, error rates
6. Privacy — local-first, AES-256-GCM encrypted API keys, zero telemetry, prompt-injection guard
7. Memory — FTS5 + vector memory built in (RAG-ready)

### Deployment Options
npm global install, Docker (docker-compose), Nix flake, Fly.io, Electron desktop app

### Integration
`npm install -g omniroute && omniroute` runs on port 20128. Chatbot changes base_url to http://localhost:20128/v1. Adds ~5-50ms latency hop.

---

## 10. Gemini API

**Docs**: https://ai.google.dev/gemini-api/docs/get-started
**Interactions API**: GA June 2026 — single unified endpoint for models + agents

### Models & Pricing
| Model | Input/MTok | Output/MTok | Context | Free Tier |
|-------|-----------|-------------|---------|-----------|
| Gemini 3.6 Flash | $1.50 | $7.50 | 1M | No |
| Gemini 3.5 Flash | $1.50 | $9.00 | 1M | Yes (rate-limited) |
| Gemini 3.1 Pro Preview | $2.00 ($4 >200K) | $12 ($18 >200K) | 2M | No |
| Gemini 2.5 Pro | $1.25 ($2.50 >200K) | $10 ($15 >200K) | 1M | No |
| Gemini 2.5 Flash | $0.30 | $2.50 | 1M | Yes (15 RPM, 1K RPD) |
| Gemini 2.5 Flash-Lite | $0.10 | $0.40 | 1M | No |

### Key Capabilities
- Context window: 1M standard, 2M on 3.1 Pro
- Max output: 64K tokens
- Implicit caching: auto-enabled on Gemini 2.5+ (75% discount, no developer work)
- Explicit caching: manual control with TTL, storage $1-4.50/MTok/hr
- Built-in tools: Google Search grounding, Google Maps, Code Execution, URL Context, File Search (RAG), Computer Use (preview)
- Native multimodal: text, image, video, audio in single prompt (up to 900 images, 8.4h audio, 1h video)
- Tool calling: OpenAI-style function calling, structured outputs with responseSchema
- Managed Agents: Deep Research, Antigravity (sandboxed Linux env)
- Background execution: background=true for async tasks
- Server-side state: previous_interaction_id for conversation continuity
- Live API: real-time voice and streaming agents

### Grounding
- Google Search grounding: per-search-query billing on Gemini 3 ($14/1K queries after 5K free)
- Google Maps grounding: 250M+ places
- Free allowance: 5,000 prompts/month shared across Gemini 3 models

### Comparison with Claude
| Dimension | Gemini | Claude |
|-----------|--------|--------|
| SWE-bench Verified | 80.6% (3.1 Pro) | 87.6% (Opus 4.7) |
| Hallucination rate | 50% | 36% |
| MCP Atlas (tool use) | 73.9% | 77.3% |
| Multimodal (BenchLM) | 82.8 | 64.3 |
| Pricing (flagship) | $2-$12/MTok | $5-$25/MTok |

### Key Cost Drivers
1. Thinking tokens counted as output → billed at output rates
2. Long-context surcharge: Pro models double past 200K
3. Grounding: per-search-query billing on Gemini 3
4. Batch: 50% discount on all models

---

## 11. freellmapi

**Repo**: https://github.com/tashfeenahmed/freellmapi
**Stars**: 16.9K

### Overview
OpenAI-compatible proxy that aggregates free tiers from 28 LLM providers behind one /v1 endpoint. 339 free model endpoints, ~4B tokens/month aggregate capacity.

### Supported Providers
Google (Gemini 2.5 Flash), Groq, Cerebras, Mistral, OpenRouter, GitHub Models, Cloudflare, Cohere, Z.ai (Zhipu), NVIDIA, HuggingFace, OpenCode Zen, and more.

### Protocols
OpenAI-compatible /v1/chat/completions, Anthropic Messages API /v1/messages, Responses API /v1/responses, embeddings, image gen, TTS

### Smart Routing
6 strategies: priority, balanced, smartest, fastest, reliable, custom. Automatic failover with cooldowns, sticky sessions (30 min).

### Key Features
- Tool calling: OpenAI-style tools passed through; text-based tool calls rescued to structured JSON
- Gemini Google Search grounding: translates google_search tool name to Gemini's native grounding in OpenAI wire format
- Fusion mode: fans prompt to multiple free models, synthesizes with judge
- MCP server at /mcp: agents can introspect model availability, health, usage stats
- Admin dashboard: key management, analytics (p50/p95 latency, token counts), playground
- Premium live catalog: $19/yr or $49 lifetime for auto-updating model catalog

---

## 12. OpenWiki

**Repo**: https://github.com/langchain-ai/openwiki
**Stars**: 13.1k | **License**: MIT | **Release**: July 2026

### Overview
CLI tool that automatically generates and maintains an LLM-optimized wiki for a codebase. Implementation of Andrej Karpathy's "LLM Wiki" concept — LLM writes/maintains structured markdown docs for other AI agents to consume.

Two modes:
- **Code mode**: generates openwiki/ docs in current repo, updates AGENTS.md/CLAUDE.md
- **Personal mode**: builds local brain wiki at ~/.openwiki/wiki/ from connectors

Output format: Google Open Knowledge Format (OKF) v0.1

### Architecture
| Layer | Technology |
|-------|-----------|
| Runtime | Node.js CLI (~70KB) |
| Agent engine | LangChain DeepAgents |
| LLM providers | OpenAI, Anthropic, Gemini, AWS Bedrock, OpenRouter, 12+ total |
| Diagrams | Auto-generated Mermaid (self-healing validation) |
| Storage | SQLite (checkpointing), flat markdown files |
| CI/CD | GitHub Actions, GitLab CI, Bitbucket Pipelines |

### How It Works
1. openwiki --init: scans repo, calls LLM, writes wiki as markdown
2. openwiki --update: uses git diff to detect changes, selectively updates affected pages
3. CI schedule (e.g. daily): creates PR with doc changes

### Features
1. Agent-native documentation — structured for LLM comprehension
2. Incremental updates via git diff — conserves API tokens
3. Auto-generated Mermaid diagrams with self-healing validation
4. Connector ecosystem: Gmail, Notion, X, Slack, web search, Hacker News for personal mode
5. Multi-provider: 12+ LLM providers with custom model support
6. AGENTS.md/CLAUDE.md integration — idempotent, preserves user content
7. CI/CD workflows — pre-built pipelines
8. OAuth flows for Gmail, X, Notion, Slack
9. LangSmith tracing — full observability

---

## 13. MinerU

**Repo**: https://github.com/opendatalab/MinerU
**Stars**: 75.6k | **License**: MinerU OSL (Apache 2.0 based)

### Overview
High-accuracy document parsing engine. Converts PDF, DOCX, PPTX, XLSX, images, web pages into structured Markdown/JSON for LLM, RAG, and Agent workflows. Built by OpenDataLab (InternLM team).

### Architecture — 3 Inference Backends
- **pipeline**: fast, CPU/GPU, no hallucination
- **vlm-engine**: VLM-based, high accuracy (vLLM/LMDeploy/mlx)
- **hybrid-engine**: native text + VLM, low hallucination

3-layer deployment: mineru CLI → mineru-api (FastAPI) → mineru-router (multi-service, multi-GPU load balancer)

Sliding-window for ultra-long documents (10k+ pages). Supports CUDA, CANN (Ascend), MPS (Apple Silicon), pure CPU.

### Key Features
- Input: PDF, image, DOCX, PPTX, XLSX, web pages
- Output: multimodal/NLP Markdown, reading-order JSON, HTML tables, LaTeX formulas
- Auto-detects scanned/garbled PDFs → OCR fallback
- OCR: 109 languages (PP-OCRv6 engine), ~11% accuracy improvement in v3.4
- Removes headers/footers/page numbers, preserves reading order, merges cross-page tables
- VLM model: MinerU2.5-Pro-1.2B for image/chart parsing
- MCP Server
- LangChain, LlamaIndex, Dify, FastGPT native integration
- REST API + Python SDK + CLI + Docker

---

## 14. Hyper-Extract

**Repo**: https://github.com/yifanfeng97/Hyper-Extract
**Stars**: 3.2k | **License**: Apache 2.0

### Overview
LLM-powered knowledge extraction CLI/framework. Transforms unstructured text into structured knowledge abstractions (graphs, hypergraphs, models, lists).

### Architecture — 3 Layers
1. **Auto-Types**: 8 data structures (AutoModel, AutoList, AutoSet, AutoGraph, AutoHypergraph, AutoTemporalGraph, AutoSpatialGraph, AutoSpatioTemporalGraph)
2. **Methods**: 10+ extraction algorithms (KG-Gen, GraphRAG, LightRAG, Hyper-RAG, Cog-RAG, iText2KG)
3. **Templates**: 80+ domain presets (finance, legal, medical, TCM, industry, general)

LLM-agnostic: OpenAI, Anthropic Claude (opus-4/sonnet-4/haiku-4), Alibaba Bailian (qwen), local vLLM (Qwen3.5-9B)

### Key Features
- Zero-code extraction via YAML templates
- Incremental knowledge evolution — feed new docs without reprocessing
- CLI commands: he parse, he feed, he search, he show, he talk, he export obsidian
- Obsidian vault export (Markdown with [[wikilinks]])
- Interactive knowledge graph visualization
- Semantic search + RAG Q&A
- Python SDK for custom pipelines
- MCP Server (he-mcp)

### Comparison with MinerU
| Aspect | MinerU | Hyper-Extract |
|--------|--------|---------------|
| Primary function | PDF/Office → clean text/markdown | Text → structured knowledge (graphs, models) |
| Stage in pipeline | Raw document ingestion | Post-parsing knowledge extraction |
| Key strength | Layout+OCR parsing | LLM-driven entity/relation extraction |
| Output | Markdown, JSON, HTML, LaTeX | Pydantic models, knowledge graphs, hypergraphs |
| Deployment | CLI, FastAPI, Docker, MCP | CLI, Python SDK, MCP |

---

## 15. qmd

**Repo**: https://github.com/tobi/qmd
**Stars**: ~28k | **Forks**: ~1.8k

### Overview
On-device hybrid search engine for markdown notes, docs, meeting transcripts, and knowledge bases. Indexes locally. Supports BM25 + vector + LLM reranking.

### Features
- Three search modes: search (BM25 keyword), vsearch (vector semantic), query (hybrid + reranking)
- Query expansion via fine-tuned GGUF model
- MCP server integration (stdio or HTTP transport)
- SDK for Node.js/Bun applications
- Context metadata that improves search relevance
- AST-aware chunking for code files
- Export formats for agentic workflows (JSON, files)
- ChromaDB-style architecture with SQLite FTS5 + vector embeddings

### Architecture
SQLite FTS5 for keyword search + vector embeddings for semantic search + GGUF reranker model for hybrid results. Fully on-device, no cloud dependency.

---

## 16. Cloud Run Sandboxes

**URL**: https://cloud.google.com/blog/topics/developers-practitioners/google-cloud-run-sandboxes-are-in-public-preview
**Date**: July 10, 2026 (Public Preview)

### Overview
Native, ultra-fast sandboxed runtime within Cloud Run for executing untrusted code (AI-generated, user-submitted, headless browsers). Starts in milliseconds.

### Key Features
- Zero-trust security: no credential access, deny-by-default network egress, read-only filesystem with temp overlay
- LLM code interpreters: execute Python/R/SQL generated by AI in isolation
- Headless browsers: safe web scraping, screenshots, browser automation
- ADK integration: CloudRunSandboxCodeExecutor in Google Agent Development Kit
- ComputeSDK support: vendor-agnostic SDK for local or remote invocation
- No additional cost: runs on existing allocated CPU/memory, no premium
- Simple API: sandbox do -- python3 script.py

---

## 17. awesome-mcp-servers

**Repo**: https://github.com/punkpeye/awesome-mcp-servers
**Stars**: ~91k | **Forks**: ~13.5k

### Overview
Curated directory of MCP (Model Context Protocol) servers. Largest community index of MCP-compatible tools for Claude Code, Codex, and OpenCode. 9,700+ commits.

### Features
- Categorized by function (browser automation, database, file system, search)
- Community-driven via PRs
- Companion site at glama.ai/mcp/servers

---

## 18. obsidian-skills

**Repo**: https://github.com/kepano/obsidian-skills
**Stars**: ~43k | **Forks**: ~3.1k

### Overview
Agent skill pack for Obsidian integration with Claude Code, Codex CLI, and OpenCode. Lets AI agents read/write Obsidian vaults natively.

### Skills Included
- **obsidian-markdown**: Create/edit Obsidian Flavored Markdown (wikilinks, embeds, callouts, properties)
- **obsidian-bases**: Create/edit Obsidian Bases (.base files with views, filters, formulas)
- **json-canvas**: Create/edit JSON Canvas (.canvas files with nodes, edges, groups)
- **obsidian-cli**: Interact with vaults via Obsidian CLI (plugin/theme dev)
- **defuddle**: Extract clean markdown from web pages

---

## 19. free-for-dev

**Repo**: https://github.com/ripienaar/free-for-dev
**Stars**: ~130k | **Forks**: ~13.6k | **Contributors**: 1,600+ | **Commits**: 7,100+

### Overview
Comprehensive directory of SaaS, PaaS, and IaaS offerings with free tiers for developers. 60+ categories.

### Categories Covered
Cloud providers, analytics, APIs/ML, CI/CD, databases, DNS, email, hosting, monitoring, search, security, auth, storage, logging, and more.

Each entry specifies exact free tier limits.

---

## 20. archify

**Repo**: https://github.com/tt-a1i/archify
**Stars**: ~7.2k | **Forks**: ~489

### Overview
Agent skill that generates interactive system architecture diagrams from codebase descriptions — directly in chat. Fork/rewrite of Cocoon-AI's architecture-diagram-generator.

### Features
- 5 diagram types: Architecture, Workflow, Sequence, Data Flow, Lifecycle
- 4 visual presets: Classic, Signal Flow, Blueprint, Editorial + dark/light themes
- Architecture Delta Review: compare Before/Delta/After for PR reviews
- Typed JSON IR: reproducible source with schema validation
- Interactive viewer: search nodes, trace routes, compare roles, guided stories
- Exports: self-contained HTML, PNG, SVG, WebM, 1200×630 share cards
- Atomic validation: schema, layout, HTML/SVG, route checks
- Evidence-backed nodes: links to Git-verified source files/line ranges
- Deployment ownership profile: validates owners, regions, DB scopes, boundaries
- Works with Claude Code, Codex CLI, Cursor, OpenCode

---

## 21. Metabase

**Repo**: https://github.com/metabase/metabase
**Stars**: ~48.3k | **Language**: Clojure (54%) + TypeScript (39%) | **License**: AGPL v3 / Commercial

### Overview
Open-source Business Intelligence (BI) tool. Non-technical users query databases and build dashboards via visual UI; engineers use SQL editor, REST API, and embedding SDK.

### Architecture
- Backend: Clojure (JVM) — REST API + query processor pipeline. Pluggable driver system for 20+ databases.
- Frontend: React SPA (TypeScript, Rspack bundler). Modular with clj-kondo-enforced boundaries.
- Query Processor: MBQL (Metabase Business Query Language) through 30+ step middleware pipeline.
- Application DB: H2 default, Postgres recommended.
- Deployment: Single JAR, Docker, Metabase Cloud.

### Key Features
- Visual Query Builder — no-SQL question creation
- Native SQL Editor with auto-complete
- Dashboards with filters, auto-refresh, subscriptions (email/Slack/webhook)
- Metabot (AI): natural-language → SQL/query, open-sourced v62+
- Agent API: purpose-built LLM endpoint (capped 200-row results, continuation tokens, typed schemas)
- Embedding: iframe, React SDK (charts, dashboards, AI chat, query builder)
- MCP Server: built-in Enterprise MCP (/api/mcp) — 6 agent tools, JSON-RPC + SSE
- Permissions: granular row-level + collection-level, sandboxing
- Data Studio: transforms, canonical metrics, versioned with Git

### Chatbot Integration Paths
1. Metabot React SDK: useMetabot hook + MetabotQuestion component — embed NL→chart chat UI
2. Agent API (/api/agent): LLM-native REST, structured tool-calling, returns typed JSON
3. MCP Server (Enterprise): standard MCP tools for queries, schema exploration

---

## 22. Obscura

**Repo**: https://github.com/h4ckf0r0day/obscura
**Stars**: ~19.7k | **Language**: Rust (99.8%) | **License**: Apache 2.0

### Overview
Headless browser engine written in Rust, purpose-built for AI agents and web scraping. Drop-in replacement for headless Chrome with Puppeteer/Playwright. Embedded V8 JS engine, CDP-compatible, MCP-native.

### Architecture
- Core: Rust binary embedding V8 JavaScript engine (no Chrome/Node dependency)
- Networking: reqwest HTTP client; custom TLS fingerprinting in stealth builds
- CDP Server: tokio-tungstenite WebSocket on port 9222, ~30 CDP methods across 9 domains
- Stealth Layer: compiled-in via --features stealth — TLS ClientHello spoofing, per-session fingerprint randomization, 3,520-domain tracker blocklist
- Workers: multi-process round-robin for parallel scraping
- MCP Server: built-in obscura mcp command with 11 browser-automation tools

### Key Features
- Performance: ~30 MB RAM, ~70 MB binary, ~85 ms page load, instant startup
- CDP compatibility: Puppeteer/Playwright drop-in
- Stealth Mode: anti-fingerprinting, navigator.webdriver = undefined, 0% detection (creepjs)
- SSRF Protection: blocks private IP ranges (127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
- MCP tools: browser_navigate, browser_snapshot, browser_click, browser_fill, browser_evaluate, browser_network_requests, browser_console_messages
- Scraping: obscura fetch, obscura scrape (parallel), --dump html|text|links|markdown|assets|original
- Request Interception: observe, block, mock, rewrite any request

---

## 23. claude-code-setup

**Repo**: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup
**Author**: Anthropic (Isabella He)

### Overview
Official Anthropic-maintained plugin from claude-plugins-official marketplace. Read-only codebase analyzer that scans project structure, dependencies, and code patterns, then recommends tailored Claude Code automations.

Install: /plugin install claude-code-setup@claude-plugins-official, then /reload-plugins.

### Features
Scans package.json, language files, directory layout, and existing config. Surfaces top 1-2 recommendations per category (3-5 if specific category requested):

| Category | Purpose | Examples |
|----------|---------|----------|
| MCP Servers | External tool/data integrations | Context7 (docs), Playwright (frontend), DB MCP |
| Skills | Reusable packaged expertise | Plan agent, frontend-design |
| Hooks | Automatic actions on tool events | auto-format, auto-lint, block .env edits |
| Subagents | Specialized isolated reviewers | Security, performance, accessibility |
| Slash Commands | Quick command shortcuts | /test, /pr-review, /explain |

### Invocation Prompts
- "recommend automations for this project"
- "help me set up Claude Code"
- "what hooks should I use?"
- "what MCP servers should I use?" (expanded list)

Plugin is read-only — analyzes and recommends but does not modify files.