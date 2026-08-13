---
type: procedure
database: Olives_BO
name: Rpt_CustomersVisitsCountByClass
schema: dbo
tags: [#backoffice, #customer, #reference, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[PaymentsTypes]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersVisitsCountByClass


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersClasses, CustomersFinancialDetails, LogActionTransaction, PaymentsTypes, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesPerson int
- @ToSalesPerson int
- @FromClass int
- @ToClass int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @VisitType int   -- 1 Actual
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[PaymentsTypes]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[PaymentsTypes]]
- [[SalesPersons]]

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
