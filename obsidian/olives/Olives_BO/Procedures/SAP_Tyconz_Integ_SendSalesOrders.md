---
type: procedure
database: Olives_BO
name: SAP_Tyconz_Integ_SendSalesOrders
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[Customers]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PaymentsTypes]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - OrderDF
  - OrderHF
  - [[OrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Tyconz_Integ_SendSalesOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OrdersDetails, OrdersHeaders, PaymentsTypes, SalesPersons, dbo. Writes OrderDF, OrderHF, OrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 7
## Tables Read
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- OrderDF
- OrderHF
- [[OrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- dbo

**Tables Written**
- OrderDF
- OrderHF
- [[OrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
