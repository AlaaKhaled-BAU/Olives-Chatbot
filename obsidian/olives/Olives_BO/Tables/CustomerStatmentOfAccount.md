---
type: table
database: Olives_BO
name: CustomerStatmentOfAccount
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[ABS_Integration_Jebrene]]
  - [[ABS_Integration_Sokhtian]]
  - [[AbuOda_Integ]]
  - [[AccPack_Integ_LuxuryItems]]
  - [[AccPack_Integ_LuxuryItems_StatmentOfAccount]]
  - [[Alpha_Integ]]
  - [[Alpha_Integ_GoldenArrow]]
  - [[Alpha_Integ_HistData]]
  - [[Alpha_updateRoute]]
  - [[Awa2el_Integ]]
  - [[Awtar_Integration_SOA]]
  - [[Bajali_SAP_Integ]]
  - [[Bonanza_Integ_Esmint]]
  - [[Bonanza_Integ_Yasmeen]]
  - [[ECO_Land_SAP_Integ]]
  - [[Falcons_Integ_Send_StatmentOfAccount]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ]]
  - [[GP_Integ_Wadi]]
  - [[Galaxy_Integration]]
  - [[IscoJordan_Integration]]
  - [[Jazeera_Integ]]
  - [[Lafarg_Integration]]
  - [[MeatLand_Integration]]
  - [[Niroukh_Integration_SOA]]
  - [[RamPharm_SAP_Integ]]
  - [[Rpt_CustomerAccountStatement_Sukhtian]]
  - [[Rpt_CustomerStatmentOfAccount]]
  - [[SAMA_SAP_Integ]]
  - [[Spartan_SAP_Integ]]
  - [[X3_Integ_SOA_Batches]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerStatmentOfAccount


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerstatmentofaccount records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| TrType | varchar | YES | ✓ |  |  |
| TrNo | varchar | YES | ✓ |  |  |
| TrSer | smallint | NO | ✓ |  |  |
| DeptNo | int | NO | ✓ |  |  |
| TrDate | smalldatetime | NO | ✓ |  |  |
| TrName | varchar | YES |  |  |  |
| Debit | money | YES |  |  |  |
| Credit | money | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| Balance | money | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
TrType
TrNo
TrSer
DeptNo
TrDate
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (28):**
- [[ABS_Integration_Jebrene]]
- [[ABS_Integration_Sokhtian]]
- [[AbuOda_Integ]]
- [[AccPack_Integ_LuxuryItems]]
- [[AccPack_Integ_LuxuryItems_StatmentOfAccount]]
- [[Alpha_Integ]]
- [[Alpha_Integ_GoldenArrow]]
- [[Alpha_Integ_HistData]]
- [[Alpha_updateRoute]]
- [[Awa2el_Integ]]
- [[Awtar_Integration_SOA]]
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[Falcons_Integ_Send_StatmentOfAccount]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ]]
- [[GP_Integ_Wadi]]
- [[Galaxy_Integration]]
- [[IscoJordan_Integration]]
- [[Jazeera_Integ]]
- [[Lafarg_Integration]]
- [[MeatLand_Integration]]
- [[Niroukh_Integration_SOA]]
- [[RamPharm_SAP_Integ]]
- [[Rpt_CustomerAccountStatement_Sukhtian]]
- [[Rpt_CustomerStatmentOfAccount]]
- [[SAMA_SAP_Integ]]
- [[Spartan_SAP_Integ]]

**Writes (24):**
- [[ABS_Integration_Jebrene]]
- [[ABS_Integration_Sokhtian]]
- [[AbuOda_Integ]]
- [[AccPack_Integ_LuxuryItems_StatmentOfAccount]]
- [[Alpha_Integ]]
- [[Alpha_Integ_HistData]]
- [[Alpha_updateRoute]]
- [[Awa2el_Integ]]
- [[Awtar_Integration_SOA]]
- [[Bajali_SAP_Integ]]
- [[Bonanza_Integ_Esmint]]
- [[Bonanza_Integ_Yasmeen]]
- [[ECO_Land_SAP_Integ]]
- [[Falcons_Integ_Send_StatmentOfAccount]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ_Wadi]]
- [[Galaxy_Integration]]
- [[IscoJordan_Integration]]
- [[Lafarg_Integration]]
- [[MeatLand_Integration]]
- [[Niroukh_Integration_SOA]]
- [[RamPharm_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[X3_Integ_SOA_Batches]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
