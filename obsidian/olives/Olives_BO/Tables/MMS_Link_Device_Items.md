---
type: table
database: Olives_BO
name: MMS_Link_Device_Items
schema: dbo
tags: [#backoffice, #inventory, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_GetDataForAndroid]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_Link_Device_Items


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| DeviceID | int | NO | ✓ |  |  |
| ItemNo | nvarchar | YES | ✓ |  |  |
## Primary Key
CompanyID
DeviceID
ItemNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_MMS_GetDataForAndroid]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
