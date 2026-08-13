---
type: procedure
database: Olives_BO
name: Rpt_PromotionCheckReport
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetInvoiceTotalAmount
  - Fun_ReCalcTransactionAmounts
  - [[Items]]
  - [[PromotionsHeaders]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[TransactionsPromotions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PromotionCheckReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetCompanyBranchesByUser, Fun_GetInvoiceTotalAmount, Fun_ReCalcTransactionAmounts, Items, PromotionsHeaders, SalesPersons, TransactionsHeaders, TransactionsPromotions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromCustID bigint
- @ToCustID bigint
- @FromSales int
- @ToSales int
- @FromPromoID int
- @ToPromoID int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @UserID Nvarchar(50)=NULL
- @TrNo int = null
- @TrYear int = null
- @PromCode int = null
## Tables Read
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- Fun_GetInvoiceTotalAmount
- Fun_ReCalcTransactionAmounts
- [[Items]]
- [[PromotionsHeaders]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- Fun_GetInvoiceTotalAmount
- Fun_ReCalcTransactionAmounts
- [[Items]]
- [[PromotionsHeaders]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]

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
