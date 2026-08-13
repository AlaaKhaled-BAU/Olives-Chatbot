---
type: table
database: Olives_BO
name: SalesPersonNotbookTransactionsSerials
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[OT_SendSalesmanData]]
  - [[Pro_SalesPersonNotbookTransactionsSerials]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonNotbookTransactionsSerials


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonnotbooktransactionsserials records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| SerYear | smallint | NO | ✓ |  |  |
| SerType | smallint | NO | ✓ |  |  |
| NotbookNo | nvarchar | YES | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| FromNo | int | YES |  |  |  |
| ToNo | int | YES |  |  |  |
| NextSerial | int | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
SerYear
SerType
NotbookNo
CustomerID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesPersonNotbookTransactionsSerials]]

**Writes (2):**
- [[OT_SendSalesmanData]]
- [[Pro_SalesPersonNotbookTransactionsSerials]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
