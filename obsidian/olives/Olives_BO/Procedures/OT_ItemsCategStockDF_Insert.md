---
type: procedure
database: Olives_BO
name: OT_ItemsCategStockDF_Insert
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
  - ItemsCategStockDetails
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OT_ItemsCategStockDF_Insert

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TransactionTypeID smallint
- @TransactionYear int
- @TransactionNo int
- @CategCode nvarchar(200)
- @UnitID nvarchar(200)
- @Quantity float
- @Notes nvarchar(300)
- @ErrNo smallint OUTPUT
## Tables Read
_None_
## Tables Written
- [[ItemsCategStockDetails]]
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
