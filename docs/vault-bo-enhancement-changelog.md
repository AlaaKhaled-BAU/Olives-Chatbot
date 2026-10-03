# Vault Olives_BO Enhancement Changelog

## 1. Executive Summary

This enhancement overhauls the **`obsidian/olives/Olives_BO/`** knowledge layer for the embeddable Olives read-only SQL chatbot. It equips the chatbot to accurately understand business queries from supervisors, sales operations, and branch managers in natural Arabic, correctly routing them to the appropriate `t.*` tenant views, joins, status codes, and grains without leaking procedure bodies or write paths.

All modifications strictly conform to:
- Read-only tenancy isolation (`t.` views + `SESSION_CONTEXT('CompanyID')`).
- No procedure bodies (`CREATE PROCEDURE` / `ALTER PROCEDURE`) in vault notes.
- Compiled vault cards structure (`Business Purpose`, `Grain & keys`, `Chatbot semantics`, `Pipeline`).
- Live database verification against `Olives_BO` and live schema cache.

---

## 2. Evidence Sources & Validation Method

1. **Live SQL Server Instance (`Olives_BO`)**:
   - SA connection via `setup/db_connect.py` on port 1433.
   - Live querying of `SystemCodes` (`SysCodeTypeID` 2 for `SalespersonType`, 50 for `ReasonType`).
   - Live querying of `WF_Functions` (47 distinct workflow types cataloged).
   - Distinct counts and code distributions for `NoTransactionsReasons`, `LogActionTransaction`, and workflow log entries.
2. **Schema Cache (`work/105/schema_cache.json` & `work/morec/schema_cache.json`)**:
   - Column-level truth and data types for all `t.*` views.
   - Introspected table column synchronizations executed via `setup/sync_vault_from_cache.py`.
3. **Stored Procedure Logic Inspection (Metadata Only)**:
   - Evaluated `WF_AddWorkFlowLevelOne`, `WF_AddWorkFlowLevels`, `WF_CancelRequest`, `OT_ImportActionLog`, and `OT_FixActionLog`.
   - Identified explicit state transition mechanics: `WF_MasterLog.LastStatus` (0=Open, 1=Approved, 2=Rejected, 3=Canceled), `WF_SubLog.ActionNeed = 'AR'`, `WF_SubLog.Action` ('A'/'R'), and `Ref1`..`Ref5` join patterns.

---

## 3. Detailed Files Touched

### 3.1 Codebooks & Catalog Enhancements (Tier 1)
- **`obsidian/olives/Olives_BO/Tables/SystemCodes.md`**:
  - Enriched with verified `SysCodeTypeID` definitions: `SalespersonType` (1=Pre-sales, 2=Van Sales, 3=Supervisor, 4=Salesman, etc.), `ReasonType` (1=No Sales, 2=No Visit, 3=Postpone), and `CheckStatus`.
  - Added explicit warnings distinguishing `SystemCodes.Status` from `WF_MasterLog.LastStatus`.
- **`obsidian/olives/Olives_BO/Tables/NoTransactionsReasons.md`**:
  - Documented `ReasonType` filter (1 = No sales exit / عدم بيع, 2 = No visit exit / عدم زيارة).
  - Detailed joins to `NoTransactionsLog` and tablet requests (`RequestSalesmanWillNotVisit`).
- **`obsidian/olives/Olives_BO/Tables/NoTransactionsLog.md`**:
  - Detailed GPS tracking, reason lookup, and grain definitions for visit cancellations and non-sale visits.
- **`obsidian/olives/Olives_BO/Tables/WF_Functions.md`**:
  - Comprehensive catalog of all 47 workflow function IDs with English and Arabic names and corresponding `Ref1` document targets.

### 3.2 Core Workflow Engine (Tier 2)
- **`obsidian/olives/Olives_BO/Tables/WF_MasterLog.md`**:
  - Business Purpose rewritten to emphasize the master approval lifecycle.
  - Complete `## Chatbot semantics` mapping Arabic inquiries (طلبات معلقة, طلبات معتمدة, طلبات مرفوضة, ملغية).
  - Clarified `Ref1`..`Ref5` join mechanisms (`TRY_CAST(Ref1 AS numeric) = AutoID` for `RequestTo*`, `OrderYear`/`OrderNo` for `OrdersHeaders`).
