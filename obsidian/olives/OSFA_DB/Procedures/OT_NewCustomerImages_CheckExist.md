---
type: procedure
database: OSFA_DB
name: OT_NewCustomerImages_CheckExist
schema: dbo
tags: [#customer, #mobile]
reads_from:
  - [[OT_NewCustomerImages]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_NewCustomerImages_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_NewCustomerImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @NewCustSysID VARCHAR(50)
- @ImageSerial bigint
- @ImageType_ID int
- @SysID  VARCHAR(50)
- @ErrNo SmallInt Output
- @Exist SmallInt Output
## Tables Read
- [[OT_NewCustomerImages]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_NewCustomerImages]]

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
