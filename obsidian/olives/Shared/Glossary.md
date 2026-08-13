---
type: shared
name: Glossary
tags: [#reference, #shared]
---
See also: [[_MOC-Olives_BO|Olives_BO Index]] | [[_MOC-OSFA_DB|OSFA_DB Index]] | [[_MOC-Workflows|Workflows Index]]

# Glossary

## Core Terms
| Term | Definition |
|------|------------|
| BO | Back Office — server-side management system (Olives_BO database) |
| OSFA | Olives Field Automation — Android tablet app (OSFA_DB database) |
| DSD | Direct Store Delivery — route-based sales model where salesperson visits customers on a fixed route |
| Tablet | Android device running the OSFA app, used by field salespersons |
| Sync | Data synchronization between OSFA tablet (OSFA_DB) and BO server (Olives_BO) |
| Route | Assigned sequence of customer visits for a salesperson on a given day |
| WF | Workflow — multi-level approval process for overrides, exceptions, and special requests |
| Load | Transfer of inventory from warehouse to salesperson's van/vehicle |
| Unload | Return of unsold/undelivered inventory from van to warehouse |
| Settlement | End-of-day reconciliation of sales, returns, cash, and inventory |
| Integration | Data exchange between Olives BO and external ERP systems (SAP, AX, GP, etc.) |
| Master Data | Core reference data (customers, items, prices) synced from BO to tablet |
| Transaction Data | Daily operations (invoices, orders, payments) created on tablet and posted to BO |
| IsPosted | Flag indicating whether a tablet transaction has been successfully synced to BO |
| ZATCA | Zakat, Tax and Customs Authority — Saudi tax compliance (e-invoicing) |

## Workflow Terms
| Term | Definition |
|------|------------|
| Onboarding | End-to-end process of configuring a new salesman (position, permissions, items, customers, routes, price list, send data) |
| Load Order | Transaction to transfer inventory from warehouse to salesman's van |
| Unload Order | Transaction to return unsold inventory from van to warehouse |
| Return Sales | Customer returns previously invoiced goods (creates credit transaction) |
| Return Order | Cancel an unfulfilled sales order before delivery |
| Back Order | Reverse a completed sales order (undo) |
| WF | Workflow — multi-level approval chain for salesman override requests |
| KPI | Key Performance Indicator — gauge-based dashboard comparing actual vs target |
| Send Data | BO→Tablet sync of master data (customers, items, prices, routes, permissions) |
| Data Update | Tablet→BO sync of transactions (invoices, orders, payments, stock counts) |
| POS Route | Salesman position + route day/week schedule — determines which customers visited which day |
| GPS Login | Tablet enforces salesman must be at customer's GPS coordinates to log into that customer |
| Journey | Salesman's daily work session: start→visits→transactions→end→sync |
| Suggested Order/Invoice | Auto-generated transaction based on customer historical purchase patterns |
| Basket | Virtual shopping cart in catalog: browse items → add to basket → proceed to order or invoice |
| Round Type | How promotion fractional output quantities are handled: Down (floor), Up (ceiling), Standard (≥0.5 rounds up) |

## Database Abbreviations
| Prefix | Meaning | Example |
|--------|---------|---------|
| OT_ | OSFA Tablet | OT_INVOICEHF — invoice header on tablet |
| MMS_ | Maintenance Management System | MMS_ORDERSHEADER — maintenance orders |
| WF_ | Workflow | WF_SETUPHEADER — workflow configuration |
| RPT_ | Report | RPT_DAILYSALES — report stored procedure |
| PRO_ | Procedure (CRUD) | PRO_CUSTOMERS — customer management |
| AZOT_ | Additional OSFA config | AZOT_SystemOptions — legacy config |

## Common Acronyms
| Acronym | Full Form                                            |
| ------- | ---------------------------------------------------- |
| HF/DF   | Header File / Detail File (header-detail table pair) |
| FK      | Foreign Key                                          |
| PK      | Primary Key                                          |
| CRUD    | Create, Read, Update, Delete                         |
| ERP     | Enterprise Resource Planning                         |
| VouNo   | Voucher Number                                       |
| VouType | Voucher Type                                         |
| WF      | Workflow                                             |
| BUS     | Business Unit                                        |
| SOA     | Statement of Account                                 |

## Related

- [[OSFA_DB/Tables/OT_GeoLevel5]]
- [[OSFA_DB/Tables/OT_SystemOptionsLists]]
- [[OSFA_DB/Tables/OT_GeoLevel3]]
- [[OSFA_DB/Tables/OT_JsonLog_Tmp]]
- [[OSFA_DB/Tables/OT_GeoLevel2]]
- [[OSFA_DB/Tables/OT_GeoLevel4]]
- [[OSFA_DB/Tables/OT_Actions]]
- [[OSFA_DB/Procedures/OT_DirectInvoice]]
- [[Olives_BO/Tables/Tech_CustomizationPerformedTasks]]
- [[Olives_BO/Tables/CustomersFinancialDetails2]]
- [[Olives_BO/Tables/forupdateonly]]
- [[Olives_BO/Tables/MultiTargets]]
- [[Olives_BO/Tables/MMS_ShowRooms]]
- [[Olives_BO/Tables/Clients]]
- [[Olives_BO/Tables/Pos_InvoiceOrderHF]]
- [[Olives_BO/Tables/CustomerSalesByCategory]]
- [[Olives_BO/Tables/CustomersReturnItemQtyLimit]]
- [[Olives_BO/Tables/ItemsSuggestGroupLinkWithItems]]
- [[Olives_BO/Tables/SalesPersonItemsBalanceBatches]]
- [[Olives_BO/Tables/SpecialCustomerTarget]]
- [[Olives_BO/Tables/Customers2]]
- [[Olives_BO/Tables/EmpDetails]]
- [[Olives_BO/Tables/ClientsWFID]]
- [[Olives_BO/Tables/ItemsInventory]]
- [[Olives_BO/Tables/MMS_DV_ErrorLog]]
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
- [[Olives_BO/Procedures/SMSSEND_ZUMOT]]
- [[Olives_BO/Procedures/Test_Banks]]
- [[Olives_BO/Procedures/Alpha_GetCurrRate]]
- [[Olives_BO/Procedures/PRO_REPORT]]
- [[Olives_BO/Procedures/Rpt_Hakkak_TargetReportFromAlpha]]