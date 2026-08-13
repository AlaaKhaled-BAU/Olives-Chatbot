---
type: procedure
database: Olives_BO
name: Rpt_RejectedTrans
schema: dbo
tags: [#reporting]
reads_from:
  - Items
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Rpt_RejectedTrans

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s). See sections below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Items]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_Checks|OT_Checks]]
- [[OSFA_DB/Tables/OT_ConsOrderDF|OT_ConsOrderDF]]
- [[OSFA_DB/Tables/OT_ConsOrderHF|OT_ConsOrderHF]]
- [[OSFA_DB/Tables/OT_InvoiceDF|OT_InvoiceDF]]
- [[OSFA_DB/Tables/OT_InvoiceHF|OT_InvoiceHF]]
- [[OSFA_DB/Tables/OT_OrderDF|OT_OrderDF]]
- [[OSFA_DB/Tables/OT_OrderHF|OT_OrderHF]]
- [[OSFA_DB/Tables/OT_Payments|OT_Payments]]
## Callers
_None_
## Callees
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
