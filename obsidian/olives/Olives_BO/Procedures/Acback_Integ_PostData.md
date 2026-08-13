---
type: procedure
database: Olives_BO
name: Acback_Integ_PostData
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
# Acback_Integ_PostData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Invoked by 1 procedure(s). Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Operation nvarchar(100)
- @JSONResult nvarchar(MAX) OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Callers
- [[Acback_Integration]]
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
- [[Acback_Integration]]


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
