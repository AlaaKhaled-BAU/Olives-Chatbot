---
type: table
database: Olives_BO
name: JoTaxResult
schema: dbo
tags: [#backoffice, #billing, #legal]
foreign_keys:
referenced_by:
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxApiFromOSFA]]
  - [[Pro_JoTaxApiFromOSFA____]]
  - [[Pro_JoTaxResend]]
support_relevance: high
last_verified: 2026-07-05
---
# JoTaxResult


## Business Purpose
Government electronic invoicing audit and clearance result table for the Jordanian Tax Authority (ISTD JoTax / الفاتورة الوطنية الإلكترونية).
- **Invoice Link**: Stores API clearance responses and tax submission logs for sales invoices (`TransactionsHeaders` with `TransactionTypeID = 1`) and return invoices (`TransactionTypeID = 2`).
- **Clearance Status**: `status` indicates whether an invoice was successfully submitted and cleared (`PASS` / `P`), or failed clearance (`ERROR`, `E`, `500`).
- **Electronic Identifiers**: Stores the official cryptographic QR code (`EINV_QR`), invoice UUID (`EINV_INV_UUID`, `UUID`), and error response details (`ErrorMessage`) returned by the tax authority API.

## Chatbot semantics
(Query `t.JoTaxResult` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| حالة الفاتورة الضريبية / الربط الضريبي | `status`, `ErrorMessage`, `UUID` | Join `t.TransactionsHeaders inv ON res.TransactionYear = inv.TransactionYear AND res.TransactionNo = inv.TransactionNo AND res.TransactionTypeID = inv.TransactionTypeID` |
| فواتير مقبولة ضريبياً / معتمدة | `status` | `status IN (N'PASS', N'P')` |
| فواتير مرفوضة أو معلقة ضريبياً | `status`, `ErrorMessage` | `status NOT IN (N'PASS', N'P')` أو `ErrorMessage IS NOT NULL` |
| رمز الاستجابة السريع والرمز التعريفي | `EINV_QR`, `UUID` | التحقق من وجود المعرف الضريبي والـ QR |

## Grain & keys
- **Grain**: One row per invoice tax clearance attempt/submission (`TransactionTypeID`, `TransactionYear`, `TransactionNo`).
- **Composite PK**: `CompanyID`, `TransactionTypeID`, `TransactionYear`, `TransactionNo`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Mobile Invoicing / BO Billing → `Pro_JoTaxApi` / `Pro_JoTaxApiFromOSFA` → API Submission to ISTD Server → `JoTaxResult` (`status`, `UUID`, `EINV_QR`).

## Related
- [[TransactionsHeaders]]
- [[TransactionsDetails]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| TransactionYear | int | NO | ✓ |  |  |
| EINV_QR | nvarchar | YES |  |  |  |
| EINV_INV_UUID | nvarchar | YES |  |  |  |
| status | nvarchar | YES |  |  |  |
| ErrorMessage | nvarchar | YES |  |  |  |
| UUID | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
TransactionNo
TransactionTypeID
TransactionYear
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]
- [[Pro_JoTaxResend]]

**Writes (3):**
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]

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
- [[Olives_BO/Tables/Tech_CustomizationPerformedTasks]]
- [[Olives_BO/Tables/CustomersFinancialDetails2]]
- [[Olives_BO/Tables/forupdateonly]]
- [[Olives_BO/Tables/MultiTargets]]
- [[Olives_BO/Tables/Clients]]
- [[Olives_BO/Tables/Pos_InvoiceOrderHF]]
- [[Olives_BO/Tables/CustomersReturnItemQtyLimit]]
- [[Olives_BO/Tables/ItemsSuggestGroupLinkWithItems]]
- [[Olives_BO/Tables/SalesPersonItemsBalanceBatches]]
- [[Olives_BO/Tables/Customers2]]
- [[Olives_BO/Tables/EmpDetails]]
- [[Olives_BO/Tables/ClientsWFID]]
- [[Olives_BO/Tables/ItemsInventory]]
- [[Olives_BO/Tables/WieghtTargets]]
- [[Olives_BO/Tables/CustomersFinancialDetails_Old]]
- [[Olives_BO/Tables/PriceListQtyRanges]]
- [[Olives_BO/Tables/LogActions]]
- [[Olives_BO/Tables/PromotionTypes]]
- [[Olives_BO/Procedures/GetCustomerAssets]]
- [[Olives_BO/Procedures/Pro_PrintCheque]]
- [[Olives_BO/Procedures/Pro_MonthlySalesPersonsTargets]]
- [[Olives_BO/Procedures/DashBoard_ExceptionsIssues]]
- [[Olives_BO/Procedures/EncodeArabicToUTF8DataFromOSFA_API]]
- [[Olives_BO/Procedures/SMSSEND_ZUMOT]]
- [[Olives_BO/Procedures/Test_Banks]]
- [[Olives_BO/Procedures/PRO_REPORT]]
