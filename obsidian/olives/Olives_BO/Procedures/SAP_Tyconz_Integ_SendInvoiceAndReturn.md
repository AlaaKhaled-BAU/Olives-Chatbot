---
type: procedure
database: Olives_BO
name: SAP_Tyconz_Integ_SendInvoiceAndReturn
schema: dbo
tags: [#backoffice, #billing, #integration, #order]
reads_from:
  - [[Customers]]
  - [[PaymentsTypes]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - InvoiceDF
  - InvoiceHF
  - SalesRet_InvoicesSettlement
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Tyconz_Integ_SendInvoiceAndReturn


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, PaymentsTypes, SalesPersons, TransactionsDetails, TransactionsHeaders, dbo. Writes InvoiceDF, InvoiceHF, SalesRet_InvoicesSettlement, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 7
## Tables Read
- [[Customers]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- InvoiceDF
- InvoiceHF
- SalesRet_InvoicesSettlement
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- InvoiceDF
- InvoiceHF
- SalesRet_InvoicesSettlement
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
