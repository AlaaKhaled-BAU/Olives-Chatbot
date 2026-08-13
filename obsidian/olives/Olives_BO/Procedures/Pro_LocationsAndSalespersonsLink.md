---
type: procedure
database: Olives_BO
name: Pro_LocationsAndSalespersonsLink
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[Assets]]
  - [[AssetsCustomerLink]]
  - [[ClientsActive]]
  - Cust
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - Fun_GetAssetsBalance
  - [[Locations]]
  - [[SalesPersons]]
writes_to:
  - [[Assets]]
  - [[CustomersFinancialDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_LocationsAndSalespersonsLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsCustomerLink, ClientsActive, Cust, Customers, CustomersFinancialDetails, CustomersGPSLocations, Fun_GetAssetsBalance, Locations, SalesPersons. Writes Assets, CustomersFinancialDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @AssetID smallint = null
- @AssetName varchar(500) =null
- @AssetType int = null
- @CustomerID bigint = null
- @StoreNo int = null
- @AssetSerial nvarchar(50)=null
- @Status int = null
- @Notes nvarchar(500)= null
- @AssetValue float = null
- @AssetVolume float = null
- @Reference1 nvarchar (50)=null
- @Reference2 nvarchar (50)=null
- @cmdType varchar(50)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
- @AssignCustomersToSalesman AssignCustomersToSalesman ReadOnly
- @UnAssignPositionsIDs AssignCustomersToSalesman ReadOnly
- @PositionsID int = null
- @SalesPersonID int = null
- @ClassID int=null
- @LocationID int = null
## Tables Read
- [[Assets]]
- [[AssetsCustomerLink]]
- [[ClientsActive]]
- Cust
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_GetAssetsBalance
- [[Locations]]
- [[SalesPersons]]
## Tables Written
- [[Assets]]
- [[CustomersFinancialDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Assets]]
- [[AssetsCustomerLink]]
- [[ClientsActive]]
- Cust
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_GetAssetsBalance
- [[Locations]]
- [[SalesPersons]]

**Tables Written**
- [[Assets]]
- [[CustomersFinancialDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
