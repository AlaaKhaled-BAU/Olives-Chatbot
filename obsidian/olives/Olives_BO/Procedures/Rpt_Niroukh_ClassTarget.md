---
type: procedure
database: Olives_BO
name: Rpt_Niroukh_ClassTarget
schema: dbo
tags: [#backoffice, #reference, #reporting, #sales]
reads_from:
  - AS
  - [[Customers]]
  - [[CustomersClasses]]
  - GetInvoiceTotalsByItemWithYear_date_customer
  - [[Items]]
  - [[SalesPersonTargetsDetails]]
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Niroukh_ClassTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AS, Customers, CustomersClasses, GetInvoiceTotalsByItemWithYear_date_customer, Items, SalesPersonTargetsDetails, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=2
- @year int=2024
- @month int=4
- @ByAmount bit = 0
- @UserID nvarchar(50)=NULL
- @AchievementType int=1
## Tables Read
- AS
- [[Customers]]
- [[CustomersClasses]]
- GetInvoiceTotalsByItemWithYear_date_customer
- [[Items]]
- [[SalesPersonTargetsDetails]]
- [[TargetsReferences]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- AS
- [[Customers]]
- [[CustomersClasses]]
- GetInvoiceTotalsByItemWithYear_date_customer
- [[Items]]
- [[SalesPersonTargetsDetails]]
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
