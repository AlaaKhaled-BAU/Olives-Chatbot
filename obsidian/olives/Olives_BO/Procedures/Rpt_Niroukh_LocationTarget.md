---
type: procedure
database: Olives_BO
name: Rpt_Niroukh_LocationTarget
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - GetInvoiceTotalsByItemWithYear_date_customer
  - GetInvoiceTotalsByItemWithYear_date_customer_target
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[LocationTargetsDetails]]
  - [[Locations]]
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Niroukh_LocationTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, GetInvoiceTotalsByItemWithYear_date_customer, GetInvoiceTotalsByItemWithYear_date_customer_target, InvoiceHistoryDF, InvoiceHistoryHF, Items, LocationTargetsDetails, Locations, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=2
- @year int=2024
- @Month int=9
- @ByAmount bit = 0
- @UserID nvarchar(50)=NULL
- @AchievementType Bit=1
- @FromSalesman int=1
- @ToSalesman int=9999
## Tables Read
- [[Customers]]
- GetInvoiceTotalsByItemWithYear_date_customer
- GetInvoiceTotalsByItemWithYear_date_customer_target
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[LocationTargetsDetails]]
- [[Locations]]
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
- GetInvoiceTotalsByItemWithYear_date_customer
- GetInvoiceTotalsByItemWithYear_date_customer_target
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[LocationTargetsDetails]]
- [[Locations]]
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
