---
type: procedure
database: Olives_BO
name: Pro_AssignItemsSuggestGroupForCustomers
schema: dbo
tags: [#backoffice, #customer, #inventory, #reference]
reads_from:
  - [[ItemsSuggestGroupLink]]
writes_to:
  - [[ItemsSuggestGroupLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AssignItemsSuggestGroupForCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ItemsSuggestGroupLink. Writes ItemsSuggestGroupLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @cmdType varchar(50) = null
- @ItemsSuggestGroupCustomersAssignment_Type_DATATABLE ItemsSuggestGroupCustomersAssignment_Type  readonly
## Tables Read
- [[ItemsSuggestGroupLink]]
## Tables Written
- [[ItemsSuggestGroupLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ItemsSuggestGroupLink]]

**Tables Written**
- [[ItemsSuggestGroupLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
