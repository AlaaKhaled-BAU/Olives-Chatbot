---
type: table
database: OSFA_DB
name: OT_Checks
schema: dbo
tags: [#mobile]
foreign_keys:
  - [[OT_Payments]]
referenced_by:
  - [[OT_AppService]]
  - [[OT_Checks_CheckExist]]
  - [[OT_Checks_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Checks



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_Payments]] |
| VouType | smallint | NO | ✓ | ✓ | [[OT_Payments]] |
| VouYear | smallint | NO | ✓ | ✓ | [[OT_Payments]] |
| VouNo | int | NO | ✓ | ✓ | [[OT_Payments]] |
| ChqNo | int | NO | ✓ |  |  |
| BankNo | int | NO | ✓ |  |  |
| BranchNo | int | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| DueDate | smalldatetime | YES |  |  |  |
| ChqAmount | float | YES |  |  |  |
| Drawer | nvarchar | YES |  |  |  |
| ForeignChqAmount | float | YES |  |  |  |
| IsGero | bit | YES |  |  |  |
| CustBankAccNo | nvarchar | YES |  |  |  |
| AC_Payee | bit | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
ChqNo
BankNo
BranchNo
CustomerNo
## Foreign Keys
CompNo, VouType, VouYear, VouNo -> [[OT_Payments]](CompNo, VouType, VouYear, VouNo)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_AppService]]
- [[OT_Checks_CheckExist]]
- [[OT_Checks_Insert]]

**Writes (1):**
- [[OT_Checks_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong


## See also
- [[Olives_BO/Tables/Checks]] (Back Office counterpart table)

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
