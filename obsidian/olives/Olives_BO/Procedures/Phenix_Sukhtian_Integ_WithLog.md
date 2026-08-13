---
type: procedure
database: Olives_BO
name: Phenix_Sukhtian_Integ_WithLog
schema: dbo
tags: [#backoffice, #integration, #log]
reads_from:
  - [[BusinessUnits]]
  - CheckCustFinDet
  - [[CompanyBranches]]
  - [[CompanyParameters]]
  - Cur_Class
  - Cur_CustomersTypes
  - Cur_Items
  - Cur_SalesPersons
  - [[Customers]]
  - [[CustomersTypes]]
  - [[IntegrationErrorLog]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
writes_to:
  - [[BusinessUnits]]
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
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
called_by:
  - [[Phenix_Sukhtian_Integ_CloseSession]]
  - [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
  - [[Phenix_Sukhtian_Integ_OpenSession]]
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# Phenix_Sukhtian_Integ_WithLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, CheckCustFinDet, CompanyBranches, CompanyParameters, Cur_Class, Cur_CustomersTypes, Cur_Items, Cur_SalesPersons, Customers, CustomersTypes, IntegrationErrorLog, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails. Writes BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesPersons, SalesPersonsGroups. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- [[BusinessUnits]]
- CheckCustFinDet
- [[CompanyBranches]]
- [[CompanyParameters]]
- Cur_Class
- Cur_CustomersTypes
- Cur_Items
- Cur_SalesPersons
- [[Customers]]
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
## Tables Written
- [[BusinessUnits]]
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
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Callers
_None (no known callers)_
## Callees
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- CheckCustFinDet
- [[CompanyBranches]]
- [[CompanyParameters]]
- Cur_Class
- Cur_CustomersTypes
- Cur_Items
- Cur_SalesPersons
- [[Customers]]
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]

**Tables Written**
- [[BusinessUnits]]
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
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

**Callers**
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
