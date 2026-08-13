---
type: table
database: OSFA_DB
name: OT_Payment_Denominations
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
referenced_by:
  - [[OT_Payment_Denominations_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payment_Denominations



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| DenoID | int | NO | ✓ |  |  |
| Qty | int | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
DenoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_Payment_Denominations_Insert]]

**Writes (1):**
- [[OT_Payment_Denominations_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
