---
type: procedure
database: Olives_BO
name: Awael_Integration_WithLog
schema: dbo
tags: [#backoffice, #integration, #log]
reads_from:
  - AccountDataMain
  - [[Banks]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - Cur_Banks
  - Cur_Branches
  - [[CustomersTypes]]
  - [[IntegrationErrorLog]]
  - [[PaymentsTypes]]
  - [[PriceLists]]
  - [[SalesPersonsGroups]]
  - `dbo`
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriceExceptions]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
called_by:
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# Awael_Integration_WithLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AccountDataMain, Banks, BusinessUnits, CompanyBranches, Cur_Banks, Cur_Branches, CustomersTypes, IntegrationErrorLog, PaymentsTypes, PriceLists, SalesPersonsGroups, dbo. Writes Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsPriceExceptions, ItemsUnits, Locations, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesPersons, SalesPersonsGroups. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- AccountDataMain
- [[Banks]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[PaymentsTypes]]
- [[PriceLists]]
- [[SalesPersonsGroups]]
- `dbo`
## Tables Written
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Callers
_None (no known callers)_
## Callees
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- AccountDataMain
- [[Banks]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[PaymentsTypes]]
- [[PriceLists]]
- [[SalesPersonsGroups]]
- dbo

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

**Callers**
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
