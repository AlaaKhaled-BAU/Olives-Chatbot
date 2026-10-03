# Agentic Harness Explained

Source: poster titled **AGENTIC HARNESS EXPLAINED** (orange-to-blue title). Credit badge: **Greg Coquillo, Product Leader**.

The poster is a light-blue page of rounded panels. Each panel has a bold header, a one-line subtitle, and a body of boxes, a diagram, or a list. Nothing below is an interpretation of our chatbot. It is the poster, panel by panel.

---

## 0. Title

- **AGENTIC HARNESS EXPLAINED**
- The word "AGENTIC" is orange. "HARNESS EXPLAINED" is blue.
- No subtitle under the title. The definition starts in the first panel.

---

## 1. What is an Agentic Harness?

**Subtitle:** Model + Harness = Agent

### 1.1 Equation

**Model + Harness = Agent**

The model alone is not the agent. The harness is the rest of the system wrapped around it.

### 1.2 Diagram: eight nodes around the model

A hub-and-spoke. The center circle is **Model**. Eight surrounding nodes:

| Node | Place in the ring |
|---|---|
| Context | upper left |
| Tools | top |
| Prompts | upper right |
| Memory | right |
| Guardrails | lower right |
| Agent loop | bottom |
| Sandbox | left |
| (the spokes connect each node to Model) | |

### 1.3 Body text (verbatim sense)

An agentic harness is everything around the language model that turns a text predictor into a system that can act: the loop that keeps it running, the tools it can call, what enters its context each turn, where its actions execute, and the rules that keep it safe.

The model is the brain. The harness is the body and nervous system: it senses, executes, and sets limits. The weights never change, but the results do.

Quoted line: **"Same model, different harness, different results."**

### 1.4 What each idea is, in the poster's own terms

- **Model:** the text predictor. Weights are fixed. It does not become a different model when the harness changes.
- **Harness:** loop, tools, context selection, execution place, and safety rules.
- **Agent:** the sum. Change the harness and the same model produces different results.
- **Brain vs body:** the model decides text. The harness senses the world, runs actions, and limits them.

---

## 2. Anatomy of a Harness

**Subtitle:** The 8 building blocks

Eight boxes in two columns. This is the poster's checklist of what a harness is made of.

### 2.1 System prompt & skills

- **Label:** System prompt & skills
- **Gloss:** Role, rules, task specs
- What the model is told it is, what it must not do, and how a task is specified. Skills are task specs the harness can load, not a second model.

### 2.2 Tool registry

- **Label:** Tool registry
- **Gloss:** Schemas the model can call
- The list of callable functions, each with a name and an argument schema. If it is not in the registry, the model cannot call it.

### 2.3 Agent loop

- **Label:** Agent loop
- **Gloss:** Reason → act → observe
- The cycle that keeps the model running until the task is done. Detailed in panel 3.

### 2.4 Context manager

- **Label:** Context manager
- **Gloss:** What the model sees each turn
- The component that chooses which text is inside the window on this turn. Not the same as memory. Memory stores. The context manager selects.

### 2.5 Memory

- **Label:** Memory
- **Gloss:** Session state + persistent files
- Two kinds: state that lives for this session, and files that survive the session.

### 2.6 Permissions & guardrails

- **Label:** Permissions & guardrails
- **Gloss:** Allow / ask / block
- Three outcomes for an action. Allow it, ask a human, or block it. Detailed in panel 6.

### 2.7 Sandbox / environment

- **Label:** Sandbox / environment
- **Gloss:** Where actions run safely
- The place a tool's effect actually happens, separated from the rest of the machine.

### 2.8 Observability & hooks

- **Label:** Observability & hooks
- **Gloss:** Traces, metrics, evals
- Three products: a trace of what happened, numbers about it, and evals that score it. Hooks are the points where the harness records or checks, before and after an action.

---

## 3. The Core Agent Loop

**Subtitle:** How one task moves through the system

### 3.1 The eight steps, left to right

A horizontal chain. Above the chain, a dashed return arrow labeled **"If not done: loop back with new context."** It runs from the Done? step back toward the start of the loop (Reason / Act), not back to the user.

