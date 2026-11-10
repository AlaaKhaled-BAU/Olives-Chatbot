# Website ↔ chatbot integration

How the existing Olives IIS site talks to this bot. This is the call contract, not a UI design.

Evidence: `api/server.py` (routes and SSE), `README.md` and `run.ps1` (Windows process), `docs/SYSTEM_BLUEPRINT.md` (product boundary), and `C:\Users\Abed\OneDrive\Desktop\customers` (2026-11-07). The customer tree is compiled sites plus `Olives_BO.dll`. There is no chatbot client inside that folder. `FIXPLAN.md` mentions `uvicorn` on port 8000 in one example; the running contract is `README.md` / `run.ps1`: `127.0.0.1:8100`, and that script exits when the console closes.

## What each side is

| Side | Process | Database login |
|---|---|---|
| Olives website | IIS, ASP.NET, per-customer folders (`ALSALAM`, `AMANAFOOD`, `ecoland`, `Luxury`, `mashrek`, `saprten`, `Thimar`, `yan`, `canary`) and `Olives_BO.dll` | SQL login `cds`, `CompanyID` in the site session |
| Chatbot | Separate Python process (`uvicorn api.server:app`). Not an IIS application today | `chatbot_ro` plus `t.` views. Never `cds`, never SA |

The DLL is not loaded by the bot. The site calls HTTP. Tenant is pinned by `CHATBOT_CLIENT` on the bot; the browser cannot switch `clients/*.yaml`.

## Where port and database login come from

`api/server.py` loads the gitignored `.env` at startup (`load_dotenv`). `run.ps1` also loads that file and binds uvicorn.

| `.env` key | What it is | Who reads it |
|---|---|---|
| `PORT` | HTTP port of the bot (default `8100`) | `run.ps1` / `run.sh` |
| `DB_HOST` | SQL Server host | `core/sql.py` |
| `DB_PORT` | SQL Server port (default `1433`). Not the HTTP port | `core/sql.py` |
| `DB_USER` | SQL login (default `chatbot_ro`) | `core/sql.py` |
| `DB_PASSWORD` | That login’s password. If empty, `work/ro_password.txt` | `core/sql.py` |

`DB_SA_USER` and `DB_SA_PASSWORD` are for setup scripts only.

## Endpoints the site needs

Base URL is the bot process (`http://127.0.0.1` plus `PORT` from `.env`). Prefer same-origin through IIS so the page does not call another origin.

What each call is for, in order:

| Call | You send | You get back | When the site uses it |
|---|---|---|---|
| `GET /health` | nothing | `{ok, provider, pinned_client, clients}` | Is the bot up, and can it reach DeepSeek and SQL? |
| `POST /context` | `session_id`, `company_id` | The company now pinned on that session | Once, after the user logs into Olives |
| `GET /context` | optional `session_id` | Companies the bot can see, plus the session transcript | Fill a company dropdown |
| `POST /ask` | `question`, `session_id`, `company_id` | SSE stream, then one final JSON object | Every user question |
| `POST /feedback` | `session_id`, `helpful`, optional `turn_id` | `{ok: true}` | Thumbs up / down on an answer |
| `DELETE /sessions/{sid}` | the session id | session removed | User clicks “new chat” or logs out |

The final `/ask` object is the payload the page renders:

| Field | What to do with it |
|---|---|
| `answer` | The Arabic sentence to show |
| `answer_sql` | The read-only query that produced the number. Show it so the user can check |
| `table` | `columns` + `rows`. Render a grid. This is also the source for the spreadsheet download |
| `chart` | Optional chart spec for the same rows |
| `followups` | Suggested next questions |
| `sources` | Guide sections, when the answer came from the manual |
| `report_name` | Name of a canned report, when one was used |
| `turn_id` | Send this back on `POST /feedback` |
| `needs_ask` | The bot is asking a clarification. Post the user’s reply as the next `question` on the same `session_id` |
| `error` | Show this and stop. No rows |

`GET /sessions` lists in-memory chats for the pilot sidebar. `GET /metrics` is Prometheus text for operators. `POST /db/test`, `POST /db/connect`, `POST /db/reset`, and `GET /db/status` change the SQL target and must not be called from the public site.

### Required

`POST /ask` — the only conversation call. Rate limit 30/minute per client address.

Request JSON:

```json
{
  "question": "Arabic or user text",
  "session_id": "stable id from the site session",
  "company_id": 2
}
```

