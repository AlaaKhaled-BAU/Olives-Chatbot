---
type: procedure
database: Olives_BO
name: Ejabi_Integ_SendReturnInvoices
schema: dbo
tags: [#backoffice, #billing, #integration, #order]
reads_from:
  - [[Companies]]
  - Curs_Vou
  - [[Customers]]
  - [[IntegrationErrorLog]]
  - [[IntegrationPostedTransactions]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
  - [[IntegrationErrorLog]]
  - [[IntegrationPostedTransactions]]
  - [[TransactionsHeaders]]
called_by:
  - [[Ejabi_Integ_PostDataToAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# Ejabi_Integ_SendReturnInvoices


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Curs_Vou, Customers, IntegrationErrorLog, IntegrationPostedTransactions, SalesPersons, TransactionsDetails, TransactionsHeaders. Writes IntegrationErrorLog, IntegrationPostedTransactions, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[Companies]]
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
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
- [[Ejabi_Integ_PostDataToAPI]]
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[TransactionsHeaders]]

**Callers**
- [[Ejabi_Integ_PostDataToAPI]]

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
