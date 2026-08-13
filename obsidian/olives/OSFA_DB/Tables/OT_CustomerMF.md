---
type: table
database: OSFA_DB
name: OT_CustomerMF
schema: dbo
tags: [#customer, #mobile]
foreign_keys:
referenced_by:
  - [[OT_AutoRefreshCustomerInfo]]
  - [[OT_GetImageCustomerMF]]
  - [[servics_app_OSFA_Mobile_Ver]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustomerMF



## Business Purpose


Customer master data on tablet — synced subset of BO Customers table for offline use.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| SalesmanNo | smallint | NO | ✓ |  |  |
| ArName | varchar | YES |  |  |  |
| EngName | varchar | YES |  |  |  |
| PrNo | smallint | YES |  |  |  |
| CustType | smallint | YES |  |  |  |
| CustClass | smallint | YES |  |  |  |
| CreditLimit | money | YES |  |  |  |
| CurrBalance | money | YES |  |  |  |
| ChqsBalance | money | YES |  |  |  |
| GeoLevel1 | int | YES |  |  |  |
| GeoLevel2 | int | YES |  |  |  |
| GeoLevel3 | int | YES |  |  |  |
| GeoLevel4 | int | YES |  |  |  |
| GeoLevel5 | int | YES |  |  |  |
| CustomerBarcode | nvarchar | YES |  |  |  |
| X_COORD | nvarchar | YES |  |  |  |
| Y_COORD | nvarchar | YES |  |  |  |
| PriceLevel | tinyint | YES |  |  |  |
| Due | smallint | YES |  |  |  |
| ChqDue | smallint | YES |  |  |  |
| TaxInclude | bit | YES |  |  |  |
| Tel | varchar | YES |  |  |  |
| Email | varchar | YES |  |  |  |
| CustomerRef1 | nvarchar | YES |  |  |  |
| CreditCash | int | YES |  |  |  |
| AllowChqs | bit | YES |  |  |  |
| ImageID | bigint | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| DiscountPerc | float | YES |  |  |  |
| FullAddress | nvarchar | YES |  |  |  |
| MaxInvoiceValue | float | YES |  |  |  |
| MaxInvoiceCount | int | YES |  |  |  |
| InvoiceCount | int | YES |  |  |  |
| ChqLimit | float | YES |  |  |  |
| CustomerRef2 | nvarchar | YES |  |  |  |
| CustomerRef3 | nvarchar | YES |  |  |  |
| LinkedSalesmanNo | int | YES |  |  |  |
| IsCollectedGPS | bit | YES |  |  |  |
| rk | int | YES |  |  |  |
| Tax_1_Include | bit | YES |  |  |  |
| Tax_2_Include | bit | YES |  |  |  |
| Group_ID | int | YES |  |  |  |
| StartVisitTime | nvarchar | YES |  |  |  |
| EndVisitTime | nvarchar | YES |  |  |  |
| HaveTrans | int | YES |  |  |  |
| ContactPerson | varchar | YES |  |  |  |
| TaxNum | varchar | YES |  |  |  |
| CustTargetTot | float | YES |  |  |  |
| CustSalesTot | float | YES |  |  |  |
| TakedSurveyIDs | varchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| AllowDiscount | bit | YES |  |  |  |
| EarlyRepaymentDiscountPerc | float | YES |  |  |  |
| PaymentTypeID | int | YES |  |  |  |
| DiscountEarlyPayDays | int | YES |  |  |  |
| VisitActivityInOrder | nvarchar | YES |  |  |  |
| CustStatusDesc | varchar | YES |  |  |  |
| AssetsRef1 | nvarchar | YES |  |  |  |
| AssetsRef2 | nvarchar | YES |  |  |  |
| DeliveryDays | int | YES |  |  |  |
| CashDiscount | float | YES |  |  |  |
| CurrencyID | int | YES |  |  |  |
| WorkingDays | nvarchar | YES |  |  |  |
| ReturnCreditLimit | float | YES |  |  |  |
| ReturnBalance | float | YES |  |  |  |
| IsWFSuspended | bit | YES |  |  |  |
| SalesOrderLimit | float | YES |  |  |  |
## Primary Key
CompNo
CustomerNo
SalesmanNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_AutoRefreshCustomerInfo]]
- [[OT_GetImageCustomerMF]]
- [[servics_app_OSFA_Mobile_Ver]]

**Writes (1):**
- [[OT_AutoRefreshCustomerInfo]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization


## See also
- [[Olives_BO/Tables/Customers]] (Back Office counterpart table)

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
