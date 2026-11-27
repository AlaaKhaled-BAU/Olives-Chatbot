# Safe enhancements

This plan changes ten small spots. None of them adds a memory store, a summary of old chats, or a ban on free queries. A monthly sales total still adds every matching invoice. Two people in two conversations still run at the same time.

Words used below:

- **The gate** is `core/gate.py`. It reads a query before it runs. It allows one read query, blocks writes, and can add a company filter and a row limit.
- **The runner** is `core/sql.py`. After the gate says yes, it sets the company on the database connection and runs the query as the read-only login `chatbot_ro`.
- **The agent** is `core/agent.py`. It is the loop that sends the question to the model, runs the tools the model asks for, and builds the answer.
- **The web server** is `api/server.py`. The screen calls `POST /ask` to ask a question and `GET /health` to see if the service is up.
- **Metrics** are `core/metrics.py`. They are saved formulas for sales, returns, orders, and similar totals, so those numbers are computed the same way every time.
- **The vault** is `core/vault.py`. It searches the written notes about tables and joins. It does not run SQL.
- **Refresh** is `setup/refresh.py`. A person runs it by hand after the database shape changes. It is not part of a user question.

## 1. Company filter on `dbo`

### What we have

The model is told to query views named `t.Customers`, `t.TransactionsHeaders`, and so on. Those views already hide other companies. The gate also adds `CompanyID = <this session>` when it sees `t.Something`. Shared lists such as currencies are left open on purpose. They have no company column.

If the database has no `t` schema, the runner rewrites `t.` to `dbo.` after the gate has already added the company filter. That path stays correct.

If the query is written as `dbo.Customers` from the start, the gate does not add the company filter. The query can see every company.

### What we will have

`dbo.Customers` gets the same company filter as `t.Customers`. `dbo.Currencies` and the other shared lists stay open. The `t.` views stay. The rewrite from `t.` to `dbo.` stays.

A `SUM` of the month still reads every invoice for that one company. It does not add a second trip to the model.

### Why this is better

The normal table names obey the same company wall as the views. Totals do not get smaller. Other companies do not leak in through a `dbo` query.

### Work

In the gate, the place that looks for schema `t` also looks for schema `dbo`. Tests: `dbo.Customers` gains the company predicate, `dbo.Currencies` does not, `t.Customers` still does.

## 2. Row cap on lists, not on totals

### What we have

If a query has no row limit, the gate adds `TOP 200` to the outer query. The database applies that limit after it has added numbers up.

So `SELECT SUM(amount) FROM invoices WHERE <this month>` becomes `SELECT TOP 200 SUM(amount) ...`. The database still adds every invoice in the month, produces one row, and returns that one row. Two hundred invoices or two thousand, the total is the full total. The model sees that one row.

The same `TOP 200` on `SELECT salesperson, SUM(amount) ... GROUP BY salesperson` keeps at most 200 people. Each person's own sum is complete. People past 200 disappear.

A query that lists invoice lines, with no limit, returns 200 lines. If the model wrote `TOP 5000`, the gate keeps 5000. The model is only shown 50 of those rows, and the screen shows 100. The extra rows are fetched and then thrown away.

### What we will have

Three rules:

- A query that is only a total (`SUM`, `COUNT`, or `AVG`, and no `GROUP BY`) gets no added `TOP`. A `TOP` already written on that query is left alone. The month is still the full month.
- A query with `GROUP BY` is not given a new `TOP`, and a `TOP` it already has is not lowered. A salesperson list is not cut by us.
- A query that lists rows (invoice lines, customers, and so on) with no limit gets `TOP 200`. If it asks for more than 200, it is lowered to 200. A `TOP 10` stays 10.

`truncated` is set only when we cut a detail list and the database returned exactly 200 rows. A one-row total is not marked truncated. A grouped list is not marked truncated by this rule.

### Why this is better

The total the user asked for does not change. A long ranking is not shortened. We stop reading thousands of detail rows that the model and the screen never show.

### Work

This lives in the gate, next to the company-filter change, with separate tests so the two behaviors are not confused. The agent copies `truncated` onto the tool result. The system prompt is not edited.

## 3. Known-bad totals, free queries stay

### What we have

Metrics hold the saved sales formula: the right invoice types, voided invoices excluded, header joined to lines. The agent still offers `run_select`, which runs any one read query through the gate.

If that free query counts invoice headers and forgets the type and the void filter, the gate returns an error that says to use the metric. The tool stays available, so the model can write a better query.

A question that says "sales" can also mean one customer, one item, or one odd date. The metric does not cover every such filter. Taking `run_select` away would make those questions impossible.

### What we will have

`run_select` stays on every path, including short count questions.

The existing header-count error stays. We add the same kind of error for a `SUM` of invoice header amounts that also lacks the type and void filters. If the query has a filter the metric does not offer, such as one customer, one item, or one salesperson, the error is not raised and the query runs.

No new sentence is added to the system prompt.

### Why this is better

A known-wrong total is pushed onto the saved formula. A question the formula cannot express still gets a real query. The model does not gain a step, and it does not lose a tool.

### Work

Extend the check in the gate. Tests: the bare header `SUM` is rejected, and the same `SUM` with a customer filter is allowed.

## 4. Empty is not zero

### What we have

When a query matches nothing, the tool returns an empty list. The prompt already tells the model that an empty month is empty and must not be called zero. The answer object has no extra flag. A successful total is a one-row list and needs nothing else.

### What we will have

