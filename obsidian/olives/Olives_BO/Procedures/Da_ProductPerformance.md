---
type: procedure
database: Olives_BO
name: Da_ProductPerformance
schema: dbo
tags: [#backoffice]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Da_ProductPerformance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromCateg nvarchar(100)='0'
- @ToCateg nvarchar(100)='zzzzzzzzzzzzzzz'
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 99999
- @FromCustomerNo bigint = 0
- @ToCustomerNo bigint = 999999999999
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
