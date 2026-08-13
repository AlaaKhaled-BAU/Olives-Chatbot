---
type: procedure
database: Olives_BO
name: Rpt_PrintReceiptDetailsInfo
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Receipts]]
writes_to:
called_by:
  - [[Rpt_PrintCollectedReceipt]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PrintReceiptDetailsInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Receipts. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @FromTransNo int
- @ToTransNo int
- @UserID nvarchar(50)=NULL
## Tables Read
- [[Receipts]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_PrintCollectedReceipt]]
## Impact / Dependencies

**Tables Read**
- [[Receipts]]

**Tables Written**
_None_

**Callers**
- [[Rpt_PrintCollectedReceipt]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
