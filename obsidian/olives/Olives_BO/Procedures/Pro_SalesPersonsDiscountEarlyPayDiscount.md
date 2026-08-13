---
type: procedure
database: Olives_BO
name: Pro_SalesPersonsDiscountEarlyPayDiscount
schema: dbo
tags: [#backoffice, #billing, #sales]
reads_from:
  - [[SalesPersonsDiscountEarlyPayDiscount]]
writes_to:
  - [[SalesPersonsDiscountEarlyPayDiscount]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonsDiscountEarlyPayDiscount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonsDiscountEarlyPayDiscount. Writes SalesPersonsDiscountEarlyPayDiscount. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @cmdType  nvarchar(max)=null
- @CompanyID smallint=null
- @PositionID int = null
- @FromDate datetime =null
- @ToDate datetime =null
- @DiscountPerc float =null
## Tables Read
- [[SalesPersonsDiscountEarlyPayDiscount]]
## Tables Written
- [[SalesPersonsDiscountEarlyPayDiscount]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonsDiscountEarlyPayDiscount]]

**Tables Written**
- [[SalesPersonsDiscountEarlyPayDiscount]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
