---
type: procedure
database: Olives_BO
name: AccPack_Integ_LuxuryItems
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersMonthlyCollectionTarget]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriceExceptions]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersMonthlyCollectionTarget]]
  - [[CustomersPaidTransList]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriceExceptions]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersonCollectionsTargets]]
  - [[SalesPersons]]
  - SalesVoucher
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AccPack_Integ_LuxuryItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersMonthlyCollectionTarget, CustomersPaidTransList, CustomersTypes, Items, ItemsCategories, ItemsPriceExceptions, ItemsUnits, ItemsUnitsDetails, Locations, PaymentsTypes, Positions, PriceListDetails. Writes Customers, CustomersFinancialDetails, CustomersMonthlyCollectionTarget, CustomersPaidTransList, Items, ItemsCategories, ItemsPriceExceptions, ItemsUnits, ItemsUnitsDetails, Positions, PriceListDetails, PriceLists, SalesPersonCollectionsTargets, SalesPersons, SalesVoucher. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersMonthlyCollectionTarget]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersMonthlyCollectionTarget]]
- [[CustomersPaidTransList]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonCollectionsTargets]]
- [[SalesPersons]]
- SalesVoucher
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersMonthlyCollectionTarget]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]

**Tables Written**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersMonthlyCollectionTarget]]
- [[CustomersPaidTransList]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonCollectionsTargets]]
- [[SalesPersons]]
- SalesVoucher

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
