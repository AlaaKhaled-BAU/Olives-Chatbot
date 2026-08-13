---
type: procedure
database: Olives_BO
name: Pro_SalespersonsSecurity_Android
schema: dbo
tags: [#auth, #backoffice, #mobile, #sales]
reads_from:
  - [[CompanyParameters]]
  - [[SalespersonsSecurity]]
  - [[VerificationCodes]]
writes_to:
  - [[SalespersonsSecurity]]
  - [[VerificationCodes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalespersonsSecurity_Android


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyParameters, SalespersonsSecurity, VerificationCodes. Writes SalespersonsSecurity, VerificationCodes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalespersonID int
- @cmdType varchar(100)
- @Pass varchar(200)=''
- @VerificationType	int=null
- @VerificationCode	int=null
- @NeedNew bit=0
## Tables Read
- [[CompanyParameters]]
- [[SalespersonsSecurity]]
- [[VerificationCodes]]
## Tables Written
- [[SalespersonsSecurity]]
- [[VerificationCodes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyParameters]]
- [[SalespersonsSecurity]]
- [[VerificationCodes]]

**Tables Written**
- [[SalespersonsSecurity]]
- [[VerificationCodes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
