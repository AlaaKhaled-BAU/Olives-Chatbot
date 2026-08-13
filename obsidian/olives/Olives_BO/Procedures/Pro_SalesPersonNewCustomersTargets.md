---
type: procedure
database: Olives_BO
name: Pro_SalesPersonNewCustomersTargets
schema: dbo
tags: [#backoffice, #customer, #sales]
reads_from:
  - [[SalesPersonNewCustomersTargets]]
  - [[SalesPersons]]
writes_to:
  - [[SalesPersonNewCustomersTargets]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonNewCustomersTargets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonNewCustomersTargets, SalesPersons. Writes SalesPersonNewCustomersTargets. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int = null
- @TargetYear int = null
- @TargetMonth int = null
- @DaysNumber int = null
- @Value float = null
- @cmdType varchar(50)=null
- @FromSalesPersonID  int = null
- @ToSalesPersonID int = null
- @FromTargetMonth int = null
- @ToTargetMonth int = null
## Tables Read
- [[SalesPersonNewCustomersTargets]]
- [[SalesPersons]]
## Tables Written
- [[SalesPersonNewCustomersTargets]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonNewCustomersTargets]]
- [[SalesPersons]]

**Tables Written**
- [[SalesPersonNewCustomersTargets]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
