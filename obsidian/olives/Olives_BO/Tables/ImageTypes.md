---
type: table
database: Olives_BO
name: ImageTypes
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_CustGalaryImages]]
  - [[Pro_ApproveImagesApp]]
  - [[Pro_ImageTypes]]
  - [[Pro_SalesmanImages]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
---
# ImageTypes


## Business Purpose

Reference/lookup table defining imagetypes categories.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| UseFor | int | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[OT_CustGalaryImages]]
- [[Pro_ApproveImagesApp]]
- [[Pro_ImageTypes]]
- [[Pro_SalesmanImages]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]

**Writes (1):**
- [[Pro_ImageTypes]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
