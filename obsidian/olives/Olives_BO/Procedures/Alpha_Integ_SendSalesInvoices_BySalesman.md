---
type: procedure
database: Olives_BO
name: Alpha_Integ_SendSalesInvoices_BySalesman
schema: dbo
tags: [#backoffice, #billing, #integration, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - [[OT_InvoiceDF]]
  - [[OT_InvoiceHF]]
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_SendSalesInvoices_BySalesman


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, SalesPersons, TransactionsHeaders, dbo. Writes OT_InvoiceDF, OT_InvoiceHF, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @AlphaSalesmanNo int
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
