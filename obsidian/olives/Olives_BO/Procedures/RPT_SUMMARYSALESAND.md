---
type: procedure
database: Olives_BO
name: RPT_SUMMARYSALESAND
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - [[CustomersTypes]]
  - [[Receipts]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-07-05
---
# RPT_SUMMARYSALESAND


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, CustomersTypes, Receipts, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromCustType int
- @ToCustType int
## Tables Read
- [[Checks]]
- [[Customers]]
- [[CustomersTypes]]
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
- [[Checks]]
- [[Customers]]
- [[CustomersTypes]]
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

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
