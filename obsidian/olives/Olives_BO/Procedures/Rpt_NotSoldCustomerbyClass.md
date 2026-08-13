---
type: procedure
database: Olives_BO
name: Rpt_NotSoldCustomerbyClass
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersClasses
  - Items
  - ItemsCategories
  - Locations
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_NotSoldCustomerbyClass

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @FromDate datetime
- @ToDate datetime
- @ItemCateg nvarchar(MAX)
- @ClassID nvarchar(MAX)
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
