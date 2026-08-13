---
type: procedure
database: Olives_BO
name: Pro_EfawateercomApi
schema: dbo
tags: [#integration]
reads_from:
writes_to:
  - EfawateercomPayment
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Pro_EfawateercomApi

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1. See sections below for the full dependency map.
## Parameters
- @GUID uniqueidentifier
- @TypeID int
- @CustID bigint
- @TimeStp datetime
- @DueAmount float
- @JsonReq nvarchar(MAX)
- @JsonRes nvarchar(MAX)
- @cmdType nvarchar(200)
## Tables Read
_None_
## Tables Written
- [[EfawateercomPayment]]
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
