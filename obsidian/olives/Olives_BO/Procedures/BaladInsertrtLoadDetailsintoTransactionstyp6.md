---
type: procedure
database: Olives_BO
name: BaladInsertrtLoadDetailsintoTransactionstyp6
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
  - [[TransactionsDetails]]
writes_to:
  - [[TransactionsDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# BaladInsertrtLoadDetailsintoTransactionstyp6


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads TransfersOrdersDetails, TransfersOrdersHeaders, TransactionsDetails. Writes TransactionsDetails. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @OrderYear int
- @OrderNo int
- @VouType int
- @ItemCode nvarchar(100)
- @UnitID nvarchar(100)
## Tables Read
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- [[TransactionsDetails]]
## Tables Written
- [[TransactionsDetails]]
## Callers
- [[Pro_TransfersOrdersDetails]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- [[transactionsdetails]]

**Tables Written**
- [[transactionsdetails]]

**Callers**
_None_

**Callees**
- [[Pro_TransfersOrdersDetails]]


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
