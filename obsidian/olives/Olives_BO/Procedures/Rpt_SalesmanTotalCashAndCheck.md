---
type: procedure
database: Olives_BO
name: Rpt_SalesmanTotalCashAndCheck
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_GetInvoiceTotalAmount
  - Fun_GetReceiptsChecksTotal
  - [[Receipts]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanTotalCashAndCheck


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetInvoiceTotalAmount, Fun_GetReceiptsChecksTotal, Receipts, SalesPersons, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @FromSaleman int = 9
- @ToSalesman int=9
- @FromDate varchar(50)='2023-10-09'
- @ToDate varchar(50) ='2023-10-09'
## Tables Read
- Fun_GetInvoiceTotalAmount
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetInvoiceTotalAmount
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
