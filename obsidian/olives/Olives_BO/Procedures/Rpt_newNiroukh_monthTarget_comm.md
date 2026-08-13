---
type: procedure
database: Olives_BO
name: Rpt_newNiroukh_monthTarget_comm
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[InvoiceHistoryHF]]
  - [[InvoiceHistoryDF]]
  - [[Items]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_newNiroukh_monthTarget_comm


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, InvoiceHistoryHF, InvoiceHistoryDF, Items, SalesPersonTargetsDetails, SalesPersons, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int=2
- @year int =2024
- @Quarter int=2
- @FromCustomer bigint=1
- @ToCustomer bigint=999999999
- @FromSalesmanID int=0
- @ToSalesmanID int=9999
- @return nvarchar(20) = ''
- @Byamount bit=1
- @AchievementType int=0
## Tables Read
- [[Customers]]
- [[InvoiceHistoryHF]]
- [[InvoiceHistoryDF]]
- [[Items]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsReferences]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[InvoiceHistoryHF]]
- [[InvoiceHistorydF]]
- [[Items]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsReferences]]

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
