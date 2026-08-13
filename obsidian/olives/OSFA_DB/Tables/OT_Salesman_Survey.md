---
type: table
database: OSFA_DB
name: OT_Salesman_Survey
schema: dbo
tags: [#mobile, #sales, #survey]
foreign_keys:
referenced_by:
  - [[OT_Add_Salesman_Survey]]
  - [[OT_Salesman_Survey_CheckExist]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Salesman_Survey



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| Salesman_Survey_No | bigint | YES | ✓ |  |  |
| CompNo | smallint | YES |  |  |  |
| Survey_ID | int | YES |  |  |  |
| Survey_Date | datetime | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| SalesmanNo | nvarchar | YES |  |  |  |
| Posted | bit | YES |  |  |  |
| IsProspectiveCustomer | bit | YES |  |  |  |
| ForSalesmanNo | nvarchar | YES |  |  |  |
## Primary Key
Salesman_Survey_No
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_Add_Salesman_Survey]]
- [[OT_Salesman_Survey_CheckExist]]

**Writes (1):**
- [[OT_Add_Salesman_Survey]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
