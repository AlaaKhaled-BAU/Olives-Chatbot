---
type: procedure
database: Olives_BO
name: Awa2el_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - CheckCustFinDet
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomerStatmentOfAccount]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Awa2el_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, CheckCustFinDet, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, Positions, PriceListDetails, SalesPersons, dbo. Writes Customers, CustomersFinancialDetails, CustomerStatmentOfAccount, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, Positions, PriceListDetails, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Branches]]
- CheckCustFinDet
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[Positions]]
- [[PriceListDetails]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[Positions]]
- [[PriceListDetails]]
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- CheckCustFinDet
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[Positions]]
- [[PriceListDetails]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[Positions]]
- [[PriceListDetails]]
- [[SalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
