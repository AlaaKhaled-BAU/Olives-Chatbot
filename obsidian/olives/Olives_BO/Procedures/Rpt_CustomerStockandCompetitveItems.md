---
type: procedure
database: Olives_BO
name: Rpt_CustomerStockandCompetitveItems
schema: dbo
tags: [#backoffice, #customer, #inventory, #reporting]
reads_from:
  - [[CompetitiveItems]]
  - [[CompetitveItemsDataDF]]
  - [[CompetitveItemsDataHF]]
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Customers]]
  - [[Items]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerStockandCompetitveItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompetitiveItems, CompetitveItemsDataDF, CompetitveItemsDataHF, CustomerStockTacking, CustomerStockTackingDetails, Customers, Items, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @FromDate smalldatetime = '2025-02-15'
- @ToDate smalldatetime = '2025-02-17'
- @FromSales int =307
- @ToSales int = 307
- @UserID nvarchar(50) = null
## Tables Read
- [[CompetitiveItems]]
- [[CompetitveItemsDataDF]]
- [[CompetitveItemsDataHF]]
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompetitiveItems]]
- [[CompetitveItemsDataDF]]
- [[CompetitveItemsDataHF]]
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
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
