---
type: procedure
database: Olives_BO
name: WF_AlertsRemoveAll
schema: dbo
tags: [#auth, #backoffice, #workflow]
reads_from:
  - [[RequestSalesmanNoTransaction]]
  - [[SalesPersons]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
writes_to:
  - [[RequestSalesmanNoTransaction]]
  - [[WF_SubLog]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_AlertsRemoveAll


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads RequestSalesmanNoTransaction, SalesPersons, WF_MasterLog, WF_SubLog. Writes RequestSalesmanNoTransaction, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @Action nvarchar(1) = 'N'
- @ActionDate smalldatetime = null
- @Notes nvarchar(500)=''
- @PositionID int
- @SalesmanNo int = 0
## Tables Read
- [[RequestSalesmanNoTransaction]]
- [[SalesPersons]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
## Tables Written
- [[RequestSalesmanNoTransaction]]
- [[WF_SubLog]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[RequestSalesmanNoTransaction]]
- [[SalesPersons]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

**Tables Written**
- [[RequestSalesmanNoTransaction]]
- [[WF_SubLog]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
