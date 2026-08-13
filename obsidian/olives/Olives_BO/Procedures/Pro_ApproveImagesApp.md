---
type: procedure
database: Olives_BO
name: Pro_ApproveImagesApp
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Customers]]
  - Fun_ConvArrayToTable
  - [[ImageTypes]]
  - [[LogActionTransaction]]
  - [[NoTransactionsReasons]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - `dbo`
writes_to:
  - [[OT_CustGalaryImages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ApproveImagesApp


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_ConvArrayToTable, ImageTypes, LogActionTransaction, NoTransactionsReasons, SalesPersons, SalesPersonsGroups, dbo. Writes OT_CustGalaryImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @cmdType varchar(50)  ='GetDataList'
- @FromDate smalldatetime ='2024-01-01'
- @ToDate smalldatetime ='2024-07-01'
- @SalemanGroupIds varchar(max)='-1'
- @SupervisorIds varchar(max)='-1'
- @SalesmanIds varchar(max)='-1'
- @ImageTypeIds varchar(max)='-1'
- @ApproveStatus smallint=-1
- @ImageID bigint=35
- @ImagesIds varchar(max)=''
- @IsApproved bit=0
- @RejectReason int=2
- @Notes varchar(max)='ttt'
## Tables Read
- [[Customers]]
- Fun_ConvArrayToTable
- [[ImageTypes]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- `dbo`
## Tables Written
- [[OT_CustGalaryImages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- Fun_ConvArrayToTable
- [[ImageTypes]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- dbo

**Tables Written**
- [[OT_CustGalaryImages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
