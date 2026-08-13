---
type: procedure
database: Olives_BO
name: ABS_Integ_SendReturnInvoices_Jebrene
schema: dbo
tags: [#backoffice, #billing, #integration, #order]
reads_from:
  - Curs_Vou
  - [[Customers]]
  - [[CustomersGPSLocations]]
  - [[IntegrationErrorLog]]
  - [[IntegrationPostedTransactions]]
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
  - [[IntegrationErrorLog]]
  - [[IntegrationPostedTransactions]]
  - [[TransactionsHeaders]]
called_by:
  - [[ABS_Integ_PostDataToAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# ABS_Integ_SendReturnInvoices_Jebrene


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Curs_Vou, Customers, CustomersGPSLocations, IntegrationErrorLog, IntegrationPostedTransactions, Items, SalesPersons, TransactionsDetails, TransactionsHeaders. Writes IntegrationErrorLog, IntegrationPostedTransactions, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- Curs_Vou
- [[Customers]]
- [[CustomersGPSLocations]]
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[ABS_Integ_PostDataToAPI]]
## Impact / Dependencies

**Tables Read**
- Curs_Vou
- [[Customers]]
- [[CustomersGPSLocations]]
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[TransactionsHeaders]]

**Callers**
- [[ABS_Integ_PostDataToAPI]]

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