- **`obsidian/olives/Olives_BO/Tables/WF_SubLog.md`**:
  - Detailed the **Supervisor Inbox** query pattern (`ActionNeed = 'AR' AND Action IS NULL`).
  - Documented audit trail for actions (`A` = Approved, `R` = Rejected).
- **`obsidian/olives/Olives_BO/Tables/WF_PositionsVer.md`**:
  - Documented position-based approval matrix versioning.
- **`obsidian/olives/Olives_BO/Tables/WF_SetupHeader.md` & `WF_SetupDetails.md`**:
  - Documented threshold definitions, escalation paths, and approval level rules.

### 3.3 RequestTo* Family (Tier 2)
Added comprehensive `## Chatbot semantics`, grains, pipelines, and `WF_MasterLog` join recipes to:
- `RequestToExceedCustomerCreditLimit.md` (Function 2 - تجاوز سقف الائتمان)
- `RequestToExceedCustomerCreditLimitInOrder.md` (Function 15 - تجاوز سقف الائتمان في الطلبية)
- `RequestToVisitCustomerNotInRoute.md` (Function 5 - زيارة خارج خط السير)
- `RequestSalesmanWillNotVisit.md` (Function 23 - عدم زيارة عميل مجدول)
- `RequestToAddDiscount.md` (Function 11 - طلب خصم إضافي)
- `RequestToAddDiscountInOrder.md` (Function 13 - طلب خصم في طلبية)
- `RequestToAddNewCustomer.md` (Function 21 - إضافة عميل جديد)
- `RequestToApprovePromotion.md` (Function 28 - اعتماد بونص / عرض)
- `RequestToChangeInvoicePaymentType.md` (Function 1 - تغيير طريقة الدفع)
- `RequestToChangeItemSellPrice.md` (Function 18/19 - تعديل سعر بيع الصنف)
- `RequestToExceedCustomerInvoiceDueDays.md` (Function 4 - تجاوز فترة الاستحقاق)
- `RequestToVoidTransaction.md` (Function 46 - إلغاء فاتورة / حركة)
- `RequestToMakeZeroAmountInvoice.md` (Function 38 - فاتورة بصافي صفر)
- `RequestToLinkCustomerToSalesman.md` (Function 36 - ربط عميل بمندوب)
- `RequestToExceedFinishAllTasks.md` (Function 37 - تجاوز إنهاء المهام)
- `RequestSalesmanNoTransaction.md` (Function 24 - عدم إجراء حركة)
- `RequestToExceedChqLimit.md` (Function 14 - تجاوز سقف الشيكات)
- `RequestToAllowTakeChecksFromCustomer.md` (Function 27 - قبول شيكات من عميل نقدي)
- `RequestToReturnInvoice.md` (Function 8 - إرجاع فاتورة)

### 3.4 Master Data, Sales, & Visits (Tier 2)
- **`obsidian/olives/Olives_BO/Tables/SalesPersonsRoutes.md`**:
  - Clarified planned route schedules vs actual visits.
  - Documented `WeekDay` (1=Saturday .. 7=Friday) and cycle weeks `Week1`..`Week4`.
- **`obsidian/olives/Olives_BO/Tables/CustomersFinancialDetails.md`**:
  - Clarified customer routing assignment (`RouteID`), stop order (`VisitOrder`), and assigned position (`PositionsID`).
- **`obsidian/olives/Olives_BO/Tables/SalesPersons.md`**:
  - Documented `Parent` column hierarchy (supervisor to salesmen link).
- **`obsidian/olives/Olives_BO/Tables/Customers.md`**:
  - Master customer demographics and suspension flags (`IsSuspended`).
- **`obsidian/olives/Olives_BO/Tables/OrdersHeaders.md` & `ReturnOrdersHeaders.md`**:
  - Pre-sales orders and return orders workflow linking.
- **`obsidian/olives/Olives_BO/Tables/OrdersDetails.md`**:
  - Line-item detail for pre-sales orders (quantities, prices, discounts, free bonus goods).
- **`obsidian/olives/Olives_BO/Tables/TransactionsHeaders.md`**:
  - Invoices vs returns (`TransactionTypeID` 1 vs 2) and payment terms (`CreditCash`).
