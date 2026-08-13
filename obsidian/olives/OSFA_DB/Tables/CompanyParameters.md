---
type: table
database: OSFA_DB
name: CompanyParameters
schema: dbo
tags: [#mobile, #reference]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# CompanyParameters



## Business Purpose


System-wide configuration flags controlling feature toggles, behavior, and ERP integration settings.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | int | NO | ✓ |  |  |
| ImportTransInServerDate | bit | YES |  |  |  |
| NumberSavedFraction | int | YES |  |  |  |
| TruncRoundValue | int | YES |  |  |  |
## Primary Key
CompanyID
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


## See also
- [[Olives_BO/Tables/CompanyParameters]] (Back Office counterpart table)
- [[Shared/Runbooks/Login-Device-Issues]]

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[Glossary]]
- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[OT_PromotionsSalesmanGroupsLink]]
- [[OT_PaymentsTypes]]
- [[OT_RequestToChangeInvoicePaymentType]]

## Cross-Database


See also: [[Olives_BO/Tables/CompanyParameters|BO CompanyParameters]]
