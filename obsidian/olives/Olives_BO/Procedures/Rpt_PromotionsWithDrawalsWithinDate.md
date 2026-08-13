---
type: procedure
database: Olives_BO
name: Rpt_PromotionsWithDrawalsWithinDate
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_GetTransCustName
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsPromotions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PromotionsWithDrawalsWithinDate


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetTransCustName, SalesPersons, TransactionsDetails, TransactionsHeaders, TransactionsPromotions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2021-03-01'
- @ToDate smalldatetime='2021-03-30'
- @FromPromo int=31
- @ToPromo int =31
- @FromGroup int=0
- @ToGroup int =9999
- @PrType smallint =1
## Tables Read
- Fun_GetTransCustName
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetTransCustName
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]

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
