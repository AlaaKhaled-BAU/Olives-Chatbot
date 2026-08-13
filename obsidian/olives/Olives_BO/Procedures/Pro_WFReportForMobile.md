---
type: procedure
database: Olives_BO
name: Pro_WFReportForMobile
schema: dbo
tags: [#reporting, #workflow]
reads_from:
  - Checks
  - ClientsActive
  - Customers
  - CustomersFinancialDetails
  - CustomersTypes
  - Items
  - ItemsCategories
  - ItemsUnits
  - Locations
  - OrdersDetails
  - OrdersHeaders
  - PriceListDetails
  - PriceLists
  - Receipts
  - SalesPersonItemsBalance
  - SalesPersons
  - SalesPersonsGroups
  - TransactionsDetails
  - TransactionsHeaders
  - TransactionsTypes
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_WFReportForMobile

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 20 table(s); calls 9 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @CustomersArray nvarchar(100)
- @SalesmanArray nvarchar(100)
- @TypeArray nvarchar(100)
- @ItemsArray nvarchar(100)
- @CustomerTypeArray nvarchar(100)
- @CategoryArray nvarchar(100)
- @ItemCodeArray nvarchar(100)
- @SalesPersonsGroups nvarchar(100)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @UserID nvarchar(50)
- @Approved bit
- @FromApproveDate smalldatetime
- @ToApproveDate smalldatetime
- @FromInvNo bigint
- @ToInvNo bigint
- @InvType smallint
- @SalespersonID int
- @SalesmanNo int
- @IsMultiSelect bit
- @FromSalesman int
- @ToSalesman int
- @FromCustType int
- @ToCustType int
- @FromSalesPerson int
- @ToSalesPerson int
- @FromType int
- @ToType int
- @Cmd nvarchar(100)
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_CalcQtyInAllUnits`
- `Fun_ConvArrayToTable`
- `Fun_GetCompanyBranchesByUser`
- `Fun_GetFromDate`
- `Fun_GetSalesmanTreeByID`
- `GetItemMasterUnitQty`
- `GetItemOrgUnitQty`
- `GetItemSmallUnitQty`
- `GetQRCode`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
