---
type: procedure
database: Olives_BO
name: Pro_GetDataList
schema: dbo
tags: [#backoffice]
reads_from:
  - Branches
  - Customers
  - CustomersTypes
  - Items
  - ItemsCategories
  - ItemsUnits
  - ItemsUnitsDetails
  - SalesPersons
  - SalesPersonsGroups
  - TransactionsTypes
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_GetDataList

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 10 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @SalesmanNo int
- @cmdType varchar(50)
- @ItemCode nvarchar(100)
## Tables Read
- [[Branches]]
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsTypes]]
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
