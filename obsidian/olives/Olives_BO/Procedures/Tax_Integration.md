---
type: procedure
database: Olives_BO
name: Tax_Integration
schema: dbo
tags: [#backoffice, #billing, #integration, #legal]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - Fun_GetReturnSalesInfoForTax
  - [[Items]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - InvoicesHeaders
  - [[TransactionsHeaders]]
called_by:
  - Alpha_PostResult
support_relevance: high
last_verified: 2026-07-05
---
# Tax_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, Fun_GetReturnSalesInfoForTax, Items, TransactionsDetails, TransactionsHeaders, dbo. Writes InvoicesHeaders, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @CmdType nvarchar(100)
- @ToDate smalldatetime = '2023-02-16'
- @TrYear smallint = null
- @TrType smallint = null
- @TrNo int = null
- @EINV_QR nvarchar(max) = null
- @EINV_INV_UUID uniqueidentifier = null
## Tables Read
- [[Companies]]
- [[Customers]]
- Fun_GetReturnSalesInfoForTax
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- InvoicesHeaders
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
- Alpha_PostResult
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Customers]]
- Fun_GetReturnSalesInfoForTax
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- InvoicesHeaders
- [[TransactionsHeaders]]

**Callers**
- Alpha_PostResult

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
