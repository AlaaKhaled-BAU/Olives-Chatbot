---
type: table
database: OSFA_DB
name: OT_OrderHistoryDF
schema: dbo
tags: [#log, #mobile, #order]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_OrderHistoryDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| OrderdQty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| DeliveredQty | money | YES |  |  |  |
| OutstandingQty | money | YES |  |  |  |
| SellValue | float | YES |  |  |  |
| DiscPerc | money | YES |  |  |  |
| DiscValue | float | YES |  |  |  |
| TaxPerc | money | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| QtyOH | money | YES |  |  |  |
| ItemDesc | varchar | YES |  |  |  |
| InvQty | money | YES |  |  |  |
| VoucherDiscount | float | YES |  |  |  |
| TaxType | smallint | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
ItemNo
UnitCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_RequestToLoginToCustomerWithoutVerficiation]]
- [[OT_JsonLog]]
- [[OT_ErrorLog]]
- [[OT_OrderHF]]
- [[OT_ConsOrderDF]]
- [[OT_SalesQuotationHF]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
- [[OSFA_DB/Tables/OT_JsonLog_Tmp]]
