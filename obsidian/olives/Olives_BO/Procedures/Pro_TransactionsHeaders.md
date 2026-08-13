---
type: procedure
database: Olives_BO
name: Pro_TransactionsHeaders
schema: dbo
tags: [#backoffice]
reads_from:
  - Approve
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[Currencies]]
  - [[Customers]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - [[DocumentsTypes]]
  - Fun_GetCompanyBranchesByUser
  - [[Locations]]
  - [[PriceLists]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
writes_to:
  - Approve
  - [[Receipts]]
  - TransactionsDetailsLog
  - [[TransactionsHeaders]]
  - TransactionsHeadersLog
  - [[TransactionsSerials]]
  - Void
called_by:
  - [[Pro_CalcSalespersonItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TransactionsHeaders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Approve, ClientsActive, CompanyParameters, Currencies, Customers, CustomersPaidTransList, CustomersTypes, DocumentsTypes, Fun_GetCompanyBranchesByUser, Locations, PriceLists, Receipts, Receipts_PaidTrans, RoutesInformation, SalesPersons. Writes Approve, Receipts, TransactionsDetailsLog, TransactionsHeaders, TransactionsHeadersLog, TransactionsSerials, Void. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @TransactionTypeID int = 1
- @IsVoid bit = null
- @TransactionNo int = '1300300383'
- @TransactionYear smallint = 2024
- @cmdType varchar(50)='Select All by ID'
- @TransactionDate smalldatetime=null
- @CustomerID bigint=null
- @SalesPersonID int = null
- @PriceListID int=null
- @DiscountAmount float=null
- @CustomerDiscountAmount float=null
- @CustomerDiscountPerc float=null
- @DiscountPercent float=null
- @ForeignDiscountAmount float=null
- @ForeignDiscountPercent float=null
- @CurrencyID int=null
- @ExchangeRate float=null
- @Notes nvarchar(500)=null
- @Latitude nvarchar(50)=null
- @Longitude nvarchar(50)=null
- @RouteID int=null
- @PaymentType int=null
- @UserID nvarchar(50) = null
- @CreditCash int = null
- @FromDate smalldatetime =null
- @ToDate smalldatetime =null
- @DocumentTypeID int = null
- @Approve bit = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID_Log nvarchar(100)=null
- @BusinessUnitID int=null
## Tables Read
- Approve
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Currencies]]
- [[Customers]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[DocumentsTypes]]
- Fun_GetCompanyBranchesByUser
- [[Locations]]
- [[PriceLists]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[RoutesInformation]]
- [[SalesPersons]]
## Tables Written
- Approve
- [[Receipts]]
- TransactionsDetailsLog
- [[TransactionsHeaders]]
- TransactionsHeadersLog
- [[TransactionsSerials]]
- Void
## Callers
_None (no known callers)_
## Callees
- [[Pro_CalcSalespersonItemBalance]]
## Impact / Dependencies

**Tables Read**
- Approve
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Currencies]]
- [[Customers]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[DocumentsTypes]]
- Fun_GetCompanyBranchesByUser
- [[Locations]]
- [[PriceLists]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[RoutesInformation]]
- [[SalesPersons]]

**Tables Written**
- Approve
- [[Receipts]]
- TransactionsDetailsLog
- [[TransactionsHeaders]]
- TransactionsHeadersLog
- [[TransactionsSerials]]
- Void

**Callers**
- [[Pro_CalcSalespersonItemBalance]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
