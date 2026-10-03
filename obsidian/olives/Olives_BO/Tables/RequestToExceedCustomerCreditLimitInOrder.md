---
type: table
database: Olives_BO
name: RequestToExceedCustomerCreditLimitInOrder
schema: dbo
tags: [#backoffice, #billing, #customer, #order, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
  - [[Rpt_ExceededLimit]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_WFFunctionsLog]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToExceedCustomerCreditLimitInOrder

## Business Purpose
Stores approval requests submitted when a salesman takes a sales order for a customer that causes their balance to exceed their defined credit limit. Corresponds to workflow `FunctionID = 15` ("Request To Exceed Customer Credit Limit In Order"). Captures order amount, credit limit, customer balance, check balance, customer, salesman, timestamp, and `IsAproved`. Queryable via `t.RequestToExceedCustomerCreditLimitInOrder`.

## Chatbot semantics
(Query `t.RequestToExceedCustomerCreditLimitInOrder` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات تجاوز حد الائتمان في الطلبيات | `CustomerNo`, `SalesPersonNo`, `TrDate` | Direct filter | Order credit limit exception requests |
| قيمة الطلبية ورصيد العميل | `OrderAmount`, `CustomerBanalce` | Numeric values | Financial snapshot |
| سقف الائتمان ومبلغ التجاوز | `CustomerCreditLimit`, `ExceedAmount` | Numeric values | Requested excess |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 15 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

**Do not confuse with:**
- `RequestToExceedCustomerCreditLimit`: Credit limit exception on *invoices* (`FunctionID = 2`).

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 order credit request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Tablet salesman takes order exceeding credit limit → `OT_ImportRequestToExceedCustomerCreditLimitInOrder` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 15, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[OrdersHeaders]]
- [[RequestToExceedCustomerCreditLimit]]
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

**Reads (5):**
- [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
- [[Rpt_ExceededLimit]]
- [[Rpt_MasterOrders]]
- [[Rpt_WFFunctionsLog]]
- [[Rpt_WorkFlowAnalysis]]

**Writes (3):**
- [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
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
