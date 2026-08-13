---
type: procedure
database: Olives_BO
name: Pro_ImportPromotionBudgetData
schema: dbo
tags: [#backoffice]
reads_from:
writes_to:
  - PromotionBudget
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Pro_ImportPromotionBudgetData

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1. See sections below for the full dependency map.
## Parameters
- @Tbl_Excel_Data importpromotionbudgetdata
- @CompNo int
## Tables Read
_None_
## Tables Written
- [[PromotionBudget]]
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
