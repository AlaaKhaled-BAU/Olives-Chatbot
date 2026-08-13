---
type: procedure
database: Olives_BO
name: Shamel_Integ_GetDataFromAPI
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
# Shamel_Integ_GetDataFromAPI


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Invoked by 5 procedure(s). Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @UserName nvarchar(50)
- @Password nvarchar(50)
- @APILink nvarchar(100)
- @ReqDataName nvarchar(100)
- @IsGetToken bit
- @DataToken nvarchar(100)
- @JSONResult nvarchar(MAX) OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Callers
- [[Shamel_Integration]]
- [[Shamel_Integ_GetItemsBalance]]
- [[Shamel_Integ_SendReciepts]]
- [[Shamel_Integ_SendSalesInvoices]]
- [[Shamel_Integ_SendSalesOrders]]
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
- [[Shamel_Integration]]
- [[Shamel_Integ_GetItemsBalance]]
- [[Shamel_Integ_SendReciepts]]
- [[Shamel_Integ_SendSalesInvoices]]
- [[Shamel_Integ_SendSalesOrders]]


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[OlivesUserPermissions]]
- [[PromotionsApprovalLog]]
- [[CustomerPaidTrans_FormERP]]
