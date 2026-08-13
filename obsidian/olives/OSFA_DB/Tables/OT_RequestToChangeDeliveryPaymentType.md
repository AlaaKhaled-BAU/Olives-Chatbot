---
type: table
database: OSFA_DB
name: OT_RequestToChangeDeliveryPaymentType
schema: dbo
tags: [#billing, #mobile, #order, #reference, #workflow]
foreign_keys:
referenced_by:
  - [[OT_RequestToChangeDeliveryPaymentType_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToChangeDeliveryPaymentType



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| OriginalSalespersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| TrTypeID | smallint | YES |  |  |  |
| TrTypeYear | smallint | YES |  |  |  |
| TrTypeNo | int | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| OldPaymentType | int | YES |  |  |  |
| NewPaymentType | int | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_RequestToChangeDeliveryPaymentType_Insert]]

**Writes (1):**
- [[OT_RequestToChangeDeliveryPaymentType_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
