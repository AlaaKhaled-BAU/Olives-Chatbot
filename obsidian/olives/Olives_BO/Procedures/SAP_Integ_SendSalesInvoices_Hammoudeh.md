---
type: procedure
database: Olives_BO
name: SAP_Integ_SendSalesInvoices_Hammoudeh
schema: dbo
tags: [#backoffice, #billing, #integration, #sales]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - SalesVoucher
  - SalesVoucherItems
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Integ_SendSalesInvoices_Hammoudeh


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, TransactionsHeaders, dbo. Writes SalesVoucher, SalesVoucherItems, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- SalesVoucher
- SalesVoucherItems
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- SalesVoucher
- SalesVoucherItems
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
