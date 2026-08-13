---
type: table
database: Olives_BO
name: Technical_CFD_temp
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[Pro_ImportRouteInfoFromExcel]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
  - [[Technical_UpdateTempCFD_temp_forRouteCreation]]
support_relevance: low
last_verified: 2026-07-05
---
# Technical_CFD_temp


## Business Purpose

Temporary or sample data — not part of core transaction flow.

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
| ReturnCreditLimit | float | YES |  |  |  |
| ReturnBalance | float | YES |  |  |  |
| LocationID | int | YES |  |  |  |
| SalesOrderLimit | float | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Pro_ImportRouteInfoFromExcel]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
- [[Technical_UpdateTempCFD_temp_forRouteCreation]]

**Writes (3):**
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_UpdateTempCFD_temp_forRouteCreation]]

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