`client` may be sent and is ignored. `company_id` must be a real company for the pinned tenant; the bot does not read the IIS cookie.

Response is `text/event-stream`. Read until a line `data: [DONE]`. Frames:

| `data:` JSON | Meaning |
|---|---|
| `{"step": "..."}` | Progress while tools run |
| `{"answer_chunk": "..."}` | Partial answer text |
| `{"needs_ask": ...}` | Bot must clarify (usually company). Next `POST /ask` on the same `session_id` is the answer |
| `{"answer", "answer_sql", "table", "chart", "followups", "sources", "confidence", "turn_id", "report_name"}` | Final turn |
| `{"error": "..."}` | User-safe failure |
| `: keep-alive` | Comment line about every 20s while the model is quiet. Do not treat it as a data frame |

Headers already set by the bot: `Cache-Control: no-transform`, `X-Accel-Buffering: no`. IIS must not buffer this response.

`POST /context` — set company without a chat turn.

```json
{ "session_id": "...", "company_id": 2 }
```

`400` if `company_id` is not in the live company list.

`GET /health` — process and database probe. `ok` is true only when the LLM provider answers and the pinned client's SQL `SELECT 1` works. Use this for the IIS / monitor check, not a TCP port check alone.

### Optional

| Call | Use |
|---|---|
| `GET /context?session_id=` | Current company and company list for the dropdown |
| `POST /feedback` | `{session_id, helpful, reason?, turn_id?}`. `404` if that session has no stored answer |
| `GET /sessions`, `DELETE /sessions/{sid}` | Session list and drop. Sessions are in memory, idle 1 hour, cap 500 |

Do not expose these to the browser. They accept a SQL password in the body and are for operators only: `POST /db/test`, `POST /db/connect`, `POST /db/reset`, `GET /db/status`.

`GET /metrics` is Prometheus text. `GET /` is the pilot chat page in `static/`. The circle widget is not built; the site does not embed that page. It calls `/ask`.

There is no CORS middleware. A page on the IIS host that calls port 8100 directly will be blocked by the browser. Put the bot behind the same site (reverse proxy) or the call must be server-side from ASP.NET.

## Bubble panel

The circle widget is not built. The open panel is a page fragment on the Olives site, not a navigation to `GET /`. Closing it hides the panel and keeps `session_id`. It does not call the bot.

The panel must contain:

| Piece | Calls |
|---|---|
| Company label. A dropdown only when `GET /context` says `multi_company` | On open: `GET /context?session_id=`. On change: `POST /context` |
| Message list, RTL, Arabic | On open, replay `transcript` from `GET /context`. Each send: `POST /ask` |
| Text box and send button | `POST /ask` with `question`, `session_id`, `company_id` |
| Answer area | Read the SSE stream. Append `answer_chunk`. On the final frame show `answer`, and `table` when rows exist |
| Download button on a table | No call. Build CSV or xlsx from `table.columns` and `table.rows` |
| SQL disclosure under a numeric answer | No call. Show `answer_sql` from the final frame |
| Thumbs | `POST /feedback` with `session_id`, `helpful`, `turn_id` |
| New chat | `DELETE /sessions/{sid}`, then mint a new `session_id` |

`session_id` is an opaque string stored in the browser tab (`sessionStorage` on the pilot). Send the same value on every call until New chat or logout.

Do this from the Olives origin. Either the browser calls `https://<olives-host>/bot/...` and IIS proxies to `127.0.0.1` plus `PORT`, or the ASP.NET page calls the bot on the server and forwards the stream. A script on the Olives page that calls port 8100 on another origin is blocked: there is no CORS middleware. Read `/ask` as `text/event-stream` until `data: [DONE]`. IIS must not buffer that response.

The website already knows `CompanyID` from the logged-in user. Send that as `company_id`. Do not ask the user to type it when the site has it.

## Call sequence

1. User is already logged into Olives. The site knows `CompanyID`.
2. Site opens one `session_id` per browser session (any opaque string). Send it on every `/ask` and `/context`.
3. `POST /context` with that company, or send `company_id` on the first `/ask`.
4. `POST /ask` and render `answer_chunk` / final `answer`. Show `answer_sql` and `table` when the answer is a number, so the user can check it.
5. If `needs_ask` arrives, show the clarification and post the user's reply as the next `question` on the same `session_id`.
6. Disconnect aborts the turn. The bot watches `is_disconnected` and stops the model.

The bot is read-only. It cannot post invoices, change customers, or run the website's save buttons.

