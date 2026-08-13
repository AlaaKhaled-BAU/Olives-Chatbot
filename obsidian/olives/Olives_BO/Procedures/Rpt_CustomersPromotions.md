---
type: procedure
database: Olives_BO
name: Rpt_CustomersPromotions
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - [[Customers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersPromotions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @UserID nvarchar(50) = 'admin'
- @PromoArray nvarchar(max) ='1,2,3,4,5,6,7'
- @FromCustomer bigint = 1
- @ToCustomer bigint = 330
- @FromDate smalldatetime = '2000-05-01'
- @ToDate smalldatetime = '2020-10-04'
## Tables Read
- [[Customers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]

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
