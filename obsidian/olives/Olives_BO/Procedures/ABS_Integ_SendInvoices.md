---
type: procedure
database: Olives_BO
name: ABS_Integ_SendInvoices
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[CompanyBranches]]
  - Curs_Vou
  - [[Customers]]
  - [[CustomersGPSLocations]]
  - Fun_GetSalespersonLinkCarInfo
  - [[IntegrationErrorLog]]
  - [[IntegrationPostedTransactions]]
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# ABS_Integ_SendInvoices


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyBranches, Curs_Vou, Customers, CustomersGPSLocations, Fun_GetSalespersonLinkCarInfo, IntegrationErrorLog, IntegrationPostedTransactions, Items, SalesPersons, TransactionsDetails, TransactionsHeaders, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[CompanyBranches]]
- Curs_Vou
- [[Customers]]
- [[CustomersGPSLocations]]
- Fun_GetSalespersonLinkCarInfo
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyBranches]]
- Curs_Vou
- [[Customers]]
- [[CustomersGPSLocations]]
- Fun_GetSalespersonLinkCarInfo
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

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
