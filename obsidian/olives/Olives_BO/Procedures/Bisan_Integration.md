---
type: procedure
database: Olives_BO
name: Bisan_Integration
schema: dbo
tags: [#integration]
reads_from:
  - Checks
  - ItemsGroups
  - OrdersDetails
  - TransactionsDetails
writes_to:
  - Banks
  - Branches
  - BusinessUnits
  - CompanyBranches
  - CustomerStatmentOfAccount
  - Customers
  - CustomersFinancialDetails
  - CustomersTypes
  - Items
  - ItemsCategories
  - ItemsUnits
  - ItemsUnitsDetails
  - Locations
  - OrdersHeaders
  - Positions
  - PriceListDetails
  - PriceLists
  - Receipts
  - SalesPersonItemsBalance
  - SalesPersons
  - SalesPersonsGroups
  - TransactionsHeaders
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Bisan_Integration

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); writes 22; calls 4 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @CmdType nvarchar(100)
- @BanksAndBranchesTable meatland_integration_banksandbranches
- @SalesmanTable meatland_integration_salesman
- @LocationsTable meatland_integration_locations
- @ItemsUnitsTable meatland_integration_itemsunits
- @ItemsBrand meatland_integration_itemsbrand
- @ItemsDataTable meatland_integration_items
- @PriceListsTable meatland_integration_pricelists
- @CustomersTable meatland_integration_customers
- @StockBalancesTable meatland_integration_stockbalances
- @CustomerStatmentOfAccount meatland_integration_customerstatmentofaccount
- @Bank nvarchar(100)
- @BankBranch nvarchar(100)
- @Code nvarchar(100)
- @NameAR nvarchar(200)
- @NameEN nvarchar(200)
- @FileType nvarchar(100)
- @TreeParent nvarchar(100)
- @TreeLevel int
- @Factor float
- @Group nvarchar(100)
- @SmallestUnit nvarchar(100)
- @DefaultUnit nvarchar(100)
- @IsTaxable nvarchar(100)
- @ItemTaxType nvarchar(100)
- @PriceList nvarchar(100)
- @PLType nvarchar(100)
- @Item nvarchar(100)
- @Unit nvarchar(100)
- @MaxDiscPerc float
- @MaxMarkupPerc float
- @RawPrice float
- @TaxedPrice float
- @IsSuspended nvarchar(100)
- @Address nvarchar(200)
- @Fax nvarchar(100)
- @Mobile nvarchar(100)
- @HomePhone nvarchar(100)
- @Email nvarchar(100)
- @Url nvarchar(100)
- @Notes nvarchar(100)
- @IsCustomer nvarchar(100)
- @IsEmployee nvarchar(100)
- @TaxId nvarchar(100)
- @Area nvarchar(100)
- @CusContactAR nvarchar(100)
- @CusTaxType nvarchar(100)
- @CusPriceList nvarchar(100)
- @Salesman nvarchar(100)
- @CusAccount nvarchar(100)
- @MaxCredit float
- @CurrentBalance float
- @PostdatedBalance float
- @ChkMaxCredit float
- @CreditDays int
- @ReportUnit nvarchar(100)
- @EndBalance float
- @SalesmanNo int
- @branch nvarchar(100)
- @TrYear smallint
- @TrNo int
- @TrType int
- @RefNo nvarchar(20)
- @itemFamily nvarchar(20)
- @itemCategory nvarchar(20)
- @brand nvarchar(20)
- @CustomerNo bigint
- @account nvarchar(100)
- @credit nvarchar(100)
- @debit nvarchar(100)
- @docComment nvarchar(200)
- @docDate smalldatetime
- @runningBalance nvarchar(100)
- @shownCurr nvarchar(10)
- @shownParent nvarchar(100)
- @subAct nvarchar(100)
- @TrSer int
- @discountPercent float
## Tables Read
- [[Checks]]
- [[ItemsGroups]]
- [[OrdersDetails]]
- [[TransactionsDetails]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsHeaders]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_CustomerMF|OT_CustomerMF]]
- [[OSFA_DB/Tables/OT_NewCustomers|OT_NewCustomers]]
- [[OSFA_DB/Tables/OT_StateAccBalance|OT_StateAccBalance]]
## Callers
_None_
## Callees
- `Fun_GetInvTotalAmount`
- `GetItemOrgUnitQty`
- `GetItemSmallUnitQty`
- `GetItemUnitBySerial`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
