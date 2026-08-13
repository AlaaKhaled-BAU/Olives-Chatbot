---
type: procedure
database: Olives_BO
name: Pro_ItemsStoreByUser
schema: dbo
tags: [#backoffice]
reads_from:
  - ERPStores
  - ItemsStoreByUser
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_ItemsStoreByUser

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @UserID nvarchar(50)
- @StoreNo int
- @ItemCode nvarchar(50)
- @cmdType nvarchar(50)
## Tables Read
- [[ERPStores]]
- [[ItemsStoreByUser]]
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
