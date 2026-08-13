---
type: procedure
database: Olives_BO
name: Pro_JoTaxApiFromOSFA_BeforeYAN
schema: dbo
tags: [#integration]
reads_from:
  - Companies
  - Currencies
  - Customers
  - InvoiceReturnLink
  - Items
  - ItemsUnits
  - JOTaxSettings
  - PriceLists
  - RoutesInformation
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
  - JoTaxResult
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_JoTaxApiFromOSFA_BeforeYAN

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 12 table(s); writes 1; calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @TransactionYear smallint
- @TransactionNo int
- @TransactionTypeID smallint
- @status nvarchar(MAX)
- @EINV_QR nvarchar(MAX)
- @EINV_INV_UUID nvarchar(MAX)
- @ErrorMessage nvarchar(MAX)
- @UUID nvarchar(MAX)
- @RoundDigit float
- @cmdType nvarchar(100)
## Tables Read
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- [[InvoiceReturnLink]]
- [[Items]]
- [[ItemsUnits]]
- [[JOTaxSettings]]
- [[PriceLists]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- [[JoTaxResult]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_InvoiceDF|OT_InvoiceDF]]
- [[OSFA_DB/Tables/OT_InvoiceHF|OT_InvoiceHF]]
## Callers
_None_
## Callees
- `Fun_GetReturnSalesInfoForTaxAPIFromOSFA`
- `Fun_Tax_getTobacco`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
