---
type: procedure
database: Olives_BO
name: ABS_Integration_Jebrene
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
  - OPENJSON
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomerStatmentOfAccount]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
called_by:
  - [[ABS_Integ_GetDataFromAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# ABS_Integration_Jebrene


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, Locations, OPENJSON, PaymentsTypes, Positions, PriceListDetails, PriceLists. Writes Banks, Branches, Customers, CustomersFinancialDetails, CustomerStatmentOfAccount, CustomersTypes, Items, ItemsCategories, ItemsUnits, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- [[Banks]]
- [[Branches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- OPENJSON
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
- [[ABS_Integ_GetDataFromAPI]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- OPENJSON
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]

**Callers**
- [[ABS_Integ_GetDataFromAPI]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
