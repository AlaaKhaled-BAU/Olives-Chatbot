---
type: procedure
database: Olives_BO
name: Rpt_Hakkak_TargetReportFromAlpha
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
writes_to:
called_by:
  - DB
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Hakkak_TargetReportFromAlpha


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @FromSalesman int=0
- @ToSalesman int=9999
- @FromDate smalldatetime='2024-01-01'
- @ToDate smalldatetime='2024-10-31'
## Tables Read
_None_
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- DB
## Impact / Dependencies

**Tables Read**
_None_

**Tables Written**
_None_

**Callers**
- DB

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[DR_DynamicReportsParameters]]
- [[DeviceReportsList]]
- [[Report5CustomersExcemptions]]
- [[CustomerTargetsDetails]]
- [[PromotionsApprovalLog]]
- [[SalesQuotationHeaders]]

- [[Rpt_SalesmanOrdersSummaryByTargetRef]]
- [[Rpt_RouteScoreBySalesman]]
- [[Rpt_TransactionsPrintStatusLog]]
- [[Glossary]]
