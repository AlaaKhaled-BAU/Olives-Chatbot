---
type: procedure
database: Olives_BO
name: Niroukh_Integration_WithLog
schema: dbo
tags: [#backoffice, #integration, #log]
reads_from:
  - [[Banks]]
  - [[BatchsItemsInfo]]
  - [[Branches]]
  - [[BusinessUnits]]
  - CheckCustFinDet
  - [[CompanyBranches]]
  - Cur_Banks
  - Cur_Branches
  - Cur_CustomerTypes
  - Cur_Customerclasss
  - Cur_GetPaymentTypes
  - Cur_Items
  - Cur_SalesPersons
  - [[Customers]]
  - [[CustomersGroups]]
writes_to:
  - [[Banks]]
  - [[BatchsItemsInfo]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGroups]]
  - [[CustomersTypes]]
  - [[Drawers]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
called_by:
  - [[Niroukh_Integ_GetDataFromAPI]]
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# Niroukh_Integration_WithLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, BatchsItemsInfo, Branches, BusinessUnits, CheckCustFinDet, CompanyBranches, Cur_Banks, Cur_Branches, Cur_CustomerTypes, Cur_Customerclasss, Cur_GetPaymentTypes, Cur_Items, Cur_SalesPersons, Customers, CustomersGroups. Writes Banks, BatchsItemsInfo, Branches, BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, CustomersGroups, CustomersTypes, Drawers, Items, ItemsCategories, ItemsUnits, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesPersons, SalesPersonsGroups. Invoked by 1 procedure(s). Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
- @APILinkUser nvarchar(100)='UserName=hani&Password=12'
## Tables Read
- [[Banks]]
- [[BatchsItemsInfo]]
- [[Branches]]
- [[BusinessUnits]]
- CheckCustFinDet
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- Cur_CustomerTypes
- Cur_Customerclasss
- Cur_GetPaymentTypes
- Cur_Items
- Cur_SalesPersons
- [[Customers]]
- [[CustomersGroups]]
## Tables Written
- [[Banks]]
- [[BatchsItemsInfo]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[CustomersTypes]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Callers
- [[Niroukh_Integ_AllUsers]]
## Callees
- [[Niroukh_Integ_GetDataFromAPI]]
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[BatchsItemsInfo]]
- [[Branches]]
- [[BusinessUnits]]
- CheckCustFinDet
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- Cur_CustomerTypes
- Cur_Customerclasss
- Cur_GetPaymentTypes
- Cur_Items
- Cur_SalesPersons
- [[Customers]]
- [[CustomersGroups]]

**Tables Written**
- [[Banks]]
- [[BatchsItemsInfo]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[CustomersTypes]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

**Callers**
- [[Niroukh_Integ_GetDataFromAPI]]
- [[SP_IntegrationErrorLog]]

**Callees**
- [[Niroukh_Integ_AllUsers]]


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
