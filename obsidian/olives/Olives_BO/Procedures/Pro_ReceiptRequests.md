---
type: procedure
database: Olives_BO
name: Pro_ReceiptRequests
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[Companies]]
  - [[CompanyParameters]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - Fun_GetCompanyBranchesByUser
  - [[ReceiptRequests]]
  - [[ReceiptRequestsInvoicesLink]]
  - [[ReceiptRequestsSchedule]]
  - [[SalespersonsMessages]]
writes_to:
  - [[ReceiptRequests]]
  - [[ReceiptRequestsInvoicesLink]]
  - [[SalespersonsMessages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ReceiptRequests


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, CompanyParameters, Customers, CustomersFinancialDetails, CustomersPaidTransList, Fun_GetCompanyBranchesByUser, ReceiptRequests, ReceiptRequestsInvoicesLink, ReceiptRequestsSchedule, SalespersonsMessages. Writes ReceiptRequests, ReceiptRequestsInvoicesLink, SalespersonsMessages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @OrderYear smallint = null
- @OrderTypeID int = null
- @DocumentTypeID int = null
- @OrderNo int = null
- @PaidTransYear smallint = null
- @PaidTransTypeID int = null
- @PaidTransNo int = null
- @OrderDate smalldatetime =null
- @CustomerID bigint=null
- @Amount float=NULL
- @Notes nvarchar(500)=null
- @IsSettlement bit = null
- @OrderStatus int = null
- @PaymentType int = null
- @Priority bit = null
- @cmdType varchar(50)=null
- @FromDate smalldatetime =null
- @ToDate smalldatetime =null
- @UserID nvarchar(50) = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
## Tables Read
- [[Companies]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- Fun_GetCompanyBranchesByUser
- [[ReceiptRequests]]
- [[ReceiptRequestsInvoicesLink]]
- [[ReceiptRequestsSchedule]]
- [[SalespersonsMessages]]
## Tables Written
- [[ReceiptRequests]]
- [[ReceiptRequestsInvoicesLink]]
- [[SalespersonsMessages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- Fun_GetCompanyBranchesByUser
- [[ReceiptRequests]]
- [[ReceiptRequestsInvoicesLink]]
- [[ReceiptRequestsSchedule]]
- [[SalespersonsMessages]]

**Tables Written**
- [[ReceiptRequests]]
- [[ReceiptRequestsInvoicesLink]]
- [[SalespersonsMessages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
