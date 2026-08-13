---
type: procedure
database: Olives_BO
name: AppDashBoard
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Companies]]
  - [[CompanyParameters]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCategoryTreeByID
  - Fun_GetSalesmanTreeByID
  - Fun_SalesYearByMonth
  - [[Items]]
  - [[ItemsCategories]]
  - [[Locations]]
  - [[LogActionTransaction]]
  - [[OlivesUserPermissions]]
  - [[SalesPersonNewCustomersTargets]]
  - [[SalesPersonTargets]]
  - [[SalesPersons]]
writes_to:
  - tblCateg
  - tblLocation
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AppDashBoard


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, CompanyParameters, Customers, CustomersFinancialDetails, Fun_GetCategoryTreeByID, Fun_GetSalesmanTreeByID, Fun_SalesYearByMonth, Items, ItemsCategories, Locations, LogActionTransaction, OlivesUserPermissions, SalesPersonNewCustomersTargets, SalesPersonTargets, SalesPersons. Writes tblCateg, tblLocation. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2010-01-01'
- @ToDate smalldatetime = '2019-12-31'
- @SalesmanNo int = 3003
- @CmdType nvarchar(100) = 'Check Access'
- @IsSummary bit = 0
- @UserID nvarchar(50) = 'admin'
- @Password nvarchar(50) = '123'
- @CategCode nvarchar(100) = '23333'
- @FromYear int = 2010
- @ToYear int = 2017
- @Level int = 2
## Tables Read
- [[Companies]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCategoryTreeByID
- Fun_GetSalesmanTreeByID
- Fun_SalesYearByMonth
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[LogActionTransaction]]
- [[OlivesUserPermissions]]
- [[SalesPersonNewCustomersTargets]]
- [[SalesPersonTargets]]
- [[SalesPersons]]
## Tables Written
- tblCateg
- tblLocation
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
- Fun_GetCategoryTreeByID
- Fun_GetSalesmanTreeByID
- Fun_SalesYearByMonth
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[LogActionTransaction]]
- [[OlivesUserPermissions]]
- [[SalesPersonNewCustomersTargets]]
- [[SalesPersonTargets]]
- [[SalesPersons]]

**Tables Written**
- tblCateg
- tblLocation

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
