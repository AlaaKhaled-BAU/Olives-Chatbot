---
type: procedure
database: Olives_BO
name: Rpt_SalesPersonStatement_ReportSubJoad
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - Customers
  - CustomersFinancialDetails
  - InvoiceDeliveryDF
  - InvoiceDeliveryHF
  - RoutesInformation
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_SalesPersonStatement_ReportSubJoad

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 3 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @FromCustomer bigint
- @ToCustomer bigint
- @TrType nvarchar(50)
- @UserID nvarchar(50)
- @IsApprove nvarchar(50)
- @IsCashCredit int
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[RoutesInformation]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
- `Fun_GetFromDate`
- `Fun_GetSalesmanParentName`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
