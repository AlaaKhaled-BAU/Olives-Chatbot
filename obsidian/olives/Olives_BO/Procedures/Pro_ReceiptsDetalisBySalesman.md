---
type: procedure
database: Olives_BO
name: Pro_ReceiptsDetalisBySalesman
schema: dbo
tags: [#backoffice]
reads_from:
  - Customers
  - Excel
  - Receipts
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_ReceiptsDetalisBySalesman

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate datetime
- @ToDate datetime
- @SalesmanID int
- @cmdType nvarchar(200)
## Tables Read
- [[Customers]]
- [[Excel]]
- [[Receipts]]
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
