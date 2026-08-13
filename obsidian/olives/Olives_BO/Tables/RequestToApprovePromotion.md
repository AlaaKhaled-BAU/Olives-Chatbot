---
type: table
database: Olives_BO
name: RequestToApprovePromotion
schema: dbo
tags: [#backoffice, #sales, #workflow]
foreign_keys:
referenced_by:
  - [[OT_ImportRequestToApprovePromotion]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToApprovePromotion


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| PromotionInfo | nvarchar | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| PromotionID | int | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportRequestToApprovePromotion]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevelOne_Promotions]]

**Writes (4):**
- [[OT_ImportRequestToApprovePromotion]]
- [[WF_AddWorkFlowLevelOne]]
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
