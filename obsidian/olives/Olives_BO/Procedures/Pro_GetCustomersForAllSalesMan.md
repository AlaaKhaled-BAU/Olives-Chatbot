---
type: procedure
database: Olives_BO
name: Pro_GetCustomersForAllSalesMan
schema: dbo
tags: [#backoffice]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - SalesPersons
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_GetCustomersForAllSalesMan

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetSalesmanTreeByID`
- `Trim`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
