---
type: table
database: OSFA_DB
name: OT_RequestToApprovePromotionDetails
schema: dbo
tags: [#mobile, #sales, #workflow]
foreign_keys:
  - [[OT_RequestToApprovePromotion]]
referenced_by:
  - [[OT_RequestToApprovePromotion_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToApprovePromotionDetails



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ReqAutoID | numeric | YES | ✓ | ✓ | [[OT_RequestToApprovePromotion]] |
| CompanyID | smallint | NO | ✓ |  |  |
| PromotionID | int | NO | ✓ |  |  |
## Primary Key
ReqAutoID
CompanyID
PromotionID
## Foreign Keys
ReqAutoID -> [[OT_RequestToApprovePromotion]](AutoID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_RequestToApprovePromotion_Insert]]

**Writes (1):**
- [[OT_RequestToApprovePromotion_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
