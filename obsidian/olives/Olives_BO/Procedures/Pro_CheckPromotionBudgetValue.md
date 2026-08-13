---
type: procedure
database: Olives_BO
name: Pro_CheckPromotionBudgetValue
schema: dbo
tags: [#backoffice]
reads_from:
  - Customers
  - CustomersTypes
  - OrdersDetails
  - OrdersHeaders
  - PromotionBudget
  - PromotionsCondUnCodInput
  - PromotionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_CheckPromotionBudgetValue

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @OrderYear int
- @OrderNo int
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PromotionBudget]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsHeaders]]
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
