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
last_verified: 2026-10-03
related_workflows:
  - Workflow-Approval-Setup
---
# WF_SetupDetails

## Business Purpose
The workflow approval step detail table — defines the specific approver roles, thresholds, and permissions for each approval level (`LevelID`) under a workflow configuration (`AutoID` linking to [[WF_SetupHeader]]). Specifies the approver category (`SalesPersonType` matching `SystemCodes.SalespersonType`), monetary approval limit (`SetupValue`), and whether this level has final approval authority (`IsFinalApprove`). Queryable via `t.WF_SetupDetails`.

## Chatbot semantics
(Query `t.WF_SetupDetails` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| رتبة ومستوى الموافقة | `LevelID`, `SalesPersonType` | Filter by `AutoID` / `LevelID` | 1=Level 1, 2=Level 2 approver role |
| صلاحية الموافقة النهائية | `IsFinalApprove` | `IsFinalApprove = 1` | Approver can grant final clearance |
| السقف المالي لصلاحية الموافقة | `SetupValue` | Numeric threshold | Max amount position can approve |
| رؤية جميع الطلبات | `SeeAllRequest` | `1` = sees all company requests | Visibility permission |

## Grain & keys
- **Composite PK**: (`CompanyID`, `AutoID`, `LevelID`, `SalesPersonType`)
- **Tenant key**: `CompanyID`
- **FK**: `AutoID` → [[WF_SetupHeader]](AutoID)

## Pipeline
Maintained in Back Office workflow setup screens (`Pro_WF_SetupDetails`). Evaluated by `WF_AddWorkFlowLevelOne` and `WF_AddWorkFlowLevels` to determine which positions receive pending approval items in `WF_SubLog`.

## Related
- [[WF_SetupHeader]]
- [[WF_Functions]]
- [[WF_SubLog]]
- [[SystemCodes]]


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
