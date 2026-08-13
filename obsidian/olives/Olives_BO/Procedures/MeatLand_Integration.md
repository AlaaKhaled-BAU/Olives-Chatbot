---
type: procedure
database: Olives_BO
name: MeatLand_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - All
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - CheckCustFinDet
  - [[Checks]]
  - [[CompanyBranches]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - Flag
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomerStatmentOfAccount]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[OrdersHeaders]]
  - [[OT_StateAccBalance]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[Receipts]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsHeaders]]
called_by:
  - [[OT_SendSalesmanData]]
support_relevance: high
last_verified: 2026-07-05
---
# MeatLand_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads All, Banks, Branches, BusinessUnits, CheckCustFinDet, Checks, CompanyBranches, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersTypes, Flag, Items, ItemsCategories, ItemsUnits. Writes Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, CustomerStatmentOfAccount, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, OrdersHeaders, OT_StateAccBalance, Positions, PriceListDetails, PriceLists, Receipts, SalesPersonItemsBalance, SalesPersons, SalesPersonsGroups, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @CmdType nvarchar(100)
- @BanksAndBranchesTable Meatland_Integration_BanksAndBranches readonly
- @SalesmanTable Meatland_Integration_Salesman readonly
- @LocationsTable Meatland_Integration_Locations readonly
- @ItemsUnitsTable Meatland_Integration_ItemsUnits readonly
- @ItemsBrand Meatland_Integration_ItemsBrand readonly
- @ItemsDataTable Meatland_Integration_Items readonly
- @PriceListsTable Meatland_Integration_PriceLists readonly
- @CustomersTable Meatland_Integration_Customers readonly
- @StockBalancesTable MeatLand_Integration_StockBalances readonly
- @CustomerStatmentOfAccount Meatland_Integration_CustomerStatmentOfAccount readonly
- @Bank nvarchar(100) = null
- @BankBranch nvarchar(100) = null
- @Code nvarchar(100) = null
- @NameAR nvarchar(200) = null
- @NameEN nvarchar(200) = null
- @FileType nvarchar(100) = null
- @TreeParent nvarchar(100) = null
- @TreeLevel int = null
- @Factor float = null
- @Group nvarchar(100) = null
- @SmallestUnit nvarchar(100) = null
- @DefaultUnit nvarchar(100) = null
- @IsTaxable nvarchar(100) = null
- @ItemTaxType nvarchar(100) = null
- @PriceList nvarchar(100) = null
- @PLType nvarchar(100) = null
- @Item nvarchar(100) = null
- @Unit nvarchar(100) = null
- @MaxDiscPerc float = null
- @MaxMarkupPerc float = null
- @RawPrice float = null
- @TaxedPrice float = null
- @IsSuspended nvarchar(100) = null
- @Address nvarchar(200) = null
- @Fax nvarchar(100) = null
- @Mobile nvarchar(100) = null
- @HomePhone nvarchar(100) = null
- @Email nvarchar(100) = null
- @Url nvarchar(100) = null
- @Notes nvarchar(100) = null
- @IsCustomer nvarchar(100) = null
- @IsEmployee nvarchar(100) = null
- @TaxId nvarchar(100) = null
- @Area nvarchar(100) = null
- @CusContactAR nvarchar(100) = null
- @CusTaxType nvarchar(100) = null
- @CusPriceList nvarchar(100) = null
- @Salesman nvarchar(100) = null
- @CusAccount nvarchar(100) = null
- @MaxCredit float = null
- @CurrentBalance float = null
- @PostdatedBalance float = null
- @ChkMaxCredit float = null
- @CreditDays int = null
- @ReportUnit nvarchar(100)=null
- @EndBalance float=0
- @SalesmanNo int = 0
- @branch nvarchar(100) = null
- @TrYear smallint = null
- @TrNo int = null
- @TrType int = null
- @RefNo nvarchar(20)=null
- @itemFamily nvarchar(20)=null
- @itemCategory nvarchar(20)=null
- @brand nvarchar(20)=null
- @CustomerNo bigint=null
- @account nvarchar(100)=null
- @credit nvarchar(100) = null
- @debit nvarchar(100) = null
- @docComment nvarchar(200)=null
- @docDate smalldatetime=null
- @runningBalance nvarchar(100) = null
- @shownCurr nvarchar(10)=null
- @shownParent nvarchar(100)=null
- @subAct nvarchar(100)=null
- @TrSer int=null
- @discountPercent float=null
## Tables Read
- All
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CheckCustFinDet
- [[Checks]]
- [[CompanyBranches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- Flag
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[OT_StateAccBalance]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[OT_SendSalesmanData]]
## Impact / Dependencies

**Tables Read**
- All
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CheckCustFinDet
- [[Checks]]
- [[CompanyBranches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- Flag
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[OT_StateAccBalance]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsHeaders]]

**Callers**
- [[OT_SendSalesmanData]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
