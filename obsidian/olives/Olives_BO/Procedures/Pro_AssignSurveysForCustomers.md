---
type: procedure
database: Olives_BO
name: Pro_AssignSurveysForCustomers
schema: dbo
tags: [#backoffice, #customer, #survey]
reads_from:
  - [[Customers]]
  - [[SurveyCustomersLink]]
writes_to:
  - [[SurveyCustomersLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AssignSurveysForCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SurveyCustomersLink. Writes SurveyCustomersLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SurveyID int = null
- @CustomerID bigint = null
- @cmdType varchar(50) = null
## Tables Read
- [[Customers]]
- [[SurveyCustomersLink]]
## Tables Written
- [[SurveyCustomersLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SurveyCustomersLink]]

**Tables Written**
- [[SurveyCustomersLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
