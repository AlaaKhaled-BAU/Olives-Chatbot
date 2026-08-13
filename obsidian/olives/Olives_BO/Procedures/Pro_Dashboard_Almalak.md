---
type: procedure
database: Olives_BO
name: Pro_Dashboard_Almalak
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetMaxItemOrderBySalesman
  - Fun_GetMaxItemSalesBySalesman
  - Fun_GetSalesmanTreeByID
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalesPersonsRoutes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Dashboard_Almalak


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, CustomersFinancialDetails, Fun_GetMaxItemOrderBySalesman, Fun_GetMaxItemSalesBySalesman, Fun_GetSalesmanTreeByID, Items, ItemsCategories, ItemsUnits, OrdersDetails, OrdersHeaders, Receipts, SalesPersons, SalesPersonsGroups, SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @CmdType nvarchar(50) = 'GetDashboardData'
- @UserID nvarchar(50) = 'admin'
- @Category nvarchar(50) = null
- @SalesAndCollectionPeriod smallint = 3, 	-- 1:Daily, 2:Monthly, 3:Yearly
- @SalesAndOrdersPeriod smallint = 3,			-- 1:Daily, 2:Monthly, 3:Yearly
- @TopSalesCustomersPeriod smallint = 3,		-- 1:Daily, 2:Monthly, 3:Yearly
- @TopSalesItemsPeriod smallint = 3,			-- 1:Daily, 2:Monthly, 3:Yearly
- @TopVisitedClientsPeriod smallint = 3,		-- 1:Daily, 2:Monthly, 3:Yearly
- @TopVisitedSalespersonPeriod smallint = 3,	-- 1:Daily, 2:Monthly, 3:Yearly
- @TopFastAndSlowTrItemPeriod smallint = 3	-- 1:Daily, 2:Monthly, 3:Yearly
## Tables Read
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetMaxItemOrderBySalesman
- Fun_GetMaxItemSalesBySalesman
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetMaxItemOrderBySalesman
- Fun_GetMaxItemSalesBySalesman
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]

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
