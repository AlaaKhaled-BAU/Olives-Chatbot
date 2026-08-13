---
type: table
database: OSFA_DB
name: OT_JsonLog_Tmp
schema: dbo
tags: [#log, #mobile]
foreign_keys:
referenced_by:
support_relevance: low
last_verified: 2026-07-05
---
# OT_JsonLog_Tmp



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | numeric | YES | ✓ |  |  |
| CompNo | smallint | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| ErrDesc | nvarchar | YES |  |  |  |
| SysDate | smalldatetime | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_RequestToLoginToCustomerWithoutVerficiation]]
- [[OT_OrderHistoryDF]]
- [[OT_JsonLog]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
