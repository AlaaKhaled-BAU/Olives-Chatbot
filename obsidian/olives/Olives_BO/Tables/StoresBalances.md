---
type: table
database: Olives_BO
name: StoresBalances
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
referenced_by:
  - [[Bajali_SAP_Integ]]
  - [[ECO_Land_SAP_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[Izhiman_SAP_Integ]]
  - [[Khobara_Integ]]
  - [[OT_SendSalesmanData]]
  - [[Qerat_Integ]]
  - [[RptOnlineRpt_ItemsStockWithReservedQty]]
  - [[SAMA_SAP_Integ]]
  - [[Salbeshian_SAP_Integ]]
  - [[Shini_Integ]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# StoresBalances


## Business Purpose

Inventory quantity-on-hand by item and store location.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Items]] |
| StoreNo | nvarchar | YES | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| Qty | money | YES |  |  |  |
## Primary Key
CompanyID
StoreNo
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_SendSalesmanData]]
- [[RptOnlineRpt_ItemsStockWithReservedQty]]

**Writes (10):**
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[Qerat_Integ]]
- [[SAMA_SAP_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[Shini_Integ]]
- [[Zedan_SAP_Integ]]

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
