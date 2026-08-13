---
type: table
database: Olives_BO
name: DeliveryManifest
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
referenced_by:
  - [[Falcons_Integ]]
  - [[OT_SendCustomersInfo]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DeliveryManifest]]
  - [[Pro_UnCloseOrder]]
  - [[Rpt_DriversDeliverySummary]]
  - [[Rpt_InvoicesDelivery]]
  - [[Rpt_SalesmanDeliverySummary]]
  - [[Tablet_GetSalesmanDeliveryTrans]]
support_relevance: high
last_verified: 2026-07-05
---
# DeliveryManifest


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores deliverymanifest records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| Serial | int | NO | ✓ |  |  |
| DeliverySalesmanNo | int | YES |  |  |  |
| AssistantSalesmanNo | int | YES |  |  |  |
| DeliveryCarID | int | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
## Primary Key
CompanyID
Serial
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (9):**
- [[Falcons_Integ]]
- [[OT_SendCustomersInfo]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryManifest]]
- [[Pro_UnCloseOrder]]
- [[Rpt_DriversDeliverySummary]]
- [[Rpt_InvoicesDelivery]]
- [[Rpt_SalesmanDeliverySummary]]
- [[Tablet_GetSalesmanDeliveryTrans]]

**Writes (2):**
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryManifest]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
