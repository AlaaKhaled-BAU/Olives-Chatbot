---
type: procedure
database: Olives_BO
name: ImportAddPromotionstData
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# ImportAddPromotionstData

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — standalone procedure. See sections below for the full dependency map.
## Parameters
- @Tbl_Excel_Data addpromotiontype
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

Run when importing data from tablets/external files into the back-office (batch or scheduled import).

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
