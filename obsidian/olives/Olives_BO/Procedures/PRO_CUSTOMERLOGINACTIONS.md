---
type: procedure
database: Olives_BO
name: PRO_CUSTOMERLOGINACTIONS
schema: dbo
tags: [#auth, #backoffice, #customer, #log]
reads_from:
  - [[CustomerLoginActions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# PRO_CUSTOMERLOGINACTIONS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerLoginActions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[CustomerLoginActions]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerLoginActions]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
