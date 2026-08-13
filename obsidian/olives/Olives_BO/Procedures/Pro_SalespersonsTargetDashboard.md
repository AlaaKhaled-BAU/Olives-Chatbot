---
type: procedure
database: Olives_BO
name: Pro_SalespersonsTargetDashboard
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_GetSalesmanTreeByID
  - [[Items]]
  - [[ItemsCategories]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalespersonsTargetDashboard


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetSalesmanTreeByID, Items, ItemsCategories, OrdersDetails, OrdersHeaders, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @CmdType varchar(50)
- @SalesmanNo int = null
- @PeriodType smallint = null
- @UserID nvarchar(50) = null
- @Date smalldatetime
- @IsTotal bit = 0
## Tables Read
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
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
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
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

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
