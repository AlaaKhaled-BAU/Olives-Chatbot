---
type: procedure
database: Olives_BO
name: Rpt_ConcreteOperationManager
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - Fun_GetOrdersDeliveredQtyTot
  - Fun_GetReceiptsTotal
  - Fun_GetSalesOrderTotalAmount
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ConcreteOperationManager


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetOrdersDeliveredQtyTot, Fun_GetReceiptsTotal, Fun_GetSalesOrderTotalAmount, OrdersDetails, OrdersHeaders, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2018-12-18'
- @ToDate smalldatetime='2024-12-18'
## Tables Read
- [[Customers]]
- Fun_GetOrdersDeliveredQtyTot
- Fun_GetReceiptsTotal
- Fun_GetSalesOrderTotalAmount
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
- Fun_GetOrdersDeliveredQtyTot
- Fun_GetReceiptsTotal
- Fun_GetSalesOrderTotalAmount
- [[OrdersDetails]]
- [[OrdersHeaders]]
- dbo

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
