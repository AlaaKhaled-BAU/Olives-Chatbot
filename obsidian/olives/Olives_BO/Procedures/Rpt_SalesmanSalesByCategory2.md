---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSalesByCategory2
schema: dbo
tags: [#backoffice, #reference, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CompanyBranches]]
  - Fun_ReCalcTransactionAmounts
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnitsDetails]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanSalesByCategory2


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyBranches, Fun_ReCalcTransactionAmounts, Items, ItemsCategories, ItemsUnitsDetails, SalesPersons, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @FromDate smalldatetime ='2015-01-01'
- @ToDate smalldatetime ='2020-12-01'
- @FromSalesman int =0
- @ToSalesman int =9999999
- @UserID  Nvarchar (50)='admin'
- @FormItemCat Nvarchar (50)='0'
- @ToItemCat Nvarchar (50)='zzzzzzzzzzzzzzzz'
## Tables Read
- [[ClientsActive]]
- [[CompanyBranches]]
- Fun_ReCalcTransactionAmounts
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnitsDetails]]
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
- [[ClientsActive]]
- [[CompanyBranches]]
- Fun_ReCalcTransactionAmounts
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnitsDetails]]
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
