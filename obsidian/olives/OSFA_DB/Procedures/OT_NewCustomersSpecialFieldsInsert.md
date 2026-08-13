---
type: procedure
database: OSFA_DB
name: OT_NewCustomersSpecialFieldsInsert
schema: dbo
tags: [#customer, #mobile]
reads_from:
  - [[OT_NewCustomers]]
  - [[OT_NewCustomersSpecialFields]]
writes_to:
  - [[OT_NewCustomersSpecialFields]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_NewCustomersSpecialFieldsInsert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_NewCustomers, OT_NewCustomersSpecialFields. Writes OT_NewCustomersSpecialFields. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @FieldID	int
- @FieldValue	nvarchar(MAX)
- @SysID	nvarchar(100)
## Tables Read
- [[OT_NewCustomers]]
- [[OT_NewCustomersSpecialFields]]
## Tables Written
- [[OT_NewCustomersSpecialFields]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_NewCustomers]]
- [[OT_NewCustomersSpecialFields]]

**Tables Written**
- [[OT_NewCustomersSpecialFields]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
