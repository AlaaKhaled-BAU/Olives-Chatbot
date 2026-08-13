---
type: procedure
database: Olives_BO
name: Pro_SalesQuotationHeaders
schema: dbo
tags: [#backoffice, #order, #sales]
reads_from:
  - [[Currencies]]
  - Fun_GetCompanyBranchesByUser
  - [[PaymentsTypes]]
  - [[PriceLists]]
  - [[ProspectiveCustomers]]
  - [[SalesPersons]]
  - [[SalesQuotationDetails]]
  - [[SalesQuotationHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesQuotationHeaders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Currencies, Fun_GetCompanyBranchesByUser, PaymentsTypes, PriceLists, ProspectiveCustomers, SalesPersons, SalesQuotationDetails, SalesQuotationHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @OrderYear	int	= null
- @OrderNo	int	= null
- @OrderDate	smalldatetime	= null
- @CustomerID	bigint	= null
- @SalesPersonID	int	= null
- @PriceListID	int	= null
- @DiscountAmount	float	= null
- @DiscountPercent	float	= null
- @ForeignDiscountAmount	float	= null
- @ForeignDiscountPercent	float	= null
- @CurrencyID	smallint	= null
- @ExchangeRate	float	= null
- @Notes	nvarchar(500)	= null
- @Latitude	nvarchar(50)	= null
- @Longitude	nvarchar(50)	= null
- @PostedToERP	bit	= null
- @Reference1	nvarchar(50)	= null
- @Reference2	nvarchar(50)	= null
- @PaymentType	int	= null
- @ServerDate	smalldatetime	= null
- @WFApproved	bit	= null
- @Approved	bit	= null
- @DocumentsTypesID	int	= null
- @TrDateTime	smalldatetime	= null
- @BusinessUnitID	int	= null
- @CustomerDiscountPerc	float	= null
- @CustomerDiscountAmount	float	= null
- @IsVoid	bit	= null
- @PrintOriginalCount	int	= null
- @PrintCopyCount	int	= null
- @ForeignCustomerDiscountPerc	float	= null
- @ForeignCustomerDiscountAmount	float	= null
- @CreditCash	int	= null
- @CustomerName	nvarchar(100)	= null
- @UserID nvarchar(50) = null
- @FromDate  smalldatetime = null
- @ToDate  smalldatetime = null
- @cmdType varchar(50)=null
## Tables Read
- [[Currencies]]
- Fun_GetCompanyBranchesByUser
- [[PaymentsTypes]]
- [[PriceLists]]
- [[ProspectiveCustomers]]
- [[SalesPersons]]
- [[SalesQuotationDetails]]
- [[SalesQuotationHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Currencies]]
- Fun_GetCompanyBranchesByUser
- [[PaymentsTypes]]
- [[PriceLists]]
- [[ProspectiveCustomers]]
- [[SalesPersons]]
- [[SalesQuotationDetails]]
- [[SalesQuotationHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
