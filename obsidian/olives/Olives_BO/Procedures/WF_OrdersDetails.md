---
type: procedure
database: Olives_BO
name: WF_OrdersDetails
schema: dbo
tags: [#workflow]
reads_from:
writes_to:
  - OrdersDetails
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# WF_OrdersDetails

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @OrderYear int
- @OrderNo nvarchar(200)
- @ItemCode nvarchar(200)
- @UnitID nvarchar(200)
- @SysCodeTypeID nvarchar(200)
- @cmdType nvarchar(200)
## Tables Read
_None_
## Tables Written
- [[OrdersDetails]]
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
