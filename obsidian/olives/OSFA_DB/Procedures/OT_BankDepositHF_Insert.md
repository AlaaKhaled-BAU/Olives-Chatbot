---
type: procedure
database: OSFA_DB
name: OT_BankDepositHF_Insert
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
  - OT_BankDepositHF
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OT_BankDepositHF_Insert

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in OSFA_DB — writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @SalesmanNo smallint
- @BankNo int
- @BranchNo int
- @Notes varchar(200)
- @VouDate smalldatetime
- @TrDateTime smalldatetime
- @GPSX varchar(50)
- @GPSY varchar(50)
- @IsPosted bit
- @ErrNo smallint OUTPUT
- @TabSysID varchar(50)
## Tables Read
_None_
## Tables Written
- [[OT_BankDepositHF]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetImportTransInServerDate`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
