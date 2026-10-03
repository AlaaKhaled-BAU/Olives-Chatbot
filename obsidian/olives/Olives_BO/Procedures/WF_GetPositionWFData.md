---
type: procedure
database: Olives_BO
name: WF_GetPositionWFData
schema: dbo
tags: [#auth, #backoffice, #workflow]
reads_from:
  - [[ClientsActive]]
  - [[CompanyBranches]]
  - Customer
  - [[OrdersHeaders]]
  - [[PromotionsHeaders]]
  - [[RequestToApprovePromotionDetails]]
  - [[SalesPersons]]
  - [[WF_Functions]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_GetPositionWFData


## Purpose

Returns the **workflow inbox** dataset for a back-office `PositionID` (supervisor approvals from the tablet).

**Pending rows for this position** (same filter used throughout the proc body): `WF_SubLog.PositionID = @PositionID` AND `WF_SubLog.Action IS NULL` AND `WF_SubLog.ActionNeed = N'AR'`. Join [[WF_MasterLog]] / [[WF_Functions]] for request type and dates.

Status code meanings (`Action`, `ActionNeed`, `LastStatus`): [[Workflow_Approval_Codes]].

> [!note] AUTO-GENERATED dependency list below — inbox filter verified from live proc definition 2026-10.
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyBranches, Customer, OrdersHeaders, PromotionsHeaders, RequestToApprovePromotionDetails, SalesPersons, WF_Functions, WF_MasterLog, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @PositionID int=1
## Tables Read
- [[ClientsActive]]
- [[CompanyBranches]]
- Customer
- [[OrdersHeaders]]
- [[PromotionsHeaders]]
- [[RequestToApprovePromotionDetails]]
- [[SalesPersons]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
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
- Customer
- [[OrdersHeaders]]
- [[PromotionsHeaders]]
- [[RequestToApprovePromotionDetails]]
- [[SalesPersons]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
