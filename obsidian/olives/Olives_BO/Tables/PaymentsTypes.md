---
type: table
database: Olives_BO
name: PaymentsTypes
schema: dbo
tags: [#backoffice, #billing, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[ABS_Integration_Jebrene]]
  - [[ABS_Integration_Sokhtian]]
  - [[AX_INTEGRATION]]
  - [[AX_INTEG_SENDORDERS]]
  - [[AX_INTEG_SENDTRANSACTIONS]]
  - [[AX_Integration_AbuTawileh]]
  - [[AccPack_Integ]]
  - [[AccPack_Integ_LuxuryItems]]
  - [[AccPack_Integyandrug]]
  - [[Alpha_Integ]]
  - [[Alpha_Integ_GoldenArrow]]
  - [[Alpha_updateRoute]]
  - [[Awael_Integration_WithLog]]
  - [[Awtar_Integration_WithLog]]
  - [[Bajali_SAP_Integ]]
  - [[Darwaza_Integ_SendSalesInvoices]]
  - [[Darwaza_Integration_WithLog]]
  - [[Defaf_Integration]]
  - [[ECO_Land_SAP_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ]]
  - [[GP_Integ_Wadi]]
  - [[GTS_Integration_WithLog]]
  - [[Galaxy_Integ_SendSalesInvoices]]
  - [[Galaxy_Integration]]
  - [[Isco_Integ_SendSalesInvoices]]
  - [[Isco_Integ_SendSalesOrders]]
  - [[Isco_Integration_WithLog]]
  - [[JV_Integ]]
  - [[Mira_Integration_WithLog]]
  - [[Mira_Wales_Integration_WithLog]]
  - [[Motakaml_Integ_SendSalesOrders]]
  - [[Motakaml_Integ_SendTransactions]]
  - [[Niroukh_Integration_WithLog]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_ImportSalesInvoices]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[ProTech_Integration]]
  - [[Pro_CustomerReceivablesInfo]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_ImportData]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_PaymentsTypes]]
  - [[Pro_SalesQuotationHeaders]]
  - [[Pro_SalesTrans]]
  - [[Rpt_CashSummary]]
  - [[Rpt_CustomersVisitsCountByClass]]
  - [[Rpt_DeliveryDetails]]
  - [[Rpt_NewCustomer]]
  - [[Rpt_ProspectiveCustomer]]
  - [[SAP_Integ]]
  - [[SAP_Integ_Amazing]]
  - [[SAP_Integ_Hammoudeh]]
  - [[SAP_Integ_Karadsheh]]
  - [[SAP_Integ_Kaylani]]
  - [[SAP_Integ_Lamis]]
  - [[SAP_Integ_MERI]]
  - [[SAP_Integ_Malak]]
  - [[SAP_Integ_NewCustomers_Lamis]]
  - [[SAP_Integration_WithLog]]
  - [[SAP_Tyconz_Integ]]
  - [[SAP_Tyconz_Integ_SendInvoiceAndReturn]]
  - [[SAP_Tyconz_Integ_SendSalesOrders]]
  - [[SN_Integration]]
  - [[Tahona_Integration_WithLog]]
  - [[Wings_Integration]]
  - [[Yolande_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# PaymentsTypes


## Business Purpose

Reference/lookup table defining paymentstypes categories.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| DueDays | int | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (50):**
- [[ABS_Integration_Jebrene]]
- [[AX_INTEGRATION]]
- [[AX_INTEG_SENDORDERS]]
- [[AX_INTEG_SENDTRANSACTIONS]]
- [[AX_Integration_AbuTawileh]]
- [[AccPack_Integ]]
- [[AccPack_Integ_LuxuryItems]]
- [[AccPack_Integyandrug]]
- [[Alpha_Integ_GoldenArrow]]
- [[Awael_Integration_WithLog]]
- [[Darwaza_Integ_SendSalesInvoices]]
- [[GP_Integ]]
- [[GP_Integ_Wadi]]
- [[Galaxy_Integ_SendSalesInvoices]]
- [[Isco_Integ_SendSalesInvoices]]
- [[Isco_Integ_SendSalesOrders]]
- [[JV_Integ]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Motakaml_Integ_SendSalesOrders]]
- [[Motakaml_Integ_SendTransactions]]
- [[OT_ImportSalesInvoices]]
- [[ProTech_Integration]]
- [[Pro_CustomerReceivablesInfo]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_ImportData]]
- [[Pro_OrdersHeaders]]
- [[Pro_PaymentsTypes]]
- [[Pro_SalesQuotationHeaders]]
- [[Pro_SalesTrans]]
- [[Rpt_CashSummary]]
- [[Rpt_CustomersVisitsCountByClass]]
- [[Rpt_DeliveryDetails]]
- [[Rpt_NewCustomer]]
- [[Rpt_ProspectiveCustomer]]
- [[SAP_Integ]]
- [[SAP_Integ_Amazing]]
- [[SAP_Integ_Hammoudeh]]
- [[SAP_Integ_Karadsheh]]
- [[SAP_Integ_Kaylani]]
- [[SAP_Integ_Lamis]]
- [[SAP_Integ_MERI]]
- [[SAP_Integ_Malak]]
- [[SAP_Integ_NewCustomers_Lamis]]
- [[SAP_Tyconz_Integ_SendInvoiceAndReturn]]
- [[SAP_Tyconz_Integ_SendSalesOrders]]
- [[SN_Integration]]
- [[Tahona_Integration_WithLog]]
- [[Wings_Integration]]
- [[Yolande_Integ]]

**Writes (41):**
- [[ABS_Integration_Jebrene]]
- [[ABS_Integration_Sokhtian]]
- [[AX_Integration_AbuTawileh]]
- [[AccPack_Integ]]
- [[AccPack_Integyandrug]]
- [[Alpha_Integ]]
- [[Alpha_updateRoute]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Bajali_SAP_Integ]]
- [[Darwaza_Integration_WithLog]]
- [[Defaf_Integration]]
- [[ECO_Land_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ]]
- [[GP_Integ_Wadi]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[Isco_Integration_WithLog]]
- [[JV_Integ]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[ProTech_Integration]]
- [[Pro_ImportData]]
- [[Pro_PaymentsTypes]]
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
- [[Wings_Integration]]
- [[Yolande_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
