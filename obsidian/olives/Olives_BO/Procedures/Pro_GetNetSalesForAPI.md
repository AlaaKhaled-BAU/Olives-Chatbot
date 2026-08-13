---
type: procedure
database: Olives_BO
name: Pro_GetNetSalesForAPI
schema: dbo
tags: [#backoffice]
reads_from:
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_GetNetSalesForAPI

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate datetime
- @ToDate datetime
- @SalesPersonID nvarchar(MAX)
## Tables Read
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
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
