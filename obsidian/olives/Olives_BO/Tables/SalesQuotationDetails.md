---
type: table
database: Olives_BO
name: SalesQuotationDetails
schema: dbo
tags: [#backoffice, #order, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesQuotationHeaders]]
referenced_by:
  - [[OT_ImportSalesQuotations]]
  - [[Pro_SalesQuotationDetails]]
  - [[Pro_SalesQuotationHeaders]]
  - [[Rpt_SalesQuotation]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesQuotationDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salesquotationdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesQuotationHeaders]] |
| OrderYear | int | NO | ✓ | ✓ | [[SalesQuotationHeaders]] |
| OrderNo | int | NO | ✓ | ✓ | [[SalesQuotationHeaders]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
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
| Manual_Disc | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, OrderYear, OrderNo -> [[SalesQuotationHeaders]](CompanyID, OrderYear, OrderNo)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Pro_SalesQuotationDetails]]
- [[Pro_SalesQuotationHeaders]]
- [[Rpt_SalesQuotation]]

**Writes (1):**
- [[OT_ImportSalesQuotations]]

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
