---
type: procedure
database: Olives_BO
name: Technical_CreateRouteBasedonReference1&ManualrouteName
schema: dbo
tags: [#maintenance]
reads_from:
  - BusinessUnits
  - Customers
  - Excel
  - Excel2
writes_to:
  - CustomersFinancialDetails
  - Positions
  - RoutesInformation
  - SalesPersonsRoutes
  - Technical_CFD_temp
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Technical_CreateRouteBasedonReference1&ManualrouteName

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); writes 5; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
- @DeleteStatus bit
## Tables Read
- [[BusinessUnits]]
- [[Customers]]
- [[Excel]]
- [[Excel2]]
## Tables Written
- [[CustomersFinancialDetails]]
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
- [[Technical_CFD_temp]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Trim`
## When to Run

Maintenance/one-off fix: run under DBA supervision; verify row counts before and after.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
