---
type: procedure
database: Olives_BO
name: WF_GetCustAgingInfo
schema: dbo
tags: [#auth, #backoffice, #workflow]
reads_from:
  - 168
  - [[Customers]]
  - [[CustomersTypes]]
  - Fun_ConvArrayToTable
  - OPENQUERY
  - [[OrdersHeaders]]
  - [[WF_SubLog]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_GetCustAgingInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 168, Customers, CustomersTypes, Fun_ConvArrayToTable, OPENQUERY, OrdersHeaders, WF_SubLog, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @SID bigint = 1260475
## Tables Read
- 168
- [[Customers]]
- [[CustomersTypes]]
- Fun_ConvArrayToTable
- OPENQUERY
- [[OrdersHeaders]]
- [[WF_SubLog]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 168
- [[Customers]]
- [[CustomersTypes]]
- Fun_ConvArrayToTable
- OPENQUERY
- [[OrdersHeaders]]
- [[WF_SubLog]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
