---
type: procedure
database: Olives_BO
name: copdevicereportsPermissions_ByRange
schema: dbo
tags: [#auth, #backoffice, #reporting]
reads_from:
  - [[SalesPersons]]
  - cursor_name
writes_to:
called_by:
  - [[TechnicalSupportTools_CopyReportsfornewSalesman]]
support_relevance: high
last_verified: 2026-07-05
---
# copdevicereportsPermissions_ByRange


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, cursor_name. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @COMPNNO int
- @FromSalesman int
- @toSalesman int
## Tables Read
- [[SalesPersons]]
- cursor_name
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[TechnicalSupportTools_CopyReportsfornewSalesman]]
## Impact / Dependencies

**Tables Read**
- [[SALESPERSONS]]
- cursor_name

**Tables Written**
_None_

**Callers**
- [[TechnicalSupportTools_CopyReportsfornewSalesman]]

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
