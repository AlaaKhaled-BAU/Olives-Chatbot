---
type: procedure
database: Olives_BO
name: Rpt_Get_SalesAnalysis_Tablet
schema: dbo
tags: [#backoffice, #mobile, #reporting, #sales]
reads_from:
  - [[Customers]]
  - OPENJSON
writes_to:
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Get_SalesAnalysis_Tablet


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OPENJSON. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @CustID int=-1
- @FromMonth int=1
- @ToMonth int=3
## Tables Read
- [[Customers]]
- OPENJSON
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- OPENJSON

**Tables Written**
_None_

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
