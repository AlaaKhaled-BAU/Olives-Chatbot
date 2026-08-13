---
type: procedure
database: Olives_BO
name: OT_ImportReprintedTransactions
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[ReprintedTransactions]]
  - `dbo`
writes_to:
  - [[OT_ReprintedTransactions]]
  - [[ReprintedTransactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportReprintedTransactions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ReprintedTransactions, dbo. Writes OT_ReprintedTransactions, ReprintedTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[ReprintedTransactions]]
- `dbo`
## Tables Written
- [[OT_ReprintedTransactions]]
- [[ReprintedTransactions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ReprintedTransactions]]
- dbo

**Tables Written**
- [[OT_ReprintedTransactions]]
- [[ReprintedTransactions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
