---
type: procedure
database: Olives_BO
name: Rpt_SalesmanNetSalesByTradechannelSUKH
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_GetSalesmanTotalSales_Sokh
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanNetSalesByTradechannelSUKH


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetSalesmanTotalSales_Sokh, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesmanNo int
- @ToSalesmanNo int
- @UserID nvarchar(50)
- @WithInvoice int
- @WithOrder int
## Tables Read
- Fun_GetSalesmanTotalSales_Sokh
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetSalesmanTotalSales_Sokh
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
