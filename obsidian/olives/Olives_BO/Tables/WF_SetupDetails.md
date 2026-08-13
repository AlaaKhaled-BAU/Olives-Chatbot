---
type: table
database: Olives_BO
name: WF_SetupDetails
schema: dbo
tags: [#auth, #backoffice, #workflow]
foreign_keys:
  - [[WF_SetupHeader]]
referenced_by:
  - [[Pro_WF_SetupDetails]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Workflow-Approval-Setup
---
# WF_SetupDetails


## Business Purpose

Workflow configuration or log table for approval process management.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | bigint | NO | ✓ | ✓ | [[WF_SetupHeader]] |
| CompanyID | smallint | NO | ✓ |  |  |
| LevelID | tinyint | NO | ✓ |  |  |
| SalesPersonType | int | NO | ✓ |  |  |
| SetupValue | float | YES |  |  |  |
| IsFinalApprove | bit | YES |  |  |  |
| SeeAllRequest | bit | YES |  |  |  |
## Primary Key
AutoID
CompanyID
LevelID
SalesPersonType
## Foreign Keys
AutoID -> [[WF_SetupHeader]](AutoID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_WF_SetupDetails]]
- [[WF_AddWorkFlowLevelOne_Promotions]]

**Writes (1):**
- [[Pro_WF_SetupDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Credit-Limit-Block]]
