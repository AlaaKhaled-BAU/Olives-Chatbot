---
type: table
database: OSFA_DB
name: OT_RequestToExceedCheckDueDate
schema: dbo
tags: [#mobile, #workflow]
foreign_keys:
referenced_by:
  - [[OT_RequestToExceedCheckDueDate_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedCheckDueDate



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| ReceiptAmount | float | YES |  |  |  |
| ChecksInfo | nvarchar | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| CustomerDueDays | smallint | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_RequestToExceedCheckDueDate_Insert]]

**Writes (1):**
- [[OT_RequestToExceedCheckDueDate_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
