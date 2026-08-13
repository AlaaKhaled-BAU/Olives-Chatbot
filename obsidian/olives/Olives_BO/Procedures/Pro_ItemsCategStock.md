---
type: procedure
database: Olives_BO
name: Pro_ItemsCategStock
schema: dbo
tags: [#backoffice]
reads_from:
  - Customers
  - Items
  - ItemsCategStockDetails
  - ItemsCategStockHeader
  - ItemsCategories
  - ItemsUnits
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_ItemsCategStock

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @cmdType varchar(50)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @TransactionNo int
- @TransactionYear smallint
- @TransactionTypeID int
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsCategStockDetails]]
- [[ItemsCategStockHeader]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[SalesPersons]]
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
