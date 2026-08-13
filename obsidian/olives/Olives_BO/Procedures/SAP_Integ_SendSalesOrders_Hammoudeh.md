---
type: procedure
database: Olives_BO
name: SAP_Integ_SendSalesOrders_Hammoudeh
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OrdersHeaders]]
  - SalesOrders
  - SalesOrdersItems
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Integ_SendSalesOrders_Hammoudeh


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OrdersHeaders, SalesPersons, dbo. Writes OrdersHeaders, SalesOrders, SalesOrdersItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Customers]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OrdersHeaders]]
- SalesOrders
- SalesOrdersItems
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[OrdersHeaders]]
- SalesOrders
- SalesOrdersItems

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
