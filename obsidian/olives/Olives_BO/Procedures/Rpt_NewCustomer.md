---
type: procedure
database: Olives_BO
name: Rpt_NewCustomer
schema: dbo
tags: [#backoffice, #customer, #reporting]
reads_from:
  - [[CustomersClasses]]
  - [[CustomersTypes]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[PriceLists]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_NewCustomer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersClasses, CustomersTypes, Locations, PaymentsTypes, PriceLists, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @FromSalesman int=0
- @ToSalesman int=999999
- @FromDate  SmallDateTime ='2021-01-01'
- @ToDate  SmallDateTime ='2025-01-24'
## Tables Read
- [[CustomersClasses]]
- [[CustomersTypes]]
- [[Locations]]
- [[PaymentsTypes]]
- [[PriceLists]]
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersClasses]]
- [[CustomersTypes]]
- [[Locations]]
- [[PaymentsTypes]]
- [[PriceLists]]
- [[SalesPersons]]
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
