---
type: procedure
database: Olives_BO
name: OT_CustGalaryImages
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[Customers]]
  - Fun_GetCustomersGalleryData
  - [[ImageTypes]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OT_CustGalaryImages]]
called_by:
  - [[FIXCORRUPTEDIMAGEGALARY]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustGalaryImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Customers, Fun_GetCustomersGalleryData, ImageTypes, SalesPersons, dbo. Writes OT_CustGalaryImages. Invoked by 1 procedure(s). Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @CustomerID bigint = null
- @SalesPersonID int = null
- @ToSalesman int = null
- @RejectReasonID int = null
- @cmdType nvarchar(50) = null
- @RejectReason nvarchar(200) = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @ImageID int = 0
- @ClassID int = -1
- @LocationID int = -1
- @IsApproved bit = null
- @ImageType_ID int = -1
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Customers]]
- Fun_GetCustomersGalleryData
- [[ImageTypes]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OT_CustGalaryImages]]
## Callers
- [[Alpha_SendData]]
## Callees
- [[FIXCORRUPTEDIMAGEGALARY]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Customers]]
- Fun_GetCustomersGalleryData
- [[ImageTypes]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[OT_CustGalaryImages]]

**Callers**
- [[FixCorruptedImageGalary]]

**Callees**
- [[Alpha_SendData]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Cross-Database
Also exists as a **table** in the tablet database (cross-type name collision): [[OSFA_DB/Tables/OT_CustGalaryImages]]. This note is the Olives_BO **procedure** that writes that table.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
