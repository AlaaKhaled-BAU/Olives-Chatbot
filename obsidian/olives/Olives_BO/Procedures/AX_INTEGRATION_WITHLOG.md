---
type: procedure
database: Olives_BO
name: AX_INTEGRATION_WITHLOG
schema: dbo
tags: [#backoffice, #integration, #log]
reads_from:
  - [[Companies]]
  - Cur_Banks
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AX_INTEGRATION_WITHLOG


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Cur_Banks, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Companies]]
- Cur_Banks
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- Cur_Banks
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
