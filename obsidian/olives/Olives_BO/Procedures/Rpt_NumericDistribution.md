---
type: procedure
database: Olives_BO
name: Rpt_NumericDistribution
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_NumericDistribution


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Items, SalesOrderHistoryDF, SalesOrderHistoryHF, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime= '1-1-2016'
- @ToDate smalldatetime= '1-1-2023'
- @FromItem varchar(100)=1
- @ToItem varchar(100)=9999999
- @FromSalesman int=1
- @ToSalesman int=9999999
- @FromGroup int = 0
- @ToGroup int = 99999999
- @UserID nvarchar(50)=null
- @FromCateg varchar(100) = '0'
- @ToCateg varchar(100) = 'zzzzzzzz'
## Tables Read
- [[CustomersFinancialDetails]]
- [[Items]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- [[Items]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

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
