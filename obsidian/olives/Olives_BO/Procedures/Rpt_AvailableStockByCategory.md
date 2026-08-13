---
type: procedure
database: Olives_BO
name: Rpt_AvailableStockByCategory
schema: dbo
tags: [#reporting]
reads_from:
  - Items
  - ItemsCategories
  - ItemsUnits
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_AvailableStockByCategory

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @CategoryCode int
## Tables Read
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_StoreItemsQty|OT_StoreItemsQty]]
## Callers
_None_
## Callees
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
