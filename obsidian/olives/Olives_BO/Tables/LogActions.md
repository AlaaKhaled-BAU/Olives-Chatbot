---
type: table
database: Olives_BO
name: LogActions
schema: dbo
tags: [#backoffice, #log]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-08-28
---
# LogActions


## Business Purpose

L1 codebook for `LogActionTransaction.ActionID` (`lookup_hot` table `LogActions` or `LogActionTransaction`).

**Not workflow:** tablet **approvals** use [[WF_SubLog]] / [[WF_MasterLog]] (`Action`, `LastStatus`) — see [[Workflow_Approval_Codes]]. Field log uses **this** table only.

Join `t.LogActions.ActionId` = `t.LogActionTransaction.ActionID`. No event rows here — facts live in [[LogActionTransaction]] (imported by [[OT_ImportActionLog]]).

### Visit / discipline (most common chatbot questions)

| ActionId | ActionDesc | User Arabic hint |
|----------|------------|------------------|
| 0 | CustEntry | دخول زبون — **عدّ كزيارة فعلية** |
| 3 | CustLeave | خروج من الزبون |
| 7 | SystemLogin | فتح التطبيق — **ليس زيارة زبون** |
| 8 | NoSaleExit | خروج بدون بيع |
| 21 | Will Not Visit Customer | لن يزور الزبون |
| 31 | Postpone Visit | تأجيل زيارة |
| 38 | No Visit Reason By Import\\Export | سبب عدم زيارة (استيراد) |
| 2 | NoGPSEntry | دخول بدون GPS |
| 10 | StartJourney | بداية جولة |
| 11 | EndJourney | نهاية جولة |

Document actions: 4 InvoiceIssue, 5 OrderIssue, 9 ReturnInvoiceIssue, 12 PaymentIssue — `Data1`/`Data2` are doc year/number on the log row, not customer id (see [[LogActionTransaction]]).

### Full codebook (live BO)

| ActionId | ActionDesc |
|----------|------------|
| 0 | CustEntry |
| 1 | NoBarcodeEntry |
| 2 | NoGPSEntry |
| 3 | CustLeave |
| 4 | InvoiceIssue |
| 5 | OrderIssue |
| 6 | SystemExit |
| 7 | SystemLogin |
| 8 | NoSaleExit |
| 9 | ReturnInvoiceIssue |
| 10 | StartJourney |
| 11 | EndJourney |
| 12 | PaymentIssue |
| 13 | Retrun Order |
| 14 | ProspectiveCustEntry |
| 15 | ProspectiveCustLeave |
| 16 | SalesQuotationIssue |
| 17 | Data Update |
| 18 | Clear Data |
| 19 | AccountBlock |
| 20 | LogIn Failed |
| 21 | Will Not Visit Customer |
| 22 | Change Settings |
| 23 | Salesman Stock Approve |
| 24 | Cust Login GPS Faild |
| 25 | Change Salesman To Other Salesman |
| 26 | Customer Stock |
| 27 | PaymentIssueWithSettelment |
| 28 | Send Invoice Delivery Via BT |
| 29 | Recieve Invoice Delivery Via BT |
| 30 | Add Notes For Customer |
| 31 | Postpone Visit |
| 32 | Use Sales Order In Upload Order |
| 33 | Survey |
| 34 | Take Photo In Cust Galary |
| 35 | Invoice Delivery |
| 36 | Return Delivery |
| 37 | Delivery Visit Trans Count |
| 38 | No Visit Reason By Import\\Export |
| 39 | LoadOrder |
| 40 | UnLoadOrder |
| 41 | Admin Login In Tablet |
| 42 | StartFromCompany |
| 43 | EndToCompany |
| 44 | StartUnload |
| 45 | Open Cash |
| 46 | Close Cash |
| 47 | Printer Status |
| 48 | Open Cash Drawer |
| 49 | Pending Invoice JSON Data |
| 50 | Categ Stock |
| 51 | Note For Auto Open Activity |

`SystemCodes` **`ReasonType`** code `2` = "No Visit Reason" labels rows in [[NoTransactionsReasons]] — use with no-visit **actions** above, not with WF `Action`/`LastStatus`.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ActionId | nvarchar | YES | ✓ |  |  |
| ActionDesc | varchar | YES |  |  |  |
## Primary Key
ActionId
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[PromotionsApprovalLog]]
- [[OWGM_LockLog]]
- [[TransfersOrdersDetails_ErrorQty]]
