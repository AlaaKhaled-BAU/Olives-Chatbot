---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesmanCombineForEFF
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[LogActionTransaction]]
  - MaxTime
  - Mintime
  - MonthDays_CTE
  - SV_LV_TV
  - VisitLength
  - gen
  - [[SalesPersons]]
writes_to:
  - SV_LV_TV
called_by:
  - Rpt_RouteSummaryBySalesmanFF
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteSummaryBySalesmanCombineForEFF


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, LogActionTransaction, MaxTime, Mintime, MonthDays_CTE, SV_LV_TV, VisitLength, gen, SalesPersons. Writes SV_LV_TV. Invoked by 1 procedure(s). Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @Month int = null
- @year int= null
- @FromSalesman int
- @ToSalesman int
- @WithTax bit = 1
## Tables Read
- [[ClientsActive]]
- [[LogActionTransaction]]
- MaxTime
- Mintime
- MonthDays_CTE
- SV_LV_TV
- VisitLength
- gen
- [[SalesPersons]]
## Tables Written
- SV_LV_TV
## Callers
- [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
## Callees
- Rpt_RouteSummaryBySalesmanFF
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[LogActionTransaction]]
- MaxTime
- Mintime
- MonthDays_CTE
- SV_LV_TV
- VisitLength
- gen
- [[salespersons]]

**Tables Written**
- SV_LV_TV

**Callers**
- Rpt_RouteSummaryBySalesmanFF

**Callees**
- [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
