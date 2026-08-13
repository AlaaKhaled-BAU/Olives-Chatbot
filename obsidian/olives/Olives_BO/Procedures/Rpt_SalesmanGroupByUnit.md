---
type: procedure
database: Olives_BO
name: Rpt_SalesmanGroupByUnit
schema: dbo
tags: [#backoffice, #inventory, #reference, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanGroupByUnit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint= 1
- @FromSalesman int= 1
- @ToSalesman int= 999999
- @FromSupervisor int= 1
- @ToSupervisor int = 999999
- @FromUnit nvarchar = '1'
- @ToUnit nvarchar = '9999999'
- @FromDate smalldatetime= null
- @ToDate smalldatetime= null
- @UserID nvarchar(50)='admin'
- @SalesPersonType int = null
- @cmdType varchar(50)=null
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[SalesPersons]]
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
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
