---
type: table
database: Olives_BO
name: PriceLists
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[Pro_CustomersPromotionsGroupsLink]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_ImportData]]
  - [[Pro_ImportPriceListData]]
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxApiFromOSFA]]
  - [[Pro_JoTaxApiFromOSFA____]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_PriceListDetails]]
  - [[Pro_PriceLists]]
  - [[Pro_ProspectiveCustomers]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Pro_SalesQuotationHeaders]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_TransactionsHeaders]]
  - [[Rpt_AcceptedSalesInvoices]]
  - [[Rpt_CustomersPriceLists]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_NewCustomer]]
  - [[Rpt_ProspectiveCustomer]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_SalesmanItemsSales]]
  - [[Rpt_SalesmanRouteDetails]]
  - [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
  - [[Rpt_UPriceReport]]
support_relevance: high
last_verified: 2026-10-03
related_workflows:
  - Customer-Setup
  - Items-Master-Data-Setup
  - PriceList-Management
  - Promotion-Setup
  - Salesman-Onboarding
---
# PriceLists

## Business Purpose
The master price list header table — defines commercial pricing tiers (e.g. Retail, Wholesale, Key Accounts, Cash Van). Provides header validity dates (`StartDate`, `EndDate`) and descriptive names (`Name`). Individual product prices under each price list live in [[PriceListDetails]]. Bound to customers via `CustomersFinancialDetails.PriceListID`. Queryable via `t.PriceLists`.

## Chatbot semantics
(Query `t.PriceLists` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| قوائم الأسعار | `ID`, `Name` | `Name LIKE N'%...%'` OR `ID = ...` | Price list tiers |
| أسعار المواد في القائمة | Join `t.PriceListDetails` | `d.PriceListID = p.ID` | Specific item selling prices |
| قائمة أسعار العميل | Join `t.CustomersFinancialDetails` | `cfd.PriceListID = p.ID` | Price tier assigned to customer |
| صلاحية قائمة الأسعار | `StartDate`, `EndDate` | Date checks | Active period of price tier |

## Grain & keys
- **Composite PK**: (`CompanyID`, `ID`)
- **Tenant key**: `CompanyID`

## Pipeline
Managed via Back Office pricing setup screens (`Pro_PriceLists`). Synced to mobile devices for calculating invoice item rates.

## Related
- [[PriceListDetails]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[TransactionsHeaders]]
- [[OrdersHeaders]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| CurrencyID | smallint | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (48):**
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]
- [[Pro_MapTransactionLog]]
- [[Pro_OrdersHeaders]]
- [[Pro_PriceListDetails]]
- [[Pro_PriceLists]]
- [[Pro_ProspectiveCustomers]]
- [[Pro_ReturnOrdersHeaders]]
- [[Pro_SalesQuotationHeaders]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_TransactionsHeaders]]
- [[Rpt_AcceptedSalesInvoices]]
- [[Rpt_CustomersPriceLists]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_NewCustomer]]
- [[Rpt_ProspectiveCustomer]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_SalesmanItemsSales]]
- [[Rpt_SalesmanRouteDetails]]
- [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
- [[Rpt_UPriceReport]]

**Writes (60):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_PriceLists]]

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
