---
type: procedure
database: Olives_BO
name: Rpt_VoidOrder
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - GO_Areas
  - GO_Countries
  - GO_Customers
  - GO_Customers_Address
  - GO_GasOrder
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_VoidOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads GO_Areas, GO_Countries, GO_Customers, GO_Customers_Address, GO_GasOrder. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
## Tables Read
- GO_Areas
- GO_Countries
- GO_Customers
- GO_Customers_Address
- GO_GasOrder
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- GO_Areas
- GO_Countries
- GO_Customers
- GO_Customers_Address
- GO_GasOrder

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
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[SalesQuotationHeaders]]
- [[MMS_OrdersHeader]]
- [[PendingOrdersDetails]]
- [[DR_DynamicReportsParameters]]
- [[DeviceReportsList]]
- [[Report5CustomersExcemptions]]

- [[Rpt_SalesmanOrdersSummaryByTargetRef]]
- [[Rpt_RouteScoreBySalesman]]
- [[Rpt_TransactionsPrintStatusLog]]
- [[Glossary]]
