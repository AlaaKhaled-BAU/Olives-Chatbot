---
type: table
database: OSFA_DB
name: OT_NewCustomersSpecialFields
schema: dbo
tags: [#customer, #mobile]
foreign_keys:
referenced_by:
  - [[OT_NewCustomersSpecialFieldsInsert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_NewCustomersSpecialFields



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| NewCustID | numeric | YES | ✓ |  |  |
| FieldID | int | NO | ✓ |  |  |
| FieldValue | nvarchar | YES |  |  |  |
## Primary Key
CompNo
NewCustID
FieldID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_NewCustomersSpecialFieldsInsert]]

**Writes (1):**
- [[OT_NewCustomersSpecialFieldsInsert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
