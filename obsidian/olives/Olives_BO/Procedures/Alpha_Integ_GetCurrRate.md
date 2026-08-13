---
type: procedure
database: Olives_BO
name: Alpha_Integ_GetCurrRate
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - InvITemsmf
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_GetCurrRate


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads InvITemsmf. Invoked by 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo	smallint
- @ItemNo nvarchar(100)
- @ExRate float output
## Tables Read
- InvITemsmf
## Tables Written
_None_
## Callers
- [[OT_ImportReturnOrder]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesIssueItems]]
- [[OT_ImportSalesOrders]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- InvITemsmf

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[OT_ImportReturnOrder]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesIssueItems]]
- [[OT_ImportSalesOrders]]


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
