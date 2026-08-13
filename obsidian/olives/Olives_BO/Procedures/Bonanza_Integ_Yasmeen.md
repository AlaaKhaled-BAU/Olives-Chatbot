---
type: procedure
database: Olives_BO
name: Bonanza_Integ_Yasmeen
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriceExceptions]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - Olives_BO
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - SSMS
  - [[SalesPersons]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomerStatmentOfAccount]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Positions]]
  - [[SalesPersons]]
  - XBT
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Bonanza_Integ_Yasmeen


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Customers, CustomersFinancialDetails, Items, ItemsCategories, ItemsPriceExceptions, ItemsUnits, ItemsUnitsDetails, Olives_BO, Positions, PriceListDetails, PriceLists, SSMS, SalesPersons. Writes Banks, Branches, Customers, CustomersFinancialDetails, CustomerStatmentOfAccount, Items, ItemsCategories, ItemsUnits, Positions, SalesPersons, XBT. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- Olives_BO
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- SSMS
- [[SalesPersons]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Positions]]
- [[SalesPersons]]
- XBT
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- Olives_BO
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- SSMS
- [[SalesPersons]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Positions]]
- [[SalesPersons]]
- XBT

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
