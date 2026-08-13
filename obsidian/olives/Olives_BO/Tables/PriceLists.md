---
type: table
database: Olives_BO
name: PriceLists
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[ABS_Integration_Jebrene]]
  - [[ABS_Integration_Sokhtian]]
  - [[AX_INTEGRATION]]
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[Acback_Integration]]
  - [[AccPack_Integ]]
  - [[AccPack_Integ_LuxuryItems]]
  - [[AccPack_Integyandrug]]
  - [[Alpha_Integ]]
  - [[Alpha_updateRoute]]
  - [[Awael_Integration_WithLog]]
  - [[Awtar_Integration_WithLog]]
  - [[Bajali_SAP_Integ]]
  - [[Bonanza_Integ_Yasmeen]]
  - [[Darwaza_Integration_WithLog]]
  - [[Defaf_Integration]]
  - [[ECO_Land_SAP_Integ]]
  - [[Falcons_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ]]
  - [[GP_Integ_Wadi]]
  - [[GP_Integ_Zumot]]
  - [[GP_Integ_Zumot_Aqaba]]
  - [[GTS_Integration_WithLog]]
  - [[Galaxy_Integration]]
  - [[Isco_Integration_WithLog]]
  - [[Izhiman_SAP_Integ]]
  - [[JV_Integ]]
  - [[Khobara_Integ]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[Motakaml_Integration_WithLog]]
  - [[NPF_Integration]]
  - [[Niroukh_Integration_WithLog]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[Presto_Integ]]
  - [[ProTech_Integration]]
  - [[Pro_CustomersPromotionsGroupsLink]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_ImportData]]
  - [[Pro_ImportPriceListData]]
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxApiFromOSFA]]
  - [[Pro_JoTaxApiFromOSFA____]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_PriceListDetails]]
  - [[Pro_PriceLists]]
  - [[Pro_ProspectiveCustomers]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Pro_SalesQuotationHeaders]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_TransactionsHeaders]]
  - [[Pro_ZatcaIntegrationApi]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RamPharm_SAP_Integ]]
  - [[Rpt_AcceptedSalesInvoices]]
  - [[Rpt_CustomersPriceLists]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_NewCustomer]]
  - [[Rpt_ProspectiveCustomer]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Spartan]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_SalesmanItemsSales]]
  - [[Rpt_SalesmanRouteDetails]]
  - [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
  - [[Rpt_UPriceReport]]
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
  - [[Shamel_Integration]]
  - [[Shini_Integ]]
  - [[Tahona_Integration_WithLog]]
  - [[Wings_Integration]]
  - [[Yolande_Integ]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Customer-Setup
  - Items-Master-Data-Setup
  - PriceList-Management
  - Promotion-Setup
  - Salesman-Onboarding
---
# PriceLists


## Business Purpose

Price list definitions — trade price, wholesale, retail tiers for products.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| CurrencyID | smallint | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (48):**
- [[ABS_Integration_Jebrene]]
- [[AX_INTEGRATION]]
- [[Acback_Integration]]
- [[AccPack_Integ]]
- [[AccPack_Integyandrug]]
- [[Awael_Integration_WithLog]]
- [[Bonanza_Integ_Yasmeen]]
- [[GP_Integ_Zumot]]
- [[GP_Integ_Zumot_Aqaba]]
- [[JV_Integ]]
- [[Presto_Integ]]
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]
- [[Pro_MapTransactionLog]]
- [[Pro_OrdersHeaders]]
- [[Pro_PriceListDetails]]
- [[Pro_PriceLists]]
- [[Pro_ProspectiveCustomers]]
- [[Pro_ReturnOrdersHeaders]]
- [[Pro_SalesQuotationHeaders]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_TransactionsHeaders]]
- [[Pro_ZatcaIntegrationApi]]
- [[Rpt_AcceptedSalesInvoices]]
- [[Rpt_CustomersPriceLists]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_NewCustomer]]
- [[Rpt_ProspectiveCustomer]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Spartan]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_SalesmanItemsSales]]
- [[Rpt_SalesmanRouteDetails]]
- [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
- [[Rpt_UPriceReport]]
- [[SAP_Naouri_Integ]]
- [[Tahona_Integration_WithLog]]

**Writes (60):**
- [[ABS_Integration_Jebrene]]
- [[ABS_Integration_Sokhtian]]
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Acback_Integration]]
- [[AccPack_Integ]]
- [[AccPack_Integ_LuxuryItems]]
- [[AccPack_Integyandrug]]
- [[Alpha_Integ]]
- [[Alpha_updateRoute]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Bajali_SAP_Integ]]
- [[Darwaza_Integration_WithLog]]
- [[Defaf_Integration]]
- [[ECO_Land_SAP_Integ]]
- [[Falcons_Integ]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ]]
- [[GP_Integ_Wadi]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[Isco_Integration_WithLog]]
- [[Izhiman_SAP_Integ]]
- [[JV_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Motakaml_Integration_WithLog]]
- [[NPF_Integration]]
- [[Niroukh_Integration_WithLog]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[ProTech_Integration]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_PriceLists]]
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
- [[SAP_Naouri_Integ]]
- [[SAP_Tyconz_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[Shamel_Integration]]
- [[Shini_Integ]]
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
