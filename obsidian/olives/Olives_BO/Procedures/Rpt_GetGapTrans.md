---
type: procedure
database: Olives_BO
name: Rpt_GetGapTrans
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[GapTransHeaders]]
  - [[GapTransTimeLine]]
  - Olives_Images
  - [[SalesPersons]]
  - [[TagCodes]]
  - `dbo`
writes_to:
  - [[GapTransHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_GetGapTrans


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, GapTransHeaders, GapTransTimeLine, Olives_Images, SalesPersons, TagCodes, dbo. Writes GapTransHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @SalesmanNo int=-1
- @CustID int=-1
- @FromDate Smalldatetime ='2021-1-1'
- @ToDate Smalldatetime ='2022-1-1'
- @GapTransYear int =null
- @GapTransNo int =null
- @stand nvarchar(50)= 'StandType1'
- @brand nvarchar(50)= 'Dettol'
- @WithFilter bit=1
- @cmdType nvarchar(50) = 'GetData'
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[GapTransHeaders]]
- [[GapTransTimeLine]]
- Olives_Images
- [[SalesPersons]]
- [[TagCodes]]
- `dbo`
## Tables Written
- [[GapTransHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[GapTransHeaders]]
- [[GapTransTimeLine]]
- Olives_Images
- [[SalesPersons]]
- [[TagCodes]]
- dbo

**Tables Written**
- [[GapTransHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
