---
type: procedure
database: Olives_BO
name: Yolande_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[CustomerChqList]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriceExceptions]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[CustomerChqList]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriceExceptions]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Yolande_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, CustomerChqList, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersTypes, Items, ItemsCategories, ItemsPriceExceptions, ItemsUnits, ItemsUnitsDetails, PaymentsTypes, Positions, PriceListDetails. Writes Banks, Branches, CustomerChqList, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersTypes, Items, ItemsCategories, ItemsPriceExceptions, ItemsUnits, ItemsUnitsDetails, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Branches]]
- [[CustomerChqList]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[CustomerChqList]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[CustomerChqList]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[CustomerChqList]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
