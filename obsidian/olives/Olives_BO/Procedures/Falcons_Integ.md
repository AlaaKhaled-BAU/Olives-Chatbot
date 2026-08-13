---
type: procedure
database: Olives_BO
name: Falcons_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - [[CompanyBranches]]
  - Cust_summary
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - CustomersTaxExclude
  - DBO
  - [[DeliveryManifest]]
  - [[DeliveryRoute]]
  - Fun_GetSalesmanTreeByID
  - [[InvoiceDeliveryHF]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - Item_Unit_Details
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Falcons_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, CompanyBranches, Cust_summary, Customers, CustomersClasses, CustomersFinancialDetails, CustomersTaxExclude, DBO, DeliveryManifest, DeliveryRoute, Fun_GetSalesmanTreeByID, InvoiceDeliveryHF, InvoiceHistoryDF, InvoiceHistoryHF. Writes Customers, CustomersFinancialDetails, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Item_Unit_Details, Positions, PriceListDetails, PriceLists, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- [[CompanyBranches]]
- Cust_summary
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- CustomersTaxExclude
- DBO
- [[DeliveryManifest]]
- [[DeliveryRoute]]
- Fun_GetSalesmanTreeByID
- [[InvoiceDeliveryHF]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- Item_Unit_Details
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- [[CompanyBranches]]
- Cust_summary
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- CustomersTaxExclude
- DBO
- [[DeliveryManifest]]
- [[DeliveryRoute]]
- Fun_GetSalesmanTreeByID
- [[InvoiceDeliveryHF]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]

**Tables Written**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- Item_Unit_Details
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
