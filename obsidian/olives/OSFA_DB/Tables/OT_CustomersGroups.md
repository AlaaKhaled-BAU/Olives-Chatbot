---
type: table
database: OSFA_DB
name: OT_CustomersGroups
schema: dbo
tags: [#customer, #mobile, #reference]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustomersGroups



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| Group_ID | int | NO | ✓ |  |  |
| ArDesc | nvarchar | YES |  |  |  |
| EngDesc | nvarchar | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
Group_ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity


## See also
- [[Olives_BO/Tables/CustomersGroups]] (Back Office counterpart table)

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_CustomersGPSLocations]]
- [[OT_RequestToAddNewCustomer]]
- [[OT_ItemsQtyAvg]]
- [[OT_PromotionsSalesmanGroupsLink]]
- [[OT_PaymentsTypes]]
- [[OT_RequestToChangeInvoicePaymentType]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
