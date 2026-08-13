---
type: table
database: Olives_BO
name: MMS_PaymentsChecksDetails
schema: dbo
tags: [#backoffice, #billing, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_PaymentsChecksDetails]]
  - [[Pro_MMS_SetDataForAndroid]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_PaymentsChecksDetails


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PaymentYear | smallint | NO | ✓ |  |  |
| PaymentNo | bigint | NO | ✓ |  |  |
| LineID | int | NO | ✓ |  |  |
| CheckNo | int | NO | ✓ |  |  |
| DueDate | smalldatetime | YES |  |  |  |
| Amount | float | YES |  |  |  |
| BankID | int | YES |  |  |  |
| BranchID | int | YES |  |  |  |
| DrawerName | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
PaymentYear
PaymentNo
LineID
CheckNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_MMS_PaymentsChecksDetails]]
- [[Pro_MMS_SetDataForAndroid]]

**Writes (1):**
- [[Pro_MMS_SetDataForAndroid]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/MMS_ShowRooms]]
- [[Olives_BO/Tables/Pos_InvoiceOrderHF]]
- [[Olives_BO/Tables/MMS_DV_ErrorLog]]
- [[Olives_BO/Tables/PriceListQtyRanges]]
