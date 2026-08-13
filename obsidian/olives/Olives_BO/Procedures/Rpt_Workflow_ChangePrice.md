---
type: procedure
database: Olives_BO
name: Rpt_Workflow_ChangePrice
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[RequestToChangeItemSellPrice]]
  - STRING_SPLIT
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Workflow_ChangePrice


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, RequestToChangeItemSellPrice, STRING_SPLIT, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=600
- @FromDate smalldatetime='2024-04-22'
- @ToDate smalldatetime='2024-4-22'
## Tables Read
- [[Customers]]
- [[Items]]
- [[RequestToChangeItemSellPrice]]
- STRING_SPLIT
- [[SalesPersons]]
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
- [[Customers]]
- [[Items]]
- [[RequestToChangeItemSellPrice]]
- STRING_SPLIT
- [[SalesPersons]]
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
