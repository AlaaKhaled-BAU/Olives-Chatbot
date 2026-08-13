---
type: procedure
database: OSFA_DB
name: OT_Payment_Currency_Insert
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_Payment_Currency]]
writes_to:
  - [[OT_Payment_Currency]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payment_Currency_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Payment_Currency. Writes OT_Payment_Currency. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @CurrID int
- @Amount float
- @CurrRate float
- @ErrNo smallint output
## Tables Read
- [[OT_Payment_Currency]]
## Tables Written
- [[OT_Payment_Currency]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Payment_Currency]]

**Tables Written**
- [[OT_Payment_Currency]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
