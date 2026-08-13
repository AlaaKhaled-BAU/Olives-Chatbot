---
type: procedure
database: Olives_BO
name: CL_Integ_SendAllTransactions
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - CLCL
  - [[Checks]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# CL_Integ_SendAllTransactions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CLCL, Checks, Customers, CustomersFinancialDetails, Receipts, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- CLCL
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CLCL
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

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
