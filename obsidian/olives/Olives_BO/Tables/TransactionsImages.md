---
type: table
database: Olives_BO
name: TransactionsImages
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[Items]]
referenced_by:
  - [[OT_ImportSalesInvoices]]
support_relevance: high
last_verified: 2026-07-05
---
# TransactionsImages


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transactionsimages records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Items]] |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| ItemImage | image | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[OT_ImportSalesInvoices]]

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
