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

## FunctionID catalog (live, 47 rows)

| ID | Function |
|----|----------|
| 1 | Request To Change Invoice Payment Type |
| 2 | Request To Exceed Customer Credit Limit |
| 3 | Request To Exceed Checks Due Date |
| 4 | Request To Exceed Customer Invoice Due Days In Invoice |
| 5 | Request To Sales Customer Not In Route |
| 6 | Request To Approve Sales Order |
| 7 | Request To Approve Load Order |
| 8 | Request To Approve Return Sales |
| 9 | Request To Approve Unload Order |
| 10 | Request To Exceed Salesman Credit Limit |
| 11 | Request To Add Discount |
| 12 | Request To Exceed Customer Invoice Due Days In Order |
| 13 | Request To Add Discount InOrder |
| 14 | Request To Approve Chq Limit |
| 15 | Request To Exceed Customer Credit Limit In Order |
| 16 | Add Extra Bonus To Invoice |
| 17 | Add Extra Bonus To Order |
| 18 | Change Price In Invoice |
| 19 | Change Price In Order |
| 20 | Request For Customer Login Without Verification |
| 21 | Request To Add New Customer |
| 22 | Request To Approve Return Order |
| 23 | Request Salesman Will Not Visit |
| 24 | NoTransaction Notification |
| 25 | Add Extra Bonus And Discount To Invoice |
| 26 | Add Extra Bonus And Discount To Order |
| 27 | Request To Allow Take Checks From Customer |
| 28 | Promo |
| 29 | Request To Make Transaction To Suspended Customer |
| 30 | Request To Add Drawer |
| 31 | Request To Exceed Invoice Amount |
| 32 | Request To Exceed Invoice Count |
| 33 | Request To Exceed Customer Visit Order |
| 34 | Add Extra Bonus And Discount To Sales Quotation |
| 35 | Request To Approve Sales Quotation |
| 36 | Request To Link Customer To Salesman |
| 37 | Request To Exceed Finish All Tasks |
| 38 | Request To Make Zero Amount Invoice |
| 39 | Request To Increase Customer Creditlimit |
| 40 | Request To Change Delivery Payment Type |
| 41 | Request To Exceed Payment Invoice Discount |
| 42 | Request To Exceed Pay Over Balance |
| 43 | Request To Approve Vacation |
| 44 | Request To Approve POA |
| 45 | Request To Approve Special Discount |
| 46 | Request To Void Transaction |
| 47 | Request To Cancel Payment |

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

## Tenancy

Chatbot queries `t.WF_Functions` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
