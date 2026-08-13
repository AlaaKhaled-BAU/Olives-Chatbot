---
type: procedure
database: Olives_BO
name: OSFA_SP_Api
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[OrdersHeaders]]
  - [[OT_NewCustomers]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OSFA_SP_Api


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks. Writes Banks, Branches, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, OrdersHeaders, OT_NewCustomers, PaymentsTypes, Positions, PriceListDetails, PriceLists, Receipts, SalesPersons, SalesPersonsGroups, TransactionsHeaders, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CmdType nvarchar(100)
- @CompanyID smallint
- @Banks OSFA_Udt_Api_Banks readonly
- @BankBranchs OSFA_Udt_Api_BankBranchs readonly
- @SalesmanGroups OSFA_Udt_Api_SalesmanGroups readonly
- @Units OSFA_Udt_Api_Units readonly
- @ItemCategory OSFA_Udt_Api_ItemCategory readonly
- @CustomerTypes OSFA_Udt_Api_CustomerTypes readonly
- @CustomerLocations OSFA_Udt_Api_CustomerLocations readonly
- @CustomerPaymentTypes OSFA_Udt_Api_CustomerPaymentTypes readonly
- @Salesmen OSFA_Udt_Api_Salesmen readonly
- @Items OSFA_Udt_Api_Items readonly
- @ItemsUnitsDetails OSFA_Udt_Api_ItemsUnitsDetails readonly
- @PriceListHFs OSFA_Udt_Api_PriceListHFs readonly
- @PriceListDFs OSFA_Udt_Api_PriceListDFs readonly
- @Customers OSFA_Udt_Api_Customers readonly
- @PostVouchers OSFA_Udt_Api_PostVouchers readonly
- @Result nvarchar(max) = null output
## Tables Read
- [[Banks]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[OT_NewCustomers]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[OT_NewCustomers]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
