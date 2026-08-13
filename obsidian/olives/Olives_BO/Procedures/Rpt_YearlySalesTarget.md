---
type: procedure
database: Olives_BO
name: Rpt_YearlySalesTarget
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - AND
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TargetsReferences]]
  - int
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_YearlySalesTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AND, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, SalesPersonsGroups, TargetsReferences, int. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromTargetsReferences int
- @ToTargetsReferences int
- @TargetYear smallint
- @FromMonth smallint
- @ToMonth smallint
- @FromGroup int = 0
- @ToGroup int = 99999999
- @UserID nvarchar(50)
## Tables Read
- AND
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TargetsReferences]]
- int
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- AND
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TargetsReferences]]
- int

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
