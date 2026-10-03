---
type: table
database: Olives_BO
name: CustomersPromotionsGroups
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[CompanyBranches]]
  - [[Customers]]
referenced_by:
  - [[Diag_Check_Linked_Sales_Cust_Promotions]]
  - [[Pro_Customers]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersPromotionsGroups]]
  - [[Pro_CustomersPromotionsGroupsByDevice]]
  - [[Rpt_CustomersPromotionsGroupsByType]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersPromotionsGroups


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerspromotionsgroups records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Customers]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| CompanyBranchID | int | YES |  | ✓ | [[CompanyBranches]] |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CompanyBranchID -> [[CompanyBranches]](CompanyID, ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (12):**
- [[Diag_Check_Linked_Sales_Cust_Promotions]]
- [[Pro_Customers]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersPromotionsGroups]]
- [[Pro_CustomersPromotionsGroupsByDevice]]
- [[Rpt_CustomersPromotionsGroupsByType]]

**Writes (6):**
- [[Pro_Customers]]
- [[Pro_CustomersPromotionsGroups]]
- [[Pro_CustomersPromotionsGroupsByDevice]]

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
