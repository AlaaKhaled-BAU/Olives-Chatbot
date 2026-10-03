# Vault supervisor battery (business language)

Questions in `vault_supervisor_battery.jsonl` are **normal supervisor / operations Arabic (and some English)** — no table names, ActionID, or FunctionID in the user text. The agent must map to `t.LogActionTransaction`, `t.WF_*`, `t.RequestTo*`, etc.

## Vault & SQL coverage (verified 2026-10-03)

| Business topic | User-facing words | Where meaning is documented | Gap? |
|----------------|-------------------|-----------------------------|------|
| Actual customer visits | زيارة فعلية، دخل على الزبون | `LogActions` + `LogActionTransaction.md` + `knowledge/reference/visits_grain.md` | OK — distinguish visit vs فتح التطبيق |
| No sale at visit | طلع بدون ما يبيع | `LogActions` → NoSaleExit (8) | OK |
| Planned route visits | خطة المسار، المخطط | `visits_grain.md`, `SalesPersonsRoutes`, `CustomersFinancialDetails` | OK — needs salesman/route clarify |
| Tablet → server sync | ما ببان بالتقرير، ترحيل | `OT_ImportActionLog.md`, `visits_grain.md` sync diagram | OK at architecture level |
| WF request types | تجاوز حد ائتمان، تحميل، خارج المسار | `WF_Functions` (`ArName` / `EngName` on `t.WF_Functions`) | OK — 47 functions in vault card |
| Pending my approval | بانتظاري، لسا ما قررت | `Workflow_Approval_Codes`, `WF_GetPositionWFData` | OK — `Action IS NULL` + `ActionNeed = AR` |
| Approved vs rejected | وافقت / رفضت | `Workflow_Approval_Codes` (`Action` A/R, `LastStatus` 1/2) | OK |
| Master request status | معلّق / منتهي | `WF_MasterLog.LastStatus` 0–3 | [[Workflow_Approval_Codes]] + `knowledge/reference/workflow_approval_status.md` |
| Device request row | طلب من المندوب | `RequestTo*` + `_RequestTo-Join-Conventions.md`, `IsAproved` | OK for credit-limit family |
| Role supervisor vs salesman | مشرف / مندوب | **`SystemCodes` `SalespersonType`**: 3=Supervisor, 4=Salesman | OK (SQL live) |
| No-visit reasons | سبب عدم الزيارة | **`SystemCodes` `ReasonType`**: code 2 = "No Visit Reason"; log action 21 | Partial — link reason pick list to log |

### `SystemCodes` (SQL)

- Not a full WF dictionary; useful types include **`SalespersonType`**, **`ReasonType`** (No Visit Reason), **`PromotionWF`**, receipt/call statuses.
- Does **not** decode WF columns — use vault `Workflow_Approval_Codes` instead.

### Procedures that **fill** meaning (for future vault cards)

| Procedure | Role |
|-----------|------|
| `OT_ImportActionLog` | Tablet action log → `LogActionTransaction` |
| `OT_ImportRequestToExceedCustomerCreditLimit` (+ other `OT_ImportRequestTo*`) | Device request → `RequestTo*` + `WF_MasterLog` |
| `WF_AddWorkFlowLevelOne` / `WF_AddWorkFlowLevels` | Approval chain rows in `WF_SubLog` |
| `WF_GetPositionWFData` | Position inbox (what supervisor sees on tablet) |

## Sessions (22 turns)

Multi-turn chats: visits July, plan vs actual, WF inbox, credit requests, load/route exceptions, GPS, hierarchy, sync troubleshooting, reason codes, one gate, tablet invoices.

## Runner

```bash
set -a && source .env && set +a
unset CHATBOT_LLM_BASE_URL CHATBOT_LLM_API_KEY
export CHATBOT_CLIENT=morec   # or 105
python3.13 evals/run_vault_supervisor_battery.py              # multi-session (22 turns)
python3.13 evals/run_vault_supervisor_battery.py --one-chat  # 27 turns, one session (hallucination stress)
```

Outputs:

- `vault_supervisor_battery_results.json` / `vault_supervisor_onechat_results.json`
- Each turn includes **`queries[]`**, **`query_log[]`** (sql + row_count), **`path_checks.tables_t`**, vault/tool flags.

Runtime knowledge: **`core/vault.py`** (in-process Obsidian notes + `retrieve_cards` prefix), **`search_docs`** (FTS on `knowledge/`), not stdio `obsidian-mcp-server.py` per turn.

Latest one-chat run (2026-10-03, client `105`): 27 turns ~464s, ~$0.38; 22/27 turns logged SQL; 4 turns called `search_schema_notes` / `read_schema_note`; recall turn `vs-028` **re-ran SQL** despite “بدون ما تعيد الحساب” (same zero as turn 1).
