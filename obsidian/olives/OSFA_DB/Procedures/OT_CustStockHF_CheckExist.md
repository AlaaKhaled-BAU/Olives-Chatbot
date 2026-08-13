---
type: procedure
database: OSFA_DB
name: OT_CustStockHF_CheckExist
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_CustStockHF]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustStockHF_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_CustStockHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @VouDate smalldatetime
- @SalesmanNo smallint
- @CustomerNo varchar(50)
- @Posted bit
- @Notes varchar (200)
- @GPSX varchar (50)
- @GPSY varchar (50)
- @ErrNo SmallInt Output
- @Exist SmallInt Output
- @TabletSysID	varchar(50)=''
## Tables Read
- [[OT_CustStockHF]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_CustStockHF]]

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
