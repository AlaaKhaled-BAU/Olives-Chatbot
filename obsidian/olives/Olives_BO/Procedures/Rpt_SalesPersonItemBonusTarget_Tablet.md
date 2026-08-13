---
type: procedure
database: Olives_BO
name: Rpt_SalesPersonItemBonusTarget_Tablet
schema: dbo
tags: [#backoffice, #inventory, #mobile, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - Fun_GetSalesmanBonusItemForTarget
  - [[Items]]
  - [[ItemsGroupBonusTarget]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersonGroupItemBonusTarget]]
  - [[SalesPersonItemBonusTarget]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsPromotions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesPersonItemBonusTarget_Tablet


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Fun_GetSalesmanBonusItemForTarget, Items, ItemsGroupBonusTarget, OrdersDetails, OrdersHeaders, SalesPersonGroupItemBonusTarget, SalesPersonItemBonusTarget, SalesPersons, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders, TransactionsPromotions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @TargetYear smallint = 2020
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 99999
- @FromItemNo nvarchar(100) = '0'
- @ToItemNo nvarchar(100) = 'zzzzzzzzzzzzzz'
- @UseItemBonusTargetSalesmanGroup bit=1
- @FromSalesmanGroupID int = 0
- @ToSalesmanGroupID int = 99999
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_GetSalesmanBonusItemForTarget
- [[Items]]
- [[ItemsGroupBonusTarget]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersonGroupItemBonusTarget]]
- [[SalesPersonItemBonusTarget]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_GetSalesmanBonusItemForTarget
- [[Items]]
- [[ItemsGroupBonusTarget]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersonGroupItemBonusTarget]]
- [[SalesPersonItemBonusTarget]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]

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
