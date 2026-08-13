---
type: procedure
database: Olives_BO
name: Pro_UserActivity
schema: dbo
tags: [#auth, #backoffice]
reads_from:
  - [[UserActivity]]
  - [[Users]]
writes_to:
  - [[UserActivity]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_UserActivity


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads UserActivity, Users. Writes UserActivity. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @UserID nvarchar(50) = null
- @AmendCreditLimit bit = null
- @AmendChqsDueDays bit = null
- @AmendAllowChqs bit = null
- @AmendPaymentType bit = null
- @AmendDueDays bit = null
- @AmendMaxInvoiceValue bit = null
- @AmendInvoiceType bit = null
- @AmendPriceList bit = null
- @AmendDicount bit = null
- @AmendMaxInoiceCount bit = null
- @AmendTaxInclude bit = null
- @cmdType varchar(50)=null
## Tables Read
- [[UserActivity]]
- [[Users]]
## Tables Written
- [[UserActivity]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[UserActivity]]
- [[users]]

**Tables Written**
- [[UserActivity]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
