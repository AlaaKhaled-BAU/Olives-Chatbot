---
type: procedure
database: Olives_BO
name: Pro_ImportSalesPersonTargets
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - By
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - cursorName
writes_to:
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ImportSalesPersonTargets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads By, SalesPersonTargets, SalesPersonTargetsDetails, cursorName. Writes SalesPersonTargets, SalesPersonTargetsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @SalesPersonTbl SalespersonTargetTbl readonly
- @CmdType NVARCHAR(50) = null
## Tables Read
- By
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- cursorName
## Tables Written
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- By
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- cursorName

**Tables Written**
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
