---
type: table
database: Olives_BO
name: NewCustomerSpecialFields_Def
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[Pro_NewCustomerSpecialFields]]
support_relevance: high
last_verified: 2026-07-05
---
# NewCustomerSpecialFields_Def


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores newcustomerspecialfields def records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| FieldID | int | NO | ✓ |  |  |
| FieldCaption | varchar | YES |  |  |  |
| FieldForeignCaption | varchar | YES |  |  |  |
| IsRequired | bit | YES |  |  |  |
## Primary Key
CompanyID
FieldID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_NewCustomerSpecialFields]]

**Writes (1):**
- [[Pro_NewCustomerSpecialFields]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
