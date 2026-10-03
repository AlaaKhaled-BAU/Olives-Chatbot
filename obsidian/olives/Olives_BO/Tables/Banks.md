---
type: table
database: Olives_BO
name: Banks
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_SendCompData]]
  - [[Pro_Banks]]
  - [[Pro_Branches]]
  - [[Pro_Checks]]
  - [[Pro_ImportData]]
  - [[Pro_ReceiptPaid]]
  - [[Pro_Receipts]]
  - [[Rpt_ALLReturnChecks]]
  - [[Rpt_CashInvoiceAndReciept]]
  - [[Rpt_CashReceipts]]
  - [[Rpt_CheckStatusDetails]]
  - [[Rpt_ChecksByStatus]]
  - [[Rpt_ChequeInfrmation]]
  - [[Rpt_ChequeStatusWithSettelment]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_PrintCollectedReceipt]]
  - [[Rpt_PrintCollectedReceiptByInvoice]]
  - [[Rpt_ReceiptVouchers]]
  - [[Rpt_ReceiptsDetails]]
  - [[Rpt_ReceivablesSalesInvoice]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
---
# Banks


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores banks records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (110):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[OT_SendCompData]]
- [[Pro_Banks]]
- [[Pro_Branches]]
- [[Pro_Checks]]
- [[Pro_ImportData]]
- [[Pro_ReceiptPaid]]
- [[Pro_Receipts]]
- [[Rpt_ALLReturnChecks]]
- [[Rpt_CashInvoiceAndReciept]]
- [[Rpt_CashReceipts]]
- [[Rpt_CheckStatusDetails]]
- [[Rpt_ChecksByStatus]]
- [[Rpt_ChequeInfrmation]]
- [[Rpt_ChequeStatusWithSettelment]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_PrintCollectedReceipt]]
- [[Rpt_PrintCollectedReceiptByInvoice]]
- [[Rpt_ReceiptVouchers]]
- [[Rpt_ReceiptsDetails]]
- [[Rpt_ReceivablesSalesInvoice]]

**Writes (55):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_Banks]]
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
- See also (OSFA counterpart): [[OSFA_DB/Tables/OT_Banks]]
