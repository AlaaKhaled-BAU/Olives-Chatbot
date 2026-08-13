---
type: procedure
database: Olives_BO
name: Rpt_StockTaking
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
# Rpt_StockTaking


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, Customers, Items, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @Salesman int =1
- @ToSalesman int =9999
- @FromCust BigInt =0
- @ToCust BigInt = 99999999999
- @FromItem Nvarchar(50) ='0'
- @ToItem Nvarchar(50) ='zzz'
- @FromDate smalldatetime ='2020-05-01'
- @ToDate smalldatetime ='2021-09-17'
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
