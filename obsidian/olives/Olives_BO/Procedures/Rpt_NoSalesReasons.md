---
type: procedure
database: Olives_BO
name: Rpt_NoSalesReasons
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_ConvArrayToTable
  - [[LogActionTransaction]]
  - [[NoTransactionsReasons]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_NoSalesReasons


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Fun_ConvArrayToTable, LogActionTransaction, NoTransactionsReasons, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @FromCustomer bigint = 0
- @ToCustomer bigint= 999999999
- @FromDate smalldatetime = '01-01-2015'
- @ToDate smalldatetime = '01-01-2025'
- @FromReason int = 0
- @ToReason int = 999
- @UserID nvarchar(50)='admin'
- @FromGroup int = 0
- @ToGroup int = 99999999
- @Salesman nvarchar(max)= '6,7,8,9,10,11,'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- Fun_ConvArrayToTable
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
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
- [[ClientsActive]]
- [[Customers]]
- Fun_ConvArrayToTable
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
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
