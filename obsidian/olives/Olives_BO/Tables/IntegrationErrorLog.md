---
type: table
database: Olives_BO
name: IntegrationErrorLog
schema: dbo
tags: [#backoffice, #integration, #log]
foreign_keys:
referenced_by:
  - [[ABS_Integ_SendInvoices]]
  - [[ABS_Integ_SendInvoices_Jebrene]]
  - [[ABS_Integ_SendPayment_Jebrene]]
  - [[ABS_Integ_SendPayment_Sokhtian]]
  - [[ABS_Integ_SendReturnInvoices_Jebrene]]
  - [[ABS_Integ_SendSalesOrder]]
  - [[ABS_Integ_SendSalesOrder_Jebrene]]
  - [[ABS_Integ_SendTransferOrders]]
  - [[ABS_Integ_SendTransferOrders_Jebrene]]
  - [[ABS_Integ_SendUnloadOrders_Jebrene]]
  - [[Acback_Integ_SendInvoices]]
  - [[Acback_Integ_SendPayments]]
  - [[Acback_Integ_SendReturnInvoices]]
  - [[Acback_Integ_SendTransfer]]
  - [[Awael_Integration_WithLog]]
  - [[Awtar_Integ_SendReceipts]]
  - [[Awtar_Integ_SendReturnOrder]]
  - [[Awtar_Integ_SendSalesOrder]]
  - [[Awtar_Integration_GetPromotion]]
  - [[CL_Integration]]
  - [[Darwaza_Integration_WithLog]]
  - [[Ejabi_Integ_SendInvoices]]
  - [[Ejabi_Integ_SendPayments]]
  - [[Ejabi_Integ_SendReturnInvoices]]
  - [[Ejabi_Integ_SendTransferOrders]]
  - [[GTS_Integration_WithLog]]
  - [[Isco_Integration_WithLog]]
  - [[Mira_Integration_WithLog]]
  - [[Mira_Wales_Integration_WithLog]]
  - [[Motakaml_Integration_WithLog]]
  - [[NPF_Integ_SendReceipts]]
  - [[NPF_Integration]]
  - [[Niroukh_Integ_SendReceipts]]
  - [[Niroukh_Integ_SendReturnOrder]]
  - [[Niroukh_Integ_SendSalesOrder]]
  - [[Niroukh_Integration_GetPromotion]]
  - [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
  - [[Phenix_Sukhtian_Integ_SendInvoiceAndReturn]]
  - [[Phenix_Sukhtian_Integ_SendReceipts]]
  - [[Phenix_Sukhtian_Integ_SendSalesOrder]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[Pro_ApprovedOrder]]
  - [[SAP_Tyconz_Integ]]
  - [[SN_Integ_SendPayments]]
  - [[SN_Integration]]
  - [[SP_IntegrationErrorLog]]
  - [[Shamel_Integ_SendReciepts]]
  - [[Shamel_Integ_SendSalesInvoices]]
  - [[Shamel_Integ_SendSalesOrders]]
  - [[Shamel_Integration]]
  - [[Tahona_Integ_SendReceipts]]
  - [[Tahona_Integration_WithLog]]
  - [[X3_INTEGRATION_WITHLOG]]
support_relevance: low
last_verified: 2026-07-05
---
# IntegrationErrorLog


## Business Purpose

Integration data store for syncing sales transactions with external systems.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyCode | nvarchar | YES |  |  |  |
| TrDateTime | datetime | YES |  |  |  |
| TableName | nvarchar | YES |  |  |  |
| ErrorMsg | nvarchar | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| JsonData | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (53):**
- [[ABS_Integ_SendInvoices]]
- [[ABS_Integ_SendInvoices_Jebrene]]
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendPayment_Sokhtian]]
- [[ABS_Integ_SendReturnInvoices_Jebrene]]
- [[ABS_Integ_SendSalesOrder]]
- [[ABS_Integ_SendSalesOrder_Jebrene]]
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]
- [[Acback_Integ_SendInvoices]]
- [[Acback_Integ_SendPayments]]
- [[Acback_Integ_SendReturnInvoices]]
- [[Acback_Integ_SendTransfer]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integ_SendReceipts]]
- [[Awtar_Integ_SendReturnOrder]]
- [[Awtar_Integ_SendSalesOrder]]
- [[Awtar_Integration_GetPromotion]]
- [[CL_Integration]]
- [[Darwaza_Integration_WithLog]]
- [[Ejabi_Integ_SendInvoices]]
- [[Ejabi_Integ_SendPayments]]
- [[Ejabi_Integ_SendReturnInvoices]]
- [[Ejabi_Integ_SendTransferOrders]]
- [[GTS_Integration_WithLog]]
- [[Isco_Integration_WithLog]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Motakaml_Integration_WithLog]]
- [[NPF_Integ_SendReceipts]]
- [[NPF_Integration]]
- [[Niroukh_Integ_SendReceipts]]
- [[Niroukh_Integ_SendReturnOrder]]
- [[Niroukh_Integ_SendSalesOrder]]
- [[Niroukh_Integration_GetPromotion]]
- [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
- [[Phenix_Sukhtian_Integ_SendInvoiceAndReturn]]
- [[Phenix_Sukhtian_Integ_SendReceipts]]
- [[Phenix_Sukhtian_Integ_SendSalesOrder]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[Pro_ApprovedOrder]]
- [[SAP_Tyconz_Integ]]
- [[SN_Integ_SendPayments]]
- [[SN_Integration]]
- [[SP_IntegrationErrorLog]]
- [[Shamel_Integ_SendReciepts]]
- [[Shamel_Integ_SendSalesInvoices]]
- [[Shamel_Integ_SendSalesOrders]]
- [[Shamel_Integration]]
- [[Tahona_Integ_SendReceipts]]
- [[Tahona_Integration_WithLog]]
- [[X3_INTEGRATION_WITHLOG]]

**Writes (18):**
- [[ABS_Integ_SendInvoices_Jebrene]]
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendPayment_Sokhtian]]
- [[ABS_Integ_SendReturnInvoices_Jebrene]]
- [[ABS_Integ_SendSalesOrder]]
- [[ABS_Integ_SendSalesOrder_Jebrene]]
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]
- [[Acback_Integ_SendInvoices]]
- [[Acback_Integ_SendPayments]]
- [[Acback_Integ_SendReturnInvoices]]
- [[Acback_Integ_SendTransfer]]
- [[Ejabi_Integ_SendInvoices]]
- [[Ejabi_Integ_SendPayments]]
- [[Ejabi_Integ_SendReturnInvoices]]
- [[Ejabi_Integ_SendTransferOrders]]
- [[SP_IntegrationErrorLog]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Integration stuck**: IsPosted flag not clearing — check ERP connection and error log
- **Duplicate sent**: Same transaction sent multiple times — ERP shows duplicates
- **Mapping error**: Field mapping fails — check IntegrationPostedTransactions for error details
- **Timeout**: Large batch exceeds ERP timeout — split into smaller batches

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Duplicate-Keys]]
