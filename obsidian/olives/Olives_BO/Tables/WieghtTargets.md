---
type: table
database: Olives_BO
name: WieghtTargets
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# WieghtTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalespersonID | int | NO | ✓ |  |  |
| Coverage_Wieght | float | YES |  |  |  |
| Coverage_PaidTargetAmt | float | YES |  |  |  |
| Distribution_Wieght | float | YES |  |  |  |
| Distribution_PaidTargetAmt | float | YES |  |  |  |
| Productivity_Wieght | float | YES |  |  |  |
| Productivity_PaidTargetAmt | float | YES |  |  |  |
| SalesTarget_Wieght | float | YES |  |  |  |
| SalesTarget_PaidTargetAmt | float | YES |  |  |  |
| TargetPercentage | float | YES |  |  |  |
| TargetPercentage_Coverage | float | YES |  |  |  |
| TargetPercentage_Productivity | float | YES |  |  |  |
| TargetPercentage_Distribution | float | YES |  |  |  |
| TargetPercentage_Sales | float | YES |  |  |  |
## Primary Key
CompanyID
SalespersonID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

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
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[CustomerTargetsDetails]]
- [[PromotionsApprovalLog]]
- [[SalesQuotationHeaders]]
