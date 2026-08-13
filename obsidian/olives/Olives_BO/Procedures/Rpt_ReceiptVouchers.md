---
type: procedure
database: Olives_BO
name: Rpt_ReceiptVouchers
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[ClientsActive]]
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - [[CustomersPaidTransList]]
  - [[Drawers]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ReceiptVouchers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, ClientsActive, Companies, Currencies, Customers, CustomersPaidTransList, Drawers, Receipts, Receipts_PaidTrans, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SmallInt = 1
- @FromInv Int = 1
- @ToInv Int = 999999999
- @FromSalesman Int = 1
- @ToSalesman Int = 999999999
- @FromDate SmallDateTime = '2017-01-01'
- @ToDate SmallDateTime = '2021-05-01'
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- [[CustomersPaidTransList]]
- [[Drawers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- [[CustomersPaidTransList]]
- [[Drawers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]

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
