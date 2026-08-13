---
type: procedure
database: Olives_BO
name: SalesmenRoutesummery_Range_forExcel
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[LogActionTransaction]]
writes_to:
called_by:
  - [[OT_FixActionLog]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesmenRoutesummery_Range_forExcel


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LogActionTransaction. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2022-04-18'
- @ToDate smalldatetime= '2022-04-19'
- @fromSalespersonID int =1
- @ToSalespersonID int =50
- @WithTax bit = 1
## Tables Read
- [[LogActionTransaction]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[OT_FixActionLog]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
## Impact / Dependencies

**Tables Read**
- [[LogActionTransaction]]

**Tables Written**
_None_

**Callers**
- [[OT_FixActionLog]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
