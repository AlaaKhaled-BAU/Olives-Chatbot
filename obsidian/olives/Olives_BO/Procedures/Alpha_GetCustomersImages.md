---
type: procedure
database: Olives_BO
name: Alpha_GetCustomersImages
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[Customers]]
  - `dbo`
writes_to:
  - [[Customers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_GetCustomersImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, dbo. Writes Customers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Customers]]
- `dbo`
## Tables Written
- [[Customers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- dbo

**Tables Written**
- [[Customers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
