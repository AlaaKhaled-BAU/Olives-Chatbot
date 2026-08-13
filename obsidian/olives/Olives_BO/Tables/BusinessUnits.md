---
type: table
database: Olives_BO
name: BusinessUnits
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[CompanyBranches]]
referenced_by:
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[Acback_Integration]]
  - [[AccPack_Integ]]
  - [[AccPack_Integyandrug]]
  - [[Awael_Integration_WithLog]]
  - [[Awtar_Integration_WithLog]]
  - [[Bajali_SAP_Integ]]
  - [[Bonanza_Integ_Esmint]]
  - [[CL_Integration]]
  - [[Darwaza_Integration_WithLog]]
  - [[ECO_Land_SAP_Integ]]
  - [[Ejabi_Integration]]
  - [[FixDuplicate_All]]
  - [[GArrow_SAP_Integ]]
  - [[GTS_Integration_WithLog]]
  - [[Galaxy_Integration]]
  - [[IscoJordan_Integration]]
  - [[Isco_Integration_WithLog]]
  - [[Izhiman_SAP_Integ]]
  - [[Khobara_Integ]]
  - [[Lafarg_Integration]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[Mira_Integration_WithLog]]
  - [[Mira_Wales_Integration_WithLog]]
  - [[NPF_Integration]]
  - [[Niroukh_Integration_WithLog]]
  - [[OT_ImportSalesIssueItems]]
  - [[OT_ImportSalesOrders]]
  - [[OT_SendCompData]]
  - [[PRESTOSOFT_INTEGRATION_COMP2]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[PrestoSoft_Integration]]
  - [[ProTech_Integration]]
  - [[Pro_BusinessUnits]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_ImportRouteInfoFromExcel]]
  - [[Pro_ImportRouteInfoFromExcel2]]
  - [[Pro_SalesPersons]]
  - [[Pro_TransLock]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RamPharm_SAP_Integ]]
  - [[SAMA_SAP_Integ]]
  - [[SAP_Integ]]
  - [[SAP_Integ_Amazing]]
  - [[SAP_Integ_Hammoudeh]]
  - [[SAP_Integ_Karadsheh]]
  - [[SAP_Integ_Kaylani]]
  - [[SAP_Integ_Lamis]]
  - [[SAP_Integ_MERI]]
  - [[SAP_Integ_Malak]]
  - [[SAP_Integration_WithLog]]
  - [[SAP_Tyconz_Integ]]
  - [[SN_Integration]]
  - [[Salbeshian_SAP_Integ]]
  - [[Shamel_Integration]]
  - [[Shini_Integ]]
  - [[Spartan_SAP_Integ]]
  - [[Tahona_Integration_WithLog]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
  - [[Wings_Integration]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
  - Salesman-Onboarding
---
# BusinessUnits


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores businessunits records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CompanyBranches]] |
| ID | int | NO | ✓ |  |  |
| Parent | int | YES |  |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Level | int | YES |  |  |  |
| CompanyBrancheID | int | YES |  | ✓ | [[CompanyBranches]] |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CompanyBrancheID -> [[CompanyBranches]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (68):**
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Acback_Integration]]
- [[AccPack_Integ]]
- [[AccPack_Integyandrug]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Bajali_SAP_Integ]]
- [[Bonanza_Integ_Esmint]]
- [[CL_Integration]]
- [[Darwaza_Integration_WithLog]]
- [[ECO_Land_SAP_Integ]]
- [[Ejabi_Integration]]
- [[FixDuplicate_All]]
- [[GArrow_SAP_Integ]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[IscoJordan_Integration]]
- [[Isco_Integration_WithLog]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[Lafarg_Integration]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[NPF_Integration]]
- [[Niroukh_Integration_WithLog]]
- [[OT_ImportSalesIssueItems]]
- [[OT_ImportSalesOrders]]
- [[OT_SendCompData]]
- [[PRESTOSOFT_INTEGRATION_COMP2]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[PrestoSoft_Integration]]
- [[ProTech_Integration]]
- [[Pro_BusinessUnits]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_ImportRouteInfoFromExcel]]
- [[Pro_ImportRouteInfoFromExcel2]]
- [[Pro_SalesPersons]]
- [[Pro_TransLock]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[SAP_Integ]]
- [[SAP_Integ_Amazing]]
- [[SAP_Integ_Hammoudeh]]
- [[SAP_Integ_Karadsheh]]
- [[SAP_Integ_Kaylani]]
- [[SAP_Integ_Lamis]]
- [[SAP_Integ_MERI]]
- [[SAP_Integ_Malak]]
- [[SAP_Integration_WithLog]]
- [[SAP_Tyconz_Integ]]
- [[SN_Integration]]
- [[Salbeshian_SAP_Integ]]
- [[Shamel_Integration]]
- [[Shini_Integ]]
- [[Spartan_SAP_Integ]]
- [[Tahona_Integration_WithLog]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
- [[Wings_Integration]]
- [[Zedan_SAP_Integ]]

**Writes (43):**
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Acback_Integration]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Bajali_SAP_Integ]]
- [[Bonanza_Integ_Esmint]]
- [[Darwaza_Integration_WithLog]]
- [[Ejabi_Integration]]
- [[GArrow_SAP_Integ]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[Isco_Integration_WithLog]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[ProTech_Integration]]
- [[Pro_BusinessUnits]]
- [[Pro_CustomersFinancialDetails]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[SAP_Integ]]
- [[SAP_Integ_Amazing]]
- [[SAP_Integ_Hammoudeh]]
- [[SAP_Integ_Karadsheh]]
- [[SAP_Integ_Kaylani]]
- [[SAP_Integ_Lamis]]
- [[SAP_Integ_MERI]]
- [[SAP_Integ_Malak]]
- [[SAP_Integration_WithLog]]
- [[SAP_Tyconz_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[Shamel_Integration]]
- [[Shini_Integ]]
- [[Zedan_SAP_Integ]]

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
