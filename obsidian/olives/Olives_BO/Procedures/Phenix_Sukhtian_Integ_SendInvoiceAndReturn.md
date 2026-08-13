---
type: procedure
database: Olives_BO
name: Phenix_Sukhtian_Integ_SendInvoiceAndReturn
schema: dbo
tags: [#backoffice, #billing, #integration, #order]
reads_from:
  - Curs_Vou
  - [[Customers]]
  - [[IntegrationErrorLog]]
  - [[Items]]
  - OPENJSON
  - [[Receipts]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
  - [[TransactionsHeaders]]
called_by:
  - [[Phenix_Sukhtian_Integ_CloseSession]]
  - [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
  - [[Phenix_Sukhtian_Integ_OpenSession]]
support_relevance: high
last_verified: 2026-07-05
---
# Phenix_Sukhtian_Integ_SendInvoiceAndReturn


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Curs_Vou, Customers, IntegrationErrorLog, Items, OPENJSON, Receipts, SalesPersons, TransactionsDetails, TransactionsHeaders. Writes TransactionsHeaders. Calls 3 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[Items]]
- OPENJSON
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- [[TransactionsHeaders]]
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
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
- [[TransactionsHeaders]]

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
