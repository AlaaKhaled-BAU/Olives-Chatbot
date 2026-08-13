---
type: procedure
database: Olives_BO
name: Defaf_SalesmenItemQTY
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - Salesman
  - master
  - [[SalesPersons]]
writes_to:
called_by:
  - [[Defaf_Rpt_WareHouse_Item_Balance]]
support_relevance: high
last_verified: 2026-07-05
---
# Defaf_SalesmenItemQTY


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Salesman, master, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromSalesPerson int = 1
- @ToSalesPerson int = 99999
- @FromDate smalldatetime = '2000-08-30'
- @ToDate smalldatetime = '2022-08-30'
- @FromItem nvarchar(100) = '0'
- @ToItem nvarchar(100) = 'zzzzzzzzzz'
- @FromCateg nvarchar(20) = '0'
- @ToCateg nvarchar(20) = 'zzzzzzzzzz' , @UserID nvarchar(50)='admin'
## Tables Read
- Salesman
- master
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Defaf_Rpt_WareHouse_Item_Balance]]
## Impact / Dependencies

**Tables Read**
- Salesman
- master
- [[salespersons]]

**Tables Written**
_None_

**Callers**
- [[Defaf_Rpt_WareHouse_Item_Balance]]

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
