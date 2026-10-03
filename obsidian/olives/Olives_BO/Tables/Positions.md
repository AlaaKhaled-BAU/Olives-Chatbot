---
type: table
database: Olives_BO
name: Positions
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Fill_Sales_Device_Reports]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[Pro_ItemsUsedInLoadOrderAssignment]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_Positions]]
  - [[Pro_ProspectiveCustomers]]
  - [[Pro_SalesPersonContractsAssignment]]
  - [[Pro_WF_SetupHeader]]
  - [[Rpt_ActiveAndInactiveCustomers]]
  - [[Rpt_CustomersAvgPerClass]]
  - [[Rpt_LinkedCallCenter]]
  - [[Rpt_SalesPersonAndCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
  - [[Rpt_WF_SalesOrderStatus]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
support_relevance: high
last_verified: 2026-10-03
related_workflows:
  - Company-Setup
  - Salesman-Onboarding
  - Workflow-Approval-Setup
---
# Positions

## Business Purpose
The organizational positions master table — defines job positions within the corporate hierarchy (e.g. Sales Representative, Route Van Driver, Regional Supervisor). Crucial in two core subsystems:
1. **Workflow Approval Hierarchy**: Approvers and request inboxes in [[WF_SubLog]] are addressed to `PositionID` (see [[WF_GetPositionWFData]]).
2. **Route and Customer Assignment**: Routes in [[SalesPersonsRoutes]] and customer assignments in [[CustomersFinancialDetails]] are bound to `PositionsID`.
Queryable via `t.Positions`.

## Chatbot semantics
(Query `t.Positions` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| مسمى / معرف الوظيفة | `ID`, `Name` | `Name LIKE N'%...%'` OR `ID = ...` | Identifies organizational role |
| موظف شاغل الوظيفة | Join `t.SalesPersons` | `SalesPersons.PositionID = p.ID` | Connects individual to position |
| طلبات الموافقة المعلقة للوظيفة | Join `t.WF_SubLog` | `s.PositionID = p.ID AND s.Action IS NULL AND s.ActionNeed = N'AR'` | Supervisor inbox items |
| مسارات الوظيفة | Join `t.SalesPersonsRoutes` | `spr.PositionsID = p.ID` | Route schedule for position |

## Grain & keys
- **PK**: `ID` (integer position number)
- **Tenant key**: `CompanyID`

## Pipeline
Configured in Back Office organizational structure screens (`Pro_Positions`).

## Related
- [[SalesPersons]]
- [[WF_SubLog]]
- [[SalesPersonsRoutes]]
- [[CustomersFinancialDetails]]
- [[WF_GetPositionWFData]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Erp_Reference | varchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (49):**
- [[Fill_Sales_Device_Reports]]
- [[Pro_ItemsUsedInLoadOrderAssignment]]
- [[Pro_OrdersHeaders]]
- [[Pro_Positions]]
- [[Pro_ProspectiveCustomers]]
- [[Pro_SalesPersonContractsAssignment]]
- [[Pro_WF_SetupHeader]]
- [[Rpt_ActiveAndInactiveCustomers]]
- [[Rpt_CustomersAvgPerClass]]
- [[Rpt_LinkedCallCenter]]
- [[Rpt_SalesPersonAndCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
- [[Rpt_WF_SalesOrderStatus]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]

**Writes (66):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_Positions]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
