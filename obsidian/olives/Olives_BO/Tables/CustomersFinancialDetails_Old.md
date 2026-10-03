---
type: table
database: Olives_BO
name: CustomersFinancialDetails_Old
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# CustomersFinancialDetails_Old


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customersfinancialdetails old records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO |  |  |  |
| CustomerID | bigint | NO |  |  |  |
| PositionsID | int | NO |  |  |  |
| BusinessUnitID | int | NO |  |  |  |
| PaymentTypeID | int | YES |  |  |  |
| PriceListID | int | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| CustomersPromotionsGroupsID | int | YES |  |  |  |
| CreditLimit | float | YES |  |  |  |
| DueDays | smallint | YES |  |  |  |
| ChqsDueDays | smallint | YES |  |  |  |
| AllowChqs | bit | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| FavouriteVisitTime | smalldatetime | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| TaxInclude | bit | YES |  |  |  |
| DiscountPerc | float | YES |  |  |  |
| CreditCash | smallint | YES |  |  |  |
| CustomerBalance | float | YES |  |  |  |
| ChqBalance | float | YES |  |  |  |
| VisitOrder | int | YES |  |  |  |
| MaxInvoiceValue | float | YES |  |  |  |
| MaxInvoiceCount | int | YES |  |  |  |
| ChqLimit | float | YES |  |  |  |
| Tax_1_Include | bit | YES |  |  |  |
| Tax_2_Include | bit | YES |  |  |  |
| AllowManualDiscount | bit | YES |  |  |  |
| CompanyBrancheID | int | YES |  |  |  |
| EarlyRepaymentDiscountPerc | float | YES |  |  |  |
| ClassID | int | YES |  |  |  |
| DiscountEarlyPayDays | int | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| DeliveryDays | int | YES |  |  |  |
| OrderCashDiscount | float | YES |  |  |  |
| CurrencyID | int | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[NewCustomerDefaultValue]]
- [[CustomerTargetsDetails]]
- [[NewCustomerSpecialFields_Def]]
