---
type: procedure
database: Olives_BO
name: Pro_SalesPersons
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[BusinessUnits]]
  - [[ClientsActive]]
  - [[CompanyBranches]]
  - [[CompanyParameters]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[DeliveryCars]]
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsUnits]]
  - Level
  - [[LogActionTransaction]]
  - [[Nairoukh_Awtar_SalespersonsExemptions]]
writes_to:
  - Level
  - [[Notifications]]
  - [[OT_SystemOptions]]
  - [[PromotionsSalesmanGroupsLink]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - SalesPersonsLog
called_by:
  - [[OT_SendSalesmanData]]
  - [[Pro_SystemOptions]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Salesman-Onboarding
---
# Pro_SalesPersons


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, ClientsActive, CompanyBranches, CompanyParameters, Customers, CustomersClasses, CustomersFinancialDetails, DeliveryCars, Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser, Items, ItemsUnits, Level, LogActionTransaction, Nairoukh_Awtar_SalespersonsExemptions. Writes Level, Notifications, OT_SystemOptions, PromotionsSalesmanGroupsLink, SalesPersons, SalesPersonsGroups, SalesPersonsLog. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ID int = null
- @Name nvarchar (200)=null
- @ForeignName nvarchar (200)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (100)=null
- @Parent Int = null
- @BusinessUnitID Int = null
- @GroupID int  = null
- @CashBoxAccount nvarchar(20) = null
- @DebitAccount nvarchar(20) = null
- @DeviceID nvarchar(50) = null
- @Longitude nvarchar(50) = null
- @Latitude nvarchar(50) = null
- @SalesPersonType int = null
- @TelephoneNo nvarchar(50) = null
- @Email nvarchar(100) = null
- @IsSuspended bit = null
- @PositionID Int= null
- @DayOff nvarchar(100) = '0'
- @Level int = null
- @SupervisorArray varchar(max) = null
- @SendDate smalldatetime = null
- @UserID nvarchar(50) = null
- @TargetMonth int = null
- @SalesPersonID int = null
- @TargetYear int = null
- @cmdType varchar(50)='Select All Supervisor'
- @CompanyBrancheID int =null
- @CreditLimit float = null
- @MaxLoadOrderAmount float = null
- @Autosenddata bit = null
- @VehicleNumber varchar(100)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @UserIDLog nvarchar(50) = null
- @PCName varchar(100)=null
- @CustCalssArray Nvarchar (MAX) =NULL
- @PromotionID int = null
- @RouteCheck bit = null
- @IsChecked bit = null
- @StoreNo int = null
- @CarID int = null
- @ItemGroup int = null
- @MonthlyAllowedDiscountValue float = null
- @Supervisor varchar(100)='7,27,6003'
## Tables Read
- [[BusinessUnits]]
- [[ClientsActive]]
- [[CompanyBranches]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[DeliveryCars]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
- Level
- [[LogActionTransaction]]
- [[Nairoukh_Awtar_SalespersonsExemptions]]
## Tables Written
- Level
- [[Notifications]]
- [[OT_SystemOptions]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- SalesPersonsLog
## Callers
_None (no known callers)_
## Callees
- [[OT_SendSalesmanData]]
- [[Pro_SystemOptions]]
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[ClientsActive]]
- [[CompanyBranches]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[DeliveryCars]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
- Level
- [[LogActionTransaction]]
- [[Nairoukh_Awtar_SalespersonsExemptions]]

**Tables Written**
- Level
- [[Notifications]]
- [[ot_systemoptions]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- SalesPersonsLog

**Callers**
- [[OT_SendSalesmanData]]
- [[Pro_SystemOptions]]

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
