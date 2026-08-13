---
type: procedure
database: Olives_BO
name: OK_ImportInvoiceAndReturnISDT_Integ
schema: dbo
tags: [#integration]
reads_from:
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OK_ImportInvoiceAndReturnISDT_Integ

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @TransactionYear int
- @TransactionTypeID int
- @TransactionNo int
## Tables Read
- [[TransactionsHeaders]]
## Tables Written
_None_
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
