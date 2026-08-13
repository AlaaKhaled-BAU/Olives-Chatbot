---
type: procedure
database: Olives_BO
name: Pro_ItemsReplacementDetails
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[ItemsReplacementDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsReplacementDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ItemsReplacementDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @TransactionYear smallint=2019
- @TransactionNo INT=11
- @cmdType varchar(50)='Select All'
## Tables Read
- [[ItemsReplacementDetails]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ItemsReplacementDetails]]

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
