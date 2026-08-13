---
type: table
database: Olives_BO
name: AddDiscountToCustomerOrders
schema: dbo
tags: [#backoffice, #billing, #customer, #order]
foreign_keys:
referenced_by:
  - [[Pro_AddDiscountToCustomerOrders]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# AddDiscountToCustomerOrders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores adddiscounttocustomerorders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| TransID | bigint | YES | ✓ |  |  |
| CompanyID | smallint | NO |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| SalesPersonID | int | YES |  |  |  |
| CategCode | nvarchar | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| WFApproved | bit | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
## Primary Key
TransID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_AddDiscountToCustomerOrders]]
- [[WF_AddWorkFlowLevels]]

**Writes (3):**
- [[Pro_AddDiscountToCustomerOrders]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

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
