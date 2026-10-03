---
type: table
database: Olives_BO
name: RequestToAllowTakeChecksFromCustomer
schema: dbo
tags: [#backoffice, #customer, #workflow]
foreign_keys:
referenced_by:
  - [[OT_ImportRequestToAllowTakeChecksFromCustomer]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToAllowTakeChecksFromCustomer

## Business Purpose
Stores approval requests submitted when a salesman attempts to receive a check payment from a customer who is restricted to cash-only transactions (`AllowChqs = 0` in `CustomersFinancialDetails`). Corresponds to workflow `FunctionID = 27` ("Request To Allow Take Checks From Customer"). Captures receipt amount, customer, salesman, timestamp, notes, and `IsAproved`. Queryable via `t.RequestToAllowTakeChecksFromCustomer`.

## Chatbot semantics
(Query `t.RequestToAllowTakeChecksFromCustomer` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات السماح باستلام شيكات من عميل | `CustomerNo`, `SalesPersonNo`, `TrDate` | Direct filter | Overrides cash-only restriction |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| قيمة السند / الدفعة | `ReceiptAmount` | Numeric | Check collection amount requested |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 27 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 check permission request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Tablet blocks check entry for cash-only customer → raises exception → `OT_ImportRequestToAllowTakeChecksFromCustomer` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 27, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[CustomersFinancialDetails]]
- [[Receipts]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
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
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ImportRequestToAllowTakeChecksFromCustomer]]
- [[Rpt_WorkFlowFunctions]]

**Writes (3):**
- [[OT_ImportRequestToAllowTakeChecksFromCustomer]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
