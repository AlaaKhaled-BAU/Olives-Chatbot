---
type: procedure
database: Olives_BO
name: Rpt_TowerTargetsCombine
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_ConvArrayToTable
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TowerTargetsCombine


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_ConvArrayToTable, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @SalesmanArray VARCHAR(MAX) = '6,26,35,61,'
- @FromDate smalldatetime='2021-04-01'
- @ToDate smalldatetime  ='2021-04-30'
## Tables Read
- Fun_ConvArrayToTable
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_ConvArrayToTable
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
