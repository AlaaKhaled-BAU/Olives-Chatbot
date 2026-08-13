---
type: table
database: Olives_BO
name: Positions
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[ABS_Integration_Jebrene]]
  - [[ABS_Integration_Sokhtian]]
  - [[AX_INTEGRATION]]
  - [[AX_Integration_AbuTawileh]]
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[Acback_Integration]]
  - [[AccPack_Integ]]
  - [[AccPack_Integ_LuxuryItems]]
  - [[AccPack_Integyandrug]]
  - [[Alpha_Integ]]
  - [[Alpha_updateRoute]]
  - [[Awa2el_Integ]]
  - [[Awael_Integration_WithLog]]
  - [[Awtar_Integration_WithLog]]
  - [[Bajali_SAP_Integ]]
  - [[Bonanza_Integ_Esmint]]
  - [[Bonanza_Integ_Yasmeen]]
  - [[DEVICEREPORT_TABLE_UPDATE]]
  - [[Darwaza_Integration_WithLog]]
  - [[Defaf_Integration]]
  - [[ECO_Land_SAP_Integ]]
  - [[Ejabi_Integration]]
  - [[Falcons_Integ]]
  - [[Fill_Sales_Device_Reports]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ]]
  - [[GP_Integ_Wadi]]
  - [[GP_Integ_Zumot]]
  - [[GP_Integ_Zumot_Aqaba]]
  - [[GP_Integration_Wadi_Collect]]
  - [[GTS_Integration_WithLog]]
  - [[Galaxy_Integration]]
  - [[Isco_Integration_WithLog]]
  - [[Izhiman_SAP_Integ]]
  - [[JV_Integ]]
  - [[Jazeera_Integ]]
  - [[Khobara_Integ]]
  - [[Lafarg_Integration]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[Mira_Integration_WithLog]]
  - [[Mira_Wales_Integration_WithLog]]
  - [[Niroukh_Integration_WithLog]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[Olives_Merch_Integ]]
  - [[PRESTOSOFT_INTEGRATION_COMP2]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[PrestoSoft_Integration]]
  - [[Presto_Integ]]
  - [[ProTech_Integration]]
  - [[Pro_ItemsUsedInLoadOrderAssignment]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_Positions]]
  - [[Pro_ProspectiveCustomers]]
  - [[Pro_SalesPersonContractsAssignment]]
  - [[Pro_WF_SetupHeader]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RamPharm_SAP_Integ]]
  - [[Rpt_ActiveAndInactiveCustomers]]
  - [[Rpt_CustomersAvgPerClass]]
  - [[Rpt_LinkedCallCenter]]
  - [[Rpt_SalesPersonAndCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
  - [[Rpt_WF_SalesOrderStatus]]
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
  - [[SAP_Naouri_Integ]]
  - [[SAP_Tyconz_Integ]]
  - [[Salbeshian_SAP_Integ]]
  - [[Shini_Integ]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
  - [[Wings_Integration]]
  - [[Yolande_Integ]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
  - Salesman-Onboarding
  - Workflow-Approval-Setup
---
# Positions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores positions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Erp_Reference | varchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (49):**
- [[ABS_Integration_Jebrene]]
- [[AX_INTEGRATION]]
- [[AX_Integration_AbuTawileh]]
- [[Acback_Integration]]
- [[AccPack_Integ]]
- [[AccPack_Integ_LuxuryItems]]
- [[AccPack_Integyandrug]]
- [[Awa2el_Integ]]
- [[Bonanza_Integ_Esmint]]
- [[Bonanza_Integ_Yasmeen]]
- [[DEVICEREPORT_TABLE_UPDATE]]
- [[Ejabi_Integration]]
- [[Fill_Sales_Device_Reports]]
- [[GP_Integ]]
- [[GP_Integ_Zumot]]
- [[GP_Integ_Zumot_Aqaba]]
- [[GP_Integration_Wadi_Collect]]
- [[JV_Integ]]
- [[Lafarg_Integration]]
- [[Olives_Merch_Integ]]
- [[PRESTOSOFT_INTEGRATION_COMP2]]
- [[PrestoSoft_Integration]]
- [[ProTech_Integration]]
- [[Pro_ItemsUsedInLoadOrderAssignment]]
- [[Pro_OrdersHeaders]]
- [[Pro_Positions]]
- [[Pro_ProspectiveCustomers]]
- [[Pro_SalesPersonContractsAssignment]]
- [[Pro_WF_SetupHeader]]
- [[Rpt_ActiveAndInactiveCustomers]]
- [[Rpt_CustomersAvgPerClass]]
- [[Rpt_LinkedCallCenter]]
- [[Rpt_SalesPersonAndCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
- [[Rpt_WF_SalesOrderStatus]]
- [[SAP_Integ]]
- [[SAP_Integ_Amazing]]
- [[SAP_Integ_Hammoudeh]]
- [[SAP_Integ_Kaylani]]
- [[SAP_Integ_Lamis]]
- [[SAP_Integ_MERI]]
- [[SAP_Integ_Malak]]
- [[SAP_Naouri_Integ]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
- [[Wings_Integration]]
- [[Yolande_Integ]]

**Writes (66):**
- [[ABS_Integration_Jebrene]]
- [[ABS_Integration_Sokhtian]]
- [[AX_Integration_AbuTawileh]]
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Acback_Integration]]
- [[AccPack_Integ_LuxuryItems]]
- [[Alpha_Integ]]
- [[Alpha_updateRoute]]
- [[Awa2el_Integ]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Bajali_SAP_Integ]]
- [[Bonanza_Integ_Esmint]]
- [[Bonanza_Integ_Yasmeen]]
- [[Darwaza_Integration_WithLog]]
- [[Defaf_Integration]]
- [[ECO_Land_SAP_Integ]]
- [[Ejabi_Integration]]
- [[Falcons_Integ]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ]]
- [[GP_Integ_Wadi]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[Isco_Integration_WithLog]]
- [[Izhiman_SAP_Integ]]
- [[JV_Integ]]
- [[Jazeera_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Olives_Merch_Integ]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[Presto_Integ]]
- [[ProTech_Integration]]
- [[Pro_Positions]]
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
- [[Shini_Integ]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
- [[Wings_Integration]]
- [[Yolande_Integ]]
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
