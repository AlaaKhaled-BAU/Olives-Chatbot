---
type: procedure
database: Olives_BO
name: WF_IsHaveDueBalance
schema: dbo
tags: [#auth, #backoffice, #inventory, #workflow]
reads_from:
  - 168
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - Fun_ConvArrayToTable
  - OPENQUERY
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_IsHaveDueBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 168, Customers, CustomersFinancialDetails, CustomersTypes, Fun_ConvArrayToTable, OPENQUERY, SalesPersons, dbo. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @CustomerNo bigint
- @SalesmanNo int
- @IsHaveDueBalance bit Output
## Tables Read
- 168
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- Fun_ConvArrayToTable
- OPENQUERY
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
- [[WF_AddWorkFlowLevels]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 168
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- Fun_ConvArrayToTable
- OPENQUERY
- [[Salespersons]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[WF_AddWorkFlowLevels]]


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
