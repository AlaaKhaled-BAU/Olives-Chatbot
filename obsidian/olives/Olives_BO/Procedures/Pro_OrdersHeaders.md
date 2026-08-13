---
type: procedure
database: Olives_BO
name: Pro_OrdersHeaders
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[BatchsItemsInfo]]
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[Currencies]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetSalesmanTreeByID
  - [[Items]]
  - [[Locations]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceLists]]
writes_to:
  - OrdersDetailsLog
  - [[OrdersHeaders]]
  - OrdersHeadersLog
  - [[SalespersonsMessages]]
  - [[TransactionsBatchsItemsInfo]]
  - [[TransactionsSerials]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OrdersHeaders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BatchsItemsInfo, ClientsActive, CompanyParameters, Currencies, Customers, CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, Fun_GetSalesmanTreeByID, Items, Locations, OrdersDetails, OrdersHeaders, PaymentsTypes, Positions, PriceLists. Writes OrdersDetailsLog, OrdersHeaders, OrdersHeadersLog, SalespersonsMessages, TransactionsBatchsItemsInfo, TransactionsSerials. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int = null
- @cmdType varchar(50)=null
- @OrderYear smallint=null
- @OrderNo int=null
- @OrderDate smalldatetime=null
- @PromisesDate smalldatetime=null
- @CustomerID bigint=null
- @PriceListID int=null
- @DiscountAmount float=null
- @DiscountPercent float=null
- @ForeignDiscountAmount float=null
- @ForeignDiscountPercent float=null
- @CustomerDiscountPerc float = null
- @CustomerDiscountAmount float = null
- @CurrencyID int=null
- @ExchangeRate float=null
- @Notes nvarchar(500)=null
- @Latitude nvarchar(50)=null
- @Longitude nvarchar(50)=null
- @RouteID int=null
- @PaymentType int=null
- @UserID nvarchar(50) = null
- @FromDate  smalldatetime = null
- @ToDate  smalldatetime = null
- @IsVoid bit = null
- @Approve bit = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @BusinessUnitID int=null
- @UserID_Log nvarchar(100)=null
- @OrdersHeaderDataTable OrderHeaders_Type readonly
- @DeliveryBatchID  INT =0 output
- @ItemNo nvarchar(100)=null
- @VouNo int =null
- @VouYear smallint = null
- @VouType smallint = null
- @Unit nvarchar(50)= null
- @Qty money = null
- @Bonus money = null
- @BatchNo varchar(100)= null
- @Driver int = null
## Tables Read
- [[BatchsItemsInfo]]
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Currencies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceLists]]
## Tables Written
- OrdersDetailsLog
- [[OrdersHeaders]]
- OrdersHeadersLog
- [[SalespersonsMessages]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsSerials]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BatchsItemsInfo]]
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Currencies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceLists]]

**Tables Written**
- OrdersDetailsLog
- [[OrdersHeaders]]
- OrdersHeadersLog
- [[SalespersonsMessages]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsSerials]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
