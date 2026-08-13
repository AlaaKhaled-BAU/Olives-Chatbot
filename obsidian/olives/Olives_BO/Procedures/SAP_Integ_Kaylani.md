---
type: procedure
database: Olives_BO
name: SAP_Integ_Kaylani
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - CheckCustFinDet
  - [[ClientsActive]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[PaymentsTypes]]
  - [[Positions]]
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
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - NewCustomerImages
  - NewCustomers
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
# SAP_Integ_Kaylani


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CheckCustFinDet, ClientsActive, CompanyBranches, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, PaymentsTypes, Positions. Writes Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, NewCustomerImages, NewCustomers, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CheckCustFinDet
- [[ClientsActive]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PaymentsTypes]]
- [[Positions]]
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
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- NewCustomerImages
- NewCustomers
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
- [[BusinessUnits]]
- CheckCustFinDet
- [[ClientsActive]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PaymentsTypes]]
- [[Positions]]

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
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- NewCustomerImages
- NewCustomers
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
