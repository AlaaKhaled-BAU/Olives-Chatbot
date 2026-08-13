---
type: procedure
database: Olives_BO
name: Pro_SalesPersonItemBonusTarget_OnlineErrorReporting
schema: dbo
tags: [#backoffice, #inventory, #log, #reporting, #sales]
reads_from:
  - [[CompanyParameters]]
  - Fun_GetSalesmanBonusItemForTarget
  - [[Items]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsHeaders]]
  - [[SalesPersonGroupItemBonusTarget]]
  - [[SalesPersonItemBonusTarget]]
  - [[SalesPersons]]
  - `dbo`
  - osfa_DB
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonItemBonusTarget_OnlineErrorReporting


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyParameters, Fun_GetSalesmanBonusItemForTarget, Items, PromotionsCondUnCodOutput, PromotionsCondUnCodInput, PromotionsHeaders, SalesPersonGroupItemBonusTarget, SalesPersonItemBonusTarget, SalesPersons, dbo, osfa_DB. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @SalesmanNo int = 3003
- @promoId int =1
- @Salesmanbonusgrouptype int =2  /* fill in either 1 to check Bonus Target for one salesman, or 2 to check Bonus Target for salesmengroup*/
## Tables Read
- [[CompanyParameters]]
- Fun_GetSalesmanBonusItemForTarget
- [[Items]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsHeaders]]
- [[SalesPersonGroupItemBonusTarget]]
- [[SalesPersonItemBonusTarget]]
- [[SalesPersons]]
- `dbo`
- osfa_DB
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyParameters]]
- Fun_GetSalesmanBonusItemForTarget
- [[Items]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCondUnCodinput]]
- [[PromotionsHeaders]]
- [[SalesPersonGroupItemBonusTarget]]
- [[SalesPersonItemBonusTarget]]
- [[SalesPersons]]
- dbo
- osfa_DB

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
