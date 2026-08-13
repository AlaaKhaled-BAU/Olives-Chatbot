---
type: procedure
database: Olives_BO
name: Pro_SalesmanImages
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Customers]]
  - Fun_ConvArrayToTable
  - [[ImageTypes]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - db_cursor
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesmanImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_ConvArrayToTable, ImageTypes, LogActionTransaction, SalesPersons, db_cursor, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1,@FromDate smalldatetime='2021-09-15',@ToDate smalldatetime='2021-09-20',@Salesmen nvarchar(500) = '3003,',@ImageTypes nvarchar(500) = '-1,'
## Tables Read
- [[Customers]]
- Fun_ConvArrayToTable
- [[ImageTypes]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- db_cursor
- `dbo`
## Tables Written
_None_
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
- [[SalesPersons]]
- db_cursor
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
