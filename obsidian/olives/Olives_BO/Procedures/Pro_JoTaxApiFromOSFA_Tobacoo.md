---
type: procedure
database: Olives_BO
name: Pro_JoTaxApiFromOSFA_Tobacoo
schema: dbo
tags: [#backoffice, #billing, #integration, #legal]
reads_from:
  - [[Items]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_JoTaxApiFromOSFA_Tobacoo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @TransactionYear smallint = 2025
- @TransactionNo int = 1300300111
- @TransactionTypeID smallint = 1
## Tables Read
- [[Items]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
