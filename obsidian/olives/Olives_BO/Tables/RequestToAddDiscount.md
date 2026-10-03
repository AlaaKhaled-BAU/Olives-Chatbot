---
type: table
database: Olives_BO
name: RequestToAddDiscount
schema: dbo
tags: [#backoffice, #billing, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToAddDiscount]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToAddDiscount

## Business Purpose
Stores approval requests submitted when a salesman requests an extra discount (manual or over-threshold discount) on an invoice. Corresponds to workflow `FunctionID = 11` ("Request To Add Discount"). Captures `DiscountAmount`, `DiscountPercent`, `InvoiceAmount`, salesman, customer, timestamp, and approval state. Queryable via `t.RequestToAddDiscount`.

## Chatbot semantics
(Query `t.RequestToAddDiscount` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات الخصم الإضافي على الفواتير | `SalesPersonNo`, `CustomerNo`, `TrDate` | Direct filter | Lists discount approval requests |
| نسبة وقيمة الخصم المطلوبة | `DiscountPercent`, `DiscountAmount` | Numeric values | Discount details requested |
| قيمة الفاتورة | `InvoiceAmount` | Total before extra discount | Financial context |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending/rejected) | Direct approval status |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 11 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

**Do not confuse with:**
- `RequestToAddDiscountInOrder`: Workflow `FunctionID = 13` (discount request on pre-sales *order*, not invoice).
- `RequestToAddExtraBonusAndDiscount`: Combined bonus and discount request (`FunctionID = 25`).

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 discount request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Tablet salesman requests discount exceeding limit → `OT_ImportRequestToAddDiscount` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 11, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[RequestToAddDiscountInOrder]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_ImportRequestToAddDiscount]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevels]]

**Writes (3):**
- [[OT_ImportRequestToAddDiscount]]
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
