---
type: procedure
database: Olives_BO
name: Pro_ImportData
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Drawers]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[RoutesInformation]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Drawers]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalesPersonTransactionsSerials]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Data-Sync-Cycle
---
# Pro_ImportData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Customers, CustomersClasses, CustomersFinancialDetails, CustomersTypes, Drawers, Items, ItemsCategories, ItemsUnits, Locations, PaymentsTypes, PriceListDetails, PriceLists, RoutesInformation. Writes Banks, Branches, Customers, CustomersClasses, CustomersFinancialDetails, CustomersTypes, Drawers, Items, ItemsCategories, ItemsUnits, Locations, PaymentsTypes, PriceListDetails, PriceLists, RoutesInformation, SalesPersons, SalesPersonsGroups, SalesPersonTransactionsSerials. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @BanksTbl ImportData_Banks readonly
- @BranchesTbl ImportData_Branches readonly
- @LocationsTbl ImportData_Locations readonly
- @PaymentsTypesTbl ImportData_PaymentsTypes readonly
- @ItemsUnitsTbl ImportData_ItemsUnits readonly
- @ItemsCategoriesTbl ImportData_ItemsCategories readonly
- @ItemsTbl ImportData_Items readonly
- @PriceListsTbl ImportData_PriceLists readonly
- @PriceListDetailsTbl ImportData_PriceListDetails readonly
- @SalesPersonsGroupsTbl ImportData_SalesPersonsGroups readonly
- @SalesPersonsTbl ImportData_SalesPersons readonly
- @SalesPersonTransactionsSerialsTbl ImportData_SalesPersonTransactionsSerials readonly
- @CustomersClassesTbl ImportData_CustomersClasses readonly
- @CustomersTypesTbl ImportData_CustomersTypes readonly
- @CustomersTbl ImportData_Customers readonly
- @DrawersTbl ImportData_Drawers readonly
- @RoutesInformationTbl ImportData_RoutesInformation readonly
- @CustomersFinancialDetailsTbl ImportData_CustomersFinancialDetails readonly
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[PaymentsTypes]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[RoutesInformation]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[PaymentsTypes]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonTransactionsSerials]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[PaymentsTypes]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[RoutesInformation]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[PaymentsTypes]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonTransactionsSerials]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
