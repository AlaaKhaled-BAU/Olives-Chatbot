---
type: procedure
database: Olives_BO
name: Rpt_SalesmanCategorySales
schema: dbo
tags: [#backoffice, #reference, #reporting, #sales]
reads_from:
  - [[Items]]
  - [[ItemsCategories]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - the
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanCategorySales


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsCategories, OrdersDetails, OrdersHeaders, SalesPersons, TransactionsDetails, TransactionsHeaders, the. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @ViewDate smalldatetime = '2016-01-01'
- @ToViewDate smalldatetime = '2016-01-01'
## Tables Read
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- the
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- the

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
