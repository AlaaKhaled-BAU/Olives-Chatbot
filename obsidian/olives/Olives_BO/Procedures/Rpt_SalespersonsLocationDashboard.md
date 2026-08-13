---
type: procedure
database: Olives_BO
name: Rpt_SalespersonsLocationDashboard
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - Customers
  - CustomersGPSLocations
  - SalesPersons
  - SalespersonsGPSTracking
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_SalespersonsLocationDashboard

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesmanNo int
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersGPSLocations]]
- [[SalesPersons]]
- [[SalespersonsGPSTracking]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_ActionLog|OT_ActionLog]]
## Callers
_None_
## Callees
- `Fun_GetSalesmanTreeByID`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
