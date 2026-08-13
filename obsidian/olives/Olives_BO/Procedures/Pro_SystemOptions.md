---
type: procedure
database: Olives_BO
name: Pro_SystemOptions
schema: dbo
tags: [#backoffice]
reads_from:
  - All
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[CustomerLoginActions]]
  - Layout
  - Specific
  - `dbo`
writes_to:
  - All
  - Layout
  - [[OT_SystemOptions]]
  - OT_SystemOptionsLog
  - Specific
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SystemOptions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads All, ClientsActive, CompanyParameters, CustomerLoginActions, Layout, Specific, dbo. Writes All, Layout, OT_SystemOptions, OT_SystemOptionsLog, Specific. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @Op_Desc nvarchar (200)=null
- @Op_Value nvarchar (max)=null
- @Notes nvarchar (40)=null
- @Op_ID int = null
- @PrinterTypeID int = null
- @SalesmanNo int = null
- @cmdType varchar(50)=null
- @UserID nvarchar(50) = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @TrType int = null
## Tables Read
- All
- [[ClientsActive]]
- [[CompanyParameters]]
- [[CustomerLoginActions]]
- Layout
- Specific
- `dbo`
## Tables Written
- All
- Layout
- [[OT_SystemOptions]]
- OT_SystemOptionsLog
- Specific
## Callers
- [[Pro_SalesPersons]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- All
- [[ClientsActive]]
- [[CompanyParameters]]
- [[CustomerLoginActions]]
- Layout
- Specific
- dbo

**Tables Written**
- All
- Layout
- [[OT_SystemOptions]]
- OT_SystemOptionsLog
- Specific

**Callers**
_None_

**Callees**
- [[Pro_SalesPersons]]


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
