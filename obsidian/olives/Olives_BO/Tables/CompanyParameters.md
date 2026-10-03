---
type: table
database: Olives_BO
name: CompanyParameters
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[AppDashBoard]]
  - [[OT_CustGalaryImages]]
  - [[OT_ImportReceipts]]
  - [[OT_ImportReturnOrder]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_ImportSalesIssueItems]]
  - [[OT_ImportSalesOrders]]
  - [[OT_ImportSalesQuotations]]
  - [[OT_ImportUploadOrders]]
  - [[OT_SendCompData]]
  - [[OT_SendSalesmanData]]
  - [[PRO_GETCUSTVISITEXITNOTES]]
  - [[PRO_GETRECEIPTSFOREMAIL]]
  - [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
  - [[Pro_AutoBasketLoadItems]]
  - [[Pro_CalcSalespersonItemBalance]]
  - [[Pro_CheckPromotionTarget]]
  - [[Pro_CheckSalesmanItemsBalance]]
  - [[Pro_CompanyParameters]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Pro_Items]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_Positions]]
  - [[Pro_PromotionsCondUnCodInput]]
  - [[Pro_PromotionsCondUnCodOutput]]
  - [[Pro_PromotionsHeaders]]
  - [[Pro_ReceiptRequests]]
  - [[Pro_Receipts]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Pro_SalesPersonItemBonusTarget_Online]]
  - [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
  - [[Pro_SalesPersons]]
  - [[Pro_SalespersonsSecurity_Android]]
  - [[Pro_SystemOptions]]
  - [[Pro_TransactionsHeaders]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Pro_Users]]
  - [[Rpt_SalesPersonItemBonusTarget]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
---
# CompanyParameters


## Business Purpose

System-wide configuration flags controlling feature toggles, behavior, and ERP integration settings.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| AutoSendInvoiceToERP | bit | YES |  |  |  |
| AutoSendReturnInvoiceToERP | bit | YES |  |  |  |
| AutoSendReceiptsToERP | bit | YES |  |  |  |
| AutoSendOrderToERP | bit | YES |  |  |  |
| AutoSendReturnOrderToERP | bit | YES |  |  |  |
| CalcItemBalance | bit | YES |  |  |  |
| SerialType | int | YES |  |  |  |
| UseRangePrice | bit | YES |  |  |  |
| LockOnSendData | bit | YES |  |  |  |
| NumberSavedFraction | int | YES |  |  |  |
| TruncRoundValue | int | YES |  |  |  |
| LockEditApprovedTrans | bit | YES |  |  |  |
| MaxRecordInSearch | int | YES |  |  |  |
| EnablePassPolicy | bit | YES |  |  |  |
| PassLength | int | YES |  |  |  |
| MaxLogin | int | YES |  |  |  |
| TimeOutLoginOnTab | int | YES |  |  |  |
| EnableVerificationCode | bit | YES |  |  |  |
| EnableMacAddressOnTab | bit | YES |  |  |  |
| PassExpiryDays | int | YES |  |  |  |
| ActivationCodeDays | int | YES |  |  |  |
| SMSLink | nvarchar | YES |  |  |  |
| UseRecaptchaInLogin | bit | YES |  |  |  |
| SendCustVisitExitNoteByEmail | bit | YES |  |  |  |
| AutoApproveLoadOrder | bit | YES |  |  |  |
| DashBoardStepSize | float | YES |  |  |  |
| UrlSamaService | nvarchar | YES |  |  |  |
| UrlSamaServiceJson | nvarchar | YES |  |  |  |
| AutoApproveCustomerGPS | bit | YES |  |  |  |
| AutoApproveWF | bit | YES |  |  |  |
| UseBonusTargetByPromotion | bit | YES |  |  |  |
| SendCustRecieptsByEmail | bit | YES |  |  |  |
| EnableWFSalesOrder | bit | YES |  |  |  |
| EnableWFLoadOrder | bit | YES |  |  |  |
| EnableWFUnLoadOrder | bit | YES |  |  |  |
| EnableWFReturnOrder | bit | YES |  |  |  |
| UseInvoiceSettlement | bit | YES |  |  |  |
| InvoiceSettlementDate | smalldatetime | YES |  |  |  |
| MaxLoadOrderConfirm | tinyint | YES |  |  |  |
| AllowWaterMarkImage | bit | YES |  |  |  |
| AllowBonusWithPrice | bit | YES |  |  |  |
| AllowApplyAllNextPromotion | bit | YES |  |  |  |
| AllowZeroAmountInReciptRequest | bit | YES |  |  |  |
| SendVoidRecieptsByEmail | bit | YES |  |  |  |
| UsePromotionsApprove | bit | YES |  |  |  |
| AllowEarlyRepaymentDiscount | bit | YES |  |  |  |
| UseItemBonusTargetGroup | bit | YES |  |  |  |
| NotAllowDuplicateItemInPromotions | bit | YES |  |  |  |
| UseDateInOutputGroup | bit | YES |  |  |  |
| ManualInsertSalesmanID | bit | YES |  |  |  |
| EnableWFSalesQuotation | bit | YES |  |  |  |
| UsePassKeyWithTime | bit | YES |  |  |  |
| CustStockItemsTargetByRef | bit | YES |  |  |  |
| UseBasketItems | bit | YES |  |  |  |
| UsePromotionWF | bit | YES |  |  |  |
| UseNewTransSerials | bit | YES |  |  |  |
| UseMaxLoadOrderAmount | bit | YES |  |  |  |
| UseBonusLimitInWF | bit | YES |  |  |  |
| AutoRejectBonusLimitWF | bit | YES |  |  |  |
| PasskeyByGeneratedKey | bit | YES |  |  |  |
| PhinixLastSessionID | varchar | YES |  |  |  |
| LastMasterDataJobRunTime | datetime | YES |  |  |  |
| UseIncreaseCreditLimitWFRequest | bit | YES |  |  |  |
| UseOlivesImagesForCustomerGallery | bit | YES |  |  |  |
| TowFactorAuthTabletAdminLogin | bit | YES |  |  |  |
| UseMustUpdateDataInSendData | bit | YES |  |  |  |
| CustomGalaryImageURL | nvarchar | YES |  |  |  |
| UseOneLoginAtSameTime | bit | YES |  |  |  |
| DontUpdateLayoutSettings | bit | YES |  |  |  |
| WF_GroupByRequests | bit | YES |  |  |  |
| Latitude | varchar | YES |  |  |  |
| Longitude | varchar | YES |  |  |  |
| EnableVerificationCodeInWF | bit | YES |  |  |  |
| PriceWithTax | bit | YES |  |  |  |
| UseSalesOrderLimit | bit | YES |  |  |  |
| UseAccumulatedAmount | bit | YES |  |  |  |
| UsePaymentTypeInItem | bit | YES |  |  |  |
| OpenUnloadOrderDate | bit | YES |  |  |  |
| MobileAppVersion | varchar | YES |  |  |  |
| TaxPriceList | int | YES |  |  |  |
| UseWFReAssign | bit | YES |  |  |  |
| ShowExceptionsIssuesDashBoard | bit | YES |  |  |  |
| EnableVerificationSanadInWF | bit | YES |  |  |  |

## Primary Key
CompanyID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (47):**
- [[AppDashBoard]]
- [[OT_CustGalaryImages]]
- [[OT_ImportReceipts]]
- [[OT_ImportReturnOrder]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesIssueItems]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportSalesQuotations]]
- [[OT_ImportUploadOrders]]
- [[OT_SendCompData]]
- [[PRO_GETCUSTVISITEXITNOTES]]
- [[PRO_GETRECEIPTSFOREMAIL]]
- [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
- [[Pro_AutoBasketLoadItems]]
- [[Pro_CalcSalespersonItemBalance]]
- [[Pro_CheckPromotionTarget]]
- [[Pro_CheckSalesmanItemsBalance]]
- [[Pro_CompanyParameters]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_Items]]
- [[Pro_OrdersHeaders]]
- [[Pro_Positions]]
- [[Pro_PromotionsCondUnCodInput]]
- [[Pro_PromotionsCondUnCodOutput]]
- [[Pro_PromotionsHeaders]]
- [[Pro_ReceiptRequests]]
- [[Pro_Receipts]]
- [[Pro_ReturnOrdersHeaders]]
- [[Pro_SalesPersonItemBonusTarget_Online]]
- [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
- [[Pro_SalesPersons]]
- [[Pro_SalespersonsSecurity_Android]]
- [[Pro_SystemOptions]]
- [[Pro_TransactionsHeaders]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_Users]]
- [[Rpt_SalesPersonItemBonusTarget]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_AddWorkFlowLevels]]

**Writes (2):**
- [[OT_SendSalesmanData]]
- [[Pro_CompanyParameters]]

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

## Cross-Database

See also: [[OSFA_DB/Tables/CompanyParameters|FO CompanyParameters]]
