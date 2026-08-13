---
type: table
database: Olives_BO
name: MMS_PaymentsHeader
schema: dbo
tags: [#backoffice, #billing, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_PaymentsHeader]]
  - [[Pro_MMS_SetDataForAndroid]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_PaymentsHeader


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PaymentYear | smallint | NO | ✓ |  |  |
| PaymentNo | bigint | NO | ✓ |  |  |
| PaymentDate | smalldatetime | YES |  |  |  |
| InvoiceYear | smallint | NO |  |  |  |
| InvoiceNo | bigint | YES |  |  |  |
| CashAmount | float | YES |  |  |  |
| CheckAmount | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| OrderAutoID | numeric | YES |  |  |  |
| OrderSubID | int | YES |  |  |  |
| ScheduleID | int | YES |  |  |  |
## Primary Key
CompanyID
PaymentYear
PaymentNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_MMS_PaymentsHeader]]
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
