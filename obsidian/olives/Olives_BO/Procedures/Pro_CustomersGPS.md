---
type: procedure
database: Olives_BO
name: Pro_CustomersGPS
schema: dbo
tags: [#backoffice, #customer, #gps]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - [[Locations]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Customers]]
  - [[CustomersGPSLocations]]
  - [[OT_GPSLog]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersGPS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, CustomersGPSLocations, Locations, SalesPersons, dbo. Writes Customers, CustomersGPSLocations, OT_GPSLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @LineID int=null
- @cmdType varchar(50)=null
- @Address nvarchar(max)=null
- @CustID bigint = null
- @SalesmanID int = null
- @CustTypeID int = null
- @Latitude nvarchar(50) = null
- @TransDate datetime = null
- @LocationID int =null
- @Longitude nvarchar(50) = null
- @FromDate date ='2020-01-01'
- @ToDate date ='2020-08-15'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- [[Locations]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Customers]]
- [[CustomersGPSLocations]]
- [[OT_GPSLog]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- [[Locations]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Customers]]
- [[CustomersGPSLocations]]
- [[OT_GPSLog]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
