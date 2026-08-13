---
type: procedure
database: Olives_BO
name: Pro_SalesPersonBonusLimit
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersBonusTypesLink]]
  - [[CustomersPaymentTypesLink]]
  - [[CustomersTypes]]
  - [[SalesPersonBonusLimit]]
  - [[SalesPersons]]
  - [[SystemCodes]]
writes_to:
  - [[CustomersBonusTypesLink]]
  - [[CustomersPaymentTypesLink]]
  - [[SalesPersonBonusLimit]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonBonusLimit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersBonusTypesLink, CustomersPaymentTypesLink, CustomersTypes, SalesPersonBonusLimit, SalesPersons, SystemCodes. Writes CustomersBonusTypesLink, CustomersPaymentTypesLink, SalesPersonBonusLimit. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int = null
- @BonusYear int = null
- @BonusMonth int = null
- @BonusLimit int = null
- @BonusType int = null
- @AssignCustomersToBonusType AssignCustomersToSalesman ReadOnly
- @cmdType varchar(50)=null
## Tables Read
- [[Customers]]
- [[CustomersBonusTypesLink]]
- [[CustomersPaymentTypesLink]]
- [[CustomersTypes]]
- [[SalesPersonBonusLimit]]
- [[SalesPersons]]
- [[SystemCodes]]
## Tables Written
- [[CustomersBonusTypesLink]]
- [[CustomersPaymentTypesLink]]
- [[SalesPersonBonusLimit]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersBonusTypesLink]]
- [[CustomersPaymentTypesLink]]
- [[CustomersTypes]]
- [[SalesPersonBonusLimit]]
- [[SalesPersons]]
- [[SystemCodes]]

**Tables Written**
- [[CustomersBonusTypesLink]]
- [[CustomersPaymentTypesLink]]
- [[SalesPersonBonusLimit]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
