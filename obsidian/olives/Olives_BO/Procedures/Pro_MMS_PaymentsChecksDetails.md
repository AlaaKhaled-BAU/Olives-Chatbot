---
type: procedure
database: Olives_BO
name: Pro_MMS_PaymentsChecksDetails
schema: dbo
tags: [#backoffice, #billing, #mms]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[MMS_PaymentsChecksDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_PaymentsChecksDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, MMS_PaymentsChecksDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @PaymentYear	smallint		= null
- @PaymentNo	bigint		= null
- @LineID	int		= null
- @CheckNo	int		= null
- @DueDate	smalldatetime		= null
- @Amount	float		= null
- @BankID	int		= null
- @BranchID	int		= null
- @DrawerName	nvarchar(500)		= null
- @cmdType nvarchar(50) = null
## Tables Read
- [[Banks]]
- [[Branches]]
- [[MMS_PaymentsChecksDetails]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[MMS_PaymentsChecksDetails]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
