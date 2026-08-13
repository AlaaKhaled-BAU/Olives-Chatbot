---
type: procedure
database: Olives_BO
name: Jazeera_Integrationc_SendSalesOrders
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OrdersHeaders]]
  - [[OT_OrderDF]]
  - [[OT_OrderHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Jazeera_Integrationc_SendSalesOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OrdersHeaders, SalesPersons, dbo. Writes OrdersHeaders, OT_OrderDF, OT_OrderHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OrdersHeaders]]
- [[OT_OrderDF]]
- [[OT_OrderHF]]
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
- [[OT_OrderDF]]
- [[OT_OrderHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
