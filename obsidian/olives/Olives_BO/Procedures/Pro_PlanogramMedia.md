---
type: procedure
database: Olives_BO
name: Pro_PlanogramMedia
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Customers]]
  - [[PlanogramMedia]]
  - [[PlanogramMediaCustomersLink]]
writes_to:
  - [[PlanogramMedia]]
  - [[PlanogramMediaCustomersLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PlanogramMedia


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, PlanogramMedia, PlanogramMediaCustomersLink. Writes PlanogramMedia, PlanogramMediaCustomersLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int=null
- @FileID int=null
- @FileName varchar(max)=null
- @FilePath varchar(max)=null
- @CustID varchar(50)=null
- @cmdType varchar(50)=null
## Tables Read
- [[Customers]]
- [[PlanogramMedia]]
- [[PlanogramMediaCustomersLink]]
## Tables Written
- [[PlanogramMedia]]
- [[PlanogramMediaCustomersLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[PlanogramMedia]]
- [[PlanogramMediaCustomersLink]]

**Tables Written**
- [[PlanogramMedia]]
- [[PlanogramMediaCustomersLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
