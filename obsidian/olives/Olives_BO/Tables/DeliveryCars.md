---
type: table
database: Olives_BO
name: DeliveryCars
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[CompanyBranches]]
referenced_by:
  - [[OSFA_MobileDeliveryAPI]]
  - [[OT_AppCarAndSalesperson]]
  - [[Pro_AssignOrderDeliveryToCar]]
  - [[Pro_CarAndSalespersonLink]]
  - [[Pro_DeliveryAssigning]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DeliveryCarSummaryReport]]
  - [[Pro_DeliveryInvoiceAssigning]]
  - [[Pro_DeliveryManifest]]
  - [[Pro_SalesPersons]]
  - [[Rpt_DeliveryBatchHeader]]
  - [[Rpt_DeliveryCarSummaryReport]]
  - [[Rpt_DeliverySales]]
  - [[Rpt_InvoicesDelivery]]
  - [[Rpt_PrintCustomersBarcode]]
  - [[Rpt_SalesPersonCarLink]]
  - [[Rpt_SalesPersonsName]]
support_relevance: high
last_verified: 2026-07-05
---
# DeliveryCars


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores deliverycars records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CompanyBranches]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| LoadWieght | float | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| CarType | int | YES |  |  |  |
| Barcode | nvarchar | YES |  |  |  |
| BranchID | int | YES |  | ✓ | [[CompanyBranches]] |
| GPSX | float | YES |  |  |  |
| GPSY | float | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, BranchID -> [[CompanyBranches]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (17):**
- [[OSFA_MobileDeliveryAPI]]
- [[OT_AppCarAndSalesperson]]
- [[Pro_AssignOrderDeliveryToCar]]
- [[Pro_CarAndSalespersonLink]]
- [[Pro_DeliveryAssigning]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryCarSummaryReport]]
- [[Pro_DeliveryInvoiceAssigning]]
- [[Pro_DeliveryManifest]]
- [[Pro_SalesPersons]]
- [[Rpt_DeliveryBatchHeader]]
- [[Rpt_DeliveryCarSummaryReport]]
- [[Rpt_DeliverySales]]
- [[Rpt_InvoicesDelivery]]
- [[Rpt_PrintCustomersBarcode]]
- [[Rpt_SalesPersonCarLink]]
- [[Rpt_SalesPersonsName]]

**Writes (1):**
- [[Pro_DeliveryCar]]

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
- [[Olives_BO/Tables/ScheduleDeliveryOrders]]
