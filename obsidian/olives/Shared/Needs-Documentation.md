---
type: shared
name: Needs-Documentation
tags: [#reference, #shared]
---

# Needs Documentation

> Generated: 2026-07-06
> Purpose: Track undocumented procedures identified during backpropagation

## 53 Stub Notes (created 2026-07-06)

These stored procedures are referenced by other procedures but have no full documentation. Stub notes created with `status: stub`.

Pro_ApproveNewCustomers, Pro_ApproveSalespersonsImages, Pro_ApproveVoidPayments,
Pro_AssignCustomersForSalesman, Pro_AssignItemForReturn, Pro_AssignItemsForStores,
Pro_AssignPlanogramForCustomers, Pro_BackOrder, Pro_ChangeCheckStatus,
Pro_CollectGPS, Pro_CopyTarget, Pro_CustomerLocationApproval,
Pro_CustomersRoutesAssignment, Pro_DashboardProductPerformance,
Pro_DashboardSalesAnalysis, Pro_DashboardSalesGrowth,
Pro_DashboardSalesmanDashboard, Pro_DashboardSalesmanKPI,
Pro_DashboardTargetDashboard, Pro_ImportOrdersIssues,
Pro_MoveSalespersonCustomersPerRoutes, Pro_PasswordGenerator,
Pro_PaymentAmountDetails, Pro_PaymentsApproval,
Pro_PriceListPromotionGroupLink, Pro_Promotions, Pro_PromotionsWFApprove,
Pro_ReceiptRequest, Pro_ReceiptRequestSchedule, Pro_ReturnOrderFinalApproval,
Pro_ReturnOrdersApproval, Pro_ReturnSalesApproval, Pro_ReturnSalesFinalApproval,
Pro_ReturnSalesVoid, Pro_Routes, Pro_SalesInvoiceApproval,
Pro_SalesInvoiceVoid, Pro_SalesmanAutoUnload, Pro_SalesOrderFinalApproval,
Pro_SalesOrdersApproval, Pro_SalespersonsItemsAssignment,
Pro_SalespersonStockTakingApproval, Pro_SendBackOrder,
Pro_ShowMultiRouteInMap, Pro_ShowRouteInMap, Pro_SortItems,
Pro_TransferCustomersByRoute, Pro_TransferOrdersApproval, Pro_TransferToERP,
Pro_UserActivityLog, Pro_WFCustomersAutoApprove, Pro_WFFunctionsReport,
Pro_WFSetup

## `writes_to` Coverage (Updated 2026-07-06)

| Database | Total Procs | With writes_to | Read-only | Coverage |
|----------|-------------|----------------|-----------|----------|
| Olives_BO | 1,503 | 726 | 777 | 48.3% |
| OSFA_DB | 205 | 126 | 79 | 61.5% |
| **Total** | **1,708** | **852** | **856** | **49.9%** |

All 852 procedures with detected write operations now have `writes_to` populated. The remaining 856 are read-only procs (SELECT-only or report queries).

## `reads_from` Format

92% of procedure notes use comma-separated strings instead of YAML list format for `reads_from`. This works with Dataview display but cannot be queried as individual items. Future fix: convert to proper YAML list format.

## `foreign_keys` Gaps

~32 table notes have empty `foreign_keys` frontmatter despite having FK columns defined in body table. Needs parsing to extract from SQL schema.

## Remaining Gaps

1. **`writes_to`**: 852/1,708 populated (49.9%) — remaining are read-only procs ✅
2. **`reads_from` format**: ~1,570 procs use comma-separated string (not YAML list)
3. **`foreign_keys` empty**: ~32 tables need FK extraction
4. **Relation frontmatter**: `parent_table`/`referenced_table`/`columns` added to all 28 ✅
5. **53 stub procedures**: Still need full documentation
