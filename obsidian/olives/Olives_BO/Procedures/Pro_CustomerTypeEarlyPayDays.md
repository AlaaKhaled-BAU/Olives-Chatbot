---
type: procedure
database: Olives_BO
name: Pro_CustomerTypeEarlyPayDays
schema: dbo
tags: [#backoffice, #customer, #reference]
reads_from:
  - [[CustomerTypeEarlyPayDays]]
writes_to:
  - [[CustomerTypeEarlyPayDays]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomerTypeEarlyPayDays


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerTypeEarlyPayDays. Writes CustomerTypeEarlyPayDays. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallInt = null
- @CustomerTypeID int = null
- @DiscountEarlyPayDays int =null
- @EarlyRepaymentDiscountPerc float= null
- @cmdType nvarchar(50) = null
## Tables Read
- [[CustomerTypeEarlyPayDays]]
## Tables Written
- [[CustomerTypeEarlyPayDays]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerTypeEarlyPayDays]]

**Tables Written**
- [[CustomerTypeEarlyPayDays]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
