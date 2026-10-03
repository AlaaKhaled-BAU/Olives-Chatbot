---
type: table
database: Olives_BO
name: SalesPersonsDevicePermissions
schema: dbo
tags: [#backoffice, #sales, #permissions, #configuration]
foreign_keys:
  - [[Companies]]
  - [[Positions]]
support_relevance: high
last_verified: 2026-09-19
---
# SalesPersonsDevicePermissions

## Business Purpose

Core mobile and tablet capability configuration table in Olives_BO.
Defines the functional selling mode and operational permissions granted to field salespersons based on their organizational role (PositionsID).

### Master Capability Flags:
- **MakeSalesInvoice**: 1 = Authorized to issue direct tax/cash sales invoices in the field. **The primary discriminator of Cash Van (فانات البيع المباشر)**.
- **MakeOrderTaking**: 1 = Authorized to book pre-orders for later warehouse delivery. **The primary discriminator of Order Taking (Pre-Sales / حجز الطلبيات)**.
- **AllowVanTransfer**: 1 = Authorized to perform van-to-van inventory transfers in the field (VanTransferHeader).
- **AllowUnloadOrder**: 1 = Authorized to generate end-of-day van stock return documents (TransfersOrdersHeaders, VouType = 2).
- **MakeReturnSales**: 1 = Authorized to process direct return invoices in the field.
- **AllowReturnOrder**: 1 = Authorized to create pre-order return requests for warehouse retrieval.

## Relational Join Path:
Links to dbo.SalesPersons via composite key:
```sql
SalesPersons.CompanyID = SalesPersonsDevicePermissions.CompanyID
AND SalesPersons.PositionID = SalesPersonsDevicePermissions.PositionsID
```

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
| AllowItemsCategStock | bit | YES |  |  |  |

## See Also
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]
- [[SalesPersonItemsBalance]]
