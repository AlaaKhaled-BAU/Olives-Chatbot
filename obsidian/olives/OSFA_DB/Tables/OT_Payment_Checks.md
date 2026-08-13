---
type: table
database: OSFA_DB
name: OT_Payment_Checks
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
referenced_by:
  - [[OT_Payment_Checks_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payment_Checks



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| PaidTransBankID | int | NO | ✓ |  |  |
| PaidTransBranchID | int | NO | ✓ |  |  |
| PaidTransYear | smallint | NO | ✓ |  |  |
| PaidTransNo | int | NO | ✓ |  |  |
| PaidTransTypeID | smallint | NO | ✓ |  |  |
| PaidTransCustomerID | bigint | NO | ✓ |  |  |
| PaidTransChequeNo | int | NO | ✓ |  |  |
| PaidAmount | float | YES |  |  |  |
## Primary Key
CompNo
TransactionYear
TransactionNo
TransactionTypeID
PaidTransBankID
PaidTransBranchID
PaidTransYear
PaidTransNo
PaidTransTypeID
PaidTransCustomerID
PaidTransChequeNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_Payment_Checks_Insert]]

**Writes (1):**
- [[OT_Payment_Checks_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
