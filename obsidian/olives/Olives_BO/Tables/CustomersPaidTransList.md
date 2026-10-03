---
type: table
database: Olives_BO
name: CustomersPaidTransList
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[CustomersInvoicesPayOnlineReport]]
  - [[OT_ImportReceipts]]
  - [[OT_ImportSalesInvoices]]
  - [[Pro_ReceiptRequests]]
  - [[Pro_TransactionsHeaders]]
  - [[RptOnlineRpt_CustAging]]
  - [[Rpt_ReceiptVouchers]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersPaidTransList


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerspaidtranslist records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| PaidTransYear | smallint | NO | ✓ |  |  |
| PaidTransNo | int | NO | ✓ |  |  |
| PaidTransTypeID | smallint | NO | ✓ |  |  |
| PaidTransAmount | float | YES |  |  |  |
| PaidTransRemainingAmount | float | YES |  |  |  |
| PaidTransDueDate | smalldatetime | YES |  |  |  |
| PaidTransDate | smalldatetime | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| Ref4 | nvarchar | YES |  |  |  |
| Ref5 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
PaidTransYear
PaidTransNo
PaidTransTypeID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (23):**
- [[CustomersInvoicesPayOnlineReport]]
- [[Pro_ReceiptRequests]]
- [[Pro_TransactionsHeaders]]
- [[RptOnlineRpt_CustAging]]
- [[Rpt_ReceiptVouchers]]

**Writes (15):**
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]

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
