---
type: procedure
database: Olives_BO
name: WF_CancelRequest
schema: dbo
tags: [#workflow]
reads_from:
  - RequestToApprovePromotion
  - RequestToChangeInvoicePaymentType
  - RequestToExceedFinishAllTasks
  - WF_MasterLog
writes_to:
  - WF_SubLog
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# WF_CancelRequest

## Purpose
Workflow request cancellation procedure in Olives_BO.
- **Trigger**: Called when a salesman cancels a pending request from the mobile tablet or when an admin aborts an open workflow.
- **Outcome**: Marks the request as canceled, updating `WF_MasterLog.LastStatus = 3` (Canceled) and updating active tasks in `WF_SubLog` to prevent further approval actions. Also updates `IsCanceled = 1` in corresponding request tables (e.g. `RequestTo*`).
## Parameters
- @CompanyID smallint
- @SalesmanNo bigint
- @FunctionID bigint
- @OSFA_AutoID bigint
## Tables Read
- [[RequestToApprovePromotion]]
- [[RequestToChangeInvoicePaymentType]]
- [[RequestToExceedFinishAllTasks]]
- [[WF_MasterLog]]
## Tables Written
- [[WF_SubLog]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
