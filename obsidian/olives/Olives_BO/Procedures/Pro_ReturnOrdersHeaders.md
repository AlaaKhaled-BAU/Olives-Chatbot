---
type: procedure
database: Olives_BO
name: Pro_ReturnOrdersHeaders
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - Approve
  - [[BatchsItemsInfo]]
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[Currencies]]
  - [[Customers]]
  - Final
  - Fun_GetCompanyBranchesByUser
  - Fun_GetRetOrdersInvoiceNo
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[PriceLists]]
  - [[ReturnOrdersDetails]]
writes_to:
  - Approve
  - Final
  - [[ReturnOrdersHeaders]]
  - ReturnOrdersHeadersLog
  - [[SalespersonsMessages]]
  - [[TransactionsBatchsItemsInvoiceLink]]
  - [[TransactionsSerials]]
  - Void
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ReturnOrdersHeaders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Approve, BatchsItemsInfo, ClientsActive, CompanyParameters, Currencies, Customers, Final, Fun_GetCompanyBranchesByUser, Fun_GetRetOrdersInvoiceNo, InvoiceHistoryDF, InvoiceHistoryHF, Items, ItemsUnits, PriceLists, ReturnOrdersDetails. Writes Approve, Final, ReturnOrdersHeaders, ReturnOrdersHeadersLog, SalespersonsMessages, TransactionsBatchsItemsInvoiceLink, TransactionsSerials, Void. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	=null
- @TransactionYear	int	=null
- @TransactionNo	int	=null
- @TransactionDate	smalldatetime	=null
- @SalesPersonID	int	=null
- @CustomerID	bigint	=null
- @PriceListID	int	=null
- @CreditCash	int	=null
- @DiscountAmount	float	=null
- @DiscountPercent	float	=null
- @ForeignDiscountAmount	float	=null
- @ForeignDiscountPercent	float	=null
- @Notes	nvarchar(500)	=null
- @Reason	nvarchar(200)	=null
- @CurrencyID	smallint	=null
- @ExchangeRate	float	=null
- @IsPrinted	bit	=null
- @Latitude	nvarchar(50)	=null
- @Longitude	nvarchar(50)	=null
- @RouteID	int	=null
- @PostedToERP	bit	=null
- @IsVoid	bit	=null
- @CustomerName	varchar(200)	=null
- @Approve	bit	=null
- @Reference1	nvarchar(50)	=null
- @Reference2	nvarchar(50)	=null
- @TrDateTime	smalldatetime	=null
- @CustomerDiscountPerc	float	=null
- @CustomerDiscountAmount	float	=null
- @PrintOriginalCount	int	=null
- @PrintCopyCount	int	=null
- @IsWFApproved	bit	=null
- @UserID nvarchar(50) = null
- @WFApproveDesc	nvarchar(200)	=null
- @ForeignCustomerDiscountPerc	float	=null
- @ForeignCustomerDiscountAmount	float	=null
- @ItemCode nvarchar(100)=null
- @UnitID nvarchar(50)=null
- @BatchNo nvarchar(50) = null
- @InvYear nvarchar(50) = null
- @InvNo nvarchar(50) = null
- @Qty float = NULL
- @cmdType varchar(50)=null
- @FromDate smalldatetime =null
- @ToDate smalldatetime =null
- @DocumentTypeID int =null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID_Log nvarchar(100)=null
## Tables Read
- Approve
- [[BatchsItemsInfo]]
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Currencies]]
- [[Customers]]
- Final
- Fun_GetCompanyBranchesByUser
- Fun_GetRetOrdersInvoiceNo
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceLists]]
- [[ReturnOrdersDetails]]
## Tables Written
- Approve
- Final
- [[ReturnOrdersHeaders]]
- ReturnOrdersHeadersLog
- [[SalespersonsMessages]]
- [[TransactionsBatchsItemsInvoiceLink]]
- [[TransactionsSerials]]
- Void
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Approve
- [[BatchsItemsInfo]]
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Currencies]]
- [[Customers]]
- Final
- Fun_GetCompanyBranchesByUser
- Fun_GetRetOrdersInvoiceNo
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceLists]]
- [[ReturnOrdersDetails]]

**Tables Written**
- Approve
- Final
- [[ReturnOrdersHeaders]]
- ReturnOrdersHeadersLog
- [[SalespersonsMessages]]
- [[TransactionsBatchsItemsInvoiceLink]]
- [[TransactionsSerials]]
- Void

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
