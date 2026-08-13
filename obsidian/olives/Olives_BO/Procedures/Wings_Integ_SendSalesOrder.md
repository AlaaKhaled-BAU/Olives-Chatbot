---
type: procedure
database: Olives_BO
name: Wings_Integ_SendSalesOrder
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - WACC
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Wings_Integ_SendSalesOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OrdersDetails, OrdersHeaders, WACC. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[OrdersDetails]]
- [[OrdersHeaders]]
- WACC
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OrdersDetails]]
- [[OrdersHeaders]]
- WACC

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
