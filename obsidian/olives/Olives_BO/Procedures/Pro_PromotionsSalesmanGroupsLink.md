---
type: procedure
database: Olives_BO
name: Pro_PromotionsSalesmanGroupsLink
schema: dbo
tags: [#backoffice, #reference, #sales]
reads_from:
  - [[PromotionsSalesmanGroupsLink]]
  - `dbo`
writes_to:
  - [[PromotionsSalesmanGroupsLink]]
  - PromotionsSalesmanGroupsLinkLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionsSalesmanGroupsLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionsSalesmanGroupsLink, dbo. Writes PromotionsSalesmanGroupsLink, PromotionsSalesmanGroupsLinkLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PromotionID INT = null
- @SalesPersonsGroupID Int = null
- @cmdType varchar(50)=null
- @LogID numeric(30,0)=null
- @OpType smallint = null
## Tables Read
- [[PromotionsSalesmanGroupsLink]]
- `dbo`
## Tables Written
- [[PromotionsSalesmanGroupsLink]]
- PromotionsSalesmanGroupsLinkLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PromotionsSalesmanGroupsLink]]
- dbo

**Tables Written**
- [[PromotionsSalesmanGroupsLink]]
- PromotionsSalesmanGroupsLinkLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
