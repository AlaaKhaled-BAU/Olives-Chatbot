---
type: table
database: OSFA_DB
name: OT_LinkedSalesman
schema: dbo
tags: [#mobile, #sales]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_LinkedSalesman



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| LinkedSalesmanNo | int | NO | ✓ |  |  |
| ArName | varchar | YES |  |  |  |
| EngName | varchar | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
LinkedSalesmanNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_PromotionsCondUnCodInput]]
- [[OT_PromotionsSalesmanGroupsLink]]
- [[OT_PromotionsHeaders]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
- [[OSFA_DB/Tables/OT_BonusItemRanges]]
- [[OSFA_DB/Tables/OT_BonusItemPriority]]
- [[OSFA_DB/Tables/CompetitiveItemsImage]]
- [[OSFA_DB/Tables/OT_PromotionsRangeInputOutput]]
- [[OSFA_DB/Tables/OT_CustomersPromotionsExceptions]]
- [[OSFA_DB/Tables/Invt_ItemsImage]]
- [[OSFA_DB/Tables/OT_PromotionsGroupsCustomersLink]]
