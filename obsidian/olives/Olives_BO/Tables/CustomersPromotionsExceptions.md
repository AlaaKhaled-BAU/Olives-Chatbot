---
type: table
database: Olives_BO
name: CustomersPromotionsExceptions
schema: dbo
tags: [#backoffice, #customer, #sales]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[PromotionsHeaders]]
referenced_by:
  - [[Pro_Customers]]
  - [[Pro_CustomersPromotionsExceptions]]
  - [[Pro_CustomersPromotionsGroupsByDevice]]
  - [[Pro_PromotionsHeaders]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersPromotionsExceptions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerspromotionsexceptions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| PromotionID | int | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| IsInclude | bit | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
PromotionID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, PromotionID -> [[PromotionsHeaders]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_Customers]]
- [[Pro_CustomersPromotionsExceptions]]
- [[Pro_CustomersPromotionsGroupsByDevice]]
- [[Pro_PromotionsHeaders]]

**Writes (3):**
- [[Pro_Customers]]
- [[Pro_CustomersPromotionsExceptions]]
- [[Pro_CustomersPromotionsGroupsByDevice]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
