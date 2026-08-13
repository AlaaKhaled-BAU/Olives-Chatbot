---
type: procedure
database: Olives_BO
name: OT_ImportBankDeposit
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
  - BankDepositDF
  - BankDepositHF
  - Receipts
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# OT_ImportBankDeposit

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 3. See sections below for the full dependency map.
## Parameters
- @CompanyID int
## Tables Read
_None_
## Tables Written
- [[BankDepositDF]]
- [[BankDepositHF]]
- [[Receipts]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_BankDepositDF|OT_BankDepositDF]]
- [[OSFA_DB/Tables/OT_BankDepositHF|OT_BankDepositHF]]
## Callers
_None_
## Callees
_None_
## When to Run

Run when importing data from tablets/external files into the back-office (batch or scheduled import).

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
