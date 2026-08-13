---
type: table
database: Olives_BO
name: WF_SetupHeader
schema: dbo
tags: [#auth, #backoffice, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_WF_SetupHeader]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Workflow-Approval-Setup
---
# WF_SetupHeader


## Business Purpose

Workflow approval process definitions — levels, approvers, and conditions.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | bigint | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| FromType | smallint | YES |  |  |  |
| FromID | bigint | YES |  |  |  |
| FunctionID | smallint | YES |  |  |  |
| LevelCount | tinyint | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_WF_SetupHeader]]
- [[WF_AddWorkFlowLevelOne_Promotions]]

**Writes (1):**
- [[Pro_WF_SetupHeader]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Credit-Limit-Block]]
