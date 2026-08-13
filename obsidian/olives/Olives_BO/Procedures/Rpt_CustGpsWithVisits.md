---
type: procedure
database: Olives_BO
name: Rpt_CustGpsWithVisits
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Locations]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - SplitString
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustGpsWithVisits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Locations, LogActionTransaction, SalesPersons, SplitString. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @UserID NVARCHAR(50)='admin'
- @CompanyID smallint=1
- @FromDate smalldatetime='04/04/2014'
- @ToDate smalldatetime='04/04/2024'
- @Location VARCHAR(100)='1'
- @SalesPerson VARCHAR(100)='4004'
- @Supervisor VARCHAR(100)='1,'
- @VistitCount int=0
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Locations]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- SplitString
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Locations]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- SplitString

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
