---
type: procedure
database: Olives_BO
name: Pro_JsonDataLog
schema: dbo
tags: [#backoffice]
reads_from:
writes_to:
  - JSONDataLog
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Pro_JsonDataLog

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1. See sections below for the full dependency map.
## Parameters
- @Cmd nvarchar(100)
- @CompanyID smallint
- @TabSysID nvarchar(100)
- @SalespersonID int
- @JSONData nvarchar(MAX)
- @ErrNo smallint OUTPUT
## Tables Read
_None_
## Tables Written
- [[JSONDataLog]]
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
