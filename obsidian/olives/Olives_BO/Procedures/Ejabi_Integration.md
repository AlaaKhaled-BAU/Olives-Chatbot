---
type: procedure
database: Olives_BO
name: Ejabi_Integration
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
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TaxCodes]]
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
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TaxCodes]]
called_by:
  - [[Ejabi_Integ_GetDataFromAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# Ejabi_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersTypes, Items, ItemsCategories, ItemsUnits, OPENJSON, Positions, PriceListDetails, SalesPersons, SalesPersonsGroups, TaxCodes. Writes Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersTypes, Items, ItemsCategories, ItemsUnits, Positions, PriceListDetails, SalesPersons, SalesPersonsGroups, TaxCodes. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
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
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TaxCodes]]
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
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TaxCodes]]
## Callers
_None (no known callers)_
## Callees
- [[Ejabi_Integ_GetDataFromAPI]]
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
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TaxCodes]]

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
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TaxCodes]]

**Callers**
- [[Ejabi_Integ_GetDataFromAPI]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
