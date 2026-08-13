---
type: procedure
database: Olives_BO
name: WF_FiltterSalesPersons
schema: dbo
tags: [#auth, #backoffice, #sales, #workflow]
reads_from:
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_FiltterSalesPersons


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @paernt varchar(50)=1
- @CompanyID varchar(50)=1
## Tables Read
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
