---
type: table
database: OSFA_DB
name: OT_SalesmanMF
schema: dbo
tags: [#mobile, #sales]
foreign_keys:
referenced_by:
  - [[OT_AutoStoreItemsQty]]
  - [[OT_UpdateSalesmanKPI]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanMF



## Business Purpose


Salesperson profile data on tablet — route assignment and device configuration.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | smallint | NO | ✓ |  |  |
| ArbSalesmanName | nvarchar | YES |  |  |  |
| EngSalesmanName | nvarchar | YES |  |  |  |
| Password | nvarchar | YES |  |  |  |
| Active | bit | YES |  |  |  |
| NextSerial | nvarchar | YES |  |  |  |
| InvNextSerial | nvarchar | YES |  |  |  |
| RetInvNextSerial | nvarchar | YES |  |  |  |
| RecNextSerial | nvarchar | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| UseDefaultUnit | bit | YES |  |  |  |
| AllowChangePrice | bit | YES |  |  |  |
| AllowSales | bit | YES |  |  |  |
| AllowReturnSales | bit | YES |  |  |  |
| AllowOrder | bit | YES |  |  |  |
| AllowRec | bit | YES |  |  |  |
| AllowCons | bit | YES |  |  |  |
| ConsNextSerial | nvarchar | YES |  |  |  |
| SalesmanGroup_ID | nvarchar | YES |  |  |  |
| AllowCustStock | bit | YES |  |  |  |
| CustStockNextSerial | nvarchar | YES |  |  |  |
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
| AllowedVoidInvCount | int | YES |  |  |  |
| DayOff | nvarchar | YES |  |  |  |
| VouDiscLimit | float | YES |  |  |  |
| AllowAddDrawer | bit | YES |  |  |  |
| MinTotalOfSalesVou | float | YES |  |  |  |
| CheckCreditLimitInOrder | bit | YES |  |  |  |
| CompetitiveItemsInfoNextSerial | nvarchar | YES |  |  |  |
| UnLoadOrdersNextSerials | nvarchar | YES |  |  |  |
| SupervisorNo | nvarchar | YES |  |  |  |
| SupervisorName | nvarchar | YES |  |  |  |
| SupervisorTel | nvarchar | YES |  |  |  |
| CompanyBrancheID | int | YES |  |  |  |
| CreditLimit | float | YES |  |  |  |
| SalesmanBalance | float | YES |  |  |  |
| MonthlySalesTarget | float | YES |  |  |  |
| MonthlySalesAmount | float | YES |  |  |  |
| MonthlyCollectionTarget | float | YES |  |  |  |
| MonthlyCollectionAmount | float | YES |  |  |  |
| MaxDiscountPerc | float | YES |  |  |  |
| SalesmanStockNextSerial | nvarchar | YES |  |  |  |
| AllowReturnOrder | bit | YES |  |  |  |
| ReturnOrderNextSerial | nvarchar | YES |  |  |  |
| VanTransferNextSerial | nvarchar | YES |  |  |  |
| AllowVanTransfer | bit | YES |  |  |  |
| AutoSendData | bit | YES |  |  |  |
| AllowSalesQuotation | bit | YES |  |  |  |
| SalesQuotationNextSerial | nvarchar | YES |  |  |  |
| AllowItemsReplacment | bit | YES |  |  |  |
| ItemsReplacmentNextSerial | nvarchar | YES |  |  |  |
| UserName | nvarchar | YES |  |  |  |
| TotalDamage | float | YES |  |  |  |
| TotalAllWork | float | YES |  |  |  |
| CustomerSalesCount | int | YES |  |  |  |
| CountOfAllCustomers | int | YES |  |  |  |
| AllowAddProspectiveCust | bit | YES |  |  |  |
| SalesmanTel | nvarchar | YES |  |  |  |
| AllowChangePriceInReturn | bit | YES |  |  |  |
| AllowItemDiscInReturn | bit | YES |  |  |  |
| AllowVouDiscInReturn | bit | YES |  |  |  |
| AllowUnloadOrder | bit | YES |  |  |  |
| AviItemsCount | int | YES |  |  |  |
| AllItemsCount | int | YES |  |  |  |
| TotalReturn | float | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| IssueItemsNextSerial | nvarchar | YES |  |  |  |
| AllowMakeIssueItems | bit | YES |  |  |  |
| SalesInvoiceNextSerial_Credit | nvarchar | YES |  |  |  |
| MaxLoadOrderAmount | float | YES |  |  |  |
| DebitCreditNoteNextSerial | bigint | YES |  |  |  |
| AllowDebitCreditNote | bit | YES |  |  |  |
| ReceiveItemsNextSerial | bigint | YES |  |  |  |
| CashOnHand | float | YES |  |  |  |
| PaymentsOrdersNextSerial | bigint | YES |  |  |  |
| IsCashOpen | int | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_AutoStoreItemsQty]]
- [[OT_UpdateSalesmanKPI]]

**Writes (1):**
- [[OT_UpdateSalesmanKPI]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement


## See also
- [[Olives_BO/Tables/SalesPersons]] (Back Office counterpart table)

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
