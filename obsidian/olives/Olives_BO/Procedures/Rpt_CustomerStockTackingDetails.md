---
type: procedure
database: Olives_BO
name: Rpt_CustomerStockTackingDetails
schema: dbo
tags: [#reporting]
reads_from:
  - CustomerStockTacking
  - CustomerStockTackingDetails
  - Customers
  - Items
  - ItemsUnits
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_CustomerStockTackingDetails

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 6 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @OrderNo int
- @DocType varchar(50)
- @LoginTime varchar(50)
- @LogoutTime varchar(50)
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `GetItemOrgUnitQty`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
