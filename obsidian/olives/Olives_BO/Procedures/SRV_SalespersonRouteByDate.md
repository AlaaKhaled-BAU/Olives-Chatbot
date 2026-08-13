---
type: procedure
database: Olives_BO
name: SRV_SalespersonRouteByDate
schema: dbo
tags: [#backoffice]
reads_from:
  - Customers
  - SalesPersons
writes_to:
  - SalespersonCustomersVisitsByDate
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# SRV_SalespersonRouteByDate

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @PositionID int
- @RouteID int
- @CustomerID bigint
- @Date date
- @Notes nvarchar(MAX)
- @IsApproved bit
- @CmdType varchar(50)
## Tables Read
- [[Customers]]
- [[SalesPersons]]
## Tables Written
- [[SalespersonCustomersVisitsByDate]]
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
