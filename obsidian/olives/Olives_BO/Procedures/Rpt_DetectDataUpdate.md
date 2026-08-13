---
type: procedure
database: Olives_BO
name: Rpt_DetectDataUpdate
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - 1
  - [[ClientsActive]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DetectDataUpdate


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 1, ClientsActive, LogActionTransaction, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = null
- @FromDate SmallDateTime = '2021-12-01'
- @ToDate SmallDateTime = '2022-12-01'
- @FromSalesperson int = null
- @ToSalesperson int = null
## Tables Read
- 1
- [[ClientsActive]]
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 1
- [[ClientsActive]]
- [[LogActionTransaction]]
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
