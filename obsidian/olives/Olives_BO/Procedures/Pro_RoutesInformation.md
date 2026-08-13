---
type: procedure
database: Olives_BO
name: Pro_RoutesInformation
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - Fun_Get_Salesmen_AssignedRoutes
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[RoutesInformation]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows: [[Route-Planning]]
---
# Pro_RoutesInformation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, Customers, CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, Fun_Get_Salesmen_AssignedRoutes, RoutesInformation, SalesPersons, dbo. Writes RoutesInformation. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ID int = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @SalesPersonID int = null
- @PositionID int = 3003
- @cmdType varchar(50)=null
- @UserID nvarchar(50) = 'ADMIN'
- @LocationID int = null
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- Fun_Get_Salesmen_AssignedRoutes
- [[RoutesInformation]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[RoutesInformation]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- Fun_Get_Salesmen_AssignedRoutes
- [[RoutesInformation]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[RoutesInformation]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
