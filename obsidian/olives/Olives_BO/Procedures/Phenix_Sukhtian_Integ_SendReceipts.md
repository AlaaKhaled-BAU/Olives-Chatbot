---
type: procedure
database: Olives_BO
name: Phenix_Sukhtian_Integ_SendReceipts
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Companies]]
  - Curs_Payment
  - [[Customers]]
  - Fun_GetReceiptsChecksTotal
  - [[IntegrationErrorLog]]
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
  - [[Receipts]]
called_by:
  - [[Phenix_Sukhtian_Integ_CloseSession]]
  - [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
  - [[Phenix_Sukhtian_Integ_OpenSession]]
support_relevance: high
last_verified: 2026-07-05
---
# Phenix_Sukhtian_Integ_SendReceipts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Curs_Payment, Customers, Fun_GetReceiptsChecksTotal, IntegrationErrorLog, Receipts, SalesPersons. Writes Receipts. Calls 3 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[Companies]]
- Curs_Payment
- [[Customers]]
- Fun_GetReceiptsChecksTotal
- [[IntegrationErrorLog]]
- [[Receipts]]
- [[SalesPersons]]
## Tables Written
- [[Receipts]]
## Callers
_None (no known callers)_
## Callees
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- Curs_Payment
- [[Customers]]
- Fun_GetReceiptsChecksTotal
- [[IntegrationErrorLog]]
- [[Receipts]]
- [[SalesPersons]]

**Tables Written**
- [[Receipts]]

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
