---
type: procedure
database: OSFA_DB
name: Pro_NewCustImages
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_NewCustomerImages]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_NewCustImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_NewCustomerImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @CustomerID nvarchar(50) = null
## Tables Read
- [[OT_NewCustomerImages]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_NewCustomerImages]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Cross-Database
Also exists in the other database: [[Olives_BO/Procedures/Pro_NewCustImages]] (BO).

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
