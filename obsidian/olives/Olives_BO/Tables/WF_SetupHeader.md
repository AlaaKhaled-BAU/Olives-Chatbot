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
last_verified: 2026-10-03
related_workflows:
  - Workflow-Approval-Setup
---
# WF_SetupHeader

## Business Purpose
The workflow approval rule configuration header — defines approval chains for each request type (`FunctionID`). Specifies the applicant source (`FromType`, `FromID`), total number of required approval levels (`LevelCount`), and whether the workflow rule is active (`IsSuspended`). The specific approver positions for each level live in [[WF_SetupDetails]]. Queryable via `t.WF_SetupHeader`.

## Chatbot semantics
(Query `t.WF_SetupHeader` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| إعدادات وسلسلة موافقات الطلب | `FunctionID`, `LevelCount` | Filter by `FunctionID` | Shows how many levels are required |
| تفاصيل الرتب والموافقين | Join `t.WF_SetupDetails` | `d.SetupID = h.AutoID` | Position assigned to each approval level |
| سلسلة موافقات نشطة | `IsSuspended` | `IsSuspended = 0` | Active workflow definition |

## Grain & keys
- **PK**: `AutoID` (bigint identity)
- **Tenant key**: `CompanyID`
- **FK**: `FunctionID` → [[WF_Functions]](ID)

## Pipeline
Configured in Back Office workflow setup screens (`Pro_WF_SetupHeader`). Evaluated by `WF_AddWorkFlowLevelOne` when creating new requests to determine how many `WF_SubLog` rows to generate.

## Related
- [[WF_SetupDetails]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SubLog]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | bigint | NO | ✓ |  |  |
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

- **Dispatch**: FromType observed live: 0(×47),1(×14),2(×5) — pairs with FromID to name the governed object
- **Function link**: FunctionID resolves against the [[WF_Functions]] catalog by convention
## Tenancy

Chatbot queries `t.WF_SetupHeader` / `t.WF_SetupDetails` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
