---
type: procedure
database: Olives_BO
name: Pro_ImportUnConditionalPromotionData
schema: dbo
tags: [#backoffice]
reads_from:
  - CustomersPromotionsGroups
  - Items
  - PromotionsApprovalSetup
writes_to:
  - PromotionsApprovalLog
  - PromotionsCondUnCodInput
  - PromotionsCondUnCodOutput
  - PromotionsCustomersGroupsLink
  - PromotionsHeaders
  - PromotionsSalesmanGroupsLink
  - UserPromotionsLink
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_ImportUnConditionalPromotionData

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s); writes 7. See sections below for the full dependency map.
## Parameters
- @MacAddress nvarchar(200)
- @IPAddress nvarchar(200)
- @PCName nvarchar(200)
- @UserID nvarchar(200)
- @Tbl_Excel_Data importdata_unileverpromotion
## Tables Read
- [[CustomersPromotionsGroups]]
- [[Items]]
- [[PromotionsApprovalSetup]]
## Tables Written
- [[PromotionsApprovalLog]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsSalesmanGroupsLink]]
- [[UserPromotionsLink]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
