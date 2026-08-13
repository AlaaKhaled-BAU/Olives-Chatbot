---
type: procedure
database: Olives_BO
name: ABS_Integration_Sokhtian
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - [[ERPStores]]
  - [[ERPStoresItemsLink]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomerStatmentOfAccount]]
  - [[CustomersTypes]]
  - [[ERPStores]]
  - [[ERPStoresItemsLink]]
  - [[InvoiceHistoryDF]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - PRM_RAM_DT_HH_Get_InvoiceList
  - [[SalesPersons]]
called_by:
  - ABS_Integ_GetDataFromAPI_Sokhtian
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# ABS_Integration_Sokhtian


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersTypes, ERPStores, ERPStoresItemsLink, InvoiceHistoryDF, InvoiceHistoryHF, Items, ItemsCategories, ItemsUnits, Locations. Writes Banks, Branches, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomerStatmentOfAccount, CustomersTypes, ERPStores, ERPStoresItemsLink, InvoiceHistoryDF, Items, ItemsCategories, ItemsUnits, Locations, PaymentsTypes, Positions, PriceListDetails, PriceLists, PRM_RAM_DT_HH_Get_InvoiceList, SalesPersons. Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- [[Banks]]
- [[Branches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[ERPStores]]
- [[ERPStoresItemsLink]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[ERPStores]]
- [[ERPStoresItemsLink]]
- [[InvoiceHistoryDF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- PRM_RAM_DT_HH_Get_InvoiceList
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
- ABS_Integ_GetDataFromAPI_Sokhtian
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[ERPStores]]
- [[ERPStoresItemsLink]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[ERPStores]]
- [[ERPStoresItemsLink]]
- [[InvoiceHistoryDF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- PRM_RAM_DT_HH_Get_InvoiceList
- [[SalesPersons]]

**Callers**
- ABS_Integ_GetDataFromAPI_Sokhtian
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
