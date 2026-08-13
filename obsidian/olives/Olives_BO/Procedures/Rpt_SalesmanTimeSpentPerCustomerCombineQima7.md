---
type: procedure
database: Olives_BO
name: Rpt_SalesmanTimeSpentPerCustomerCombineQima7
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - Fun_ConvArrayToTable
  - [[LogActionTransaction]]
  - [[SalesPersons]]
writes_to:
called_by:
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanTimeSpentPerCustomerCombineQima7


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_ConvArrayToTable, LogActionTransaction, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smallDateTime = '2024-07-03'
- @ToDate smallDateTime = '2024-07-03'
- @FromSalesman int = 201
- @ToSalesman int = 300
- @UserID nvarchar(50) = 'admin'
## Tables Read
- Fun_ConvArrayToTable
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
## Impact / Dependencies

**Tables Read**
- Fun_ConvArrayToTable
- [[LogActionTransaction]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