When the tool result is an empty list, the model receives that empty list plus one line: this result is empty, and empty is not a zero total. A query that returned a row, including a row whose number is zero, does not get that line. The system prompt is not changed.

### Why this is better

The empty case is labeled at the moment it happens. A normal sales total is the same size and the same shape as today.

### Work

In the agent, where tool rows are prepared for the model. One test for `[]` and one test for a one-row total.

## 5. Glossary, only if notes were already searched

### What we have

`Glossary.md` is a written list of short names (BO, ZATCA, and others). The vault search only returns notes whose type is table, procedure, or relation, so the glossary never comes back. A sales question that does not search notes does not pay for this.

### What we will have

When the model already called note search, and the word is in the glossary, one glossary hit is added after the table notes. It does not take a table note's place. It does not start a new tool call. Procedure notes still have their body sections removed. The raw procedure dump is still not indexed.

### Why this is better

A definition can be found on a search that was going to happen anyway. Sales totals do not gain a step.

### Work

In the vault search function. Test that a table note still fills the limit, and the glossary hit is an extra item when the word matches.

## 6. Same conversation waits, others do not

### What we have

Each question starts its own background work. Two questions with the same `session_id` share one session record and can overwrite each other. Two different `session_id` values are already independent. There is no "still working" state. Returning an error on the second click would throw away a question the user meant to ask.

The rate limit uses a different header, `X-Session-Id`. That header only chooses the rate-limit bucket. It is not the conversation id.

### What we will have

The lock key is the `session_id` in the question body.

- A second question with that same id waits until the first finishes, then runs.
- A different id never waits.
- A question with no id is not piled onto one shared anonymous lock.
- The lock is released when the turn ends, including cancel and error.
- The user gets an answer. We do not return 409.

### Why this is better

One conversation cannot corrupt its own history. Everyone else stays as fast as they are now. A double-click still produces an answer instead of an error.

### Work

In the web server, around `POST /ask`. Tests: two different ids overlap, the same id runs one after the other, a missing id does not block other missing ids.

## 7. Refresh updates columns and leaves the prose

### What we have

Refresh rebuilds the schema cache, rebuilds the `t.` views, drops leftover views, clears the saved-query cache, and recompiles the note cards from the notes as they are. It does not update the column lists inside the notes.

A separate command already does that column update. It rewrites the Columns section and the foreign-key list in the note header. It does not rewrite the business-purpose paragraphs. Nobody runs it as part of refresh, so a renamed column can stay wrong in the notes until someone remembers the second command.

Neither command runs while a user is asking a question.

### What we will have

Refresh runs that column update after it rebuilds the schema cache. The business-purpose text of a note is the same bytes before and after. Questions still do not write notes.

### Why this is better

One admin command follows a renamed column. The sentences a person wrote stay. Chat does not get slower.

### Work

Call the existing sync from refresh. Test a note whose purpose paragraph is unchanged and whose Columns section shows the new name.

## 8. Procedure names use the keys that exist

### What we have

The join tool asks the graph file for `reads_by` and `writes_by`. The file stores `procedures_reading` and `procedures_writing` on every table. The lists come back empty. Live foreign keys from the schema cache already decide how tables join. Those keep working.

The graph's caller and callee links are a different issue and are not part of this change.

### What we will have

The tool reads `procedures_reading` and `procedures_writing`. Live foreign keys still decide the join. The procedure lists are labeled as names, not as join instructions. Caller and callee are not swapped. The graph file is not rebuilt.

### Why this is better

Names that are already in the file show up. The join the model uses for SQL does not change.

### Work

Two key names in the vault join function. A test fixture uses the real key names and expects those lists, and expects the live foreign key to remain the join.

## 9. Health tells three facts

### What we have

`GET /health` checks that the model provider answers and that `SELECT 1` works. If the schema cache file or the document index is missing, health can still say ok. The first sign is an empty search during a real question. This endpoint does not call the model to answer a user.

### What we will have

For the pinned client, health reports three separate yes/no facts: the schema cache file parses, the document index file exists, and `SELECT 1` succeeds. Overall ok is true only when the provider and all three are true. The tenant pack, which runs four extra queries and is only used in tests, is not called.

### Why this is better

An operator can see a missing file before a user asks. A question takes the same path it takes today.

### Work

In the health function. Tests with a missing file and with the files present.

## 10. Name the gaps only when we already cannot answer

### What we have

The agent may run four business queries. If it still has no evidence and no answer text, the user sees: "I can't answer that confidently from the available data." That sentence does not say which words matched nothing.

Refusing before any query would drop real questions whose wording is not in the metric alias list.

### What we will have

Tools stay. The model is still called. SQL still runs when the model asks for it.

Only in that existing refusal, we append the words from the question that matched no metric alias, no report alias, and no viewable table name. If every word matched something, we append nothing.

### Why this is better

A dead end is more specific. A question we can answer is unchanged, including Arabic phrasing the alias list does not contain.

### Work

At the one refusal line in the agent. Test a refusal that names an unknown word, and a normal sales question that still runs SQL.

## Order

1. Company filter and detail cap, in the gate, with separate tests.
2. Bare invoice `SUM` error.
3. Empty-result line.
4. Glossary extra hit.
5. Session queue.
6. Refresh column sync.
7. Join key names.
8. Health flags.
9. Refusal names.

## Left alone

Chat memory and history limits. The plan cache that saves SQL and runs it again. The 45-second row cache. The DeepSeek prefix cache. Password columns. A ban on `run_select`. An early coverage refusal. A 409 on a second click. A `TOP` on a pure total. A lowered `TOP` on a grouped list.
