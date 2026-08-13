---
type: procedure
database: Olives_BO
name: Pro_ImportPriceListData
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[PriceListDetails]]
  - [[PriceLists]]
writes_to:
  - [[CustomersFinancialDetails]]
  - [[PriceListDetails]]
  - [[PriceLists]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ImportPriceListData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, PriceListDetails, PriceLists. Writes CustomersFinancialDetails, PriceListDetails, PriceLists. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @PriceListTbl ImportData_PriceLists readonly
- @PriceListDetailTbl ImportData_PriceListDetails readonly
- @CustomersPricelistTbl ImportData_CustomersPricelist readonly
- @ItemCode NVARCHAR(100) = null
- @UnitID  NVARCHAR(50) = null
- @PriceListID int = null
- @Price  Decimal(18,2) = null
- @CmdType NVARCHAR(50) = null
## Tables Read
- [[CustomersFinancialDetails]]
- [[PriceListDetails]]
- [[PriceLists]]
## Tables Written
- [[CustomersFinancialDetails]]
- [[PriceListDetails]]
- [[PriceLists]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- [[PriceListDetails]]
- [[PriceLists]]

**Tables Written**
- [[CustomersFinancialDetails]]
- [[PriceListDetails]]
- [[PriceLists]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
