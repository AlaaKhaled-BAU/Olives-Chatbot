---
type: table
database: OSFA_DB
name: OT_ConsOrderHF
schema: dbo
tags: [#mobile, #order]
foreign_keys:
referenced_by:
  - [[ADNAN_osfa]]
  - [[A_UnpostedbyTransactionOSFA]]
  - [[OT_ConsOrderHF_CheckExist]]
  - [[OT_ConsOrderHF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ConsOrderHF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| VouType | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| Posted | bit | NO |  |  |  |
| Notes | varchar | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| IssendSMS | bit | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
VouType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[ADNAN_osfa]]
- [[A_UnpostedbyTransactionOSFA]]
- [[OT_ConsOrderHF_CheckExist]]
- [[OT_ConsOrderHF_Insert]]

**Writes (1):**
- [[OT_ConsOrderHF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
