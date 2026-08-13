---
type: procedure
database: Olives_BO
name: Rpt_CompareCustomerStockWithOrder
schema: dbo
tags: [#backoffice, #customer, #inventory, #order, #reporting]
reads_from:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CompareCustomerStockWithOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, Items, OrdersDetails, OrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Company int = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @FromItem varchar(100) = null
- @ToItem varchar(100) = null
- @Cutomer int = null
- @UserID nvarchar(50) = null
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]

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
