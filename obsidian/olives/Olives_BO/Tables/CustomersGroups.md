---
type: table
database: Olives_BO
name: CustomersGroups
schema: dbo
tags: [#backoffice, #customer, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Awtar_Integration_WithLog]]
  - [[ECO_Land_SAP_Integ]]
  - [[Niroukh_Integration_WithLog]]
  - [[POAOnlineReport]]
  - [[Pro_Customers]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersGroups]]
  - [[Rpt_CustomerNameByLocation]]
  - [[Spartan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Customer-Setup
  - PriceList-Management
---
# CustomersGroups


## Business Purpose

Customer grouping for promotions, pricing, and route assignment.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| GroupID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
GroupID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (9):**
- [[Awtar_Integration_WithLog]]
- [[ECO_Land_SAP_Integ]]
- [[Niroukh_Integration_WithLog]]
- [[POAOnlineReport]]
- [[Pro_Customers]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersGroups]]
- [[Rpt_CustomerNameByLocation]]
- [[Spartan_SAP_Integ]]

**Writes (4):**
- [[Awtar_Integration_WithLog]]
- [[ECO_Land_SAP_Integ]]
- [[Niroukh_Integration_WithLog]]
- [[Pro_CustomersGroups]]

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
- See also (OSFA counterpart): [[OSFA_DB/Tables/OT_CustomersGroups]]
