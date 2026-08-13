---
type: procedure
database: Olives_BO
name: Shamel_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - Cur_Banks
  - Cur_Branches
  - [[IntegrationErrorLog]]
  - OPENJSON
  - [[SalesPersonsGroups]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersonsGroups]]
called_by:
  - [[Shamel_Integ_GetDataFromAPI]]
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# Shamel_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CompanyBranches, Cur_Banks, Cur_Branches, IntegrationErrorLog, OPENJSON, SalesPersonsGroups. Writes Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, PriceListDetails, PriceLists, SalesPersonsGroups. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[IntegrationErrorLog]]
- OPENJSON
- [[SalesPersonsGroups]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonsGroups]]
## Callers
_None (no known callers)_
## Callees
- [[Shamel_Integ_GetDataFromAPI]]
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[IntegrationErrorLog]]
- OPENJSON
- [[SalesPersonsGroups]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonsGroups]]

**Callers**
- [[Shamel_Integ_GetDataFromAPI]]
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
