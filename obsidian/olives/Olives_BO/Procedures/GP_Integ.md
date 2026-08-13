---
type: procedure
database: Olives_BO
name: GP_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - CheckCustFinDet
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
writes_to:
  - [[Banks]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[OrdersHeaders]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - SalesOrder
  - SalesOrderItems
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GP_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, CheckCustFinDet, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, Locations, OrdersDetails, OrdersHeaders, PaymentsTypes, Positions, PriceListDetails. Writes Banks, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, Locations, OrdersHeaders, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesOrder, SalesOrderItems, SalesPersonItemsBalance, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- CheckCustFinDet
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
## Tables Written
- [[Banks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- SalesOrder
- SalesOrderItems
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- CheckCustFinDet
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]

**Tables Written**
- [[Banks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- SalesOrder
- SalesOrderItems
- [[SalesPersonItemsBalance]]
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
