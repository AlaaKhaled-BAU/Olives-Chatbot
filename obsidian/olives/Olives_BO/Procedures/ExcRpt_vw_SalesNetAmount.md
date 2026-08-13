---
type: procedure
database: Olives_BO
name: ExcRpt_vw_SalesNetAmount
schema: dbo
tags: [#backoffice]
reads_from:
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# ExcRpt_vw_SalesNetAmount

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — standalone procedure. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
