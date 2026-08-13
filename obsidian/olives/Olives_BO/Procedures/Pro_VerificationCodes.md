---
type: procedure
database: Olives_BO
name: Pro_VerificationCodes
schema: dbo
tags: [#backoffice, #reference]
reads_from:
  - [[VerificationCodes]]
writes_to:
  - [[VerificationCodes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_VerificationCodes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads VerificationCodes. Writes VerificationCodes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	 = null
- @AutoID	numeric(30, 0)	 = null
- @VerificationType	int	 = null
- @UserID	nvarchar(50)	 = null
- @SalespersonID	int	 = null
- @VerificationCode	int	 = null
- @IsUsed	bit	 = null
- @CreateDateTime	smalldatetime	 = null
- @cmdType nvarchar(50) = null
## Tables Read
- [[VerificationCodes]]
## Tables Written
- [[VerificationCodes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[VerificationCodes]]

**Tables Written**
- [[VerificationCodes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
