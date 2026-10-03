---
type: table
database: Olives_BO
name: RequestToExceedCustomerInvoiceDueDays
schema: dbo
tags: [#backoffice, #billing, #customer, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToExceedCustomerInvoiceDueDays]]
  - [[Rpt_ReturnOrdersMaster]]
  - [[Rpt_WFFunctionsLog]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToExceedCustomerInvoiceDueDays

## Business Purpose
Stores approval requests submitted when a salesman attempts to issue an invoice to a customer who has past-due invoices exceeding their permitted credit due days (grace period). Corresponds to workflow `FunctionID = 4` ("Request To Exceed Customer Invoice Due Days In Invoice"). Captures invoice amount, customer balance, due days, salesman, customer, timestamp, and `IsAproved`. Queryable via `t.RequestToExceedCustomerInvoiceDueDays`.

## Chatbot semantics
(Query `t.RequestToExceedCustomerInvoiceDueDays` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات تجاوز فترة استحقاق الفواتير | `CustomerNo`, `SalesPersonNo`, `TrDate` | Direct filter | Aging/overdue invoice exceptions |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| قيمة الفاتورة ورصيد العميل | `InvoiceAmount`, `CustomerBanalce` | Numeric values | Snapshot of balance and invoice value |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 4 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

**Do not confuse with:**
- `RequestToExceedCustomerInvoiceDueDaysInOrder`: Workflow `FunctionID = 12` (due days exception during pre-sales *order*, not invoice).
- `RequestToExceedCustomerCreditLimit`: Credit ceiling exception (`FunctionID = 2`).

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 due days exception request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Tablet detects overdue invoices for customer → `OT_ImportRequestToExceedCustomerInvoiceDueDays` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 4, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
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
| TabletSysID | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_ImportRequestToExceedCustomerInvoiceDueDays]]
- [[Rpt_ReturnOrdersMaster]]
- [[Rpt_WFFunctionsLog]]
- [[WF_AddWorkFlowLevelOne]]

**Writes (3):**
- [[OT_ImportRequestToExceedCustomerInvoiceDueDays]]
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
