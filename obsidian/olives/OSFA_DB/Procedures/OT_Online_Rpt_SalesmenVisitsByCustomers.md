---
type: procedure
database: OSFA_DB
name: OT_Online_Rpt_SalesmenVisitsByCustomers
schema: dbo
tags: [#customer, #mobile, #reporting, #sales]
reads_from:
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Online_Rpt_SalesmenVisitsByCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @SalesmanNo int = 3003
- @FromDate smalldatetime = '2020-09-01'
- @ToDate smalldatetime = '2020-10-26'
- @FromCustomerNo bigint = 314
- @ToCustomerNo bigint = 314
## Tables Read
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
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
