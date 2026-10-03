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
last_verified: 2026-10-03
---
# WF_PositionsVer

## Business Purpose
The workflow position version cache table — tracks the synchronization version (`WFVer`) of approval hierarchies for each position (`PositionID`). When workflow setup changes or a new request level is created, the version counter increments so that mobile devices and supervisor tablets know their inbox setup must refresh. Queryable via `t.WF_PositionsVer`.

## Chatbot semantics
(Query `t.WF_PositionsVer` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| نسخة إعدادات الموافقات للوظيفة | `PositionID`, `WFVer` | Direct filter | Version number of position workflow |
| تحديث إعدادات التابلت | `WFVer` | Monotonically increasing counter | Trigger for tablet inbox sync |

## Grain & keys
- **Composite PK**: (`CompanyID`, `PositionID`)
- **Tenant key**: `CompanyID`
- **FK**: `PositionID` → [[Positions]](ID)

## Pipeline
Updated by `WF_AddWorkFlowLevelOne` and `WF_AddWorkFlowLevels` when approval rows are generated. Read by `OT_SendSalesmanData` during mobile sync.

## Related
- [[Positions]]
- [[WF_SubLog]]
- [[WF_SetupHeader]]
- [[WF_SetupDetails]]


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
