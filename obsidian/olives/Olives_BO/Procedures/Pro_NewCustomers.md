---
type: procedure
database: Olives_BO
name: Pro_NewCustomers
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[Locations]]
  - [[Notifications]]
  - OSFA_DB
  - `dbo`
writes_to:
  - [[Notifications]]
  - [[OT_NewCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_NewCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Locations, Notifications, OSFA_DB, dbo. Writes Notifications, OT_NewCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID bigint = null
- @SalesmanNo int = null
- @CustType int = null
- @PrNo int = null
- @Class_ID int = null
- @LocationID int = null
- @PayType int = null
- @CustName nvarchar(max) = null
- @Address nvarchar(max) = null
- @Tel nvarchar(max) = null
- @Mobile nvarchar(max) = null
- @Contact nvarchar(max) = null
- @Email nvarchar(max) = null
- @Notes nvarchar(max) = null
- @CommercialRegistrationNo  nvarchar(max) = null
- @ProfessionlicenceNo nvarchar(max) = null
- @CompanyNationalID nvarchar(max) = null
- @RefNo nvarchar(max) = null
- @ShipAddress nvarchar(max) = null
- @MoreInfo1 nvarchar(max) = null
- @MoreInfo2 nvarchar(max) = null
- @CollectionDue nvarchar(max) = null
- @CommercialName nvarchar(max) = null
- @Approve bit=null
- @CreditLimit   float = null
- @ExpectedAnnualSales float = null
- @ChecksLimit float = null
- @RegistrationDate smalldatetime = null
- @ChequeDueDays int = null
- @InvoiceDueDays int = null
- @cmdType nvarchar(50)=null
- @GroupID int = null
- @NewCustID bigint=null
- @ContactPersonID int = null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[Locations]]
- [[Notifications]]
- OSFA_DB
- `dbo`
## Tables Written
- [[Notifications]]
- [[OT_NewCustomers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[Locations]]
- [[Notifications]]
- OSFA_DB
- dbo

**Tables Written**
- [[Notifications]]
- [[OT_NewCustomers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
