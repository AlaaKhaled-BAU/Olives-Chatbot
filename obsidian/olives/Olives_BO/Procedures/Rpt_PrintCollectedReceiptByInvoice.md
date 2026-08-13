---
type: procedure
database: Olives_BO
name: Rpt_PrintCollectedReceiptByInvoice
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersons]]
writes_to:
called_by:
  - [[Rpt_PrintCollectedReceipt]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PrintCollectedReceiptByInvoice


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, ClientsActive, Customers, Fun_GetCompanyBranchesByUser, Receipts, Receipts_PaidTrans, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
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
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_PrintCollectedReceipt]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
- [[Rpt_PrintCollectedReceipt]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
