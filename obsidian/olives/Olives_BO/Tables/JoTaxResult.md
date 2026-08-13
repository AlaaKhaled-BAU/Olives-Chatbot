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
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores jotaxresult records.

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
- [[Olives_BO/Tables/MMS_ShowRooms]]
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
- [[Olives_BO/Procedures/RunSQLWebAPI_Integ]]
- [[Olives_BO/Procedures/EncodeArabicToUTF8DataFromOSFA_API]]
- [[Olives_BO/Procedures/SMSSEND_ZUMOT]]
- [[Olives_BO/Procedures/Test_Banks]]
- [[Olives_BO/Procedures/Alpha_GetCurrRate]]
- [[Olives_BO/Procedures/Awtar_Integ_GetDataFromAPI]]
- [[Olives_BO/Procedures/PRO_REPORT]]
