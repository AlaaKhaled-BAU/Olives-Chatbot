---
type: table
database: Olives_BO
name: SystemCodes
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
referenced_by:
  - [[Pro_AssetTransfer]]
  - [[Pro_AssetsDefinition]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_DeliveryAssigning]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DeliveryInvoiceAssigning]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_OT_Layout_Setting]]
  - [[Pro_ReceiptRequestsSchedule]]
  - [[Pro_SalesPersonBonusLimit]]
  - [[Pro_SalespersonsSendOrders]]
  - [[Pro_SystemCodes]]
  - [[Pro_SystemCodes_Manage]]
  - [[Pro_Territories]]
  - [[Pro_Vacations]]
  - [[Pro_WithdrawAssets]]
  - [[Rpt_BonusTypeForCustomers]]
  - [[Rpt_CashSummary]]
  - [[Rpt_ExpensesTrans]]
  - [[Rpt_SalesPersonCarLink]]
  - [[Rpt_TechnicianVisitDetails]]
  - [[TerritoriesOnlineReport]]
support_relevance: high
last_verified: 2026-10-03
---
# SystemCodes

## Business Purpose
Reference code dictionary mapping integer or string codes to human-readable names across multiple functional subsystems (`SysCodeTypeID`). Queryable via `t.SystemCodes`. Used heavily for UI dropdowns, role distinctions, and reason categories.

**Important:** SystemCodes does **not** store workflow approval statuses (e.g. `WF_MasterLog.LastStatus` or `WF_SubLog.Action`). For workflow lifecycle codes, see [[Workflow_Approval_Codes]].

## Chatbot semantics
(Query `t.SystemCodes` — reference lookup table.)

| User / Arabic intent | SysCodeTypeID | SysCode filter | Notes |
|----------------------|---------------|----------------|-------|
| مشرف مبيعات (Supervisor) | `SalespersonType` | `SysCode = N'3'` | Used on `SalesPersons.SalesPersonType = 3` |
| مندوب مبيعات (Salesman) | `SalespersonType` | `SysCode = N'4'` | Used on `SalesPersons.SalesPersonType = 4` |
| مدير مبيعات / مدير منطقة | `SalespersonType` | `SysCode = N'0'` (Manager), `1` (Area) | Management hierarchy roles |
| أسباب عدم الزيارة | `ReasonType` | `SysCode = N'2'` | Name = 'No Visit Reason' (links to `NoTransactionsReasons`) |
| أسباب عدم البيع | `ReasonType` | `SysCode = N'1'` | Name = 'No Sales Reason' |
| أسباب الإرجاع | `ReasonType` | `SysCode = N'3'` | Name = 'Return Reason' |
| حالة الشيك (راجع) | `CheckStatus` | `SysCode = N'1'` | Name = 'راجع' |
| حالة الشيك (تحويل قضية) | `CheckStatus` | `SysCode = N'2'` | Name = 'تحويل قضية' |

**Do not confuse with:**
- `WF_MasterLog.LastStatus`: 0 (Open), 1 (Approved), 2 (Rejected), 3 (Canceled). These are hardcoded in workflow procs and documented in [[Workflow_Approval_Codes]], not in `SystemCodes`.
- `LogActionTransaction.ActionID`: 0 (CustEntry), 3 (CustLeave), 8 (NoSaleExit), etc. These are action logs decoded in [[LogActions]].

## Key Codebooks (Olives_BO Verified)

### SalespersonType
| SysCode | Name (EN) | Arabic | Role meaning |
|---------|-----------|--------|--------------|
| `0` | Sales Manager | مدير مبيعات | Head of sales |
| `1` | Area Manager | مدير منطقة | Regional manager |
| `2` | Product Manager | مدير منتج | Category manager |
| `3` | Supervisor | مشرف | Field supervisor (manages salesmen team) |
| `4` | Salesman | مندوب | Route salesperson |
| `5` | Promoter | مروّج | Promotional staff |
| `6` | Merchandiser | مصفف رفوف | Merchandising staff |
| `7` | Driver | سائق | Delivery driver |
| `8` | Driver Assistant | مساعد سائق | Delivery crew assistant |
| `9` | Controller | مراقب | Audit/compliance inspector |

### ReasonType
| SysCode | Name | Purpose / Target Table |
|---------|------|------------------------|
| `1` | No Sales Reason | Reason when salesman enters customer but creates no sales doc (`NoSaleExit`, ActionID 8) |
| `2` | No Visit Reason | Reason when scheduled customer is skipped; matches `NoTransactionsReasons.ReasonType = 2` |
| `3` | Return Reason | Customer returns reason |
| `4` | Cancel Invoice Delivery Reason | Driver invoice delivery cancellation |
| `5` | Cancel Return Delivery Reason | Return pickup cancellation |
| `6` | Customer Gallary Image Reject Reason | Shelf image audit rejection |

## Grain & keys
Composite PK: (`SysCodeTypeID`, `SysCode`). Master reference table.

## Pipeline
Populated by back-office administration screens (`Pro_SystemCodes_Manage`). Synchronized to mobile devices for form selections.

## Related
- [[SalesPersons]]
- [[NoTransactionsReasons]]
- [[NoTransactionsLog]]
- [[Workflow_Approval_Codes]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| SysCodeTypeID | nvarchar | YES | ✓ |  |  |
| SysCode | nvarchar | YES | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| CanEdit | bit | YES |  |  |  |
## Primary Key
SysCodeTypeID
SysCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (22):**
- [[Pro_AssetTransfer]]
- [[Pro_AssetsDefinition]]
- [[Pro_CustomersAndAssets]]
- [[Pro_DeliveryAssigning]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryInvoiceAssigning]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_OT_Layout_Setting]]
- [[Pro_ReceiptRequestsSchedule]]
- [[Pro_SalesPersonBonusLimit]]
- [[Pro_SalespersonsSendOrders]]
- [[Pro_SystemCodes]]
- [[Pro_SystemCodes_Manage]]
- [[Pro_Territories]]
- [[Pro_Vacations]]
- [[Pro_WithdrawAssets]]
- [[Rpt_BonusTypeForCustomers]]
- [[Rpt_CashSummary]]
- [[Rpt_ExpensesTrans]]
- [[Rpt_SalesPersonCarLink]]
- [[Rpt_TechnicianVisitDetails]]
- [[TerritoriesOnlineReport]]

**Writes (1):**
- [[Pro_SystemCodes_Manage]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
