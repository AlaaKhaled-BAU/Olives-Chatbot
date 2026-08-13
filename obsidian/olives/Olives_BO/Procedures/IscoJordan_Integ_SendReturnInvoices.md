---
type: procedure
database: Olives_BO
name: IscoJordan_Integ_SendReturnInvoices
schema: dbo
tags: [#backoffice, #billing, #integration, #order]
reads_from:
  - [[Customers]]
  - DATA
  - InvoiceHeader
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# IscoJordan_Integ_SendReturnInvoices


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DATA, InvoiceHeader, Items, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- DATA
- InvoiceHeader
- [[Items]]
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
- [[Customers]]
- DATA
- InvoiceHeader
- [[Items]]
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
