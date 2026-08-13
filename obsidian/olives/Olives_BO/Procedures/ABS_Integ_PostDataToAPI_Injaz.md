---
type: procedure
database: Olives_BO
name: ABS_Integ_PostDataToAPI_Injaz
schema: dbo
tags: [#integration]
reads_from:
writes_to:
called_by:
  - ABS_Integ_SendInvoicesPayment_Injaz
  - ABS_Integ_SendInvoices_Injaz
  - ABS_Integ_SendPaymentCashInvoice_Injaz
  - ABS_Integ_SendPayment_Injaz
  - ABS_Integ_SendPayment_Injaz_Draft
  - ABS_Integ_SendRetInvoices_Injaz
  - ABS_Integ_SendSalesOrder_Injaz
  - ABS_Integ_SendTransferOrders_Injaz
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# ABS_Integ_PostDataToAPI_Injaz

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — called by 8 proc(s). See sections below for the full dependency map.
## Parameters
- @ReqDataName nvarchar(1000)
- @HD_JSON nvarchar(MAX)
- @JSONResult nvarchar(MAX) OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[ABS_Integ_SendInvoicesPayment_Injaz]]
- [[ABS_Integ_SendInvoices_Injaz]]
- [[ABS_Integ_SendPaymentCashInvoice_Injaz]]
- [[ABS_Integ_SendPayment_Injaz]]
- [[ABS_Integ_SendPayment_Injaz_Draft]]
- [[ABS_Integ_SendRetInvoices_Injaz]]
- [[ABS_Integ_SendSalesOrder_Injaz]]
- [[ABS_Integ_SendTransferOrders_Injaz]]
## Callees
_None_
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
