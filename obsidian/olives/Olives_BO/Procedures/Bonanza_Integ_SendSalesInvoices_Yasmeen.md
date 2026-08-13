---
type: procedure
database: Olives_BO
name: Bonanza_Integ_SendSalesInvoices_Yasmeen
schema: dbo
tags: [#backoffice, #billing, #integration, #sales]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - InvInvoiceDetails_InCube
  - InvInvoiceHeader_InCube
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Bonanza_Integ_SendSalesInvoices_Yasmeen


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, TransactionsDetails, TransactionsHeaders, dbo. Writes InvInvoiceDetails_InCube, InvInvoiceHeader_InCube, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- InvInvoiceDetails_InCube
- InvInvoiceHeader_InCube
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- InvInvoiceDetails_InCube
- InvInvoiceHeader_InCube
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
