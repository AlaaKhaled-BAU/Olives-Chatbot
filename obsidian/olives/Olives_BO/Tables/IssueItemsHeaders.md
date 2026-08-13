---
type: table
database: Olives_BO
name: IssueItemsHeaders
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - [[SalesPersons]]
referenced_by:
  - [[GetIssueItemsForOnline]]
  - [[OT_ImportSalesIssueItems]]
support_relevance: high
last_verified: 2026-07-05
---
# IssueItemsHeaders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores issueitemsheaders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| OrderYear | int | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| PriceListID | int | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| CurrencyID | smallint | YES |  | ✓ | [[Currencies]] |
| ExchangeRate | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| WFApproved | bit | YES |  |  |  |
| Approved | bit | YES |  |  |  |
| DocumentsTypesID | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| BusinessUnitID | int | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| IsVoid | bit | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ContractID | nvarchar | YES |  |  |  |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| IsPostBackOrder | bit | YES |  |  |  |
| IsPostBackOrderToERP | bit | YES |  |  |  |
| CreditCash | int | YES |  |  |  |
| PostedByEmail | bit | YES |  |  |  |
| AcceptDate | smalldatetime | YES |  |  |  |
| DetailCount | int | YES |  |  |  |
| DeliveryBatchID | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| ExtraNote | nvarchar | YES |  |  |  |
| IsDelivered | bit | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| BackOrderYear | smallint | YES |  |  |  |
| BackOrderNo | bigint | YES |  |  |  |
| FinalApproval | bit | YES |  |  |  |
| PostedToERPDateTime | smalldatetime | YES |  |  |  |
| UsedInAutoUploadOrder | bit | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| MakeCashDiscount | bit | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CurrencyID -> [[Currencies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[GetIssueItemsForOnline]]

**Writes (1):**
- [[OT_ImportSalesIssueItems]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
