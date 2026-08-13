---
type: table
database: Olives_BO
name: UserCustomersPromotionsGroupLink
schema: dbo
tags: [#auth, #backoffice, #customer, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[CustomersPromotionsGroups]]
  - [[Users]]
referenced_by:
  - [[Pro_CustomersPromotionsGroups]]
support_relevance: high
last_verified: 2026-07-05
---
# UserCustomersPromotionsGroupLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores usercustomerspromotionsgrouplink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CustomersPromotionsGroups]] |
| UserID | nvarchar | YES | ✓ | ✓ | [[Users]] |
| CustomersPromotionsGroupsID | int | NO | ✓ | ✓ | [[CustomersPromotionsGroups]] |
## Primary Key
CompanyID
UserID
CustomersPromotionsGroupsID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomersPromotionsGroupsID -> [[CustomersPromotionsGroups]](CompanyID, ID)
UserID -> [[Users]](UserID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_CustomersPromotionsGroups]]

**Writes (1):**
- [[Pro_CustomersPromotionsGroups]]

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
