---
type: table
database: Olives_BO
name: RequestToVoidTransaction
schema: dbo
tags: [#backoffice, #workflow]
foreign_keys:
referenced_by:
  - [[RequestToVoidTransaction_Insert]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToVoidTransaction

## Business Purpose
Stores approval requests submitted when a salesman requests cancelling / voiding an already-issued transaction (invoice, receipt, or order). Corresponds to workflow `FunctionID = 46` ("Request To Void Transaction"). Captures the target transaction identifier (`TrTypeID`, `TrTypeYear`, `TrTypeNo`), reason code/notes, salesman, timestamp, and `IsAproved`. Queryable via `t.RequestToVoidTransaction`.

## Chatbot semantics
(Query `t.RequestToVoidTransaction` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات إلغاء الفواتير والحركات | `SalesPersonNo`, `TrTypeYear`, `TrTypeNo` | Filter by salesman or doc number | Transaction void requests |
| الحركة المطلوب إلغاؤها | `TrTypeID`, `TrTypeYear`, `TrTypeNo` | Match against document headers | Identifies target transaction |
| حالة الموافقة على الإلغاء | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 46 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 void request)
- **Tenant key**: `CompanyID`
- **Conventions**: `SalesPersonNo` → [[SalesPersons]](ID), (`TrTypeID`, `TrTypeYear`, `TrTypeNo`) → [[TransactionsHeaders]] or [[Receipts]]

## Pipeline (how rows get here)
Salesman requests voiding on tablet → imported via `RequestToVoidTransaction_Insert` → calls `WF_AddWorkFlowLevelOne @CompNo, 46, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1` and updates `IsVoid = 1` on target transaction.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[TransactionsHeaders]]
- [[Receipts]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| TrTypeID | smallint | YES |  |  |  |
| TrTypeYear | smallint | YES |  |  |  |
| TrTypeNo | int | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[RequestToVoidTransaction_Insert]]

**Writes (3):**
- [[RequestToVoidTransaction_Insert]]
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
