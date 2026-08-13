---
type: procedure
database: OSFA_DB
name: OT_NewCustomers_Insert
schema: dbo
tags: [#customer, #mobile]
reads_from:
  - [[OT_NewCustomers]]
writes_to:
  - [[OT_NewCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_NewCustomers_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_NewCustomers. Writes OT_NewCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo	smallint
- @SalesmanNo	smallint
- @CustName	varchar(150)
- @Address	varchar(150)
- @Tel	varchar(50)
- @Mobile	varchar(50)
- @Contact	varchar(50)
- @Email	varchar(50)
- @GPSX	varchar(50)
- @GPSY	varchar(50)
- @Notes	nvarchar(200)
- @CustType int=null
- @MainType	int	=1
- @TaxInclude	int=1
- @SysID	varchar(50)=''
- @PrNo	int	=1
- @CommercialRegistrationNo varchar(100) = null
- @ProfessionlicenceNo  varchar(100) = null
- @RefNo  varchar(100) = null
- @Class_ID int =null
- @CompanyNationalID  varchar(1000) = null
- @ShipAddress varchar(1500) = null
- @PayType int = null
- @CreditLimit float = null
- @ExpectedAnnualSales float = null
- @MoreInfo1 varchar(1500) = null
- @MoreInfo2 varchar(1500) = null
- @ChecksLimit	float=0
- @CollectionDue	varchar(500)=''
- @CommercialName	varchar(500)=''
- @RegistrationDate	smalldatetime=null
- @LocationID int=0
- @GroupID int=0
- @VisitDays varchar(500)=''
- @IsStartWork bit =0
- @AssetDate smalldatetime=null
- @Channel varchar(500)=''
- @Division varchar(500)=''
- @Segment varchar(500)=''
- @Sub_channel varchar(500)=''
- @Block varchar(500)=''
- @City varchar(500)=''
- @Street varchar(500)=''
## Tables Read
- [[OT_NewCustomers]]
## Tables Written
- [[OT_NewCustomers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_NewCustomers]]

**Tables Written**
- [[OT_NewCustomers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
