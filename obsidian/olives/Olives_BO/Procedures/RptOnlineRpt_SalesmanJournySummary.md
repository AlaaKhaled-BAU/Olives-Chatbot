---
type: procedure
database: Olives_BO
name: RptOnlineRpt_SalesmanJournySummary
schema: dbo
tags: [#backoffice, #integration, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - Fun_GetInvoiceTotalAmount
  - Fun_GetReceiptsChecksTotal
  - [[LogActionTransaction]]
  - [[Receipts]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# RptOnlineRpt_SalesmanJournySummary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Fun_GetInvoiceTotalAmount, Fun_GetReceiptsChecksTotal, LogActionTransaction, Receipts, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @SalesmanNo int=410
- @WorkDay smalldatetime='2023-05-07'
## Tables Read
- [[ClientsActive]]
- Fun_GetInvoiceTotalAmount
- Fun_GetReceiptsChecksTotal
- [[LogActionTransaction]]
- [[Receipts]]
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
- [[ClientsActive]]
- Fun_GetInvoiceTotalAmount
- Fun_GetReceiptsChecksTotal
- [[LogActionTransaction]]
- [[Receipts]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
