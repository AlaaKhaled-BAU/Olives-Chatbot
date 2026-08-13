---
type: procedure
database: Olives_BO
name: AccPack_Integ_SendSalesOrdersLuxuryItemstest
schema: dbo
tags: [#backoffice, #integration, #inventory, #order, #sales]
reads_from:
  - [[Customers]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OrdersHeaders]]
  - SalesOrder
  - SalesOrderItems
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AccPack_Integ_SendSalesOrdersLuxuryItemstest


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OrdersDetails, OrdersHeaders, SalesPersons, dbo. Writes OrdersHeaders, SalesOrder, SalesOrderItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OrdersHeaders]]
- SalesOrder
- SalesOrderItems
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[OrdersHeaders]]
- SalesOrder
- SalesOrderItems

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
