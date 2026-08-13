---
type: procedure
database: Olives_BO
name: Rpt_WorkFlowExceeds
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - [[Receipts]]
  - [[RequestToExceedCheckDueDate]]
  - STRING_SPLIT
  - [[SalesPersons]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WorkFlowExceeds


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, Receipts, RequestToExceedCheckDueDate, STRING_SPLIT, SalesPersons, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID  smallint =1
- @FromDate datetime = '2025-02-01'
- @ToDate datetime = '2025-02-28'
## Tables Read
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[RequestToExceedCheckDueDate]]
- STRING_SPLIT
- [[SalesPersons]]
- [[WF_SubLog]]
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
- [[Receipts]]
- [[RequestToExceedCheckDueDate]]
- STRING_SPLIT
- [[SalesPersons]]
- [[WF_SubLog]]

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
