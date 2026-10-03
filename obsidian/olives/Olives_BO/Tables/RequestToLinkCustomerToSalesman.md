---
type: table
database: Olives_BO
name: RequestToLinkCustomerToSalesman
schema: dbo
tags: [#backoffice, #customer, #sales, #workflow]
foreign_keys:
referenced_by:
  - [[OT_ImportRequestToLinkCustomerToSalesman]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToLinkCustomerToSalesman

## Business Purpose
Stores approval requests submitted when a salesman requests linking an existing customer to their route or sales portfolio. Corresponds to workflow `FunctionID = 36` ("Request To Link Customer To Salesman"). Captures salesman, customer, visit time, timestamp, GPS coordinates, and `IsAproved`. Queryable via `t.RequestToLinkCustomerToSalesman`.

## Chatbot semantics
(Query `t.RequestToLinkCustomerToSalesman` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات ربط زبون بمندوب | `SalesPersonNo`, `CustomerNo`, `TrDate` | Direct filter | Customer portfolio assignment requests |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 36 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 customer link request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Salesman requests linking on tablet → `OT_ImportRequestToLinkCustomerToSalesman` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 36, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1` and creates the `CustomersFinancialDetails` link.

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
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| VisitTime | smalldatetime | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_ImportRequestToLinkCustomerToSalesman]]

**Writes (3):**
- [[OT_ImportRequestToLinkCustomerToSalesman]]
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
