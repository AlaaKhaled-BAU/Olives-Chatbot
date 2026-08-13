---
type: procedure
database: Olives_BO
name: Pro_RequestToLoginToCustomerWithoutVerficiation
schema: dbo
tags: [#auth, #backoffice, #customer, #log, #workflow]
reads_from:
  - [[Customers]]
  - [[RequestToLoginToCustomerWithoutVerficiation]]
  - [[SalesPersons]]
writes_to:
  - [[RequestToLoginToCustomerWithoutVerficiation]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_RequestToLoginToCustomerWithoutVerficiation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, RequestToLoginToCustomerWithoutVerficiation, SalesPersons. Writes RequestToLoginToCustomerWithoutVerficiation. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID bigint  = null
- @Name nvarchar (200)=null
- @IsAproved bit = null
- @cmdType varchar(50)=null
- @UserID nvarchar (50)=null
## Tables Read
- [[Customers]]
- [[RequestToLoginToCustomerWithoutVerficiation]]
- [[SalesPersons]]
## Tables Written
- [[RequestToLoginToCustomerWithoutVerficiation]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[RequestToLoginToCustomerWithoutVerficiation]]
- [[SalesPersons]]

**Tables Written**
- [[RequestToLoginToCustomerWithoutVerficiation]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
