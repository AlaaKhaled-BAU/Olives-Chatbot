---
type: procedure
database: Olives_BO
name: Pro_TransfersOrdersQtyValidation
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - 168
  - [[PriceListDetails]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - TrMaster
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
  - [[SalesPersonItemsBalance]]
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TransfersOrdersQtyValidation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 168, PriceListDetails, SalesPersonItemsBalance, SalesPersons, TrMaster, TransactionsDetails, TransactionsHeaders, TransfersOrdersDetails, TransfersOrdersHeaders. Writes SalesPersonItemsBalance, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @OrderYear smallint=null
- @OrderNo bigint=null
- @VouType int=null
## Tables Read
- 168
- [[PriceListDetails]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- TrMaster
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
- [[SalesPersonItemsBalance]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 168
- [[PriceListDetails]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- TrMaster
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

**Tables Written**
- [[SalesPersonItemsBalance]]
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
