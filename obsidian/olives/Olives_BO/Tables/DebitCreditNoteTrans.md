---
type: table
database: Olives_BO
name: DebitCreditNoteTrans
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[OT_ImportDebitCreditNoteTrans]]
  - [[Pro_DebitCreditNoteTrans]]
  - [[Rpt_DebitCreditNoteTrans]]
  - [[Rpt_ReceivablesSalesInvoice]]
support_relevance: high
last_verified: 2026-07-05
---
# DebitCreditNoteTrans


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores debitcreditnotetrans records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| InvNo | varchar | YES |  |  |  |
| InvAmount | float | YES |  |  |  |
| TotDisccount | float | YES |  |  |  |
| Tax | float | YES |  |  |  |
| NetDisccount | float | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_ImportDebitCreditNoteTrans]]
- [[Pro_DebitCreditNoteTrans]]
- [[Rpt_DebitCreditNoteTrans]]
- [[Rpt_ReceivablesSalesInvoice]]

**Writes (2):**
- [[OT_ImportDebitCreditNoteTrans]]
- [[Pro_DebitCreditNoteTrans]]

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
