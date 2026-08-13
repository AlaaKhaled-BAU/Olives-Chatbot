---
type: procedure
database: Olives_BO
name: OT_AppCarAndSalesperson
schema: dbo
tags: [#backoffice, #mobile, #sales]
reads_from:
  - [[CarAndSalespersonLink]]
  - [[DeliveryCars]]
  - Fun_GetCompanyBranchesByUser
  - [[SalesPersons]]
  - [[Users]]
writes_to:
  - [[CarAndSalespersonLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_AppCarAndSalesperson


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CarAndSalespersonLink, DeliveryCars, Fun_GetCompanyBranchesByUser, SalesPersons, Users. Writes CarAndSalespersonLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @CmdType nvarchar(200)='GetDeliveryCars'
- @SalesmanNo int = 117
- @TabletSysID varchar(100)=null
- @Password nvarchar(100) = '123'
- @UserName nvarchar(100) = 'Adnan'
- @CarID nvarchar(100) = '4'
- @WorkingDate smalldatetime='2020-1-1'
- @DriverID nvarchar(100) = '6007'
- @SalespersonID nvarchar(100) = '1'
- @AssistantID nvarchar(100) = '4030'
- @Barcode nvarchar(100) = '4030'
- @LocationID nvarchar(100) = '4'
- @ErrNo SmallInt  =0 OUTPUT
- @Exist SmallInt  =0 OUTPUT
- @AutoID	numeric(18, 0)=0
- @UserID nvarchar (20)=admin
## Tables Read
- [[CarAndSalespersonLink]]
- [[DeliveryCars]]
- Fun_GetCompanyBranchesByUser
- [[SalesPersons]]
- [[Users]]
## Tables Written
- [[CarAndSalespersonLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CarAndSalespersonLink]]
- [[DeliveryCars]]
- Fun_GetCompanyBranchesByUser
- [[SalesPersons]]
- [[Users]]

**Tables Written**
- [[CarAndSalespersonLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
