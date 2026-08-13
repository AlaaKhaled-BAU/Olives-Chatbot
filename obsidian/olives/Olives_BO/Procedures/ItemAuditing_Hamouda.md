---
type: procedure
database: Olives_BO
name: ItemAuditing_Hamouda
schema: dbo
tags: [#backoffice]
reads_from:
  - ERPStores
  - ItemsStoreByUser
  - SalesPersons
  - TransfersOrdersDetails
  - TransfersOrdersHeaders
writes_to:
  - Items
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# ItemAuditing_Hamouda

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @UserID nvarchar(50)
- @FromDate date
- @SalesPersonID int
- @Supervisor int
## Tables Read
- [[ERPStores]]
- [[ItemsStoreByUser]]
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
- [[Items]]
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
