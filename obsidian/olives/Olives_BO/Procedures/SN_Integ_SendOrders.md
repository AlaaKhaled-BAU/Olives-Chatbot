---
type: procedure
database: Olives_BO
name: SN_Integ_SendOrders
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnitsDetails]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - SN
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SN_Integ_SendOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, ItemsUnitsDetails, OrdersDetails, OrdersHeaders, SN, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsUnitsDetails]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- SN
- [[SalesPersons]]
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
- [[ItemsUnitsDetails]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- SN
- [[SalesPersons]]

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
