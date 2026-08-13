---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesmanCombine_Sukhtian
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - Fun_ConvArrayToTable
  - [[LogActionTransaction]]
writes_to:
called_by:
  - Rpt_RouteSummaryBySalesman_Sukhtian_Draft
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteSummaryBySalesmanCombine_Sukhtian


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Fun_ConvArrayToTable, LogActionTransaction. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2025-04-06 00:00:00'
- @ToDate smalldatetime= '2025-04-06 00:00:00'
- @SalesmanArray VARCHAR(MAX) = N'262,'
- @UserID nvarchar(50) = N'efarraj'
- @WithTax bit = 1
## Tables Read
- [[ClientsActive]]
- Fun_ConvArrayToTable
- [[LogActionTransaction]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- Rpt_RouteSummaryBySalesman_Sukhtian_Draft
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- Fun_ConvArrayToTable
- [[LogActionTransaction]]

**Tables Written**
_None_

**Callers**
- Rpt_RouteSummaryBySalesman_Sukhtian_Draft

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
