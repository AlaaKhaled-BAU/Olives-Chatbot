---
type: procedure
database: Olives_BO
name: Pro_ImportData_Order
schema: dbo
tags: [#backoffice]
reads_from:
  - TransactionsSerials
writes_to:
  - OrdersDetails
  - OrdersHeaders
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_ImportData_Order

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); writes 2. See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @SalespersonID int
- @CustomerID bigint
- @CmdType nvarchar(50)
- @Tbl importdata_order
## Tables Read
- [[TransactionsSerials]]
## Tables Written
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
