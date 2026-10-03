---
type: table
database: Olives_BO
name: WF_SalesPersonItemsCategoryValues
schema: dbo
tags: [#auth, #backoffice, #inventory, #reference, #sales, #workflow]
foreign_keys:

referenced_by:
  - [[Pro_WF_SalesPersonItemsCategoryValues]]
support_relevance: high
last_verified: 2026-07-05
---
# WF_SalesPersonItemsCategoryValues


## Business Purpose

Workflow configuration or log table for approval process management.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ItemCode | nvarchar | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| AllowValue | float | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |

## Primary Key
CompanyID
ItemCode
SalesPersonID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_WF_SalesPersonItemsCategoryValues]]

**Writes (1):**
- [[Pro_WF_SalesPersonItemsCategoryValues]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
