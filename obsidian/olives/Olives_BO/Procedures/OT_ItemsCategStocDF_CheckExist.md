---
type: procedure
database: Olives_BO
name: OT_ItemsCategStocDF_CheckExist
schema: dbo
tags: [#maintenance]
reads_from:
  - ItemsCategStockDetails
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OT_ItemsCategStocDF_CheckExist

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TransactionTypeID smallint
- @TransactionYear int
- @TransactionNo int
- @CategCode nvarchar(50)
- @UnitID nvarchar(50)
- @Quantity float
- @Notes nvarchar(300)
- @ErrNo smallint OUTPUT
- @Exist smallint OUTPUT
## Tables Read
- [[ItemsCategStockDetails]]
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
