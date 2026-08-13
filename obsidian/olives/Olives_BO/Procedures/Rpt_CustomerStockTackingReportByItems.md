---
type: procedure
database: Olives_BO
name: Rpt_CustomerStockTackingReportByItems
schema: dbo
tags: [#backoffice, #customer, #inventory, #reporting]
reads_from:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Customers]]
  - [[Items]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerStockTackingReportByItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, Customers, Items. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesPersonID int = null
- @FromCustomer bigint = null
- @ToCustomer bigint= null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @UserID nvarchar(50)=null
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]

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
