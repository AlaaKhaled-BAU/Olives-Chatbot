---
type: procedure
database: Olives_BO
name: Pro_PromotionsApproval
schema: dbo
tags: [#backoffice, #integration, #sales, #workflow]
reads_from:
  - [[PromotionsApprovalLog]]
  - [[PromotionsApprovalSetup]]
  - [[PromotionsHeaders]]
  - [[Users]]
writes_to:
  - [[PromotionsApprovalLog]]
  - [[PromotionsApprovalSetup]]
  - [[PromotionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Promotion-Setup
---
# Pro_PromotionsApproval


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionsApprovalLog, PromotionsApprovalSetup, PromotionsHeaders, Users. Writes PromotionsApprovalLog, PromotionsApprovalSetup, PromotionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @Level smallint=null
- @ID int = null
- @StartDate smalldatetime =null
- @EndDate smalldatetime =null
- @Approved bit = null
- @Notes nvarchar (Max) = null
- @UserID nvarchar(100)=null
- @cmdType varchar(50)=null
## Tables Read
- [[PromotionsApprovalLog]]
- [[PromotionsApprovalSetup]]
- [[PromotionsHeaders]]
- [[Users]]
## Tables Written
- [[PromotionsApprovalLog]]
- [[PromotionsApprovalSetup]]
- [[PromotionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PromotionsApprovalLog]]
- [[PromotionsApprovalSetup]]
- [[PromotionsHeaders]]
- [[Users]]

**Tables Written**
- [[PromotionsApprovalLog]]
- [[PromotionsApprovalSetup]]
- [[PromotionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
