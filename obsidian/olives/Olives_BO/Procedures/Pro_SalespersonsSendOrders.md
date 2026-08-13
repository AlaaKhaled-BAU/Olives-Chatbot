---
type: procedure
database: Olives_BO
name: Pro_SalespersonsSendOrders
schema: dbo
tags: [#backoffice, #order, #sales]
reads_from:
  - [[ClientsActive]]
  - Fun_ConvArrayToTable
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalespersonsSendOrders]]
  - SendOrders
  - [[SystemCodes]]
  - `dbo`
writes_to:
  - [[SalespersonsSendOrders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalespersonsSendOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Fun_ConvArrayToTable, SalesPersons, SalesPersonsGroups, SalespersonsSendOrders, SendOrders, SystemCodes, dbo. Writes SalespersonsSendOrders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = null
- @CmdType nvarchar(50) = ''
- @FromDept int = null
- @ToDept int = null
- @Departments nvarchar(max) = null
- @Branch int = null
- @SalespersonGroup varchar(max) = '0'
- @SendOrders SalesPersonsSendOrder_Type readonly
## Tables Read
- [[ClientsActive]]
- Fun_ConvArrayToTable
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalespersonsSendOrders]]
- SendOrders
- [[SystemCodes]]
- `dbo`
## Tables Written
- [[SalespersonsSendOrders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- Fun_ConvArrayToTable
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalespersonsSendOrders]]
- SendOrders
- [[SystemCodes]]
- dbo

**Tables Written**
- [[SalespersonsSendOrders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
