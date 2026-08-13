---
type: table
database: Olives_BO
name: SalesPersonsDevicePermissions
schema: dbo
tags: [#auth, #backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[Positions]]
referenced_by:
  - [[Alpha_SalesmanCustRoute]]
  - [[DEVICEREPORT_TABLE_UPDATE]]
  - [[DiagnosticTools_CheckSalespersonConfiguration]]
  - [[Fill_Sales_Device_Reports]]
  - [[OT_ImportNewCust]]
  - [[OT_SendSalesmanData]]
  - [[Pro_SalesPersonsDevicePermissions]]
  - [[Retco_Integ_ItemBal]]
  - [[Rpt_first_last_visit_Invoice_TowerExcel]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Salesman-Onboarding
---
# SalesPersonsDevicePermissions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsdevicepermissions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| UserName | nvarchar | YES |  |  |  |
| Password | nvarchar | YES |  |  |  |
| UseDefaultUnit | bit | YES |  |  |  |
| ChangePrice | bit | YES |  |  |  |
| MakeOrderTaking | bit | YES |  |  |  |
| MakeTransferOrder | bit | YES |  |  |  |
| MakeSalesInvoice | bit | YES |  |  |  |
| MakeReturnSales | bit | YES |  |  |  |
| MakeReceipt | bit | YES |  |  |  |
| AllowCons | bit | YES |  |  |  |
| AllowCustStock | bit | YES |  |  |  |
| AllowChangeOrderStore | bit | YES |  |  |  |
| AllowChangeOrderBusUnit | bit | YES |  |  |  |
| AllowChangeOrderDocType | bit | YES |  |  |  |
| AllowChangeOrderCustName | bit | YES |  |  |  |
| AllowMakeBonus | bit | YES |  |  |  |
| AllowAddCust | bit | YES |  |  |  |
| AllowGetCustGPS | bit | YES |  |  |  |
| AllowItemDisc | bit | YES |  |  |  |
| AllowVouDisc | bit | YES |  |  |  |
| UseMultiStoreInSales | bit | YES |  |  |  |
| CanceledInvoiceNo | int | YES |  |  |  |
| VouDiscLimit | float | YES |  |  |  |
| UseBarcodeForCustLogin | bit | YES |  |  |  |
| MinTotalOfSalesVou | float | YES |  |  |  |
| CheckCreditLimitInOrder | bit | YES |  |  |  |
| AmendChangeCashCreditInInvoice | bit | YES |  |  |  |
| AmendChangeCashCreditInRetInvoice | bit | YES |  |  |  |
| CashOnlyInvoice | bit | YES |  |  |  |
| CreditOnlyReturnInvoice | bit | YES |  |  |  |
| AllowCompetitiveItems | bit | YES |  |  |  |
| AllowAddDrawer | bit | YES |  |  |  |
| MaxDiscountPerc | float | YES |  |  |  |
| AllowReturnOrder | bit | YES |  |  |  |
| AllowVanTransfer | bit | YES |  |  |  |
| AllowSalesQuotation | bit | YES |  |  |  |
| AllowItemsReplacement | bit | YES |  |  |  |
| AllowAddProspectiveCustomer | bit | YES |  |  |  |
| AllowChangePriceInReturn | bit | YES |  |  |  |
| AllowItemDiscInReturn | bit | YES |  |  |  |
| AllowVouDiscInReturn | bit | YES |  |  |  |
| AllowUnloadOrder | bit | YES |  |  |  |
| AllowMakeIssueItems | bit | YES |  |  |  |
| AllowDebitCreditNote | bit | YES |  |  |  |
## Primary Key
CompanyID
PositionsID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (9):**
- [[Alpha_SalesmanCustRoute]]
- [[DEVICEREPORT_TABLE_UPDATE]]
- [[DiagnosticTools_CheckSalespersonConfiguration]]
- [[Fill_Sales_Device_Reports]]
- [[OT_ImportNewCust]]
- [[OT_SendSalesmanData]]
- [[Pro_SalesPersonsDevicePermissions]]
- [[Retco_Integ_ItemBal]]
- [[Rpt_first_last_visit_Invoice_TowerExcel]]

**Writes (1):**
- [[Pro_SalesPersonsDevicePermissions]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Login-Device-Issues]]
