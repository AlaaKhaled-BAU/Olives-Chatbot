---
type: procedure
database: Olives_BO
name: QR_SCAN_OSFA_MOBILE
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[Companies]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# QR_SCAN_OSFA_MOBILE


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @comp varchar(100)='6459D311-59ED-480D-8ECD-76E8A2815C47',@cmd
## Tables Read
- [[Companies]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
