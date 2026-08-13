---
type: procedure
database: Olives_BO
name: Acback_Integ_PostTransactionsData
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
# Acback_Integ_PostTransactionsData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Invoked by 5 procedure(s). Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Operation nvarchar(100)
- @Content NVARCHAR(MAX)
- @JSONResult nvarchar(MAX) OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Callers
- [[AcBack_Integ_GetItemBalance]]
- [[Acback_Integ_SendInvoices]]
- [[Acback_Integ_SendPayments]]
- [[Acback_Integ_SendReturnInvoices]]
- [[Acback_Integ_SendTransfer]]
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
- [[AcBack_Integ_GetItemBalance]]
- [[Acback_Integ_SendInvoices]]
- [[Acback_Integ_SendPayments]]
- [[Acback_Integ_SendReturnInvoices]]
- [[Acback_Integ_SendTransfer]]


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
