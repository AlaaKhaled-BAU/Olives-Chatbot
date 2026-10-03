---
type: table
database: Olives_BO
name: RequestToAddNewCustomer
schema: dbo
tags: [#backoffice, #customer, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToAddNewCustomer]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToAddNewCustomer

## Business Purpose
Stores approval requests submitted when a salesman in the field registers a new prospective customer and requests official account creation. Corresponds to workflow `FunctionID = 21` ("Request To Add New Customer"). Captures customer data, salesman, timestamp, notes, GPS coordinates, and `IsAproved`. Queryable via `t.RequestToAddNewCustomer`.

## Chatbot semantics
(Query `t.RequestToAddNewCustomer` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات إضافة زبون جديد من الميدان | `SalesPersonNo`, `TrDate`, `Notes` | Direct filter | Lists new customer onboarding requests |
| حالة الموافقة على إنشاء الحساب | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 21 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |
| موقع تسجيل العميل | `Latitude`, `Longitude` | GPS strings | Audit location where salesman created customer |

**Do not confuse with:**
- `Customers`: The official approved customer master table.
- `ProspectiveCustomers` / `Add_Customer`: Temporary staging tables during import.

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 new customer request)
- **Tenant key**: `CompanyID`
- **Conventions**: `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Salesman adds customer on tablet → `OT_ImportRequestToAddNewCustomer` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 21, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1` and creates the real `Customers` master record.

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
| Notes | nvarchar | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_ImportRequestToAddNewCustomer]]

**Writes (3):**
- [[OT_ImportRequestToAddNewCustomer]]
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
