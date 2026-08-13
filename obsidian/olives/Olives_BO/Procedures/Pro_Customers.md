---
type: procedure
database: Olives_BO
name: Pro_Customers
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[AssetsCustomerLink]]
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersContactPersons]]
  - [[CustomersContactPersonsLink]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - [[CustomersGroups]]
  - [[CustomersPromotionsExceptions]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - [[CustomersTypes]]
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
writes_to:
  - [[Customers]]
  - CustomersImages
  - [[CustomersLog]]
  - [[CustomersPromotionsExceptions]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - CustomersSignatures
  - [[PromotionsCustomersGroupsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows: [[Customer-Setup]]
---
# Pro_Customers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AssetsCustomerLink, ClientsActive, Customers, CustomersClasses, CustomersContactPersons, CustomersContactPersonsLink, CustomersFinancialDetails, CustomersGPSLocations, CustomersGroups, CustomersPromotionsExceptions, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, CustomersTypes, Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser. Writes Customers, CustomersImages, CustomersLog, CustomersPromotionsExceptions, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, CustomersSignatures, PromotionsCustomersGroupsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ID bigint = null
- @Name nvarchar (200)=null
- @ForeignName nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (100)=null
- @TypeID int=null
- @LocationID int=2
- @Account nvarchar(50) = null
- @Barcode nvarchar(20) = null
- @Contact nvarchar(100) = null
- @TelephoneNo nvarchar(50) = null
- @MobileNo nvarchar(50) = null
- @FaxNo nvarchar(50) = null
- @POBox nvarchar(50) = null
- @Address nvarchar(200) = null
- @SuspendedReason nvarchar(200) = null
- @Latitude nvarchar(50) = null
- @Longitude nvarchar(50) = null
- @WebSite nvarchar(100) = null
- @Email nvarchar(100) = null
- @IsSuspended bit = null
- @UserID nvarchar(20) = null
- @Password nvarchar(20) = null
- @RouteID int = null
- @PriceListID NVarChar(1000) = null
- @Group_ID int = null
- @cmdType varchar(50)='Select All'
- @CustomerImage image=null
- @CustomersType nvarchar(100) = null
- @Balance float = null
- @SendInvByEmail bit = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserIDLog nvarchar(100)='admin'
- @Class_ID int =null
- @PromotionID int = null
- @CarType int = null
- @DayOff nvarchar(100) = '0'
- @IsChecked bit = null
- @PriceListID_Tmp int = null
- @FormRoute  int = 0
- @ToRoute  int = 99999
- @LocationIDs nvarchar(max) = '3,1,6,'
- @TaxNumber nvarchar(100) = null
## Tables Read
- [[AssetsCustomerLink]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLink]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- [[CustomersGroups]]
- [[CustomersPromotionsExceptions]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
## Tables Written
- [[Customers]]
- CustomersImages
- [[CustomersLog]]
- [[CustomersPromotionsExceptions]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- CustomersSignatures
- [[PromotionsCustomersGroupsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[AssetsCustomerLink]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLink]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- [[CustomersGroups]]
- [[CustomersPromotionsExceptions]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser

**Tables Written**
- [[Customers]]
- CustomersImages
- [[CustomersLog]]
- [[CustomersPromotionsExceptions]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- CustomersSignatures
- [[PromotionsCustomersGroupsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