## Excel

Excel import and “To Excel” already live inside the website assembly `Olives_BO.dll` (about 20 MB, DevExpress `ASPx*` pages). A string scan of that DLL found no chatbot URL and no call to `/ask`. It did find the Excel import path the site already owns:

- ACE connection `Extended Properties=Excel 12.0`
- SQL table parameters `@Tbl_Excel_Data` and `@Tbl_Excel_DataRoutes`
- Templates under `..\Temp\`: `CustomerPricelistImport.xlsx`, `CustomersAllowManualDiscount.xlsx`, `CustomersPromotionGroup.xlsx`, `PricelistImport.xlsx`, `PromotionTemplate.xlsx`, `SalesPersonCustomerCountTargets.xlsx`, `SalesPersonTargets.xlsx`
- Page and handler names: `AddPromotionFromExcel_Page`, `ToExcel_Click`, `btnExportExcel_Click`, `ReadExcel_EPPlus`, `ExportToXlsx`, `ExportXlsxToResponse`, `WriteXlsx`, `WriteXlsxToResponse`, `Rpt_CustomerAddressInfoForExcel_Page`

A second pass that kept only `chatbot`, `/ask`, `xlsx`, `Tbl_Excel`, `ImportExcel`, and `http://` / `https://` returned those Excel symbols and no URL. The assembly does not call the bot.

`api/server.py` has no upload, download, or `.xlsx` route. The guides under `knowledge/guide-headed/` describe the same screens for users.

### Two different Excel features

**Olives import / “To Excel” on the ERP screens** stays in `Olives_BO.dll` (`ReadExcel_EPPlus`, `ToExcel_Click`, `WriteXlsxToResponse`). Those write into the database through `cds`. The bot cannot do that job.

**Saving the bot’s answer as a spreadsheet** is already possible, and it does not need a new bot endpoint. When a question returns rows, the final SSE frame includes `table`:

```json
{ "columns": ["Name", "Net"], "rows": [["Acme", 1200]] }
```

The pilot page (`static/app.js`, `downloadTableCsv`) builds a UTF-8 CSV in the browser and downloads `olives_report_YYYY-MM-DD.csv`. Excel on Windows opens that file. The server never builds an `.xlsx`.

In the integration, the website does the same thing with the `table` it already received from `POST /ask`: turn `columns` and `rows` into a CSV or into an `.xlsx` with whatever library the ASP.NET page already uses. No second call, and no file is posted to the bot.

If a later feature should “ask about this sheet”, that is a new endpoint and a new allow-list. It is not part of the current contract.

## IIS, always reachable

The bot is not ready to drop into an IIS site as the DLL is. Checked gaps:

| Gap | Why it matters |
|---|---|
| No Windows service / IIS hosting | Closing a console `uvicorn` stops the bot. IIS app-pool recycle does not keep this process up |
| No reverse proxy in this repo | ARR or HttpPlatformHandler must forward `/bot/` to `127.0.0.1:8100` and turn off dynamic compression and response buffering for `text/event-stream` |
| No CORS | Browser calls from the Olives origin to another port fail |
| Sessions are RAM only | An app recycle or a second worker drops `session_id` history. Run one worker |
| `GET /health` depends on DeepSeek and SQL | A green port with a bad key or a down database is `ok: false` |
| `CHATBOT_CLIENT` and `.env` | Must be set for the service account. The key stays out of the site `Web.config` |
| Customer folder | `Olives_BO.dll` and the company folders are the website. Nothing there calls `/ask` yet |

Minimum layout on the Windows server:

1. Python 3.13 venv, repo, `.env` (`DEEPSEEK_API_KEY`, `CHATBOT_CLIENT`, `DB_HOST`, `DB_PORT=1433`).
2. `chatbot_ro` already created on the same SQL instance as `Olives_BO`.
3. A Windows service that runs `uvicorn api.server:app --host 127.0.0.1 --port 8100` and restarts it.
4. IIS URL Rewrite + ARR: `https://<olives-host>/bot/ask` → `http://127.0.0.1:8100/ask`, with buffering off.
5. The ASP.NET page (or a small handler next to `Olives_BO.dll`) server-side POSTs `/ask` with the logged-in `CompanyID` and a `session_id`, or the browser uses the same-origin `/bot/ask` URL.
6. Monitor `GET /health` and alert when `ok` is false.

Until steps 3–5 exist, the bot is a pilot on port 8100, not an always-on part of the website.
