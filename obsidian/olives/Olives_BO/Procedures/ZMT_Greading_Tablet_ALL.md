---
type: procedure
database: Olives_BO
name: ZMT_Greading_Tablet_ALL
schema: dbo
tags: [#backoffice]
reads_from:
  - Items
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# ZMT_Greading_Tablet_ALL

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
- @FromDate nvarchar(200)
- @ToDate nvarchar(200)
- @Cmd varchar(20)
## Tables Read
- [[Items]]
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
