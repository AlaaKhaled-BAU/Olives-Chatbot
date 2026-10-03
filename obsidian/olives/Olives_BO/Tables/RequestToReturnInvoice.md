---
type: table
database: Olives_BO
name: RequestToReturnInvoice
schema: dbo
tags: [#backoffice, #billing, #order, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToReturnInvoice]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToReturnInvoice

## Business Purpose
Stores approval requests submitted when a salesman requests issuing a return invoice for a customer. Corresponds to workflow `FunctionID = 8` ("Request To Approve Return Sales"). Captures the return invoice amount, customer, salesman, timestamp, and `IsAproved`. Queryable via `t.RequestToReturnInvoice`.

## Chatbot semantics
(Query `t.RequestToReturnInvoice` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات الموافقة على إرجاع فاتورة | `CustomerNo`, `SalesPersonNo`, `TrDate` | Direct filter | Sales return permission requests |
| قيمة فاتورة الإرجاع | `InvoiceAmount` | Numeric | Total amount of items being returned |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 8 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

**Do not confuse with:**
- `ReturnOrdersHeaders`: Return orders entered for warehouse processing (`FunctionID = 22`).
- `TransactionsHeaders` with `TransactionTypeID = 2`: Actual final posted return invoices.

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 return request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Tablet salesman requests sales return → `OT_ImportRequestToReturnInvoice` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 8, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[ReturnOrdersHeaders]]
- [[TransactionsHeaders]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_ImportRequestToReturnInvoice]]

**Writes (3):**
- [[OT_ImportRequestToReturnInvoice]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
