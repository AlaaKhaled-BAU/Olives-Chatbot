---
type: table
database: Olives_BO
name: RequestToVisitCustomerNotInRoute
schema: dbo
tags: [#backoffice, #customer, #gps, #sales, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToVisitCustomerNotInRoute]]
  - [[RPT_RoutesummarybysalesmancompineExcel2]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WFCustomersVisitsCounts]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToVisitCustomerNotInRoute

## Business Purpose
Stores approval requests submitted when a salesman attempts to visit or sell to a customer who is not assigned to their active daily journey plan / route schedule. Corresponds to workflow `FunctionID = 5` ("Request To Sales Customer Not In Route"). Captures the salesman, customer, timestamp, GPS coordinates, and approval status. Queryable via `t.RequestToVisitCustomerNotInRoute`.

## Chatbot semantics
(Query `t.RequestToVisitCustomerNotInRoute` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات زيارة / بيع خارج المسار | `SalesPersonNo`, `CustomerNo`, `TrDate` | Direct filter | Lists off-route approval requests |
| حالة الموافقة على الزيارة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending/rejected) | Direct approval indicator |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 5 AND TRY_CAST(m.Ref1 AS numeric) = r.AutoID AND m.CompanyID = r.CompanyID` | View supervisor decision levels & notes |
| موقع تقديم الطلب | `Latitude`, `Longitude` | GPS strings | Audit coordinates where salesman submitted request |

**Do not confuse with:**
- `SalesPersonsRoutes`: The planned static route schedule for salesmen.
- `LogActionTransaction`: Field activity log where actual customer visits are recorded (`ActionID = N'0'`).
- `RequestSalesmanWillNotVisit`: The reverse request — when a salesman requests *skipping* a customer who *is* on their route (`FunctionID = 23`).

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 off-route request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Tablet detects customer is outside today's route → raises request → `OT_ImportRequestToVisitCustomerNotInRoute` inserts into this table (`IsAproved = 0`) → executes `WF_AddWorkFlowLevelOne @CompNo, 5, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When approved, `WF_AddWorkFlowLevels` sets `IsAproved = 1` and tablet allows check-in.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[SalesPersonsRoutes]]
- [[RequestSalesmanWillNotVisit]]
- [[LogActionTransaction]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (7):**
- [[OT_ImportRequestToVisitCustomerNotInRoute]]
- [[RPT_RoutesummarybysalesmancompineExcel2]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WFCustomersVisitsCounts]]
- [[Rpt_WorkFlowAnalysis]]
- [[WF_AddWorkFlowLevelOne]]

**Writes (3):**
- [[OT_ImportRequestToVisitCustomerNotInRoute]]
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
