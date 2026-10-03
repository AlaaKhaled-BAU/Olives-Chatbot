---
type: table
database: Olives_BO
name: GapTransTags
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[OT_ImportGapTrans]]
support_relevance: high
last_verified: 2026-07-05
---
# GapTransTags


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores gaptranstags records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| GapTransYear | smallint | NO | ✓ |  |  |
| GapTransNo | bigint | NO | ✓ |  |  |
| GapTagID | int | NO | ✓ |  |  |
| GapTagValue | varchar | YES |  |  |  |
## Primary Key
CompanyID
GapTransYear
GapTransNo
GapTagID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[OT_ImportGapTrans]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]

- [[GapTransHeaders]]
- [[GapTransTimeLine]]
- [[GapTags]]
## Cross-Database

See also: [[OSFA_DB/Tables/GapTransTags|FO GapTransTags]]
