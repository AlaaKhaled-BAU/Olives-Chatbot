---
type: table
database: Olives_BO
name: CouponsBooksDetails
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[CouponsBooksHeaders]]
  - [[PromotionsHeaders]]
referenced_by:
  - [[OT_ImportSalesInvoices]]
  - [[Pro_CouponsBooksDetails]]
  - [[Pro_CouponsBooksHeaders]]
  - [[SMS_ZumotPromoCodes]]
support_relevance: high
last_verified: 2026-07-05
---
# CouponsBooksDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores couponsbooksdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| BookID | int | NO | ✓ | ✓ | [[CouponsBooksHeaders]] |
| CuoponNumber | nvarchar | YES | ✓ |  |  |
| CuoponBarcode | nvarchar | YES |  |  |  |
| PromotionID | int | YES |  | ✓ | [[PromotionsHeaders]] |
| IsUsed | bit | YES |  |  |  |
| UsedInTrType | smallint | YES |  |  |  |
| UsedInTrYear | smallint | YES |  |  |  |
| UsedInTrNo | int | YES |  |  |  |
| ExpDate | smalldatetime | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
## Primary Key
CompanyID
BookID
CuoponNumber
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, BookID -> [[CouponsBooksHeaders]](CompanyID, ID)
CompanyID, PromotionID -> [[PromotionsHeaders]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Pro_CouponsBooksDetails]]
- [[Pro_CouponsBooksHeaders]]
- [[SMS_ZumotPromoCodes]]

**Writes (4):**
- [[OT_ImportSalesInvoices]]
- [[Pro_CouponsBooksDetails]]
- [[Pro_CouponsBooksHeaders]]
- [[SMS_ZumotPromoCodes]]

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
