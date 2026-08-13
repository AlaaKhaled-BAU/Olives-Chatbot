---
type: procedure
database: OSFA_DB
name: OT_EditCustomerTrans_Verify
schema: dbo
tags: [#customer, #mobile]
reads_from:
  - [[OT_EditCustomerTrans]]
writes_to:
  - [[OT_EditCustomerTrans]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_EditCustomerTrans_Verify


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_EditCustomerTrans. Writes OT_EditCustomerTrans. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @SalesmanNo int=3003
- @CustomerNo bigint=314
- @TabletSysID nvarchar(50)='3003_2022011610555439'
- @VerificationCode nvarchar(50)='405162179'
- @Res SmallInt=0 Output
## Tables Read
- [[OT_EditCustomerTrans]]
## Tables Written
- [[OT_EditCustomerTrans]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_EditCustomerTrans]]

**Tables Written**
- [[OT_EditCustomerTrans]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
