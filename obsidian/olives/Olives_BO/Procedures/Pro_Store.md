---
type: procedure
database: Olives_BO
name: Pro_Store
schema: dbo
tags: [#backoffice]
reads_from:
  - [[ERPStores]]
writes_to:
  - [[ERPStores]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Store


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ERPStores. Writes ERPStores. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @cmdType Varchar(50)=null
- @StoreNo int = null
- @ArDesc Varchar(100) = null
## Tables Read
- [[ERPStores]]
## Tables Written
- [[ERPStores]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ERPStores]]

**Tables Written**
- [[ERPStores]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
