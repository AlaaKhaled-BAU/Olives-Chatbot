---
type: table
database: Olives_BO
name: RequestToExceedChqLimit
schema: dbo
tags: [#backoffice, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToExceedChqLimit]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToExceedChqLimit

## Business Purpose
Stores approval requests submitted when a salesman attempts to receive a check from a customer whose uncleared check balance exceeds their defined check limit (`ChqLimit`). Corresponds to workflow `FunctionID = 14` ("Request To Approve Chq Limit"). Captures check value, customer check balance, limit, customer, salesman, timestamp, and `IsAproved`. Queryable via `t.RequestToExceedChqLimit`.

## Chatbot semantics
(Query `t.RequestToExceedChqLimit` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات تجاوز سقف الشيكات | `CustomerNo`, `SalesPersonNo`, `TrDate` | Direct filter | Lists check ceiling exceptions |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| سقف الشيكات وقيمة الشيك | `ChqLimit`, `ChqValue` | Numeric values | Limits and requested check amounts |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 14 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 check limit exception request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Tablet detects check ceiling exceeded → `OT_ImportRequestToExceedChqLimit` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 14, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[CustomersFinancialDetails]]
- [[Checks]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| ReceiptAmount | float | YES |  |  |  |
| ChecksInfo | nvarchar | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| CustomerCreditLimit | float | YES |  |  |  |
| CustomerBanalce | float | YES |  |  |  |
| CustomerChqBanalce | float | YES |  |  |  |
| ExceedAmount | float | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ImportRequestToExceedChqLimit]]
- [[Rpt_WorkFlowFunctions]]

**Writes (3):**
- [[OT_ImportRequestToExceedChqLimit]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
