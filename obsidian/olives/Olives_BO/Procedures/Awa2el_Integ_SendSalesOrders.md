---
type: procedure
database: Olives_BO
name: Awa2el_Integ_SendSalesOrders
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - `dbo`
writes_to:
  - [[OrdersHeaders]]
  - SalesOrder_D
  - SalesOrder_H
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Awa2el_Integ_SendSalesOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OrdersDetails, OrdersHeaders, dbo. Writes OrdersHeaders, SalesOrder_D, SalesOrder_H. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[OrdersDetails]]
- [[OrdersHeaders]]
- `dbo`
## Tables Written
- [[OrdersHeaders]]
- SalesOrder_D
- SalesOrder_H
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OrdersDetails]]
- [[OrdersHeaders]]
- dbo

**Tables Written**
- [[OrdersHeaders]]
- SalesOrder_D
- SalesOrder_H

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
