---
type: procedure
database: Olives_BO
name: Rpt_CustomersVisitsPerRoute_SUP
schema: dbo
tags: [#backoffice, #customer, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[Locations]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersVisitsPerRoute_SUP


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Locations, LogActionTransaction, SalesPersons, TransactionsDetails, TransactionsHeaders, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromDate datetime='2023-07-09'
- @ToDate datetime='2023-07-11'
- @CompanyBranch int=2
- @FromLocation int = 0
- @ToLocation int = 999999
- @FromCustomer bigint = 0
- @ToCustomer bigint = 99999999999
- @Sold int= -1
- @IsSuspended int=1
- @Visits int=-1
## Tables Read
- [[Customers]]
- [[Locations]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Locations]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

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
