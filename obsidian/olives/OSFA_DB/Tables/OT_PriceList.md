---
type: table
database: OSFA_DB
name: OT_PriceList
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_PriceList



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | smallint | NO | ✓ |  |  |
| PrNo | smallint | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| SellPrice | float | YES |  |  |  |
| TaxPerc | float | YES |  |  |  |
| SellPrice2 | float | YES |  |  |  |
| SellPrice3 | float | YES |  |  |  |
| TaxType | bit | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| UseInReturn | bit | YES |  |  |  |
| UseInSales | bit | YES |  |  |  |
| Qty | money | YES |  |  |  |
| Tax_1_Type | bit | YES |  |  |  |
| Tax_1_Perc | float | YES |  |  |  |
| Tax_2_Type | bit | YES |  |  |  |
| Tax_2_Perc | float | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
PrNo
ItemNo
UnitCode
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

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_PaymentsTypes]]
- [[OT_RequestToChangeInvoicePaymentType]]
- [[OT_ItemsPriceExceptions]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
- [[OSFA_DB/Tables/OT_Payment_Invoices_Test]]
- [[OSFA_DB/Procedures/OT_DirectInvoice]]
