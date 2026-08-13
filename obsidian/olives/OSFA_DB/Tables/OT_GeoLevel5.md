---
type: table
database: OSFA_DB
name: OT_GeoLevel5
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_GeoLevel5



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| GeoLevel1 | smallint | NO | ✓ |  |  |
| GeoLevel2 | smallint | NO | ✓ |  |  |
| GeoLevel3 | smallint | NO | ✓ |  |  |
| GeoLevel4 | smallint | NO | ✓ |  |  |
| GeoLevel5 | smallint | NO | ✓ |  |  |
| ArDesc | varchar | YES |  |  |  |
| EngDesc | varchar | YES |  |  |  |
## Primary Key
GeoLevel1
GeoLevel2
GeoLevel3
GeoLevel4
GeoLevel5
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
