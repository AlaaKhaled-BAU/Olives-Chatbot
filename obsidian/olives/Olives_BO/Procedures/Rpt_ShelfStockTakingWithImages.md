---
type: procedure
database: Olives_BO
name: Rpt_ShelfStockTakingWithImages
schema: dbo
tags: [#backoffice, #inventory, #reporting]
reads_from:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Customers]]
  - [[Items]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ShelfStockTakingWithImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, Customers, Items, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SmallInt = 1
- @FromDate SmallDateTime = '2021-01-01'
- @ToDate SmallDateTime = '2022-01-01'
- @FromSales Int = 1
- @ToSales Int = 9999999
- @FromCust BigInt = 1
- @ToCust BigInt = 9999999999999
- @FromItem Nvarchar(50) = '0'
- @ToItem Nvarchar(50) = 'zzzz'
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
