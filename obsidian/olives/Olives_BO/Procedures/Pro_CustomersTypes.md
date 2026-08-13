---
type: procedure
database: Olives_BO
name: Pro_CustomersTypes
schema: dbo
tags: [#backoffice, #customer, #reference]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - `dbo`
writes_to:
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - CustomersTypesLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersTypes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, CustomersTypes, dbo. Writes CustomersFinancialDetails, CustomersTypes, CustomersTypesLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @SalesOrderLimit nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- `dbo`
## Tables Written
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- CustomersTypesLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- dbo

**Tables Written**
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- CustomersTypesLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
