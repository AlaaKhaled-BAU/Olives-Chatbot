---
type: procedure
database: Olives_BO
name: Rpt_ItemSalesSummaryBySelection
schema: dbo
tags: [#backoffice, #inventory, #reporting, #sales]
reads_from:
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ItemSalesSummaryBySelection


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser, Items, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @ItemsList nvarchar(MAx)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @Salesmanlist nvarchar(MAx)
- @UserID nvarchar(50)=null
## Tables Read
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[Items]]
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
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[Items]]
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
