---
type: procedure
database: Olives_BO
name: X3_INTEGRATION_WITHLOG
schema: dbo
tags: [#backoffice, #integration, #log]
reads_from:
  - [[Banks]]
  - [[Companies]]
  - Cur_Banks
  - Cur_Branches
  - [[IntegrationErrorLog]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# X3_INTEGRATION_WITHLOG


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Companies, Cur_Banks, Cur_Branches, IntegrationErrorLog, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Banks]]
- [[Companies]]
- Cur_Banks
- Cur_Branches
- [[IntegrationErrorLog]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Companies]]
- Cur_Banks
- Cur_Branches
- [[IntegrationErrorLog]]
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
