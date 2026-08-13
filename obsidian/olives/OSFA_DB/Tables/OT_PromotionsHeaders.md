---
type: table
database: OSFA_DB
name: OT_PromotionsHeaders
schema: dbo
tags: [#mobile, #sales]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_PromotionsHeaders



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| PromotionCode | nvarchar | YES | ✓ |  |  |
| PromotionType | smallint | NO |  |  |  |
| PromotionName | nvarchar | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| InputItemUnit | nvarchar | YES |  |  |  |
| InputQtyAmount | float | YES |  |  |  |
| OutPutType | smallint | YES |  |  |  |
| OutItemUnit | nvarchar | YES |  |  |  |
| OutQtyAmount | float | YES |  |  |  |
| OutQtyAmount_2 | float | YES |  |  |  |
| UseInReturn | bit | YES |  |  |  |
| UseInSales | bit | YES |  |  |  |
| PromotionDetails | nvarchar | YES |  |  |  |
| UseRateToCalcBonus | bit | YES |  |  |  |
| NotDouble | bit | YES |  |  |  |
| ApplyForAllUnit | bit | YES |  |  |  |
| DiscountType | smallint | YES |  |  |  |
| IncludeInTargetBonus | bit | YES |  |  |  |
| PriorityID | int | YES |  |  |  |
| PrioritySerial | int | YES |  |  |  |
| RoundType | smallint | YES |  |  |  |
| IsNeedCoupon | bit | YES |  |  |  |
| InvoiceType | smallint | YES |  |  |  |
| RunAfterAllPromos | bit | YES |  |  |  |
| OutPutSameInput | bit | YES |  |  |  |
| SalesmanCanChangeOutPutQty | bit | YES |  |  |  |
| NeedWorkFlowApproval | bit | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
PromotionCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_LinkedSalesman]]
- [[OT_PromotionsCondUnCodInput]]
- [[OT_PromotionsSalesmanGroupsLink]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
- [[OSFA_DB/Tables/OT_PromotionsGroupsCustomersLink]]
