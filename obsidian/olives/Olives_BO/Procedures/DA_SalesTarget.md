---
type: procedure
database: Olives_BO
name: DA_SalesTarget
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersMonthlyCollectionTarget]]
  - Fun_GetSalesmanTreeByID
  - LUXintegratopn
  - [[LogActionTransaction]]
  - [[Receipts]]
  - [[SalesPersonCollectionsTargets]]
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# DA_SalesTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, CustomersMonthlyCollectionTarget, Fun_GetSalesmanTreeByID, LUXintegratopn, LogActionTransaction, Receipts, SalesPersonCollectionsTargets, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, TransactionsDetails, TransactionsHeaders, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @Year int
- @Month int
- @UserID nvarchar(50) =null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersMonthlyCollectionTarget]]
- Fun_GetSalesmanTreeByID
- LUXintegratopn
- [[LogActionTransaction]]
- [[Receipts]]
- [[SalesPersonCollectionsTargets]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersMonthlyCollectionTarget]]
- Fun_GetSalesmanTreeByID
- LUXintegratopn
- [[LogActionTransaction]]
- [[Receipts]]
- [[SalesPersonCollectionsTargets]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
