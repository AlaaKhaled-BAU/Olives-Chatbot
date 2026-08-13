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
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); writes 1. See sections below for the full dependency map.
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
