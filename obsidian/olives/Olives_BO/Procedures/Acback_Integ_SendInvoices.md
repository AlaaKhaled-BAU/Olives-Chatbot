---
type: procedure
database: Olives_BO
name: Acback_Integ_SendInvoices
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - Curs_Vou
  - [[Customers]]
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
  - [[Acback_Integ_PostTransactionsData]]
support_relevance: high
last_verified: 2026-07-05
---
# Acback_Integ_SendInvoices


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Curs_Vou, Customers, IntegrationErrorLog, IntegrationPostedTransactions, Items, SalesPersons, TransactionsDetails, TransactionsHeaders. Writes IntegrationErrorLog, IntegrationPostedTransactions, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- Curs_Vou
- [[Customers]]
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
- [[Acback_Integ_PostTransactionsData]]
## Impact / Dependencies

**Tables Read**
- Curs_Vou
- [[Customers]]
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
- [[Acback_Integ_PostTransactionsData]]

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
