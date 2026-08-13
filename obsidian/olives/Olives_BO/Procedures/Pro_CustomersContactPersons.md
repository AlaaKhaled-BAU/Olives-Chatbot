---
type: procedure
database: Olives_BO
name: Pro_CustomersContactPersons
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[CustomersContactPersons]]
  - [[CustomersContactPersonsLink]]
writes_to:
  - [[CustomersContactPersons]]
  - [[CustomersContactPersonsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersContactPersons


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersContactPersons, CustomersContactPersonsLink. Writes CustomersContactPersons, CustomersContactPersonsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @CustomerID bigint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)=null
- @ContactPersonID int=null
## Tables Read
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLink]]
## Tables Written
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLINK]]

**Tables Written**
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLINK]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
