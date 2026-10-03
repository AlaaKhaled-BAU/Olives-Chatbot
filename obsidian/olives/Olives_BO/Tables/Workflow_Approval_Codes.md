---
type: table
database: Olives_BO
name: Workflow_Approval_Codes
schema: dbo
tags: [#workflow, #backoffice, #codebook]
support_relevance: high
last_verified: 2026-10-03
---
# Workflow approval status codes (WF_MasterLog / WF_SubLog)

Tablet **approval requests** (تجاوز حد ائتمان، بيع لزبون مش على المسار، تحميل بضاعة، …) land in BO via `OT_ImportRequestTo*` → [[WF_MasterLog]] + [[WF_SubLog]]. The supervisor **inbox** UI is fed by [[WF_GetPositionWFData]].

These codes are **not** in `SystemCodes` (unlike `SalespersonType` or `ReasonType`). Decode from this note + `lookup_hot` is not applicable — use the tables below when explaining counts or filtering SQL.

> **Do not confuse** with `SystemCodes` where `SysCodeTypeID = 'Status'` (Draft / In Review / Approved). That row set is for a **different** screen/domain; `WF_MasterLog.LastStatus` uses its own 0–3 scheme documented here (verified from `WF_AddWorkFlowLevelOne`, `WF_AddWorkFlowLevels`, `OT_ImportRequestTo*` proc text, live BO sample 2026-10).

## WF_MasterLog.LastStatus — whole request outcome

| Code | Meaning (EN) | Arabic (user-facing) | When set |
|------|----------------|----------------------|----------|
| `0` | Open / in workflow | **قيد الموافقة** / **مفتوح** | Default on `INSERT INTO WF_MasterLog` (`WF_AddWorkFlowLevelOne`); chain not finished |
| `1` | Approved (final) | **موافق عليه** | `WF_AddWorkFlowLevels` — `SET LastStatus = 1 --Approved` |
| `2` | Rejected (final) | **مرفوض** | `WF_AddWorkFlowLevels` — `SET LastStatus = 2 --Rejected` |
| `3` | Canceled | **ملغي** | Import/cancel paths — e.g. `LastStatus = '3' -- Canceled` when tablet cancels before BO approval |

**Chatbot filters (plain language → SQL):**

| User says | Typical filter on `t.WF_MasterLog` |
|-----------|-------------------------------------|
| طلبات لسا معلّقة / ما انتهت | `LastStatus = N'0'` (and often still rows in SubLog with pending approver) |
| انوافق / مقبول | `LastStatus = N'1'` |
| مرفوض | `LastStatus = N'2'` |
| ملغي من المندوب | `LastStatus = N'3'` |

Request **type** (credit limit, off-route visit, …) is `FunctionID` → [[WF_Functions]] (`ArName` / `EngName`), not `LastStatus`.

## WF_SubLog.Action — this approver line’s decision

| Code | Meaning | Arabic |
|------|---------|--------|
| `NULL` | No decision on **this** line yet | **بانتظار قرارك** (when `ActionNeed = 'AR'`) |
| `A` | This position **approved** | **وافق** |
| `R` | This position **rejected** | **رفض** |
| `N` | **Notification / history** row (engine logged a step; not the pending inbox row) | سجل إشعار — غالباً مع نص `TrDesc` يذكر "Approved/Rejected By Level …" |

Live distribution (Olives_BO): `N`, `R`, `A` all common; empty string rare.

**Important:** Counting "how many did I approve this week" for supervisor position `P` usually means `Action = N'A'` and `PositionID = P` (and date on `ActionDate`), **not** `Action IS NULL`.

## WF_SubLog.ActionNeed — line role

| Code | Meaning | Arabic |
|------|---------|--------|
| `AR` | **Action required** — approver must act | **يحتاج موافقة** |
| `N` | Notification / copy line | **إشعار** |

### Supervisor inbox (matches WF_GetPositionWFData)

Rows waiting on **my** position:

- `WF_SubLog.PositionID = @myPosition`
- `WF_SubLog.Action IS NULL`
- `WF_SubLog.ActionNeed = N'AR'`

Join `t.WF_MasterLog` on `ReqID` + company for request date, `FunctionID`, `LastStatus`, salesman refs in `Ref*`.

`Companies.GetSalesman()` overflow logic also counts active WF lines with `ActionNeed = 'AR'` (license pressure) — same `AR` semantics.

## WF_SubLog.IsCanceled

`bit`, rare. Prefer `WF_MasterLog.LastStatus = 3` for canceled **requests** unless support ticket references sub-line cancel.

## Related tables & procs

| Object | Role |
|--------|------|
| [[WF_MasterLog]] | One row per request (`ReqID`); `LastStatus`, `FunctionID`, `ReqDate`, `Ref1`… |
| [[WF_SubLog]] | One row per workflow step / approver position; `Action`, `ActionNeed`, `ARLevel` |
| [[WF_Functions]] | Request type labels |
| [[WF_GetPositionWFData]] | Back-office / tablet inbox dataset for a `PositionID` |
| `OT_ImportRequestTo*` | Creates master + sub rows when tablet syncs |

## LogActionTransaction — same idea, different codebook

Field **visits and tablet actions** are **not** workflow approvals.

| Aspect | Workflow (this note) | Field log [[LogActionTransaction]] |
|--------|----------------------|-----------------------------------|
| Fact table | [[WF_MasterLog]] / [[WF_SubLog]] | [[LogActionTransaction]] |
| Code column | `LastStatus`, `Action`, `ActionNeed` | `ActionID` |
| Meaning lookup | This note (not `SystemCodes`) | [[LogActions]] via `lookup_hot` / `t.LogActions` |
| Pipeline | `OT_ImportRequestTo*` | [[OT_ImportActionLog]] ← OSFA `OT_ActionLog` |
| User language | موافقة، رفض، طلب تابلت | زيارة، دخول زبون، فاتورة، بدون بيع |

Visit semantics (CustEntry vs SystemLogin, Data1/Data2 overload): [[LogActionTransaction]] + `knowledge/reference/visits_grain.md`.

**No-visit reasons:** often `ActionID` `21` (Will Not Visit), `31` (Postpone), `38` (import/export) plus reason master [[NoTransactionsReasons]] where `ReasonType` matches `SystemCodes` **`ReasonType` code `2`** = "No Visit Reason" (join path is reason tables, not `WF_SubLog.Action`).

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[LogActions]]
- [[LogActionTransaction]]
