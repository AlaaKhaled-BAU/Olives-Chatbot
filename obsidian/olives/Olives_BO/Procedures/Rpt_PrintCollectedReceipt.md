---
type: procedure
database: Olives_BO
name: Rpt_PrintCollectedReceipt
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[ClientsActive]]
  - [[Customers]]
  - [[Drawers]]
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PrintCollectedReceipt


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, ClientsActive, Customers, Drawers, Fun_GetCompanyBranchesByUser, Receipts, SalesPersons. Invoked by 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @UserID nvarchar(50)=NULL
- @TransactionsHeadersDataTable TransactionsHeaders_Type readonly
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[Drawers]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
- [[Rpt_PrintCollectedReceiptByInvoice]]
- [[Rpt_PrintReceiptDetailsInfo]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[Drawers]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Rpt_PrintCollectedReceiptByInvoice]]
- [[Rpt_PrintReceiptDetailsInfo]]


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
