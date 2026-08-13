---
type: procedure
database: OSFA_DB
name: OT_BankDepositDF_Insert
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
  - OT_BankDepositDF
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OT_BankDepositDF_Insert

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in OSFA_DB — writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @RecYear smallint
- @RecType smallint
- @RecNo int
- @RecAmount float
- @ErrNo smallint OUTPUT
## Tables Read
_None_
## Tables Written
- [[OT_BankDepositDF]]
## Cross-DB Tables
References tables in **Olives_BO** (qualified as `Olives_BO.dbo.*`):
- [[Olives_BO/Tables/Receipts|Receipts]]
## Callers
_None_
## Callees
- `Fun_GetImportTransInServerDate`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
