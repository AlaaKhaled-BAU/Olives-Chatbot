---
type: procedure
database: Olives_BO
name: Pro_CompetitveItemsDataHF
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[CompetitveItemsDataHF]]
  - [[Customers]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CompetitveItemsDataHF


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompetitveItemsDataHF, Customers, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @cmdType varchar(50)=null
## Tables Read
- [[CompetitveItemsDataHF]]
- [[Customers]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompetitveItemsDataHF]]
- [[Customers]]
- [[SalesPersons]]

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
- [[Olives_BO/Procedures/Pro_PrintCheque]]
