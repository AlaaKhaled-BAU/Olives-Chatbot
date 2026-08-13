---
type: procedure
database: Olives_BO
name: Pro_NewCustomerDefaultValue
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[NewCustomerDefaultValue]]
writes_to:
  - [[NewCustomerDefaultValue]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_NewCustomerDefaultValue


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads NewCustomerDefaultValue. Writes NewCustomerDefaultValue. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @BusinessUnitID int = null
- @PaymentTypeID int = null
- @PriceListID int = null
- @CreditLimit float = null
- @DueDays smallint = null
- @ChqsDueDays smallint = null
- @AllowChqs bit = null
- @TaxInclude bit = null
- @cmdType varchar(50)=null
## Tables Read
- [[NewCustomerDefaultValue]]
## Tables Written
- [[NewCustomerDefaultValue]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[NewCustomerDefaultValue]]

**Tables Written**
- [[NewCustomerDefaultValue]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