| Step | Color role | One-line gloss on the poster | Who owns it |
|---|---|---|---|
| 1. Goal | orange circle | User task or trigger | HARNESS |
| 2. Reason | orange circle | Model reads context, plans next step | MODEL |
| 3. Act | orange circle | Model emits a tool call | MODEL |
| 4. Execute | blue circle | Harness runs it in the sandbox | HARNESS |
| 5. Observe | blue circle | Result appended to context | HARNESS |
| 6. Verify | blue circle | Tests, checks, self-review | HARNESS |
| 7. Done? | blue circle | Stop, or loop again | HARNESS |
| 8. Answer | blue circle | Final output + saved state | HARNESS |

### 3.2 The sentence under the chain

**"The model only ever does two things: reason and choose an action. Every other step, including deciding whether to call the model again, belongs to the harness."**

So Goal, Execute, Observe, Verify, Done?, and Answer are harness. Reason and Act are model.

### 3.3 What each step is

- **Goal.** Something outside the model starts the task: a user message or a trigger. The harness frames it as the goal.
- **Reason.** The model reads whatever the context manager put in the window and plans the next step.
- **Act.** The model emits a tool call. It does not run the tool.
- **Execute.** The harness runs that call inside the sandbox.
- **Observe.** The harness appends the result to the context the model will see next.
- **Verify.** The harness tests, checks, or self-reviews the result. This is not the model grading itself unless the harness asks it to.
- **Done?** The harness decides to stop or to loop. The loop carries new context (the observation), not the same prompt again.
- **Answer.** Final output to the user, plus state saved for later.

---

## 4. Tool Call Lifecycle

**Subtitle:** What happens when the model uses a tool

### 4.1 Five steps

1. **Model emits a call.** Structured JSON: a name and arguments.
2. **Harness validates.** Schema check. Permission check.
3. **Executes in sandbox.** Examples named on the poster: shell, file, API, MCP server.
4. **Post-processes result.** Truncate, format, capture errors.
5. **Appends to context.** The model sees the observation on the next turn.

### 4.2 Tool design rules (six bullets)

- **Fewer, more expressive tools beat a long menu of narrow ones.**
- **Descriptions are prompts.** They say when to use the tool and what it returns.
- **Return errors the model can act on, not stack traces.**
- **Cap output size.** Big results should go to a file, not into the context.
- The poster groups these as "Tool Design Rules" beside the lifecycle. Two of them are about the menu and the description. Two are about what comes back (actionable errors, size cap).

---

## 5. Context & Memory Management

**Subtitle:** What the model sees each turn, and what it remembers

This panel is split into a budget diagram and four tactics.

### 5.1 A typical context-window budget

Five segments of one bar:

| Share | What fills it |
|---|---|
| 10% | System prompt & skills |
| 10% | Tool definitions |
| 25% | Conversation |
| 40% | Tool results |
| 15% | Headroom |

Headroom is empty space left on purpose so the next observation still fits.

### 5.2 How the harness keeps context small and relevant

Four tactics:

1. **Compaction.** Summarize old turns when the window fills.
2. **Persistent memory.** Files that survive sessions: preferences, project facts.
3. **Observation masking.** Drop stale tool outputs. Keep the decisions.
4. **Just-in-time loading.** Retrieve docs, skills, and code only when needed.
5. **Scratchpad files.** Write plans and notes to disk. Read them back on demand.

The poster shows these as the methods under the budget, not as five more building blocks. Compaction and masking shrink the window. Persistent memory and scratchpads live outside the window. Just-in-time loading decides what enters.

---

## 6. Guardrails & Permissions

**Subtitle:** Every action passes through a policy gate

### 6.1 The gate

A proposed action enters from the left. The example on the poster is **`rm -rf`** or **Build**.

The diamond is **Policy Check**. The axes named on the diamond:

- allowlist
- risk
- budget

Three exits:

| Exit | When | Examples on the poster |
|---|---|---|
| **AUTO-ALLOW** | Read-only, reversible, inside the sandbox | (no extra examples) |
| **ASK A HUMAN** | Writes, payments, external messages | |
| **BLOCK** | Destructive, out of scope, deny-listed | |

### 6.2 Constraints around the gate

- **Max turns / tokens / cost.** A budget, not only a safety list.
- **Timeouts per step.**
- **Isolated sandbox.**
- **Secrets never in context.**
- **Pre- and post-tool hooks.**
- **Confirm before irreversible ops.**

---

## 7. Orchestration & Sub-agents

**Subtitle:** Splitting work across specialised agents

### 7.1 Shape

An **ORCHESTRATOR** on top: plans, delegates, merges results.

Three workers under it:

