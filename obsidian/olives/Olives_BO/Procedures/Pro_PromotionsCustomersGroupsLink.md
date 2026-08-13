---
type: procedure
database: Olives_BO
name: Pro_PromotionsCustomersGroupsLink
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
reads_from:
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - `dbo`
writes_to:
  - [[PromotionsCustomersGroupsLink]]
  - PromotionsCustomersGroupsLinkLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionsCustomersGroupsLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionsCustomersGroupsLink, PromotionsHeaders, dbo. Writes PromotionsCustomersGroupsLink, PromotionsCustomersGroupsLinkLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PromotionID INT = null
- @CustomersPromotionsGroupsID Int = null
- @cmdType varchar(50)=null
- @LogID numeric(30,0)=null
- @OpType smallint = null
- @AssignCustomersPromotions  AssignCustomersPromotions readonly
## Tables Read
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- `dbo`
## Tables Written
- [[PromotionsCustomersGroupsLink]]
- PromotionsCustomersGroupsLinkLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- dbo

**Tables Written**
- [[PromotionsCustomersGroupsLink]]
- PromotionsCustomersGroupsLinkLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
