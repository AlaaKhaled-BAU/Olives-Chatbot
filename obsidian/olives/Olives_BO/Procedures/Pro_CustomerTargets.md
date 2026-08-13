---
type: procedure
database: Olives_BO
name: Pro_CustomerTargets
schema: dbo
tags: [#backoffice, #customer, #sales]
reads_from:
  - [[CustomerTargets]]
  - [[CustomerTargetsDetails]]
  - [[Customers]]
  - [[TargetsTypes]]
writes_to:
  - [[CustomerTargets]]
  - [[CustomerTargetsDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomerTargets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerTargets, CustomerTargetsDetails, Customers, TargetsTypes. Writes CustomerTargets, CustomerTargetsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @CustomerID int = null
- @TargetYear int = null
- @TargetMonth int = null
- @TargetTypeID int = null
- @Amount float = null
- @FromCustomerID int = null
- @ToCustomerID int = null
- @FromTargetMonth int = null
- @ToTargetMonth int = null
- @cmdType varchar(50)=null
## Tables Read
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[TargetsTypes]]
## Tables Written
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[TargetsTypes]]

**Tables Written**
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
