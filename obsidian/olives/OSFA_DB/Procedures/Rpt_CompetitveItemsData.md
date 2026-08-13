---
type: procedure
database: OSFA_DB
name: Rpt_CompetitveItemsData
schema: dbo
tags: [#reporting]
reads_from:
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Rpt_CompetitveItemsData

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in OSFA_DB — standalone procedure. See sections below for the full dependency map.
## Parameters
- @FromSalesPerson int
- @ToSalesPerson int
- @FromDate date
- @ToDate date
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
References tables in **Olives_BO** (qualified as `Olives_BO.dbo.*`):
- [[Olives_BO/Tables/CompetitveItemsDataHF|CompetitveItemsDataHF]]
- [[Olives_BO/Tables/SalesPersons|SalesPersons]]
## Callers
_None_
## Callees
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
