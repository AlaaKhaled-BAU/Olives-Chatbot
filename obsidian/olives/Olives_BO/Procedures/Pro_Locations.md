---
type: procedure
database: Olives_BO
name: Pro_Locations
schema: dbo
tags: [#backoffice, #gps]
reads_from:
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - Level
  - [[Locations]]
  - [[SalesPersons]]
  - SplitString
  - `dbo`
writes_to:
  - Level
  - [[Locations]]
  - LocationsLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Locations


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersClasses, CustomersFinancialDetails, Level, Locations, SalesPersons, SplitString, dbo. Writes Level, Locations, LocationsLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ID int = null
- @Parent int = null
- @PopulationNo bigint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @ForeignName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)='Select All by CustomersClass'
- @Loc_Level int = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
- @SalesPersons varchar(100)='1,27,'
- @CustomersClass nvarchar(100)=1
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- Level
- [[Locations]]
- [[SalesPersons]]
- SplitString
- `dbo`
## Tables Written
- Level
- [[Locations]]
- LocationsLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- Level
- [[Locations]]
- [[SalesPersons]]
- SplitString
- dbo

**Tables Written**
- Level
- [[Locations]]
- LocationsLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
