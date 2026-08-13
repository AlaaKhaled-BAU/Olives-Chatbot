---
type: procedure
database: Olives_BO
name: Acback_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - OPENJSON
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
called_by:
  - [[Acback_Integ_PostData]]
support_relevance: high
last_verified: 2026-07-05
---
# Acback_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersTypes, Items, ItemsCategories, ItemsUnits, OPENJSON, Positions, PriceListDetails, PriceLists, SalesPersons, SalesPersonsGroups. Writes Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersTypes, Items, ItemsCategories, ItemsUnits, Positions, PriceListDetails, PriceLists, SalesPersons, SalesPersonsGroups. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- OPENJSON
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Callers
_None (no known callers)_
## Callees
- [[Acback_Integ_PostData]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- OPENJSON
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

**Callers**
- [[Acback_Integ_PostData]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
