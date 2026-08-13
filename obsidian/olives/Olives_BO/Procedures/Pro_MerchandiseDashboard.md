---
type: procedure
database: Olives_BO
name: Pro_MerchandiseDashboard
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
  - Fun_GetSalesPersonFullTree
  - Fun_GetSalesmanTreeByID
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - RankedItems
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MerchandiseDashboard


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, Companies, Currencies, Customers, CustomersFinancialDetails, CustomersGPSLocations, Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser, Fun_GetSalesPersonFullTree, Fun_GetSalesmanTreeByID, Items, OrdersDetails, OrdersHeaders, RankedItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @CmdType nvarchar(50) = null
- @UserID nvarchar(50) = null
- @RepresentativesPeriod smallint = 0
- @AvgTimeAtClientPeriod smallint = 0
- @TotalVisitsPeriod smallint = 0
- @TotalSalesPeriod smallint = 0
- @TotalCollectionsPeriod smallint = 0
- @CovneragePercPeriod smallint = 0
- @TopVisitedClientsPeriod smallint = 0
- @TopVisitedSalespersonPeriod smallint = 0
- @SalesmanPeriod smallint = 0
- @TopSalesItemsPeriod smallint = 0
- @TopSalesSalesmanPeriod smallint = 0
- @TopSalesCustomersPeriod smallint = 0
- @AVGUPricePeriod smallint = 0
- @IsIncludeTax bit = 0
- @IsByDate bit = 0
- @PeriodType smallint = 2
- @FromDate smalldatetime =NULL
- @ToDate smalldatetime =NULL
- @Groups nvarchar(500) = ''-1,''
- @FromSalesperson int=0
- @ToSalesperson int=999999
- @FromLocation int =0
- @ToLocation int=999999
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesPersonFullTree
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- RankedItems
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesPersonFullTree
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- RankedItems

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
