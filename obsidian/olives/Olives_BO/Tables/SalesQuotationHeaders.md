---
type: table
database: Olives_BO
name: SalesQuotationHeaders
schema: dbo
tags: [#backoffice, #order, #sales]
foreign_keys:
referenced_by:
  - [[OT_ImportActionLog]]
  - [[OT_ImportSalesQuotations]]
  - [[Pro_CompanyParameters]]
  - [[Pro_SalesQuotationHeaders]]
  - [[Rpt_SalesQuotation]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesQuotationHeaders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salesquotationheaders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderYear | int | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| SalesPersonID | int | YES |  |  |  |
| PriceListID | int | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| CurrencyID | smallint | YES |  |  |  |
| ExchangeRate | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| WFApproved | bit | YES |  |  |  |
| Approved | bit | YES |  |  |  |
| DocumentsTypesID | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| BusinessUnitID | int | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| IsVoid | bit | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| CreditCash | int | YES |  |  |  |
| CustomerName | nvarchar | YES |  |  |  |
| DeliveryLocation | nvarchar | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
| IsProspectiveCustomer | bit | YES |  |  |  |
| NormalCustomerID | bigint | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| DeliveryDays | int | YES |  |  |  |
| PostedToERPDateTime | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Pro_CompanyParameters]]
- [[Pro_SalesQuotationHeaders]]
- [[Rpt_SalesQuotation]]

**Writes (5):**
- [[OT_ImportActionLog]]
- [[OT_ImportSalesQuotations]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

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
- [[Olives_BO/Tables/MultiTargets]]
- [[Olives_BO/Tables/CustomerSalesByCategory]]
- [[Olives_BO/Tables/CustomersReturnItemQtyLimit]]
- [[Olives_BO/Tables/SalesPersonItemsBalanceBatches]]
- [[Olives_BO/Tables/SpecialCustomerTarget]]
- [[Olives_BO/Tables/WieghtTargets]]
- [[Olives_BO/Tables/PromotionTypes]]
- [[Olives_BO/Procedures/Pro_MonthlySalesPersonsTargets]]
- [[Olives_BO/Procedures/Rpt_Hakkak_TargetReportFromAlpha]]
