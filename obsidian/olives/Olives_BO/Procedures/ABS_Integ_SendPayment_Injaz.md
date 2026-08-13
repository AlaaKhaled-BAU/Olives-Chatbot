---
type: procedure
database: Olives_BO
name: ABS_Integ_SendPayment_Injaz
schema: dbo
tags: [#integration]
reads_from:
  - Banks
  - Checks
  - Currencies
  - Customers
  - NoTransactionsReasons
  - Receipts_PaidTrans
  - SalesPersons
  - TransactionsHeaders
writes_to:
  - IntegrationErrorLog
  - IntegrationPostedTransactions
  - Receipts
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# ABS_Integ_SendPayment_Injaz

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 8 table(s); writes 3; calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Checks]]
- [[Currencies]]
- [[Customers]]
- [[NoTransactionsReasons]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[Receipts]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[ABS_Integ_PostDataToAPI_Injaz]]
- `Fun_GetReceiptsChecksTotal`
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
