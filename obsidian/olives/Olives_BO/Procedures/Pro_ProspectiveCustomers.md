---
type: procedure
database: Olives_BO
name: Pro_ProspectiveCustomers
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[CustomersTypes]]
  - [[Locations]]
  - [[Positions]]
  - [[PriceLists]]
  - [[ProspectiveCustomers]]
writes_to:
  - [[ProspectiveCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ProspectiveCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersTypes, Locations, Positions, PriceLists, ProspectiveCustomers. Writes ProspectiveCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	 = null
- @ID	bigint	= null
- @Name	nvarchar(200)	= null
- @ForeignName	nvarchar(200)	= null
- @ShortName	nvarchar(50)	= null
- @TypeID	int	= null
- @LocationID	int	= null
- @Reference1	nvarchar(50)	= null
- @Reference2	nvarchar(20)	= null
- @Account	nvarchar(50)	= null
- @Barcode	nvarchar(20)	= null
- @Contact	nvarchar(100)	= null
- @TelephoneNo	nvarchar(50)	= null
- @MobileNo	nvarchar(50)	= null
- @FaxNo	nvarchar(50)	= null
- @POBox	nvarchar(50)	= null
- @Address	nvarchar(200)	= null
- @Latitude	nvarchar(50)	= null
- @Longitude	nvarchar(50)	= null
- @WebSite	nvarchar(100)	= null
- @Email	nvarchar(100)	= null
- @IsSuspended	bit	= null
- @UserID	nvarchar(20)	= null
- @Password	nvarchar(20)	= null
- @CustomerImage	image	= null
- @PriceListID	int	= null
- @PositionsID	int	= null
- @TaxInclude	bit	= null
- @CreditCash	smallint	= null
- @cmdType varchar(50)=null
## Tables Read
- [[CustomersTypes]]
- [[Locations]]
- [[Positions]]
- [[PriceLists]]
- [[ProspectiveCustomers]]
## Tables Written
- [[ProspectiveCustomers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersTypes]]
- [[Locations]]
- [[Positions]]
- [[PriceLists]]
- [[ProspectiveCustomers]]

**Tables Written**
- [[ProspectiveCustomers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
