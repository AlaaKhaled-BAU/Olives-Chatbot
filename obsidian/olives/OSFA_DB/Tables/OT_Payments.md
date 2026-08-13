---
type: table
database: OSFA_DB
name: OT_Payments
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
referenced_by:
  - [[ADNAN_osfa]]
  - [[A_UnpostedbyTransactionOSFA]]
  - [[OT_Payments_CheckExist]]
  - [[OT_Payments_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payments



## Business Purpose


Payment records collected via Android tablets — cash, checks, and bank transfers.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| DocType | smallint | YES |  |  |  |
| Amount | float | YES |  |  |  |
| GPSx | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| IsPosted | bit | NO |  |  |  |
| RouteID | int | YES |  |  |  |
| Discount | float | YES |  |  |  |
| RefNo | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| IsWFApproved | bit | YES |  |  |  |
| WFApproveDesc | nvarchar | YES |  |  |  |
| Currency | int | YES |  |  |  |
| ExRate | float | YES |  |  |  |
| ForeignAmount | float | YES |  |  |  |
| ForeignDiscount | float | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| DetailCount | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| RequestOrderYear | smallint | YES |  |  |  |
| RequestOrderNo | int | YES |  |  |  |
| Bank_TransferNo | nvarchar | YES |  |  |  |
| Bank_Transfer_Date | smalldatetime | YES |  |  |  |
| Bank_Transfer_Amount | float | YES |  |  |  |
| Bank_Transfer_BankID | int | YES |  |  |  |
| Bank_Transfer_BankAccount | int | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[ADNAN_osfa]]
- [[A_UnpostedbyTransactionOSFA]]
- [[OT_Payments_CheckExist]]
- [[OT_Payments_Insert]]

**Writes (1):**
- [[OT_Payments_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong


## See also
- [[Olives_BO/Tables/Receipts]] (Back Office counterpart table)

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
