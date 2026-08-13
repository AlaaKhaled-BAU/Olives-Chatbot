---
type: table
database: Olives_BO
name: ItemsStoreByUser
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 8
support_relevance: high
last_verified: 2026-08-05
---
# ItemsStoreByUser

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| StoreNo | int | NO | ✓ |  |  |
| ItemCode | nvarchar(50) | NO | ✓ |  |  |
| UserID | nvarchar(50) | NO | ✓ |  |  |
## Primary Key
CompanyID StoreNo ItemCode UserID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 8 procedure(s): 0 writing, 8 reading.
**Readers (8):**
- [[ItemAuditing_Hamouda]]
- [[ItemsOrderList_Details_Report]]
- [[ItemsOrderList_Header_Report]]
- [[PRO_PostProductionLoadingOrderApproval]]
- [[PRO_PreProductionLoadingOrderApproval]]
- [[Pro_ItemsOrderList]]
- [[Pro_ItemsStoreByUser]]
- [[Pro_TransfersOrdersDetails]]

## Estimated Size / Volatility
~0 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
