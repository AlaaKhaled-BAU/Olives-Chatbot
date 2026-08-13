---
type: procedure
database: Olives_BO
name: IscoJordan_Integ_SendOrders
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - Code
  - [[Customers]]
  - DATA
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - orders_1
  - ordtran_1
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# IscoJordan_Integ_SendOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Code, Customers, DATA, Items, OrdersDetails, OrdersHeaders, SalesPersons, orders_1, ordtran_1. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- Code
- [[Customers]]
- DATA
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- orders_1
- ordtran_1
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Code
- [[Customers]]
- DATA
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- orders_1
- ordtran_1

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
