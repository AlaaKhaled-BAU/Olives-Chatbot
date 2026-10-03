---
type: table
database: Olives_BO
name: RequestToExceedCustomerCreditLimit
schema: dbo
tags: [#backoffice, #billing, #customer, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToExceedCustomerCreditLimit]]
  - [[Rpt_ExceededLimit]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToExceedCustomerCreditLimit

## Business Purpose
Stores mobile requests submitted by salesmen when creating an invoice that exceeds the customer's defined credit limit. Corresponds to workflow `FunctionID = 2`. Captures the financial snapshot at request time: requested `InvoiceAmount`, current `CustomerCreditLimit`, current `CustomerBanalce` (balance), `CustomerChqBanalce` (uncleared checks), and the `ExceedAmount`. Queryable as `t.RequestToExceedCustomerCreditLimit`.

## Chatbot semantics
(Query `t.RequestToExceedCustomerCreditLimit` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات تجاوز سقف الائتمان | `CustomerNo`, `SalesPersonNo`, `InvoiceAmount` | e.g. `CustomerNo = ...` | Lists credit limit requests |
| حالة الموافقة في جدول الطلب | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending/rejected) | Direct flag stamped upon approval |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 2 AND TRY_CAST(m.Ref1 AS numeric) = r.AutoID AND m.CompanyID = r.CompanyID` | Enables checking approver levels and notes |
| قيمة التجاوز | `ExceedAmount`, `InvoiceAmount` | Numeric fields | Excess over credit ceiling |
| رصيد العميل وسقف الائتمان وقت الطلب | `CustomerCreditLimit`, `CustomerBanalce` | Snapshot values | Preserved historical amounts |

**Do not confuse with:**
- `RequestToExceedCustomerCreditLimitInOrder`: Workflow `FunctionID = 15` (credit limit exception during pre-sales order, not invoice).
- `RequestToIncreaseCustomerCreditlimit`: Permanent credit limit change requests (`FunctionID = 39`), whereas this table is for a single transaction exception.

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 credit exception request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Tablet raises credit exception → `OT_ImportRequestToExceedCustomerCreditLimit` imports row into this table (`IsAproved = 0`) → executes `WF_AddWorkFlowLevelOne @CompNo, 2, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` updates `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[Customers]]
- [[CustomersFinancialDetails]]
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
| Notes | nvarchar | YES |  |  |  |
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

**Reads (5):**
- [[OT_ImportRequestToExceedCustomerCreditLimit]]
- [[Rpt_ExceededLimit]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevelOne]]

**Writes (3):**
- [[OT_ImportRequestToExceedCustomerCreditLimit]]
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
