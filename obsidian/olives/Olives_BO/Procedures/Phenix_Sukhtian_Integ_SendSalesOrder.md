---
type: procedure
database: Olives_BO
name: Phenix_Sukhtian_Integ_SendSalesOrder
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - Curs_Vou
  - [[Customers]]
  - [[IntegrationErrorLog]]
  - [[Items]]
  - OPENJSON
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
  - [[OrdersHeaders]]
called_by:
  - [[Phenix_Sukhtian_Integ_CloseSession]]
  - [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
  - [[Phenix_Sukhtian_Integ_OpenSession]]
support_relevance: high
last_verified: 2026-07-05
---
# Phenix_Sukhtian_Integ_SendSalesOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Curs_Vou, Customers, IntegrationErrorLog, Items, OPENJSON, OrdersDetails, OrdersHeaders, Receipts, SalesPersons. Writes OrdersHeaders. Calls 3 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[Items]]
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
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]
## Impact / Dependencies

**Tables Read**
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[Items]]
- OPENJSON
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]

**Tables Written**
- [[OrdersHeaders]]

**Callers**
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
