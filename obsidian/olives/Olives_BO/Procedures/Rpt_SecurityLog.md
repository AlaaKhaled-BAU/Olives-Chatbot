---
type: procedure
database: Olives_BO
name: Rpt_SecurityLog
schema: dbo
tags: [#auth, #backoffice, #log, #reporting]
reads_from:
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - [[Users]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SecurityLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LogActionTransaction, SalesPersons, Users, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2014-01-01'
- @ToDate smalldatetime='2019-01-01'
- @UserID nvarchar(50)=NULL
- @RptType VARCHAR(500)='ByUser'--'BySalesman'
## Tables Read
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[Users]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[Users]]
- dbo

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
