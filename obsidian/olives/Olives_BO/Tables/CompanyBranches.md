---
type: table
database: Olives_BO
name: CompanyBranches
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[ABS_Integ_SendInvoices]]
  - [[ABS_Integ_SendPayment_Sokhtian]]
  - [[Acback_Integration]]
  - [[AccPack_Integ]]
  - [[AccPack_Integyandrug]]
  - [[Awael_Integration_WithLog]]
  - [[Awtar_Integration_WithLog]]
  - [[Bonanza_Integ_Esmint]]
  - [[CL_Integration]]
  - [[Darwaza_Integration_WithLog]]
  - [[Ejabi_Integration]]
  - [[Falcons_GetItemBalance]]
  - [[Falcons_Integ]]
  - [[GTS_Integration_WithLog]]
  - [[Galaxy_Integration]]
  - [[IscoJordan_Integration]]
  - [[Isco_Integration_WithLog]]
  - [[JV_Integ]]
  - [[Lafarg_Integration]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[Mira_Integration_WithLog]]
  - [[Mira_Wales_Integration_WithLog]]
  - [[Motakaml_Integ_GetItemBalance]]
  - [[Motakaml_Integration_WithLog]]
  - [[NPF_Integration]]
  - [[Niroukh_Integration_WithLog]]
  - [[OT_SendCompData]]
  - [[OT_SendSalesmanData]]
  - [[PRESTOSOFT_INTEGRATION_COMP2]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[PrestoSoft_Integration]]
  - [[ProTech_Integration]]
  - [[Pro_CompanyBranches]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersPromotionsGroups]]
  - [[Pro_DeliveryCar]]
  - [[Pro_LastSalesmenTransactionsDateTime]]
  - [[Pro_PromotionsHeaders]]
  - [[Pro_SalesPersons]]
  - [[Pro_TransLock]]
  - [[Pro_UserCompanyBranchesLink]]
  - [[Rpt_CollectedReceiptsByCompany]]
  - [[Rpt_CustomerInfoAndRouteDetails]]
  - [[Rpt_CustomersSalesDetails]]
  - [[Rpt_IncreaseCreditLimit]]
  - [[Rpt_IncreaseCreditLimit_forALPHA]]
  - [[Rpt_LinkedCallCenter]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_ReportHeader]]
  - [[Rpt_SalesPersonsName]]
  - [[Rpt_SalesTransactionByDocumentsTypes]]
  - [[Rpt_SalesmanSalesByCategory2]]
  - [[Rpt_SalesmanSalesDetails]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
  - [[Rpt_WFCustomersVisits]]
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
  - [[SN_Integration]]
  - [[Shamel_Integration]]
  - [[Tahona_Integration_WithLog]]
  - [[WF_GetPositionWFData]]
  - [[Wings_Integration]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
  - Users-and-Permissions
---
# CompanyBranches


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores companybranches records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Address | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (73):**
- [[ABS_Integ_SendInvoices]]
- [[ABS_Integ_SendPayment_Sokhtian]]
- [[Acback_Integration]]
- [[AccPack_Integ]]
- [[AccPack_Integyandrug]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Bonanza_Integ_Esmint]]
- [[CL_Integration]]
- [[Darwaza_Integration_WithLog]]
- [[Ejabi_Integration]]
- [[Falcons_GetItemBalance]]
- [[Falcons_Integ]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[IscoJordan_Integration]]
- [[Isco_Integration_WithLog]]
- [[JV_Integ]]
- [[Lafarg_Integration]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Motakaml_Integ_GetItemBalance]]
- [[Motakaml_Integration_WithLog]]
- [[NPF_Integration]]
- [[Niroukh_Integration_WithLog]]
- [[OT_SendCompData]]
- [[OT_SendSalesmanData]]
- [[PRESTOSOFT_INTEGRATION_COMP2]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[PrestoSoft_Integration]]
- [[ProTech_Integration]]
- [[Pro_CompanyBranches]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersPromotionsGroups]]
- [[Pro_DeliveryCar]]
- [[Pro_LastSalesmenTransactionsDateTime]]
- [[Pro_PromotionsHeaders]]
- [[Pro_SalesPersons]]
- [[Pro_TransLock]]
- [[Pro_UserCompanyBranchesLink]]
- [[Rpt_CollectedReceiptsByCompany]]
- [[Rpt_CustomerInfoAndRouteDetails]]
- [[Rpt_CustomersSalesDetails]]
- [[Rpt_IncreaseCreditLimit]]
- [[Rpt_IncreaseCreditLimit_forALPHA]]
- [[Rpt_LinkedCallCenter]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_ReportHeader]]
- [[Rpt_SalesPersonsName]]
- [[Rpt_SalesTransactionByDocumentsTypes]]
- [[Rpt_SalesmanSalesByCategory2]]
- [[Rpt_SalesmanSalesDetails]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
- [[Rpt_WFCustomersVisits]]
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
- [[SN_Integration]]
- [[Shamel_Integration]]
- [[Tahona_Integration_WithLog]]
- [[WF_GetPositionWFData]]
- [[Wings_Integration]]

**Writes (28):**
- [[Acback_Integration]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Bonanza_Integ_Esmint]]
- [[Darwaza_Integration_WithLog]]
- [[Ejabi_Integration]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[Isco_Integration_WithLog]]
- [[JV_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[ProTech_Integration]]
- [[Pro_CompanyBranches]]
- [[SAP_Integ]]
- [[SAP_Integ_Amazing]]
- [[SAP_Integ_Hammoudeh]]
- [[SAP_Integ_Kaylani]]
- [[SAP_Integ_Lamis]]
- [[SAP_Integ_MERI]]
- [[SAP_Integration_WithLog]]
- [[SAP_Naouri_Integ]]
- [[SAP_Tyconz_Integ]]
- [[Shamel_Integration]]

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
