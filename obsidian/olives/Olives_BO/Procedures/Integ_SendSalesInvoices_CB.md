---
type: procedure
database: Olives_BO
name: Integ_SendSalesInvoices_CB
schema: dbo
tags: [#backoffice, #billing, #integration, #sales]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - TrHeader_Cusror
  - TrPromotion_Cursor
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsPromotions]]
  - `dbo`
writes_to:
  - OT_TransactionDF
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Integ_SendSalesInvoices_CB


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, TrHeader_Cusror, TrPromotion_Cursor, TransactionsDetails, TransactionsHeaders, TransactionsPromotions, dbo. Writes OT_TransactionDF, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- TrHeader_Cusror
- TrPromotion_Cursor
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]
- `dbo`
## Tables Written
- OT_TransactionDF
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- TrHeader_Cusror
- TrPromotion_Cursor
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]
- dbo

**Tables Written**
- OT_TransactionDF
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
