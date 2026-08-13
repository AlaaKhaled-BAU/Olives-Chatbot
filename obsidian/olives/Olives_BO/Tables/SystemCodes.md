---
type: table
database: Olives_BO
name: SystemCodes
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
referenced_by:
  - [[Pro_AssetTransfer]]
  - [[Pro_AssetsDefinition]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_DeliveryAssigning]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DeliveryInvoiceAssigning]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_OT_Layout_Setting]]
  - [[Pro_ReceiptRequestsSchedule]]
  - [[Pro_SalesPersonBonusLimit]]
  - [[Pro_SalespersonsSendOrders]]
  - [[Pro_SystemCodes]]
  - [[Pro_SystemCodes_Manage]]
  - [[Pro_Territories]]
  - [[Pro_Vacations]]
  - [[Pro_WithdrawAssets]]
  - [[Rpt_BonusTypeForCustomers]]
  - [[Rpt_CashSummary]]
  - [[Rpt_ExpensesTrans]]
  - [[Rpt_SalesPersonCarLink]]
  - [[Rpt_TechnicianVisitDetails]]
  - [[TerritoriesOnlineReport]]
support_relevance: high
last_verified: 2026-07-05
---
# SystemCodes


## Business Purpose

Classification or reference codes for sales data categorization.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| SysCodeTypeID | nvarchar | YES | ✓ |  |  |
| SysCode | nvarchar | YES | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| CanEdit | bit | YES |  |  |  |
## Primary Key
SysCodeTypeID
SysCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (22):**
- [[Pro_AssetTransfer]]
- [[Pro_AssetsDefinition]]
- [[Pro_CustomersAndAssets]]
- [[Pro_DeliveryAssigning]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryInvoiceAssigning]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_OT_Layout_Setting]]
- [[Pro_ReceiptRequestsSchedule]]
- [[Pro_SalesPersonBonusLimit]]
- [[Pro_SalespersonsSendOrders]]
- [[Pro_SystemCodes]]
- [[Pro_SystemCodes_Manage]]
- [[Pro_Territories]]
- [[Pro_Vacations]]
- [[Pro_WithdrawAssets]]
- [[Rpt_BonusTypeForCustomers]]
- [[Rpt_CashSummary]]
- [[Rpt_ExpensesTrans]]
- [[Rpt_SalesPersonCarLink]]
- [[Rpt_TechnicianVisitDetails]]
- [[TerritoriesOnlineReport]]

**Writes (1):**
- [[Pro_SystemCodes_Manage]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
