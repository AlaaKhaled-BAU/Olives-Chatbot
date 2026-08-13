---
type: procedure
database: OSFA_DB
name: OT_Add_CustGalaryImages
schema: dbo
tags: [#mobile]
reads_from:
  - OLIVES_BO
  - [[OT_CustGalaryImages]]
  - Olives_Images
writes_to:
  - [[OT_CustGalaryImages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Add_CustGalaryImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OLIVES_BO, OT_CustGalaryImages, Olives_Images. Writes OT_CustGalaryImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo smallint
- @CustomerNo bigint
- @ImageData image
- @GPSX VARCHAR(50)
- @GPSY VARCHAR(50)
- @ErrNo SmallInt Output
- @ImageDate	smalldatetime=GETDATE
- @ImageType_ID int=0
- @PlanogramFileAutoID bigint=0
- @ImageSeqType int=0
- @Notes VARCHAR(50)=''
## Tables Read
- OLIVES_BO
- [[OT_CustGalaryImages]]
- Olives_Images
## Tables Written
- [[OT_CustGalaryImages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- OLIVES_BO
- [[OT_CustGalaryImages]]
- Olives_Images

**Tables Written**
- [[OT_CustGalaryImages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
