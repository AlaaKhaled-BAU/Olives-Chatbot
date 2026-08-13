---
type: procedure
database: Olives_BO
name: Commate_Integ_PostToAPI
schema: dbo
tags: [#integration]
reads_from:
  - Customers
  - Items
  - ItemsUnits
  - SalesPersons
  - TransactionsDetails
writes_to:
  - TransactionsHeaders
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Commate_Integ_PostToAPI

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s); writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @TransactionNo int
- @TransactionTypeID float
- @TransactionYear int
- @EndPoint nvarchar(100)
- @Cmd nvarchar(100)
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersons]]
- [[TransactionsDetails]]
## Tables Written
- [[TransactionsHeaders]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[Commate_Integ_CreateToken]]
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
