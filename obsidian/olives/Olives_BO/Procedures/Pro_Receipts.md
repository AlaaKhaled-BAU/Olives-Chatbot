---
type: procedure
database: Olives_BO
name: Pro_Receipts
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[Currencies]]
  - [[Customers]]
  - [[DocumentsTypes]]
  - [[Drawers]]
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[Receipts_PaidTransChecks]]
  - [[SalesPersons]]
  - [[TransactionsSerials]]
  - [[WF_SubLog]]
writes_to:
  - ChecksLog
  - [[Receipts]]
  - ReceiptsLog
  - [[TransactionsSerials]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Receipts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, ClientsActive, CompanyParameters, Currencies, Customers, DocumentsTypes, Drawers, Fun_GetCompanyBranchesByUser, Receipts, Receipts_PaidTransChecks, SalesPersons, TransactionsSerials, WF_SubLog. Writes ChecksLog, Receipts, ReceiptsLog, TransactionsSerials. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @TransactionTypeID int = null
- @TransactionYear smallint = null
- @TransactionNo int = null
- @IsChecked bit = null
- @cmdType varchar(50)='Select All'
- @FromDate smalldatetime ='8/29/2014'
- @ToDate smalldatetime ='8/29/2024'
- @UserID nvarchar(50) = 'admin'
- @SalesmanNo int =null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @FromAmount float=NULL
- @ToAmount float=NULL
- @FirstVoid bit=NuLL
- @IsVoid bit = Null
- @TransactionDate smalldatetime = null
- @DocumentTypeID int  = null
- @CustomerID bigint = null
- @SalesPersonID int = null
- @Amount float = null
- @ForeignAmount float = null
- @CurrencyID int = null
- @ExchangeRate float = null
- @IsPrinted bit = null
- @Notes nvarchar(max) = null
- @Latitude nvarchar = null
- @Longitude nvarchar = null
- @RouteID int = null
- @PostedToERP bit = null
- @Collected bit = null
- @Discount float = null
- @RefNo nvarchar = null
- @TrDateTime smalldatetime = null
- @PrintOriginalCount int = null
- @PrintCopyCount int = null
- @IsWFApproved bit = null
- @WFApproveDesc bit = null
- @AcceptDate smalldatetime = null
- @ServerDate smalldatetime = null
- @DetailCount float = null
- @TabletSysID int = null
- @AcceptedBy nvarchar = null
- @ReceiptRequestYear smallint = null
- @ReceiptRequestNo  int = null
- @Reference1 nvarchar = null
- @Reference2 nvarchar = null
- @PostedToEmail bit = null
- @Bank_TransferNo nvarchar  = null
- @Bank_Transfer_Date smalldatetime = null
- @Bank_Transfer_Amount float = null
- @Bank_Transfer_BankID int = null
- @Bank_Transfer_BankAccount int = null
- @VoidPostedToERP bit = null
- @VoidPostedToEmail bit = null
- @VoidedByUser nvarchar = null
- @SecondCollected bit = null
- @PostedToERPDateTime smalldatetime = null
- @LocationLineID int = null
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Currencies]]
- [[Customers]]
- [[DocumentsTypes]]
- [[Drawers]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[Receipts_PaidTransChecks]]
- [[SalesPersons]]
- [[TransactionsSerials]]
- [[WF_SubLog]]
## Tables Written
- ChecksLog
- [[Receipts]]
- ReceiptsLog
- [[TransactionsSerials]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Currencies]]
- [[Customers]]
- [[DocumentsTypes]]
- [[Drawers]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[Receipts_PaidTransChecks]]
- [[SalesPersons]]
- [[TransactionsSerials]]
- [[WF_SubLog]]

**Tables Written**
- ChecksLog
- [[Receipts]]
- ReceiptsLog
- [[TransactionsSerials]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
