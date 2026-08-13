---
type: procedure
database: OSFA_DB
name: OT_BankDepositDF_CheckExist
schema: dbo
tags: [#maintenance]
reads_from:
  - OT_BankDepositDF
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OT_BankDepositDF_CheckExist

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in OSFA_DB — reads 1 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @RecYear smallint
- @RecType smallint
- @RecNo int
- @ErrNo smallint OUTPUT
- @Exist smallint OUTPUT
## Tables Read
- [[OT_BankDepositDF]]
## Tables Written
_None_
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
