---
type: procedure
database: Olives_BO
name: ABS_Integ_PostDataToAPI
schema: dbo
tags: [#backoffice, #integration]
reads_from:
writes_to:
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# ABS_Integ_PostDataToAPI


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Invoked by 8 procedure(s). Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @ReqDataName nvarchar(1000)
- @HD_JSON NVARCHAR(max)
- @JSONResult nvarchar(MAX) OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Callers
- [[ABS_Integ_SendInvoices_Jebrene]]
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendReturnInvoices_Jebrene]]
- [[ABS_Integ_SendSalesOrder]]
- [[ABS_Integ_SendSalesOrder_Jebrene]]
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
_None_

**Tables Written**
_None_

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
- [[ABS_Integ_SendInvoices_Jebrene]]
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendReturnInvoices_Jebrene]]
- [[ABS_Integ_SendSalesOrder]]
- [[ABS_Integ_SendSalesOrder_Jebrene]]
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[OlivesUserPermissions]]
- [[PromotionsApprovalLog]]
- [[CustomerPaidTrans_FormERP]]
