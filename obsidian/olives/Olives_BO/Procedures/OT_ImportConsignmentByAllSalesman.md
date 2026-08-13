---
type: procedure
database: Olives_BO
name: OT_ImportConsignmentByAllSalesman
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OT_ImportConsignmentByAllSalesman

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — standalone procedure. See sections below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_ConsOrderDF|OT_ConsOrderDF]]
- [[OSFA_DB/Tables/OT_ConsOrderHF|OT_ConsOrderHF]]
- [[OSFA_DB/Tables/OT_InvoiceDF|OT_InvoiceDF]]
## Callers
_None_
## Callees
_None_
## When to Run

Run when importing data from tablets/external files into the back-office (batch or scheduled import).

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
