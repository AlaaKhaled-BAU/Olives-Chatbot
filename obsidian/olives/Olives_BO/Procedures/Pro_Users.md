---
type: procedure
database: Olives_BO
name: Pro_Users
schema: dbo
tags: [#auth, #backoffice]
reads_from:
  - [[Companies]]
  - [[CompanyParameters]]
  - Last
  - [[OlivesUserPermissions]]
  - [[SalesPersons]]
  - [[Users]]
  - [[UsersCloseDate]]
  - `dbo`
writes_to:
  - FailedLoginLog
  - Last
  - [[Users]]
called_by:
  - [[SMS_Niroukh]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Users-and-Permissions
---
# Pro_Users


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, CompanyParameters, Last, OlivesUserPermissions, SalesPersons, Users, UsersCloseDate, dbo. Writes FailedLoginLog, Last, Users. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @UserID nvarchar(50)=null
- @UserPWD nvarchar(50)=null
- @UserName nvarchar(100)=null
- @IsSuspended bit=null
- @LastLoginDate smalldatetime = null
- @PhoneNo nvarchar(50) = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @cmdType varchar(50)=null
- @TrType int = null
- @AllPromotion bit=null
- @IsSuccess bit=null
- @Email nvarchar(50)=null
## Tables Read
- [[Companies]]
- [[CompanyParameters]]
- Last
- [[OlivesUserPermissions]]
- [[SalesPersons]]
- [[Users]]
- [[UsersCloseDate]]
- `dbo`
## Tables Written
- FailedLoginLog
- Last
- [[Users]]
## Callers
_None (no known callers)_
## Callees
- [[SMS_Niroukh]]
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[CompanyParameters]]
- Last
- [[OlivesUserPermissions]]
- [[SalesPersons]]
- [[Users]]
- [[UsersCloseDate]]
- dbo

**Tables Written**
- FailedLoginLog
- Last
- [[Users]]

**Callers**
- [[SMS_Niroukh]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
