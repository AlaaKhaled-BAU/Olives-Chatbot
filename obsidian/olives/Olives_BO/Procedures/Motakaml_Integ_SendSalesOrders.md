---
type: procedure
database: Olives_BO
name: Motakaml_Integ_SendSalesOrders
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[Customers]]
  - OLIV
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PaymentsTypes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Motakaml_Integ_SendSalesOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OLIV, OrdersDetails, OrdersHeaders, PaymentsTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[Customers]]
- OLIV
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- OLIV
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]

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
