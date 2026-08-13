---
type: procedure
database: OSFA_DB
name: OT_EditCustomerTrans_Insert
schema: dbo
tags: [#customer, #mobile]
reads_from:
  - [[OT_EditCustomerTrans]]
  - `dbo`
writes_to:
  - [[OT_EditCustomerTrans]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_EditCustomerTrans_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_EditCustomerTrans, dbo. Writes OT_EditCustomerTrans. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @CustomerNo bigint
- @TabletSysID nvarchar(50)
- @CustClass int
- @Tel nvarchar(50)=''
- @FullAddress nvarchar(500)=''
- @ContactPerson nvarchar(100)=''
- @Notes nvarchar(MAX)=''
- @AssetsRef1 nvarchar(50)=''
- @AssetsRef2 nvarchar(50)=''
- @VerificationCode nvarchar(50)=''
- @ErrNo SmallInt Output
## Tables Read
- [[OT_EditCustomerTrans]]
- `dbo`
## Tables Written
- [[OT_EditCustomerTrans]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_EditCustomerTrans]]
- dbo

**Tables Written**
- [[OT_EditCustomerTrans]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
