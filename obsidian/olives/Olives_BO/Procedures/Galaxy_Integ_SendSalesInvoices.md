---
type: procedure
database: Olives_BO
name: Galaxy_Integ_SendSalesInvoices
schema: dbo
tags: [#backoffice, #billing, #integration, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Galaxy_Integration]]
  - [[InvoiceReturnLink]]
  - [[NoTransactionsReasons]]
  - [[PaymentsTypes]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
  - InvoiceDF
  - InvoiceHF
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
callees: [[Galaxy_Integration]]
---
# Galaxy_Integ_SendSalesInvoices


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, Galaxy_Integration, InvoiceReturnLink, NoTransactionsReasons, PaymentsTypes, SalesPersons, TransactionsDetails, TransactionsHeaders. Writes InvoiceDF, InvoiceHF, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Galaxy_Integration]]
- [[InvoiceReturnLink]]
- [[NoTransactionsReasons]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- InvoiceDF
- InvoiceHF
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Galaxy_Integration]]
- [[InvoiceReturnLink]]
- [[NoTransactionsReasons]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
- InvoiceDF
- InvoiceHF
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
