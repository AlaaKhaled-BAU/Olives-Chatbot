---
type: procedure
database: Olives_BO
name: Pro_SalesAcheivmentGrades
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[SalesAcheivmentGrades]]
writes_to:
  - [[SalesAcheivmentGrades]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesAcheivmentGrades


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesAcheivmentGrades. Writes SalesAcheivmentGrades. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @Name nvarchar (200)=null
- @MinValue float =null
- @MaxValue float =null
- @Factor float =null
- @cmdType varchar(50)=null
## Tables Read
- [[SalesAcheivmentGrades]]
## Tables Written
- [[SalesAcheivmentGrades]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesAcheivmentGrades]]

**Tables Written**
- [[SalesAcheivmentGrades]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
