---
type: table
database: Olives_BO
name: CustomersPromotionsGroupsLink
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[CustomersPromotionsGroups]]
referenced_by:
  - [[Diag_Check_Linked_Sales_Cust_Promotions]]
  - [[OT_ImportNewCust]]
  - [[OT_ImportNewCust_145]]
  - [[Pro_Customers]]
  - [[Pro_CustomersPromotionsGroupsByDevice]]
  - [[Pro_CustomersPromotionsGroupsLink]]
  - [[Pro_PriceList_PromGroup_SalesLink]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersPromotionsGroupsLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerspromotionsgroupslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CustomersPromotionsGroups]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| CustomersPromotionsGroupsID | int | NO | ✓ | ✓ | [[CustomersPromotionsGroups]] |
## Primary Key
CompanyID
CustomerID
CustomersPromotionsGroupsID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, CustomersPromotionsGroupsID -> [[CustomersPromotionsGroups]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (17):**
- [[Diag_Check_Linked_Sales_Cust_Promotions]]
- [[OT_ImportNewCust]]
- [[Pro_Customers]]
- [[Pro_CustomersPromotionsGroupsByDevice]]
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_PriceList_PromGroup_SalesLink]]

**Writes (14):**
- [[OT_ImportNewCust]]
- [[OT_ImportNewCust_145]]
- [[Pro_Customers]]
- [[Pro_CustomersPromotionsGroupsByDevice]]
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_PriceList_PromGroup_SalesLink]]

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