- **`obsidian/olives/Olives_BO/Tables/TransactionsDetails.md`**:
  - Line-item detail for sales invoices and return invoices (exact billed goods, bonus, line taxes).
- **`obsidian/olives/Olives_BO/Tables/ReturnOrdersDetails.md`**:
  - Line-item detail for customer return requests prior to invoice conversion.
- **`obsidian/olives/Olives_BO/Tables/Receipts.md`**:
  - Collections, cash vs check vouchers.
- **`obsidian/olives/Olives_BO/Tables/Checks.md`**:
  - Check instrument portfolio, bank, due date aging, and status tracking.
- **`obsidian/olives/Olives_BO/Tables/Receipts_PaidTrans.md`**:
  - Payment settlement and allocation bridge connecting receipts to specific sales invoices.
- **`obsidian/olives/Olives_BO/Tables/TransfersOrdersHeaders.md` & `TransfersOrdersDetails.md`**:
  - Vehicle restocking load orders (`VouType = 1`) and return unload orders (`VouType = 2`).
- **`obsidian/olives/Olives_BO/Tables/SalesPersonTargetsDetails.md`**:
  - Monthly representative sales targets, quotas, quantities, and commission percentages.
- **`obsidian/olives/Olives_BO/Tables/PromotionsHeaders.md`**:
  - Active promotion campaigns, validity dates, bonus rules, and eligibility thresholds.
- **`obsidian/olives/Olives_BO/Tables/BankDepositHF.md` & `BankDepositDF.md`**:
  - End-of-day salesman bank deposit vouchers, GPS presence logging, and receipt details.
- **`obsidian/olives/Olives_BO/Tables/LogActionTransaction.md`**:
  - Tablet action log, actual visits (`ActionID = N'0'`), duration calculations, no-sale exits, and journey lifecycle.
- **`obsidian/olives/Olives_BO/Tables/JoTaxResult.md`**:
  - Jordanian National Electronic Invoicing (ISTD JoTax) clearance responses, status codes (`PASS`, `ERROR`), QR codes, and UUIDs.
- **`obsidian/olives/Olives_BO/Tables/Items.md` & `ItemsCategories.md`**:
  - Master product catalog, SKU descriptions, status flags, and category hierarchy trees.
- **`obsidian/olives/Olives_BO/Tables/SalesPersonItemsAssignment.md` & `CustomersItemsAssigment.md`**:
  - Item authorization portfolios per salesman position and customer-specific product restrictions/assortment.
- **`obsidian/olives/Olives_BO/Tables/InvoiceHistoryHF.md` & `InvoiceHistoryDF.md`**:
  - Historical / legacy ERP sales invoice archive (clarified distinction from live `TransactionsHeaders` / `TransactionsDetails`).
- **`obsidian/olives/Olives_BO/Tables/SalesOrderHistoryHF.md` & `SalesOrderHistoryDF.md`**:
  - Historical pre-sales order archive and delivery fulfillment tracking (clarified distinction from live `OrdersHeaders` / `OrdersDetails`).
- **`obsidian/olives/Olives_BO/Tables/PriceLists.md` & `PriceListDetails.md`**:
  - Customer tier pricing.
- **`obsidian/olives/Olives_BO/Tables/Positions.md`**:
  - Organizational positions as workflow inbox targets.
- **`obsidian/olives/Olives_BO/Tables/RoutesInformation.md`**:
  - Route code definitions.
- **`obsidian/olives/Olives_BO/Tables/CustomersVisitActivity.md`**:
  - Task execution requirements per customer visit.
- **`obsidian/olives/Olives_BO/Tables/SalespersonRouteByDate.md`**:
  - Specific date route exceptions.
- **`obsidian/olives/Olives_BO/Tables/SalesPersonItemsBalance.md`**:
  - Van inventory balances.

### 3.5 Relations (Tier 3)
Created new, authoritative relation notes:
- **`obsidian/olives/Olives_BO/Relations/WF_MasterLog--WF_SubLog.md`**:
  - Connects master requests with approval task steps (`ReqID`).
