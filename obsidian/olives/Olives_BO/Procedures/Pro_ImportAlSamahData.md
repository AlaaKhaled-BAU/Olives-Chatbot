---
type: procedure
database: Olives_BO
name: Pro_ImportAlSamahData
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
  - [[Customers]]
  - [[Items]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ImportAlSamahData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, TransactionsDetails, TransactionsHeaders. Writes Customers, Items, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @CmdType NVARCHAR(50) = NULL
- @CustomersTbl ImportCustomersBalanceData readonly
- @ItemsTbl ImportItemsQtyInAllStoresData readonly
- @ImportData_SalesmanSales ImportData_SalesmanSales readonly
## Tables Read
- [[Customers]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- [[Customers]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
- [[Customers]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
