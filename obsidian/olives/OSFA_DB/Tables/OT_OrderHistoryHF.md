---
type: table
database: OSFA_DB
name: OT_OrderHistoryHF
schema: dbo
tags: [#log, #mobile, #order]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_OrderHistoryHF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| OrderState | smallint | YES |  |  |  |
| Reason | smallint | YES |  |  |  |
| OrderStateDesc | varchar | YES |  |  |  |
| ReasonDesc | varchar | YES |  |  |  |
| PO_No | nvarchar | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| DeliveryOrderYear | int | YES |  |  |  |
| DeliveryOrderNo | bigint | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
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
- [[OT_OrderHistoryDF]]
- [[OT_JsonLog]]
- [[OT_OrderHF]]
- [[OT_ConsOrderDF]]
- [[OT_SalesQuotationHF]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
