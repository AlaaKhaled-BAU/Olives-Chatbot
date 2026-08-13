---
type: procedure
database: Olives_BO
name: Online_RptSalesmanCustomerCategAreaSales_Zumot
schema: dbo
tags: [#backoffice, #customer, #sales]
reads_from:
  - RIGHT
  - float
  - int
writes_to:
called_by:
  - db
support_relevance: high
last_verified: 2026-07-05
---
# Online_RptSalesmanCustomerCategAreaSales_Zumot


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads RIGHT, float, int. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo as smallint=1
- @FromMonth as smallint=8
- @FromYear as smallint =2022
- @ToMonth as smallint=8
- @ToYear as smallint =2022
- @FromChanel as int=0
- @ToChanel as int=9999999
- @SalesmanNo as int=9955
- @FromCustNo as bigint=0
- @ToCustNo as bigint=999999999999
- @FromItemNo as varchar(100)='0'
- @ToItemNo as  varchar(100)='zzzzzzzzzzzzzzzzz'
- @ToMonthWorkingDays as int =30
## Tables Read
- RIGHT
- float
- int
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- db
## Impact / Dependencies

**Tables Read**
- RIGHT
- float
- int

**Tables Written**
_None_

**Callers**
- db

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
