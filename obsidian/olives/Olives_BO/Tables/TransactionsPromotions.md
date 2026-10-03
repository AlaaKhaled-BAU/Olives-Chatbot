---
type: table
database: Olives_BO
name: TransactionsPromotions
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportReturnOrder]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_ImportSalesOrders]]
  - [[Pro_CheckPromotionTarget]]
  - [[Rpt_CustomersPromotionLog]]
  - [[Rpt_PromotionCheckReport]]
  - [[Rpt_PromotionsWithDrawalsWithinDate]]
  - [[Rpt_RoutesByPeriod]]
  - [[Rpt_SalesPersonItemBonusTarget]]
support_relevance: high
last_verified: 2026-07-05
related_workflows: [[Promotion-Setup]]
---
# TransactionsPromotions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transactionspromotions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| TrTypeID | smallint | NO | ✓ |  |  |
| TrYear | smallint | NO | ✓ |  |  |
| TrNo | int | NO | ✓ |  |  |
| SerID | int | NO | ✓ |  |  |
| PromotionCode | nvarchar | YES |  |  |  |
| PromotionType | int | YES |  |  |  |
| PromotionName | nvarchar | YES |  |  |  |
| InputItem | nvarchar | YES |  |  |  |
| InputUnit | nvarchar | YES |  |  |  |
| InputQty | money | YES |  |  |  |
| InputAmount | float | YES |  |  |  |
| ItemNo | nvarchar | YES |  |  |  |
| UnitCode | nvarchar | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| ItemDiscountAmount | float | YES |  |  |  |
| ItemDiscountPercent | float | YES |  |  |  |
| VouDiscountAmount | float | YES |  |  |  |
| VouDiscountPercent | float | YES |  |  |  |
| IncludeInTargetBonus | bit | YES |  |  |  |
| IsInInput | bit | YES |  |  |  |
## Primary Key
CompanyID
TrTypeID
TrYear
TrNo
SerID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (9):**
- [[Pro_CheckPromotionTarget]]
- [[Rpt_CustomersPromotionLog]]
- [[Rpt_PromotionCheckReport]]
- [[Rpt_PromotionsWithDrawalsWithinDate]]
- [[Rpt_RoutesByPeriod]]
- [[Rpt_SalesPersonItemBonusTarget]]

**Writes (3):**
- [[OT_ImportReturnOrder]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
