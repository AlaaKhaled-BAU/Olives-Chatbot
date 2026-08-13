---
type: procedure
database: Olives_BO
name: Rpt_SalesmanDaySummaryCombine
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_ConvArrayToTable
  - [[LogActionTransaction]]
writes_to:
called_by:
  - [[OT_FixActionLog]]
  - [[Rpt_SalesmanDaySummary]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanDaySummaryCombine


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_ConvArrayToTable, LogActionTransaction. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @SalesmanArray VARCHAR(MAX)
- @UserID nvarchar(50) = null
## Tables Read
- Fun_ConvArrayToTable
- [[LogActionTransaction]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[OT_FixActionLog]]
- [[Rpt_SalesmanDaySummary]]
## Impact / Dependencies

**Tables Read**
- Fun_ConvArrayToTable
- [[LogActionTransaction]]

**Tables Written**
_None_

**Callers**
- [[OT_FixActionLog]]
- [[Rpt_SalesmanDaySummary]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
