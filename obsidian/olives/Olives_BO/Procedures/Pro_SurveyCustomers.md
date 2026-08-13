---
type: procedure
database: Olives_BO
name: Pro_SurveyCustomers
schema: dbo
tags: [#backoffice, #customer, #survey]
reads_from:
  - [[SurveyCustomers]]
writes_to:
  - [[SurveyCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SurveyCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SurveyCustomers. Writes SurveyCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @SurveyID int = null
- @CustomerID bigint = null
- @CustSurveyID bigint = null
- @ItemCode nvarchar(100) = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @cmdType nvarchar(50) = null
## Tables Read
- [[SurveyCustomers]]
## Tables Written
- [[SurveyCustomers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SurveyCustomers]]

**Tables Written**
- [[SurveyCustomers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
