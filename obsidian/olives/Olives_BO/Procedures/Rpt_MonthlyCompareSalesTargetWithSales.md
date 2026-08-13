---
type: procedure
database: Olives_BO
name: Rpt_MonthlyCompareSalesTargetWithSales
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - AS
  - [[ClientsActive]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetSalesmanTreeBySalemanType
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - ON
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_MonthlyCompareSalesTargetWithSales


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AS, ClientsActive, Fun_GetCompanyBranchesByUser, Fun_GetSalesmanTreeBySalemanType, InvoiceHistoryDF, InvoiceHistoryHF, Items, ON, OrdersDetails, OrdersHeaders, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, SalesPersonsGroups, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromSalesman int=3
- @ToSalesman int=3
- @Year smallint=2023
- @FromMonth smallint=3
- @ToMonth smallint=3
- @SalesmanType int=4
- @FromGroup int = 0
- @ToGroup int = 99999999
- @UserID nvarchar(50)='admin'
- @IsMainTarget smallint = 1
## Tables Read
- AS
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTreeBySalemanType
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- ON
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTreeBySalemanType
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- ON
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
