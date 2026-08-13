---
type: procedure
database: Olives_BO
name: Presto_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Checks]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetInvoiceTotalAmount
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[ProstoSoftAccounts]]
  - [[Receipts]]
  - SalesPersonDeleteBalance
  - [[SalesPersonItemsBalance]]
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Positions]]
  - [[Receipts]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Presto_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Checks, Customers, CustomersFinancialDetails, Fun_GetInvoiceTotalAmount, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, PriceListDetails, PriceLists, ProstoSoftAccounts, Receipts, SalesPersonDeleteBalance, SalesPersonItemsBalance. Writes Customers, CustomersFinancialDetails, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Positions, Receipts, SalesPersonItemsBalance, SalesPersons, TransactionsHeaders, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @CmdType varchar(50)
- @SalesPersonID int =null
- @GROUP_NO int=null
- @GROUP_NAME varchar(200)=null
- @UNIT_NO int=null
- @UNIT_NAME  varchar(20)=null
- @C_STORE int=null
- @C_SUB varchar(20)=null
- @C_GROUP int=null
- @TOT_PRICE float=null
- @ONE_PRICE  float=null
- @C_UNIT int=null
- @SUB_DESC varchar(200)=null
- @BAR_CODE varchar(20)=null
- @DRB_P  float=null
- @D_ACC_NO bigint=null
- @D_ACC_NAME varchar(200)=null
- @M_NO int=null
- @MAN_NO int=null
- @MAN_NAME varchar(200)=null
- @TransactionTypeID smallint=null
- @TransactionYear smallint=null
- @TransactionNo int=null
- @Qty money=null
- @CreditLimit float=null
## Tables Read
- [[Banks]]
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetInvoiceTotalAmount
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[ProstoSoftAccounts]]
- [[Receipts]]
- SalesPersonDeleteBalance
- [[SalesPersonItemsBalance]]
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Positions]]
- [[Receipts]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetInvoiceTotalAmount
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[ProstoSoftAccounts]]
- [[Receipts]]
- SalesPersonDeleteBalance
- [[SalesPersonItemsBalance]]

**Tables Written**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Positions]]
- [[Receipts]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
