---
type: table
database: Olives_BO
name: SalesOrderHistoryHF
schema: dbo
tags: [#backoffice, #log, #order, #sales]
foreign_keys:
referenced_by:
  - [[Alpha_Integ]]
  - [[Alpha_Integ_HistData]]
  - [[Alpha_updateRoute]]
  - [[Awtar_Integ_AllUsers]]
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[GetSalesOrdersForApiReport_GCI]]
  - [[GetSalesOrdersForOnlineReport]]
  - [[GetSalesOrdersForOnlineReport_GCI]]
  - [[NPF_IntegrationHisData]]
  - [[Niroukh_Integ_AllUsers]]
  - [[Online_RptSalesOrderStatusInERP]]
  - [[Pro_DeliveryAssigning]]
  - [[Rpt_DailyDriver]]
  - [[Rpt_DailyUnit]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_NumericDistribution]]
  - [[SAP_Integ_Lamis]]
  - [[Spartan_SAP_Integ_draft]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesOrderHistoryHF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salesorderhistoryhf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| OrderState | smallint | YES |  |  |  |
| Reason | smallint | YES |  |  |  |
| OrderStateDesc | varchar | YES |  |  |  |
| ReasonDesc | varchar | YES |  |  |  |
| PO_No | varchar | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| OrderDeliveryDate | smalldatetime | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (15):**
- [[Alpha_Integ_HistData]]
- [[Awtar_Integ_AllUsers]]
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[GetSalesOrdersForApiReport_GCI]]
- [[GetSalesOrdersForOnlineReport]]
- [[GetSalesOrdersForOnlineReport_GCI]]
- [[NPF_IntegrationHisData]]
- [[Niroukh_Integ_AllUsers]]
- [[Online_RptSalesOrderStatusInERP]]
- [[Pro_DeliveryAssigning]]
- [[Rpt_DailyDriver]]
- [[Rpt_DailyUnit]]
- [[Rpt_MasterOrders]]
- [[Rpt_NumericDistribution]]
- [[Spartan_SAP_Integ_draft]]

**Writes (6):**
- [[Alpha_Integ]]
- [[Alpha_Integ_HistData]]
- [[Alpha_updateRoute]]
- [[Awtar_Integ_AllUsers]]
- [[Niroukh_Integ_AllUsers]]
- [[SAP_Integ_Lamis]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Role**: archived twin of SalesOrderDeliveryHF (identical shape); query here for closed periods
## Tenancy

Both tables surface as `t.` views scoped via their `CompNo` column (= `SESSION_CONTEXT(N'CompanyID')`; proven live: company 1 sees 2 of SalesOrderHistoryDF's SalesOrderHistoryHF rows). `CompNo` holds the company id.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
