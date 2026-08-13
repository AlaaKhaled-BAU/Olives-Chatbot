---
type: table
database: Olives_BO
name: WF_Functions
schema: dbo
tags: [#auth, #backoffice, #workflow]
foreign_keys:
referenced_by:
  - [[Pro_WF_Functions]]
  - [[Pro_WF_SetupHeader]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WFCustomersVisitsCounts]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_GetPositionWFData]]
  - [[WF_GetPositionWFDataByDate_Alerts]]
  - [[WF_GetPositionWFData_Alerts]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Workflow-Approval-Setup
---
# WF_Functions


## Business Purpose

Workflow function registry — all available approval/action functions.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | smallint | NO | ✓ |  |  |
| ArName | nvarchar | YES |  |  |  |
| EngName | nvarchar | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (9):**
- [[Pro_WF_Functions]]
- [[Pro_WF_SetupHeader]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WFCustomersVisitsCounts]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_GetPositionWFData]]
- [[WF_GetPositionWFDataByDate_Alerts]]
- [[WF_GetPositionWFData_Alerts]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
