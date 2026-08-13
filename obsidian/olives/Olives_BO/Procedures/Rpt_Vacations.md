---
type: procedure
database: Olives_BO
name: Rpt_Vacations
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[SalesPersons]]
  - [[Vacations]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Vacations


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, Vacations. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2024-12-10'
- @ToDate smalldatetime='2024-12-10'
- @FromSalesman int=1
- @ToSalesman int=3003
## Tables Read
- [[SalesPersons]]
- [[Vacations]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]
- [[Vacations]]

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
