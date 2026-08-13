---
type: table
database: Olives_BO
name: RequestToApprovePromotionDetails
schema: dbo
tags: [#backoffice, #sales, #workflow]
foreign_keys:
  - [[RequestToApprovePromotion]]
referenced_by:
  - [[OT_ImportRequestToApprovePromotion]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_AddWorkFlowLevels]]
  - [[WF_GetPositionWFData]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToApprovePromotionDetails


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ReqAutoID | numeric | YES | ✓ | ✓ | [[RequestToApprovePromotion]] |
| CompanyID | smallint | NO | ✓ |  |  |
| PromotionID | int | NO | ✓ |  |  |
| IsAproved | bit | YES |  |  |  |
| MasterReqID | numeric | YES |  |  |  |
## Primary Key
ReqAutoID
CompanyID
PromotionID
## Foreign Keys
ReqAutoID -> [[RequestToApprovePromotion]](AutoID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportRequestToApprovePromotion]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_GetPositionWFData]]

**Writes (3):**
- [[OT_ImportRequestToApprovePromotion]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