| Agent | Job | Constraint |
|---|---|---|
| Research Agent | Searches docs & web | Own context window |
| Coding Agent | Edits & runs tests | Own tools & sandbox |
| Review Agent | Checks the diff | Read-only permissions |

### 7.2 Rules under the tree

- **Shared state lives in files & task lists, not in one giant context.**
- **Sub-agents run in parallel and return only what matters.**

### 7.3 Three ways to split work

| Mode | When |
|---|---|
| Single loop | Simple tasks |
| Orchestrator → workers | (the tree above) |
| Pipeline / handoffs | Long-running: checkpoint & resume |

A fourth note sits with them: **Human-in-the-loop checkpoints.**

---

## 8. Observability, Evals & the Improvement Loop

**Subtitle:** You cannot fix what you cannot trace

### 8.1 What to measure on every run

Six metrics in two rows of three:

| Metric | What it counts |
|---|---|
| Task success rate | % of tasks completed correctly |
| Cost per task | tokens × price, per run |
| Turns to finish | fewer loops = better harness |
| Tool error rate | failed / malformed calls |
| Latency | wall-clock per task |
| Human interventions | how often a person had to step in |

### 8.2 Example trace strip

A small sequence drawn under the metrics:

`reason` → `call: read_file` → `result 2.1 KB` → `reason` → `call: run_tests` → `3 failed` → `reason` → `done` · **7 turns · $0.42**

The point of the strip: a trace is a chain of reasons, calls, and results, and it ends with a turn count and a dollar cost.

### 8.3 The harness-engineering flywheel

Five steps, each with a meaning:

| Step | Meaning on the poster |
|---|---|
| 1. Observe a failure | Trace shows where it went wrong |
| 2. Find the root cause | Bad tool, missing context, weak check |
| 3. Change the harness | New tool, prompt rule, guard, verifier |
| 4. Add a regression eval | The task now lives in the test suite |
| 5. Ship & re-run | Every future run is protected |

The flywheel says: a failure becomes a test. The fix is a harness change (tool, prompt, guard, or verifier), not a change to the model weights.

---

## 9. Cross-panel links (what the poster treats as one system)

These are not a ninth panel. They are the same ideas showing up twice, so a catalog that lists panels only would split them.

- **Context manager** (block 4) is what fills the **budget** (panel 5) and what **Observe** appends to (panel 3).
- **Memory** (block 5) is session state plus files. Panel 5 splits that into compaction, persistent files, and scratchpads.
- **Permissions** (block 6) are the **policy gate** (panel 6): allow, ask, block.
- **Sandbox** (block 7 and the ring) is where **Execute** happens, and where AUTO-ALLOW must stay.
- **Observability** (block 8) is traces, metrics, and evals, and it is also the flywheel's first step.
- **Agent loop** (block 3) is the eight-step chain. The model owns only Reason and Act.
- **Tools** on the ring are the registry plus the five-step lifecycle plus the six design rules.
- **Prompts** on the ring are the system prompt, the skill specs, and the tool descriptions ("descriptions are prompts").
- The quote **"same model, different harness, different results"** is the reason the flywheel changes the harness, not the weights.

---

## 10. Inventory, so nothing in the drawing is dropped

- Title and color split
- Author badge: Greg Coquillo, Product Leader
- Equation Model + Harness = Agent
- Ring of eight: Context, Tools, Prompts, Memory, Guardrails, Agent loop, Sandbox, Model at the center
- Brain / body sentence
- Quote about the same model
- Eight anatomy blocks with their one-line glosses
- Loop of eight steps with harness/model tags
- Dashed "if not done" arrow
- Closing sentence: the model only reasons and chooses an action
- Tool lifecycle, five steps, JSON name + arguments
- Sandbox examples: shell, file, API, MCP server
- Post-process: truncate, format, capture errors
- Four tool-design rules
- Context budget 10 / 10 / 25 / 40 / 15
- Five context tactics: compaction, persistent memory, observation masking, just-in-time loading, scratchpad files
- Policy diamond: allowlist, risk, budget
- Three verdicts: AUTO-ALLOW, ASK A HUMAN, BLOCK
- Example actions: `rm -rf`, Build
- Six gate constraints: max turns/tokens/cost, timeouts, isolated sandbox, secrets never in context, pre/post hooks, confirm irreversible ops
- Orchestrator: plans, delegates, merges
- Three sub-agents and their permission boundaries
- Shared state in files and task lists
- Parallel sub-agents return only what matters
- Three split modes plus human checkpoints
- Six run metrics
- Sample trace ending in 7 turns and $0.42
- Five-step flywheel

