---
type: procedure
database: Olives_BO
name: WF_GetPositionWFData_Alerts
schema: dbo
tags: [#auth, #backoffice, #workflow]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[WF_Functions]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_GetPositionWFData_Alerts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, OrdersHeaders, SalesPersons, WF_Functions, WF_MasterLog, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @PositionID int=1
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

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
