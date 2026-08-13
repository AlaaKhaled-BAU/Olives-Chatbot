---
type: table
database: Olives_BO
name: WF_PositionsVer
schema: dbo
tags: [#auth, #backoffice, #workflow]
foreign_keys:
  - [[Companies]]
  - [[Positions]]
referenced_by:
  - [[OT_SendSalesmanData]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# WF_PositionsVer


## Business Purpose

Workflow configuration or log table for approval process management.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| PositionID | int | NO | ✓ | ✓ | [[Positions]] |
| WFVer | numeric | YES |  |  |  |
## Primary Key
CompanyID
PositionID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, PositionID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (4):**
- [[OT_SendSalesmanData]]
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
