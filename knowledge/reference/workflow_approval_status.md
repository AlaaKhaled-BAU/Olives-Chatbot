# Workflow approval status codes (tablet requests)

Same content as vault note `Workflow_Approval_Codes` — indexed for `search_docs`.

## WF_MasterLog.LastStatus

| Code | Meaning | Arabic |
|------|---------|--------|
| 0 | Open / in workflow | قيد الموافقة |
| 1 | Approved (final) | موافق عليه |
| 2 | Rejected (final) | مرفوض |
| 3 | Canceled | ملغي |

Not the same as `SystemCodes` type `Status` (Draft / In Review / Approved).

## WF_SubLog.Action

| Code | Meaning |
|------|---------|
| NULL | Pending on this approver line |
| A | Approved |
| R | Rejected |
| N | Notification/history line (read TrDesc) |

## WF_SubLog.ActionNeed

| Code | Meaning |
|------|---------|
| AR | Action required — supervisor inbox (`Action IS NULL` AND `ActionNeed = AR`) |
| N | Notification line |

## Versus LogActionTransaction

Visits and tablet actions use `ActionID` on `LogActionTransaction`, decoded from `LogActions` (lookup_hot), imported via `OT_ImportActionLog`. Workflow uses `WF_MasterLog` / `WF_SubLog` and the codes above — different tables, different pipeline.

Visit counting: `ActionID = 0` CustEntry, not `7` SystemLogin. See `visits_grain.md`.
