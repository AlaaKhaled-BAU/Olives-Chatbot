---
type: table
database: Olives_BO
name: ReturnOrdersDetails
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[ReturnOrdersHeaders]]
referenced_by:
  - [[Awtar_Integ_SendReturnOrder]]
  - [[ConvertReturnOrderToInvoiceDelivery]]
  - [[Niroukh_Integ_SendReturnOrder]]
  - [[OT_ImportReturnOrder]]
  - [[PrestoSoft_Integ_SendReturnOrders]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_ReturnOrdersDetails]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Rpt_CustomerReturnOrdersDetails]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_ReturnOrder]]
  - [[Rpt_ReturnOrdersMaster]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Return-Reversal-Workflow
---
# ReturnOrdersDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores returnordersdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ReturnOrdersHeaders]] |
| TransactionYear | smallint | NO | ✓ | ✓ | [[ReturnOrdersHeaders]] |
| TransactionNo | int | NO | ✓ | ✓ | [[ReturnOrdersHeaders]] |
| ItemCode | nvarchar | NO | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | NO | ✓ | ✓ | [[ItemsUnits]] |
| ItemSerial | int | YES |  |  |  |
| Quantity | float | YES |  |  |  |
| Bonus | float | YES |  |  |  |
| Price | float | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| VoucherDiscount | float | YES |  |  |  |
| TaxType | smallint | YES |  |  |  |
| TaxPercent | float | YES |  |  |  |
| TaxAmount | float | YES |  |  |  |
| ForeignPrice | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ForeignVouDiscount | float | YES |  |  |  |
| ForeignTaxPercent | float | YES |  |  |  |
| ForeignTaxAmount | float | YES |  |  |  |
| ItemStatus | smallint | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxType1 | smallint | YES |  |  |  |
| TaxPercent1 | float | YES |  |  |  |
| TaxAmount1 | float | YES |  |  |  |
| TaxType2 | smallint | YES |  |  |  |
| TaxPercent2 | float | YES |  |  |  |
| TaxAmount2 | float | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| ExchangeRate | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| ReturnReason | int | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| ExpDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
TransactionYear
TransactionNo
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, TransactionYear, TransactionNo -> [[ReturnOrdersHeaders]](CompanyID, TransactionYear, TransactionNo)
## Impact / Procedures Using This Table

**Reads (16):**
- [[Awtar_Integ_SendReturnOrder]]
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[Niroukh_Integ_SendReturnOrder]]
- [[PrestoSoft_Integ_SendReturnOrders]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_ReturnOrdersDetails]]
- [[Pro_ReturnOrdersHeaders]]
- [[Rpt_CustomerReturnOrdersDetails]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_ReturnOrder]]
- [[Rpt_ReturnOrdersMaster]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]

**Writes (2):**
- [[OT_ImportReturnOrder]]
- [[Pro_ReturnOrdersDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