---

## 11. This chatbot against that poster

Read back after the catalog above. The poster is a general harness. This product is one read-only analyst. "Must have" means a hole that already makes a user wrong or lost. It does not mean building every box on the poster.

### Already in place

| Poster piece | Where it lives here |
|---|---|
| Model is not the agent | DeepSeek is called from `core/llm.py`. The loop, tools, and gate are ours. |
| System prompt and task specs | `prompts/system.md` plus `prompts/join_playbook.md`, byte-stable so the provider can cache them. |
| Tool registry | Schemas in `core/agent.py`: `search_docs`, `run_select`, `run_metric`, `run_report`, `ask_user`, `analyze`, `recall_turns`, schema tools. |
| Agent loop, reason then act | `ask_stream`. The harness stops at `MAX_QUERIES = 4` and after results are in context. The model does not decide the budget. |
| Execute in a sandbox | `chatbot_ro`, `t.` views, `SESSION_CONTEXT` company. `core/gate.py` rejects writes, `EXEC`, and `dbo`. |
| Allow / ask / block | Block is the gate. Ask is `ask_user`. Allow is a select that passed the gate. |
| Secrets out of the prompt | The API key is read only in `core/llm.py`. |
| Memory: session plus files | `work/sessions.sqlite` (100 turns, 30 days). Plan cache and result cache in `core/memory.py`. |
| Just-in-time docs | `search_docs` and schema tools. The vault is not stuffed into every turn. |
| Traces, latency, evals | `core/trace.py`, `tools_ms` on the done event, `evals/` and pytest. |
| Timeouts | Gear timeouts in `core/llm.py`. |
| Single loop | No orchestrator. The poster says single loop is the mode for a simple task. This bot should stay one loop. |

### Missing, and must have

1. **A context manager for the last result.** The poster splits memory (what is stored) from the context manager (what this turn sees). We store 100 turns and show the model 4 clipped answers, about 220 characters each. The headline number, the month, and the basis fall out of that clip. «قديش منيحين؟» and «قبل الضريبة» then guess. The thread card in `docs/superpowers/plans/2026-10-02-chat-thread.md` is this box. It is compaction of the decision, not a second chat log.

2. **Verify before Answer.** Step 6 on the poster is the harness, not the model. Nothing checks that a stated invoice count matches a header count. The live July answer said 5 invoices because `COUNT(*)` ran on detail lines. Two headers, five lines, money still 449.00. A check that fails the turn when the prose count disagrees with `invoice_count` from a header query is the missing verifier. The playbook line (count headers, not the join) is the guard that should sit next to it.

3. **Cost and turns on the trace.** The poster’s sample trace ends with `7 turns · $0.42`. We log latency and `tools_ms`. Token use is printed by `core/llm.py` and not stored as cost-per-question on `trace.jsonl`. Without that, the flywheel’s "cost per task" metric does not exist. Add tokens and turn count to the done event. Do not add a new tracing product.

4. **The flywheel’s last two steps, as a habit.** We already have eval files. A live miss (5 invoices, empty-session follow-up) did not become a regression row by itself. The must-have is small: when a checked failure is real, add one case to the golden or unit tests before the next change. Not a new eval platform.

### On the poster, and we should not build

| Poster piece | Why it stays out |
|---|---|
| Research / coding / review sub-agents | One question, one database, one loop. Workers would duplicate the gate and burn the balance. |
| Shell, file, and MCP as the sandbox | The sandbox here is SQL. Adding a shell is a different product and a larger blast radius. |
| A 25% conversation share of the window | Our window is mostly schema and playbook, on purpose, so the cache hits. Growing the chat to a quarter of the prompt fights that. |
| A second model call to rewrite every follow-up | Same reason: cost. The card replaces it. |
| Scratchpad files and a coding-agent task list | Nothing in this bot writes plans to disk for itself. |
| Ask-a-human for every write | The app cannot write. The gate already blocks. |

### Verdict

The harness around the model is real: tools, gate, tenant sandbox, loop cap, traces, evals. The weak panels are the ones the user touches. The context manager does not keep the last decision. The verify step does not check the sentence against the query. Cost is not on the trace, so a bad run cannot be compared to the poster’s `$0.42`. Sub-agents, a shell, and a long chat transcript are not the missing parts.
