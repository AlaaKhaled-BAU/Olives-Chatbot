---
type: table
database: Olives_BO
name: Drawers
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
referenced_by:
  - [[OT_ImportNewCust]]
  - [[OT_ImportReceipts]]
  - [[Pro_Checks]]
  - [[Pro_Drawers]]
  - [[Pro_ImportData]]
  - [[Pro_ReceiptPaid]]
  - [[Pro_Receipts]]
  - [[Rpt_PrintCollectedReceipt]]
  - [[Rpt_ReceiptVouchers]]
  - [[Rpt_ReceivablesSalesInvoice]]
support_relevance: high
last_verified: 2026-07-05
---
# Drawers


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores drawers records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Customers]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Drawers | nchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (18):**
- [[Pro_Checks]]
- [[Pro_Drawers]]
- [[Pro_ImportData]]
- [[Pro_ReceiptPaid]]
- [[Pro_Receipts]]
- [[Rpt_PrintCollectedReceipt]]
- [[Rpt_ReceiptVouchers]]
- [[Rpt_ReceivablesSalesInvoice]]

**Writes (10):**
- [[OT_ImportNewCust]]
- [[OT_ImportReceipts]]
- [[Pro_Drawers]]
- [[Pro_ImportData]]

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
