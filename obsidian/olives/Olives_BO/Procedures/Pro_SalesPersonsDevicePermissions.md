---
type: procedure
database: Olives_BO
name: Pro_SalesPersonsDevicePermissions
schema: dbo
tags: [#auth, #backoffice, #sales]
reads_from:
  - [[DeviceReportsList]]
  - [[SalesPersonsDevicePermissions]]
  - [[SalesPersonsDeviceReportsPermissions]]
  - `dbo`
writes_to:
  - [[SalesPersonsDevicePermissions]]
  - SalesPersonsDevicePermissionsLog
  - [[SalesPersonsDeviceReportsPermissions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Salesman-Onboarding
---
# Pro_SalesPersonsDevicePermissions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads DeviceReportsList, SalesPersonsDevicePermissions, SalesPersonsDeviceReportsPermissions, dbo. Writes SalesPersonsDevicePermissions, SalesPersonsDevicePermissionsLog, SalesPersonsDeviceReportsPermissions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PositionsID INT = null
- @UserName nvarchar(20) = null
- @Password nvarchar(20) = null
- @UseDefaultUnit bit = null
- @ChangePrice bit = null
- @MakeOrderTaking bit = null
- @MakeTransferOrder bit = null
- @MakeSalesInvoice bit = null
- @MakeReturnSales bit = null
- @MakeReceipt bit = null
- @AllowCons bit = null
- @AllowCustStock bit = null
- @AllowChangeOrderStore bit = null
- @AllowChangeOrderBusUnit bit = null
- @AllowChangeOrderDocType bit = null
- @AllowChangeOrderCustName bit = null
- @AllowMakeBonus bit = null
- @AllowAddCust bit = null
- @AllowGetCustGPS bit = null
- @AllowItemDisc bit = null
- @AllowVouDisc bit = null
- @UseMultiStoreInSales bit = null
- @VouDiscLimit int = null
- @UseBarcodeForCustLogin bit = null
- @CanceledInvoiceNo int = 0
- @cmdType varchar(50)=null
- @MinTotalOfSalesVou float=null
- @CheckCreditLimitInOrder bit=null
- @AmendChangeCashCreditInInvoice bit = null
- @AmendChangeCashCreditInRetInvoice bit = null
- @CashOnlyInvoice bit = null
- @CreditOnlyReturnInvoice bit = null
- @AllowCompetitiveItems bit = null
- @AllowAddDrawer bit = null
- @MaxDiscountPerc float = null
- @FromPosition int = null
- @ToPosition int = null
- @AllowReturnOrder bit = null
- @AllowItemsReplacement bit = null
- @AllowChangePriceInReturn bit = null
- @AllowSalesQuotation bit = null
- @AllowAddProspectiveCustomer bit = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
- @AllowItemDiscInReturn bit  = null
- @AllowVouDiscInReturn bit = null
- @AllowMakeIssueItems bit = null
- @AllowDebitCreditNote bit = null
- @PrID int = null
- @AllowUnloadOrder bit = null
## Tables Read
- [[DeviceReportsList]]
- [[SalesPersonsDevicePermissions]]
- [[SalesPersonsDeviceReportsPermissions]]
- `dbo`
## Tables Written
- [[SalesPersonsDevicePermissions]]
- SalesPersonsDevicePermissionsLog
- [[SalesPersonsDeviceReportsPermissions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[DeviceReportsList]]
- [[SalesPersonsDevicePermissions]]
- [[SalesPersonsDeviceReportsPermissions]]
- dbo

**Tables Written**
- [[SalesPersonsDevicePermissions]]
- SalesPersonsDevicePermissionsLog
- [[SalesPersonsDeviceReportsPermissions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
