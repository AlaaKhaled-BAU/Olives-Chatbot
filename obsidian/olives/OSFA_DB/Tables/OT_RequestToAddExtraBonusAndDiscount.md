---
type: table
database: OSFA_DB
name: OT_RequestToAddExtraBonusAndDiscount
schema: dbo
tags: [#billing, #mobile, #workflow]
foreign_keys:
referenced_by:
  - [[OT_RequestToAddExtraBonusAndDiscount_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToAddExtraBonusAndDiscount



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| TrType | int | YES |  |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| ApprovePercent | float | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_RequestToAddExtraBonusAndDiscount_Insert]]

**Writes (1):**
- [[OT_RequestToAddExtraBonusAndDiscount_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
