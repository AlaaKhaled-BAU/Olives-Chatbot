---
type: procedure
database: Olives_BO
name: Pro_ExportCustomersImages
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[Customers]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ExportCustomersImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Reference2 NVARCHAR(50)
- @CompanyID SMALLINT
- @Cmd NVARCHAR(50)
## Tables Read
- [[Customers]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- dbo

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
