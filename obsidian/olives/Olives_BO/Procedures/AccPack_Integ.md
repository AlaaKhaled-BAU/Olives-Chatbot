---
type: procedure
database: Olives_BO
name: AccPack_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[PaymentsTypes]]
  - [[PriceListDetails]]
  - [[PriceLists]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AccPack_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesPersons. Writes Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, PaymentsTypes, PriceListDetails, PriceLists. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[PaymentsTypes]]
- [[PriceListDetails]]
- [[PriceLists]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]

**Tables Written**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[PaymentsTypes]]
- [[PriceListDetails]]
- [[PriceLists]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