- **`obsidian/olives/Olives_BO/Relations/WF_MasterLog--WF_Functions.md`**:
  - Connects master requests with function catalog (`FunctionID`).
- **`obsidian/olives/Olives_BO/Relations/SalesPersons--SalesPersons.md`**:
  - Documents self-referencing hierarchy (`Parent` = supervisor `ID`).

### 3.6 Stored Procedure Metadata (Tier 4)
Updated auto-generated Purpose text with trigger/outcome semantics (free of SQL code):
- **`WF_AddWorkFlowLevelOne.md`**: Level 1 approval creation trigger and `Ref1`..`Ref5` parameters.
- **`WF_AddWorkFlowLevels.md`**: Approver decision execution, state transition, and final approval triggers.
- **`WF_CancelRequest.md`**: Request cancellation mechanics and status updating (`LastStatus = 3`).
- **`OT_FixActionLog.md`**: Pre-report reconciliation between tablet logs and transactional headers.

### 3.7 Integration & Non-BO Cleanup (Trimming)
Removed all third-party ERP integration and client-specific sync knowledge from the vault:
- **Procedures (491 notes removed)**:
  - Eliminated all third-party sync routines (`SAP_*`, `ABS_*`, `Bonanza_*`, `AX_*`, `GP_*`, `AccPack_*`, `X3_*`, `Awtar_*`, `PrestoSoft_*`, `Phenix_*`, `Wings_*`, `Yolande_*`, `Galaxy_*`, `JV_*`, `Motakaml_*`, `Shamel_*`, `ProTech_*`, `JoTax_*`, `Zatca_*`, etc.).
  - Eliminated SMS integration procedures (`SMS_*`).
  - Eliminated generic integration routines containing `*Integ*`.
  - Preserved strictly core Back-Office procedures (1,231 procedures remaining).
- **Tables & Relations (39 notes removed)**:
  - Removed Maintenance Module / Integration tables (`MMS_*`, `IntegrationErrorLog`, `IntegrationPostedTransactions`).
  - Removed obsolete relation `IntegrationPostedTransactions--TransactionsHeaders.md`.
  - Preserved 401 core BO tables.

---

## 4. Build Pipeline & Verification Checklist

- [x] **No Procedure Bodies**: Cleaned and verified via `grep -ri "CREATE PROCEDURE"` and `grep -ri "ALTER PROCEDURE"`. Zero matches.
- [x] **Only `Olives_BO/` Modified**: No touches to `OSFA_DB/`, `Shared/Runbooks/`, `core/`, `api/`, or `.env`.
- [x] **No Secrets or Customer PII**: Only generic codes, schema definitions, and system parameters documented.
- [x] **Cache & Cards Compiled**:
  - `python3.13 setup/sync_vault_from_cache.py --client 105` succeeded.
  - `python3.13 setup/compile_vault_cards.py --client 105` succeeded (511 cards written to `vault_cards.sqlite`).
  - `python3.13 setup/04_assemble_docs_corpus.py` and `setup/05_index_docs.py --client 105` completed (10,353 chunks indexed).
- [x] **Runtime Discoverability**:
  - `core.vault.search_schema_notes` verified for `WF_MasterLog`, `RequestTo*`, and relations.
  - `core.vault.read_schema_note` verified.
  - `core.vault.get_joins` verified (retrieves newly created relations).
- [x] **Supervisor Battery Smoke**:
  - `python3.13 evals/run_vault_supervisor_battery.py --one-chat --max-turns 3 --client 105` completed without crashing in 18.2s with 3/3 queries logged.

---

## 5. List of Unverified Claims & Future Follow-ups

1. **Back-office UI Approval Screen Defaults**:
   - `WF_SubLog.Notes`: In some client setups, rejection requires a mandatory note, while approval allows a null note. Needs UI screen confirmation.
2. **`RequestTo*` Direct Voiding vs Workflow Cancellation**:
   - Some client configurations permit cancelling a request directly on the back-office screen without creating a `WF_CancelRequest` transaction. Needs operational workflow verification.
3. **Route Assignment Priority**:
   - When a customer is scheduled on both `SalesPersonsRoutes` (weekly template) and `SalespersonRouteByDate` (date exception), the date exception overrides the weekly template. Verified by query logic, but operational practice per client should be monitored.
