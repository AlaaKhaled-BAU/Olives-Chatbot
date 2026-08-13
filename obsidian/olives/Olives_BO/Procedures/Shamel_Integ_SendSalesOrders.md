---
type: procedure
database: Olives_BO
name: Shamel_Integ_SendSalesOrders
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - Curs_Vou
  - [[Customers]]
  - [[IntegrationErrorLog]]
  - [[Items]]
  - [[ItemsUnits]]
  - OPENJSON
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
  - [[OrdersHeaders]]
called_by:
  - [[Shamel_Integ_GetDataFromAPI]]
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Shamel_Integ_SendSalesOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Curs_Vou, Customers, IntegrationErrorLog, Items, ItemsUnits, OPENJSON, OrdersDetails, OrdersHeaders, Receipts, SalesPersons. Writes OrdersHeaders. Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[Items]]
- [[ItemsUnits]]
- OPENJSON
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
## Tables Written
- [[OrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[Shamel_Integ_GetDataFromAPI]]
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[Items]]
- [[ItemsUnits]]
- OPENJSON
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]

**Tables Written**
- [[OrdersHeaders]]

**Callers**
- [[Shamel_Integ_GetDataFromAPI]]
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
