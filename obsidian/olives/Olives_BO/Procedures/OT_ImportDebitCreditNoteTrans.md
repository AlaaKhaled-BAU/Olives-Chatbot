---
type: procedure
database: Olives_BO
name: OT_ImportDebitCreditNoteTrans
schema: dbo
tags: [#backoffice, #billing, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[DebitCreditNoteTrans]]
  - Header
  - `dbo`
writes_to:
  - [[DebitCreditNoteTrans]]
  - [[OT_DebitCreditNoteTrans]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportDebitCreditNoteTrans


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, DebitCreditNoteTrans, Header, dbo. Writes DebitCreditNoteTrans, OT_DebitCreditNoteTrans. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[ClientsActive]]
- [[DebitCreditNoteTrans]]
- Header
- `dbo`
## Tables Written
- [[DebitCreditNoteTrans]]
- [[OT_DebitCreditNoteTrans]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[DebitCreditNoteTrans]]
- Header
- dbo

**Tables Written**
- [[DebitCreditNoteTrans]]
- [[OT_DebitCreditNoteTrans]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
