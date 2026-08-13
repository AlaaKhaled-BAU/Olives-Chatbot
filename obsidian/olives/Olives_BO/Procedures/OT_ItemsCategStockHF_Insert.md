---
type: procedure
database: Olives_BO
name: OT_ItemsCategStockHF_Insert
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
  - ItemsCategStockHeader
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OT_ItemsCategStockHF_Insert

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TransactionTypeID smallint
- @TransactionYear smallint
- @TransactionNo int
- @TransactionDate smalldatetime
- @SalesPersonID int
- @CustomerID bigint
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(200)
- @PostedToERP bit
- @RouteID int
- @TrDateTime smalldatetime
- @ErrNo smallint OUTPUT
## Tables Read
_None_
## Tables Written
- [[ItemsCategStockHeader]]
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
