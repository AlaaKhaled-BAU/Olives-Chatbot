---
type: procedure
database: Olives_BO
name: Pro_OlivesReportingAPI
schema: dbo
tags: [#reporting]
reads_from:
  - Companies
  - Customers
  - Items
  - ItemsUnits
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_OlivesReportingAPI

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @TransactionNo int
- @TransactionTypeID float
- @TransactionYear int
- @Cmd nvarchar(100)
## Tables Read
- [[Companies]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersons]]
- [[TransactionsDetails]]
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
