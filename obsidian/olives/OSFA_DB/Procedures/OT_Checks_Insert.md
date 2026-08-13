---
type: procedure
database: OSFA_DB
name: OT_Checks_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_Checks]]
writes_to:
  - [[OT_Checks]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Checks_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Checks. Writes OT_Checks. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @ChqNo int
- @BankNo int
- @BranchNo int
- @CustomerNo bigint
- @DueDate smalldatetime
- @ChqAmount float
- @ErrNo SmallInt Output
- @Drawer nvarchar(200)
- @IsGero bit=0
- @CustBankAccNo	nvarchar(200)=''
- @AC_Payee bit=0
## Tables Read
- [[OT_Checks]]
## Tables Written
- [[OT_Checks]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Checks]]

**Tables Written**
- [[OT_Checks]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
