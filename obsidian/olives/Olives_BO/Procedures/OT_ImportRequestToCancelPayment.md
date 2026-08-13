---
type: procedure
database: Olives_BO
name: OT_ImportRequestToCancelPayment
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
  - RequestToCancelPayment
  - WF_MasterLog
  - WF_SubLog
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# OT_ImportRequestToCancelPayment

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 3. See sections below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
_None_
## Tables Written
- [[RequestToCancelPayment]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_RequestToCancelPayment|OT_RequestToCancelPayment]]
## Callers
_None_
## Callees
_None_
## When to Run

Run when importing data from tablets/external files into the back-office (batch or scheduled import).

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
