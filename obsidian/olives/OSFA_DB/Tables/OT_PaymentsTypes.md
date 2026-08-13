---
type: table
database: OSFA_DB
name: OT_PaymentsTypes
schema: dbo
tags: [#billing, #mobile, #reference]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_PaymentsTypes



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| PTypeID | smallint | NO | ✓ |  |  |
| PTypeName | varchar | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| DueDays | int | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
PTypeID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_PriceList]]
- [[OT_RequestToChangeInvoicePaymentType]]
- [[OT_ItemsPriceExceptions]]
- [[OT_PromotionsSalesmanGroupsLink]]
- [[OT_PromotionsCustomersGroupsLink]]
- [[CompanyParameters]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
- [[OSFA_DB/Tables/OT_SystemOptionsTypes]]
- [[OSFA_DB/Tables/OT_Payment_Invoices_Test]]
