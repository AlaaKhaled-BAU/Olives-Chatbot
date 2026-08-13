---
type: procedure
database: Olives_BO
name: Pro_SalespersonsSecurity
schema: dbo
tags: [#auth, #backoffice, #sales]
reads_from:
  - [[SalespersonsSecurity]]
writes_to:
  - [[SalespersonsSecurity]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalespersonsSecurity


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalespersonsSecurity. Writes SalespersonsSecurity. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint = null
- @SalespersonID	int	= null
- @UserID	nvarchar(50)	= null
- @Pass	nvarchar(50)	= null
- @IsSuspended	bit	= null
- @LastPassChangeDate	smalldatetime	= null
- @LastActivationCodeChangeDate	smalldatetime	= null
- @cmdType nvarchar(50) = null
## Tables Read
- [[SalespersonsSecurity]]
## Tables Written
- [[SalespersonsSecurity]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalespersonsSecurity]]

**Tables Written**
- [[SalespersonsSecurity]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
