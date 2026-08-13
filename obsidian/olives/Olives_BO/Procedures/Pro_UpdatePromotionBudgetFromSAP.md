---
type: procedure
database: Olives_BO
name: Pro_UpdatePromotionBudgetFromSAP
schema: dbo
tags: [#integration]
reads_from:
  - Customers
  - CustomersPromotionsGroupsLink
  - CustomersTypes
  - PromotionsCondUnCodInput
  - PromotionsCustomersGroupsLink
  - PromotionsHeaders
writes_to:
  - PromotionBudget
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_UpdatePromotionBudgetFromSAP

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 6 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID int
## Tables Read
- [[Customers]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
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
