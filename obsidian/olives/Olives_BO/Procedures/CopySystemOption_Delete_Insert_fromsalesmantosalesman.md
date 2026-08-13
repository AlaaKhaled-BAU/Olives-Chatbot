---
type: procedure
database: Olives_BO
name: CopySystemOption_Delete_Insert_fromsalesmantosalesman
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - OSFA_DB
  - `dbo`
writes_to:
  - [[OT_SystemOptions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# CopySystemOption_Delete_Insert_fromsalesmantosalesman


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OSFA_DB, dbo. Writes OT_SystemOptions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @companyid int
- @SourceSalesManid int, /* المندوب المصدر*/
- @DistinationSalesMan int /*   المندوب المستهدف*/
## Tables Read
- OSFA_DB
- `dbo`
## Tables Written
- [[OT_SystemOptions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- OSFA_DB
- dbo

**Tables Written**
- [[OT_SystemOptions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
