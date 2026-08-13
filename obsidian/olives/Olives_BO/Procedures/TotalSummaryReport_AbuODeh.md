---
type: procedure
database: Olives_BO
name: TotalSummaryReport_AbuODeh
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[MAZ_Route_EMAIL_Final]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# TotalSummaryReport_AbuODeh


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MAZ_Route_EMAIL_Final. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int =1
- @salesmanNo int=3003
## Tables Read
- [[MAZ_Route_EMAIL_Final]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MAZ_Route_EMAIL_Final]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
