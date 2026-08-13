---
type: procedure
database: OSFA_DB
name: OT_Add_NewCustomerImages
schema: dbo
tags: [#customer, #mobile]
reads_from:
  - [[OT_NewCustomerImages]]
writes_to:
  - [[OT_NewCustomerImages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Add_NewCustomerImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_NewCustomerImages. Writes OT_NewCustomerImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @NewCustSysID VARCHAR(50)
- @ImageSerial bigint
- @ImageType_ID int
- @NewCustImage image
- @SysID  VARCHAR(50)
- @ErrNo SmallInt Output
## Tables Read
- [[OT_NewCustomerImages]]
## Tables Written
- [[OT_NewCustomerImages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_NewCustomerImages]]

**Tables Written**
- [[OT_NewCustomerImages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
