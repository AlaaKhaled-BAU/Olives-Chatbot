---
type: procedure
database: OSFA_DB
name: OT_Online_RptNotSoldCustomersByItemsAndSalesman
schema: dbo
tags: [#customer, #inventory, #mobile, #sales]
reads_from:
  - Olives_BO
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Online_RptNotSoldCustomersByItemsAndSalesman


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads Olives_BO, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 2
- @SupervisorNo int = 4
- @SalesmanNo int = 4
- @FromCustomer bigint = 6
- @ToCustomer bigint = 6
- @FromItemNo nvarchar(100) = '0'
- @ToItemNo nvarchar(100)  = 'zzzzzzzzzzzzz'
- @FromDate smalldatetime = '2021-04-06'
- @ToDate smalldatetime = '2021-04-06'
## Tables Read
- Olives_BO
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Olives_BO
- dbo

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

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
