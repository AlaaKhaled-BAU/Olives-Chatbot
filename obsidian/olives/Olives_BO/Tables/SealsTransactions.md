---
type: table
database: Olives_BO
name: SealsTransactions
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[Pro_SealsTransactions]]
support_relevance: high
last_verified: 2026-07-05
---
# SealsTransactions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores sealstransactions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| TrDateTime | smalldatetime | NO | ✓ |  |  |
| SealNo1 | varchar | YES |  |  |  |
| SealNo2 | varchar | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
TrDateTime
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SealsTransactions]]

**Writes (1):**
- [[Pro_SealsTransactions]]

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
