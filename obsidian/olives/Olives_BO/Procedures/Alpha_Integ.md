---
type: procedure
database: Olives_BO
name: Alpha_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - CheckCustFinDet
  - [[ClientsActive]]
  - [[CustomerChqList]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - [[CustomersTypes]]
  - [[Drawers]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[CustomerChqList]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomerStatmentOfAccount]]
  - [[CustomersTypes]]
  - [[Drawers]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, CheckCustFinDet, ClientsActive, CustomerChqList, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, CustomersTypes, Drawers, InvoiceHistoryDF, InvoiceHistoryHF. Writes Banks, Branches, CustomerChqList, Customers, CustomersFinancialDetails, CustomerStatmentOfAccount, CustomersTypes, Drawers, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, PaymentsTypes, Positions, PriceListDetails, PriceLists, SalesOrderHistoryDF, SalesOrderHistoryHF, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Branches]]
- CheckCustFinDet
- [[ClientsActive]]
- [[CustomerChqList]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- [[Drawers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[CustomerChqList]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
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
- CheckCustFinDet
- [[ClientsActive]]
- [[CustomerChqList]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- [[Drawers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[CustomerChqList]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
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
