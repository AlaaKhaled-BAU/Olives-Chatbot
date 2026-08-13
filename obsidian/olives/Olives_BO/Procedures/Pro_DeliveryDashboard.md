---
type: procedure
database: Olives_BO
name: Pro_DeliveryDashboard
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[Checks]]
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - Fun_GetSalesmanTreeByID
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Items]]
  - [[LogActionTransaction]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalespersonsGPSTracking]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DeliveryDashboard


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Companies, Currencies, Customers, Fun_GetSalesmanTreeByID, InvoiceDeliveryDF, InvoiceDeliveryHF, Items, LogActionTransaction, Receipts, SalesPersons, SalespersonsGPSTracking, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @CmdType nvarchar(50) = 'HeaderData'
- @UserID nvarchar(50) = 'admin'
- @RepresentativesPeriod smallint = 0
- @AvgTimeAtClientPeriod smallint = 0
- @TotalVisitsPeriod smallint = 0
- @TotalSalesPeriod smallint = 0
- @TotalCollectionsPeriod smallint = 0
- @CoveragePercPeriod smallint = 0
- @TopVisitedClientsPeriod smallint = 0
- @TopVisitedSalespersonPeriod smallint = 0
- @SalesmanPeriod smallint = 0
- @TopSalesItemsPeriod smallint = 0
- @TopSalesSalesmanPeriod smallint = 0
- @TopSalesCustomersPeriod smallint = 0
- @AVGUPricePeriod smallint = 0
- @IsIncludeTax bit = 0
- @IsByDate bit = 1
- @PeriodType smallint = 2
- @FromDate smalldatetime = '2000-01-01'
- @ToDate smalldatetime = '2022-06-01'
- @FromGroup int = 0
- @ToGroup int = 999999999
## Tables Read
- [[Checks]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- Fun_GetSalesmanTreeByID
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[LogActionTransaction]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalespersonsGPSTracking]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- Fun_GetSalesmanTreeByID
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[LogActionTransaction]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalespersonsGPSTracking]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

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
