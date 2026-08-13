---
type: procedure
database: Olives_BO
name: Pro_SalesReport_ItemCode
schema: dbo
tags: [#backoffice, #inventory, #reference, #reporting, #sales]
reads_from:
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesReport_ItemCode


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalesPersons, TransactionsDetails, TransactionsHeaders, TransfersOrdersDetails, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2024-08-1'
- @ToDate smalldatetime='2024-08-25'
- @FromSalesman int =1
- @ToSalesman int =9999
## Tables Read
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
