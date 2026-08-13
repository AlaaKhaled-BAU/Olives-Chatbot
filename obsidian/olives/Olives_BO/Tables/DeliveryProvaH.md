---
type: table
database: Olives_BO
name: DeliveryProvaH
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
referenced_by:
  - [[Pro_DeliveryAssigning]]
  - [[Pro_DeliveryInvoiceAssigning]]
  - [[Rpt_MasterOrders]]
  - [[Spartan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# DeliveryProvaH


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores deliveryprovah records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| DeliveryProvaNo | bigint | NO | ✓ |  |  |
| DeliverySalesmanNo | int | YES |  |  |  |
| DeliveryCarID | int | YES |  |  |  |
| DeliveryDate | smalldatetime | YES |  |  |  |
| Reference1 | varchar | YES |  |  |  |
| Reference2 | varchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| Approved | bit | YES |  |  |  |
## Primary Key
CompanyID
DeliveryProvaNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_DeliveryAssigning]]
- [[Pro_DeliveryInvoiceAssigning]]
- [[Rpt_MasterOrders]]
- [[Spartan_SAP_Integ]]

**Writes (1):**
- [[Pro_DeliveryAssigning]]

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
