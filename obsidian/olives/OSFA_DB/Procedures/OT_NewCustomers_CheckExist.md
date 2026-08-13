---
type: procedure
database: OSFA_DB
name: OT_NewCustomers_CheckExist
schema: dbo
tags: [#customer, #mobile]
reads_from:
  - [[OT_NewCustomers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_NewCustomers_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_NewCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo	smallint
- @SalesmanNo	smallint
- @CustName	varchar(150)
- @Address	varchar(150)
- @Tel	varchar(50)
- @Mobile	varchar(50)
- @Contact	varchar(50)
- @Email	varchar(50)
- @GPSX	varchar(50)
- @GPSY	varchar(50)
- @Notes	nvarchar(200)
- @SysID	nvarchar(200)
- @Exist SmallInt Output
## Tables Read
- [[OT_NewCustomers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_NewCustomers]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
