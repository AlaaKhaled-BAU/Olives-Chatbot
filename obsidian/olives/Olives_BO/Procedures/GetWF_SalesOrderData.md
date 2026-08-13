---
type: procedure
database: Olives_BO
name: GetWF_SalesOrderData
schema: dbo
tags: [#auth, #backoffice, #order, #sales, #workflow]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriority]]
  - [[ItemsUnits]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GetWF_SalesOrderData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, ItemsCategories, ItemsPriority, ItemsUnits, OrdersDetails, OrdersHeaders, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @OrderYear int=2024
- @OrderNo bigint=1300300128
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriority]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriority]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
