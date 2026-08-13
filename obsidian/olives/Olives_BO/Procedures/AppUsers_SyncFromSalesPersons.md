---
type: procedure
database: Olives_BO
name: AppUsers_SyncFromSalesPersons
schema: dbo
tags: [#backoffice]
reads_from:
  - SalesPersons
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# AppUsers_SyncFromSalesPersons

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @DefaultTempPassword nvarchar(200)
## Tables Read
- [[SalesPersons]]
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
