---
type: procedure
database: Olives_BO
name: MaintinanceOrders_Insert
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[MaintinanceOrders]]
writes_to:
  - [[MaintinanceOrders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# MaintinanceOrders_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MaintinanceOrders. Writes MaintinanceOrders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesmanNo int
- @CustomerID bigint=null
- @CustTel varchar (500)=null
- @ContactPerson varchar (500)=null
- @LicencePersonName varchar (500)=null
- @CommercialCustName varchar (500)=null
- @MaintenanceOrderType int=null
- @FavouriteVisitTime varchar (500)=null
- @CustRefrigerator varchar (4000)=null
- @NewCustName varchar (500)=null
- @NewLicenceCustName varchar (500)=null
- @NewContactPerson varchar (500)=null
- @NewCommercialCustName varchar (500)=null
- @NewCustTel varchar (500)=null
- @CustRefrigeratorNo varchar (500)=null
- @ContractNo varchar (500)=null
- @Diagnostic varchar (4000)=null
- @MaintenanceNotes varchar (MAX)=null
- @RefrigeratorSerialNo varchar (500)=null
- @RefrigeratorModel varchar (500)=null
- @RefrigeratorDrawReasonID int=null
- @RefrigeratorDrawReasonNotes varchar (MAX)=null
- @DeviceSysID varchar (50)=null
- @CustomerHasBeenVisited bit=null
- @SupervisorNotes nvarchar (MAX)=null
- @EvaluatingCustomerSite nvarchar (MAX)=null
- @EvaluatingCustomerWithdrawals nvarchar (MAX)=null
- @EvaluatingCustomerFinancialPosition nvarchar (MAX)=null
- @CustomerAgreement nvarchar (MAX)=null
- @ErrNo SmallInt Output
## Tables Read
- [[MaintinanceOrders]]
## Tables Written
- [[MaintinanceOrders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MaintinanceOrders]]

**Tables Written**
- [[MaintinanceOrders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
