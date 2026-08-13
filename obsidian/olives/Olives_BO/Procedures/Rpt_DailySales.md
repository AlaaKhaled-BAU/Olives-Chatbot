---
type: procedure
database: Olives_BO
name: Rpt_DailySales
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DailySales


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsCategories, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SmallInt = 1
- @FromCateg NVarChar(50) = '0'
- @ToCateg NVarChar(50) = 'zzz'
- @FromSalesman Int = 1
- @ToSalesman Int = 9999999
- @Date SmallDateTime = '2021-01-22'
- @ToDate SmallDateTime = '2021-06-22'
## Tables Read
- [[Items]]
- [[ItemsCategories]]
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
- [[Items]]
- [[ItemsCategories]]
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
