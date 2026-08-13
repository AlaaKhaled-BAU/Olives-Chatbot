---
type: procedure
database: Olives_BO
name: WF_AddWorkFlowLevelOne_Promotions
schema: dbo
tags: [#auth, #backoffice, #sales, #workflow]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - Create_Approve_Req
  - [[Customers]]
  - [[CustomersWFFunctionsAutoApprove]]
  - Fun_GetSalesPersonTree
  - [[PromotionsHeaders]]
  - [[RequestToApprovePromotion]]
  - [[RequestToApprovePromotionDetails]]
  - [[SalesPersons]]
  - [[WF_Functions]]
  - [[WF_MasterLog]]
  - [[WF_SetupDetails]]
  - [[WF_SetupHeader]]
  - [[WF_SubLog]]
writes_to:
  - [[RequestToApprovePromotion]]
  - [[RequestToApprovePromotionDetails]]
  - [[WF_MasterLog]]
  - [[WF_PositionsVer]]
  - [[WF_SubLog]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_AddWorkFlowLevelOne_Promotions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Create_Approve_Req, Customers, CustomersWFFunctionsAutoApprove, Fun_GetSalesPersonTree, PromotionsHeaders, RequestToApprovePromotion, RequestToApprovePromotionDetails, SalesPersons, WF_Functions, WF_MasterLog, WF_SetupDetails, WF_SetupHeader, WF_SubLog. Writes RequestToApprovePromotion, RequestToApprovePromotionDetails, WF_MasterLog, WF_PositionsVer, WF_SubLog. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FunctionID int = 28
- @Ref1 nvarchar(100) = '150'
- @Ref2 nvarchar(100) = ''
- @Ref3 nvarchar(100) = ''
- @Ref4 nvarchar(100) = ''
- @Ref5 nvarchar(100) = ''
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- Create_Approve_Req
- [[Customers]]
- [[CustomersWFFunctionsAutoApprove]]
- Fun_GetSalesPersonTree
- [[PromotionsHeaders]]
- [[RequestToApprovePromotion]]
- [[RequestToApprovePromotionDetails]]
- [[SalesPersons]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SetupDetails]]
- [[WF_SetupHeader]]
- [[WF_SubLog]]
## Tables Written
- [[RequestToApprovePromotion]]
- [[RequestToApprovePromotionDetails]]
- [[WF_MasterLog]]
- [[WF_PositionsVer]]
- [[WF_SubLog]]
## Callers
- [[OT_ImportRequestToApprovePromotion]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- Create_Approve_Req
- [[Customers]]
- [[CustomersWFFunctionsAutoApprove]]
- Fun_GetSalesPersonTree
- [[PromotionsHeaders]]
- [[RequestToApprovePromotion]]
- [[RequestToApprovePromotionDetails]]
- [[SalesPersons]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SetupDetails]]
- [[WF_SetupHeader]]
- [[WF_SubLog]]

**Tables Written**
- [[RequestToApprovePromotion]]
- [[RequestToApprovePromotionDetails]]
- [[WF_MasterLog]]
- [[WF_PositionsVer]]
- [[WF_SubLog]]

**Callers**
_None_

**Callees**
- [[OT_ImportRequestToApprovePromotion]]


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
