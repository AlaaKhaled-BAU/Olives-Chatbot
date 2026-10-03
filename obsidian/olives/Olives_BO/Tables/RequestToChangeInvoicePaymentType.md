---
type: table
database: Olives_BO
name: RequestToChangeInvoicePaymentType
schema: dbo
tags: [#backoffice, #billing, #legal, #reference, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToChangeInvoicePaymentType]]
  - [[Rpt_WFFunctionsLog]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToChangeInvoicePaymentType

## Business Purpose
Stores approval requests submitted when a salesman requests changing an invoice payment type (e.g., from cash to credit or vice versa) during invoicing on a mobile device. Corresponds to workflow `FunctionID = 1` ("Request To Change Invoice Payment Type"). Captures `PaymentTypeID`, `OldPaymentTypeID`, `InvoiceAmount`, customer, salesman, timestamp, and `IsAproved`. Queryable via `t.RequestToChangeInvoicePaymentType`.

## Chatbot semantics
(Query `t.RequestToChangeInvoicePaymentType` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات تغيير طريقة دفع الفاتورة | `CustomerNo`, `SalesPersonNo`, `TrDate` | Direct filter | Lists payment type change requests |
| طريقة الدفع المطلوبة والسابقة | `PaymentTypeID`, `OldPaymentTypeID` | Links to `PaymentsTypes` | e.g. converting cash sale to credit sale |
| قيمة الفاتورة | `InvoiceAmount` | Numeric | Invoice financial value |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 1 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 payment type change request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID), `PaymentTypeID` → [[PaymentsTypes]](ID)

## Pipeline (how rows get here)
Salesman requests payment term switch on tablet → `OT_ImportRequestToChangeInvoicePaymentType` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 1, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[PaymentsTypes]]
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
| InvDueDays | int | YES |  |  |  |
| IsCanceled | bit | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_ImportRequestToChangeInvoicePaymentType]]
- [[Rpt_WFFunctionsLog]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevelOne]]

**Writes (3):**
- [[OT_ImportRequestToChangeInvoicePaymentType]]
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
