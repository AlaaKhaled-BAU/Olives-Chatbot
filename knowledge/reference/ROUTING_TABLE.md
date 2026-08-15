# Routing Table — Olives Knowledge Graph

> Generated from codebase-memory-mcp graph (3428 nodes, 2870 edges)

---

## Graph Overview

| Metric | Value |
|---|---|
| Node labels | Section (2443), Route (489), Folder (245), Variable (92), File (69), Module (59), Channel (28), Decorator (2), Project (1) |
| Edge types | DEFINES (2594), CONTAINS_FOLDER (213), CONTAINS_FILE (62), HANDLES (1) |
| Languages | SQL (9 files) |
| Modules | 59 markdown/JS modules |
| Routes | 489 HTTP/regex route definitions |
| Files indexed | 65 |

---

## 1. Structural Hubs (Folders)

Most-connected container nodes. Entry points to navigate the codebase.

| Rank | Node | Degree | Path | What It Contains | Use When |
|---|---|---|---|---|---|
| 1 | `tinymce/plugins` | 44 | `olives/Olives/vendors/tinymce/plugins/` | 40+ TinyMCE plugins (advlist, anchor, autolink, charmap, code, link, lists, media, paste, table, etc.) | Browsing/extending rich-text editor capabilities |
| 2 | `vendors` | 33 | `olives/Olives/vendors/` | All 3rd-party JS/CSS vendors (bootstrap, chart, echarts, leaflet, tinymce, swiper, dayjs, flatpickr, lodash, etc.) | Understanding front-end dependency surface |
| 3 | `plugins` | 24 | `olives/Olives/plugins/` | UI plugins (ckeditor, datatables+11 extensions, chartjs, select2, datepicker, fullcalendar, flot, jvectormap, etc.) | Locating UI widget integrations |
| 4 | `front-office` | 17 | `front-office/` | 16 salesman-facing guides | Understanding front-line workflows |
| 5 | `back-office` | 16 | `back-office/` | 15 admin guides | Understanding admin/management workflows |
| 6 | `assets` | 9 | `olives/Olives/assets/` | CSS, JS, images, DataTables, ChartsJS, login theme, fonts | Locating static front-end resources |
| 7 | `olives/Olives` | 9 | `olives/Olives/` | Root of the web app (assets, plugins, vendors, bootstrap, scripts, styles) | Top-level entry to the web application |
| 8 | `support-agent` | 8 | `support-agent/` | AGENT.md, database_mapping, diagram, orchestrator, system_options_guide, workflow_guide, 5 tickets | Navigating support agent documentation |
| 9 | `db` | 6 | `db/` | SQL database files (OSFA_DB.sql, Olives_BO.sql, new_procedures/) | Finding database schema and migration scripts |
| 10 | `.obsidian` | 6 | `obsidian/olives/.obsidian/` | Obsidian vault config (workspace, app, appearance, core-plugins, graph, app.json) | Configuring the Obsidian note-taking environment |

---

## 2. Content Hubs (Files)

Files with the most graph connections — read these first.

| Rank | File | Degree | What It Defines | Connected To |
|---|---|---|---|---|
| 1 | `obsidian/.obsidian/workspace.json` | 43 | Obsidian workspace layout | Obsidian modules graph |
| 2 | `note.md` | 37 | **OSFA↔BO table mapping & data flow bible** — 36 sections covering TransactionsHeaders/Details, OrdersHeaders/Details, OT_InvoiceHF/DF mapping, state machines, bidirectional sync cycle | The entire core data model |
| 3 | `obsidian/.obsidian/core-plugins.json` | 33 | 30 Obsidian core plugin toggles | 30 Variable nodes per plugin toggle |
| 4 | `support-agent/database_mapping.md` | 22 | DB table-to-concept mapping (Customers, GPS, SalesPersons, Transactions, Orders, Checks, Exceed Request, System Options) | Section entities across the data layer |
| 5 | `support-agent/system_options_guide.md` | 15 | System Options troubleshooting guide — 12 categories (GPS, Pricing, Invoicing, Returns, Promotions, Payments, Stock, Printer, Security, General Sync) | Ticket and workflow sections |
| 6 | `support-agent/diagram.md` | 13 | Technical support process flow & sample case walkthrough — 5 stages (Extraction, Category Routing, Diagnostics, Solution Design, Response) | Orchestrator and AGENT modules |
| 7 | `support-agent/orchestrator.md` | 13 | Support orchestrator workflow — Universal Diagnostic Loop + 3 categories (UX, DB, DEV) + data alteration safety protocol | AGENT.md, tickets, diagrams |
| 8 | `tables summary.md` | 10 | **OSFA↔BO Table Mapping Summary** — 8 sections with column-level mapping for each table pair | Back-office and front-office guides |
| 9 | `support-agent/AGENT.md` | 10 | Support AI agent profile & operating instructions — 8 sections (architecture, sync flow, concepts, directory layout, operating instructions, rules, data-altering policy) | All other support-agent modules |
| 10 | `procedures.md` | 8 | 6 SQL stored procedure excerpts (OT_PriceList, OT_PromotionsGroupsCustomersLink, OT_SystemOptions insert, etc.) | DB scripts and tickets |
| 11 | `support-agent/tickets/ticket_0002.md` | 17 | New Items Missing in Front Office Custody Loading (Upload Order) — 6 hypotheses with verification queries | Root note, procedures, database_mapping |
| 12 | `support-agent/tickets/ticket_0003.md` | 14 | Edit Invoice Printing Font on Salesman Printer — 3-step solution (identify LayoutId, update Font, sync tablet) | system_options_guide |

### Root-Level Documentation Files

| File | Label | Purpose |
|---|---|---|
| `OLIVES USER GUIDE_2021Updated2025.md` | Module | Full user guide (back-office + front-office) |
| `Olives SQL_Documentation.md` | Module | SQL schema documentation |
| `system option explained.md` | Module | System options explained reference |
| `note.md` | Module | **Core data model note** — OSFA↔BO table mapping, state machines, sync cycle |
| `tables summary.md` | Module | **Table mapping summary** — column-level OSFA↔BO mapping for 7 table pairs |
| `procedures.md` | Module | Stored procedures reference |

---

## 3. Domain Modules (by Layer)

### 3.1 note.md — The Core Data Model Reference

The most critical document in the project. 36 sections covering:

| Section Area | Sections | Content |
|---|---|---|
| **BO Tables** | 1–3 | `TransactionsHeaders` (CreditCash, PaymentType, IsVoid), `TransactionsDetails`, Orders vs TransfersOrders distinction |
| **OSFA↔BO Mapping** | 4–9 | Full bidirectional table mapping: `OT_InvoiceHF` ↔ `TransactionsHeaders`, `OT_InvoiceDF` ↔ `TransactionsDetails`, `OT_OrderHF` ↔ `OrdersHeaders`, `OT_ConsOrderHF` ↔ `TransfersOrdersHeaders`, `OT_CustomerMF` ↔ `Customers`+`CustomersFinancialDetails`, `OT_SalesmanMF` ↔ `SalesPersons`, `OT_StoreItemsQty` ↔ Warehouse Stock |
| **Data Flows** | — | Invoice Flow, Order Flow, Transfer Order Flow, Master Data Flow (BO→OSFA), Full Bidirectional Sync Cycle |
| **State Machines** | — | OSFA→BO data flow state machine, Table-by-Table flow |
| **Column Details** | — | Column name conventions, Column mapping details |

### 3.2 Back-Office Modules (`back-office/`)

15 modules — admin/management side of the system.

| Module | File | Purpose |
|---|---|---|
| `agreements` | `back-office/agreements.md` | Customer agreement management |
| `competitive_items` | `back-office/competitive_items.md` | Competitive item tracking |
| `customers` | `back-office/customers.md` | Customer administration |
| `dashboards` | `back-office/dashboards.md` | Dashboard & KPIs |
| `delivery` | `back-office/delivery.md` | Delivery management |
| `intro` | `back-office/intro.md` | Back-office introduction |
| `items` | `back-office/items.md` | Item/product catalog |
| `promotions` | `back-office/promotions.md` | Promotions & discounts |
| `reports` | `back-office/reports.md` | Reporting & analytics |
| `routes` | `back-office/routes.md` | Sales route planning |
| `salespersons` | `back-office/salespersons.md` | Salesperson management |
| `settings` | `back-office/settings.md` | System settings |
| `transactions` | `back-office/transactions.md` | Financial transactions |
| `users_permissions` | `back-office/users_permissions.md` | User roles & permissions |
| `work_flow` | `back-office/work_flow.md` | Approval workflows |

### 3.3 Front-Office Modules (`front-office/`)

16 modules — salesman-facing mobile workflows.

| Module | File | Purpose |
|---|---|---|
| `add_customer` | `front-office/add_customer.md` | Add customer on the go |
| `alerts` | `front-office/alerts.md` | System alerts & notifications |
| `catalog` | `front-office/catalog.md` | Product catalog browsing |
| `change_printer` | `front-office/change_printer.md` | Bluetooth printer setup |
| `collect_gps` | `front-office/collect_gps.md` | GPS location collection |
| `data_updates` | `front-office/data_updates.md` | Data synchronization |
| `intro` | `front-office/intro.md` | Front-office introduction |
| `item_stock` | `front-office/item_stock.md` | Stock availability check |
| `promotion_list` | `front-office/promotion_list.md` | Active promotions display |
| `reprint_orders` | `front-office/reprint_orders.md` | Order reprinting |
| `salesman_reports` | `front-office/salesman_reports.md` | Salesman daily reports |
| `settings` | `front-office/settings.md` | Device settings |
| `transaction_list` | `front-office/transaction_list.md` | Transaction history |
| `unload_order` | `front-office/unload_order.md` | Upload orders from device to BO |
| `upload_order` | `front-office/upload_order.md` | Download orders/items to device |
| `view_customers` | `front-office/view_customers.md` | Customer lookup |

### 3.4 Support Agent (`support-agent/`)

| Module | File | Purpose | Sections |
|---|---|---|---|
| `AGENT` | `support-agent/AGENT.md` | Support AI agent profile & operating instructions | 8: profile, architecture, sync flow, system concepts, directory layout, operating instructions, rules, data-altering policy |
| `database_mapping` | `support-agent/database_mapping.md` | DB table-to-concept mapping — core tables, schemas, workflow tables, system options sync | 20 sections covering Customers, GPS, SalesPersons, DevicePermissions, Transactions, Orders, ReturnOrders, Checks, Exceed Request, Mobile Options |
| `system_options_guide` | `support-agent/system_options_guide.md` | System Options reference — 12 categories | GPS/Geofencing/Map, Pricing, Invoicing, Returns, Promotions, Payments, Stock, Printer, Security, General/Sync, Options Sync, Categories |
| `orchestrator` | `support-agent/orchestrator.md` | Orchestration flow — Universal Diagnostic Loop + 3 diagnostic categories | 11 sections: UDL, UX processes, DB constraints, DEV bugs, data alteration rules, safety checklist, ticket archiving |
| `diagram` | `support-agent/diagram.md` | Architecture diagrams — lifecycle, flowchart, staged diagnostic walkthrough | 11 sections: 5-stage support lifecycle, mermaid flowchart, sample case walkthrough |
| `workflow_guide` | `support-agent/workflow_guide.md` | Support workflow & diagnostic guide | 4 sections: system criticality warning, end-to-end ticket lifecycle, walkthrough scenarios |

### 3.5 Support Tickets (`support-agent/tickets/`)

| Ticket | File | Issue | Sections |
|---|---|---|---|
| Ticket 0001 | `ticket_0001.md` | Send Data Blocked by `isupdated stock = false` | 1 |
| Ticket 0002 | `ticket_0002.md` | New Items Missing in Front Office Custody Loading (Upload Order) — **6 hypotheses** (missing SalesPersonItemsAssignment, ItemsCategories/Units, SalesPersonItemsBalance filter, Items.IsSuspended, Option 279, Sync not run) | 15 (including chain of causation, verification queries, solution) |
| Ticket 0003 | `ticket_0003.md` | Edit Invoice Printing Font on Salesman Printer — 3-step solution (identify LayoutId, update Font property, sync tablet) | 12 |
| Ticket 0004 | `ticket_0004.md` | User "heba" Cannot Access Customers in CustomerPromotionGroupLink | 4 |
| Ticket 0005 | `ticket_0005.md` | Bonus Report Shows Wrong Values (7 Instead of 107) — references `OT_SalesmanItemBonusTarget` sync procedure | 6 |

### 3.6 Database Layer (`db/`)

#### Raw SQL Files

| File | Contents |
|---|---|
| `db/OSFA_DB.sql` | Main OLTP database schema & stored procedures (187 tables, 205 procs) |
| `db/OSFA_DB6-8-2026.sql` | Updated version as of June 8 2026 |
| `db/Olives_BO.sql` | Back-office database schema (410 tables, 1450 procs) |
| `db/Olives_BO6-8-2026.sql` | Updated version as of June 8 2026 |
| `db/new_procedures/Phenix_NadheerAlSaadi_Integ_Billtype_24.sql` | Integration billing type procedure |

#### Indexed Schema Reference (Column-Level)

Four auto-generated markdown files under `db/` — every table and procedure is indexed as an individual Section node with full column details, PKs, FKs, and cross-references.

| File | Sections | Contents | Cross-References |
|---|---|---|---|
| `db/osfa_tables.md` | 190 | 187 OSFA_DB tables (columns, types, PKs, FKs) | OSFA↔BO mapping table, links to `note.md` |
| `db/osfa_procedures.md` | 207 | 205 OSFA_DB procedures (params, referenced tables) | Procedure→Table reference index |
| `db/bo_tables.md` | 413 | 410 Olives_BO tables (columns, types, PKs, FKs) | BO↔OSFA reverse mapping |
| `db/bo_procedures.md` | 1452 | 1450 Olives_BO procedures (params, referenced tables) | Procedure→Table reference index |

Search any table or procedure with:
```
search_graph(name_pattern=".*TABLE_OR_PROC_NAME.*")
```
Returns the schema section (from `db/`) AND matching documentation sections (from `note.md`, `tables summary.md`, `database_mapping.md`).

Examples:
- `name_pattern=".*OT_INVOICEHF.*"` → table + procs `OT_INVOICEHF_CHECKEXIST`, `OT_INVOICEHF_INSERT`
- `name_pattern=".*SP_CREATEDIAGRAM.*"` → BO procedure
- `name_pattern=".*TransactionsHeaders.*"` → table + doc references

### 3.7 Test Databases (`test-db/`)

| File | Contents |
|---|---|
| `test-db/OSFA_DB.sql` | Test version of OSFA_DB schema |
| `test-db/OSFA_DB_2026.sql` | Test version (2026) |
| `test-db/Olives_BO.sql` | Test version of Olives_BO schema |
| `test-db/Olives_BO_2026.sql` | Test version (2026) |

### 3.8 Stored Procedures (`procedures.md`)

6 procedure excerpts referenced by tickets:

| Procedure | Purpose |
|---|---|
| `OT_PriceList` | Price list sync with timing log |
| `OT_PromotionsGroupsCustomersLink` | Promotion group-to-customer link sync |
| `OT_SystemOptions` (Op_ID=39) | Competitive items system option per salesman |
| (3 additional commented-out procedure patterns) | Various sync operations |

### 3.9 Web Application (`olives/Olives/`)

| Subfolder | Contents |
|---|---|
| `assets/` | CSS, JS, images, DataTables, ChartsJS, login theme, gauge, jquery-validation, animated icons, favicons |
| `plugins/` | ckeditor, datatables (+11 extensions: AutoFill, ColReorder, ColVis, FixedColumns, FixedHeader, KeyTable, Responsive, Scroller, TableTools), chartjs, select2 (+i18n), datepicker (+locales), fullcalendar, flot, jvectormap, morris, pace, slimScroll, sparkline, bootstrap-slider, bootstrap-wysihtml5, colorpicker, daterangepicker, fastclick, iCheck (+6 skins), input-mask (+phone-codes), ionslider, jQuery, jQueryUI, knob, timepicker |
| `vendors/` | tinymce (+themes, skins, icons), bootstrap, echarts, leaflet (+markercluster, tilelayer.colorfilter), swiper, lodash, dayjs, flatpickr, dropzone, choices, simplebar, validator, progressbar, draggable, popper, rater-js, list.js, glightbox, overlayscrollbars, plyr, countup, anchorjs, prism, typed.js, echarts-countries-js, lottie, is, tiny-slider |
| `bootstrap/` | Bootstrap CSS + JS |
| `Scripts/` | Application scripts |
| `Styles/` | Application styles |
| `App_GlobalResources/` | Global resource files |
| `SqlServerTypes/` | SQL Server spatial types |
| `bin/` | Compiled binaries |

### 3.10 Obsidian Vault (`obsidian/olives/`)

| File | Type | Purpose |
|---|---|---|
| `2026-06-20.md` | File | Daily note |
| `Welcome.md` | File + Module | Obsidian welcome page |
| `create a link.md` | File | How-to for creating links |
| `.obsidian/workspace.json` | File (degree 43) | Workspace layout |
| `.obsidian/core-plugins.json` | File (degree 33) | 30 core plugin toggles |
| `.obsidian/graph.json` | File (degree 22) | Obsidian graph view config |
| `.obsidian/app.json` | File | App settings |
| `.obsidian/appearance.json` | File | Appearance/theme settings |

---

## 4. Connection Patterns

### Edge Type Distribution

```
DEFINES (301)        ─── file defines module/section/variable
CONTAINS_FOLDER (213) ─── folder nests subfolder
CONTAINS_FILE (65)   ─── folder contains file
HANDLES (1)          ─── route handled by handler
```

### Graph Traversal Patterns

```
Project → CONTAINS_FOLDER → Folder → CONTAINS_FOLDER → Subfolder
  → CONTAINS_FILE → File → DEFINES → Module → DEFINES → Section
                                          ↓
                                     Variable (config values)
```

### Navigation Rules

| I want to... | Traverse to |
|---|---|
| Understand the core data model | `note.md` (36 sections of OSFA↔BO mapping) |
| Find a table mapping | `tables summary.md` (column-level) or `note.md` (conceptual) |
| Map a column name | `support-agent/database_mapping.md` (21 sections) |
| Diagnose a ticket | `support-agent/tickets/ticket_NNNN.md` → cross-ref `procedures.md` + `system_options_guide.md` |
| Understand support agent flow | `support-agent/AGENT.md` → `orchestrator.md` → `diagram.md` → `workflow_guide.md` |
| Check system option ranges | `support-agent/system_options_guide.md` (12 categories) |
| Browse salesman workflow | `front-office/` (16 modules) |
| Administer the system | `back-office/` (15 modules) |
| Check DB schema | `db/osfa_tables.md`, `db/osfa_procedures.md`, `db/bo_tables.md`, `db/bo_procedures.md` |
| Modify the web app UI | `olives/Olives/` (assets/plugins/vendors) |
| Configure Obsidian | `.obsidian/` (workspace, core-plugins, appearance) |
| Look up any table schema (columns, PK, FKs) | `search_graph(name_pattern=".*TABLE_NAME.*")` — returns section from `db/osfa_tables.md` or `db/bo_tables.md` |
| Find a stored procedure | `search_graph(name_pattern=".*PROC_NAME.*")` — returns section from `db/osfa_procedures.md` or `db/bo_procedures.md` |

---

## 5. Routes (HTTP Endpoints)

489 route definitions extracted — predominantly regex patterns from TinyMCE and other JS libraries (e.g., `/(.)s$/`, `/MMMM|MM|DD|dddd/g`, `/%d/i`, browser user-agent sniffing patterns). Single `HANDLES` edge indicates route-to-handler resolution is limited — routes are defined in JS vendor files rather than a centralized router.

---

## 6. Channels (Event Emitters)

28 event_emitter channels found in the tiny-slider library:

| Channel | Type |
|---|---|
| `indexChanged`, `newBreakpointStart`, `newBreakpointEnd` | Lifecycle |
| `transitionStart`, `transitionEnd` | Animation |
| `touchStart`, `touchMove`, `touchEnd` | Touch events |
| `pointerdown`, `pointermove`, `pointerup` | Pointer events |
| `dragstart`, `dragmove`, `dragend` | Drag events |
| `outerResized`, `innerLoaded`, `_resize` | Layout |
| `select`, `draw`, `data`, `hitupdate` | Interaction |
| `optionsChanged`, `created` | Initialization |

---

## 7. Global Variables

92 variables extracted — predominantly Obsidian core-plugins config toggles: `backlink`, `canvas`, `command-palette`, `daily-notes`, `graph`, `outgoing-link`, `page-preview`, `starred`, `switcher`, `tag-pane`, `templates`, `webviewer`, `sync`, `publish`, `file-recovery`, `workspaces`, `audio-recorder`, `slides`, `word-count`, `outline`, `random-note`, `zk-prefixer`, `markdown-importer`, `bookmarks`, `editor-status`, `slash-command`, `note-composer`, `properties`, `footnotes`, `global-search`.

---

## Quick-Start: Where To Look

| I need to... | Go to |
|---|---|
| Understand OSFA↔BO table mapping | `note.md` or `tables summary.md` |
| Map a specific table column | `support-agent/database_mapping.md` |
| Diagnose a support ticket | `support-agent/tickets/` |
| Understand the support AI agent | `support-agent/AGENT.md` |
| Run the diagnostic workflow | `support-agent/orchestrator.md` |
| See support process diagrams | `support-agent/diagram.md` |
| Check system options reference | `support-agent/system_options_guide.md` |
| Find a stored procedure | `search_graph(name_pattern=".*PROC_NAME.*")` — indexed in `db/osfa_procedures.md` / `db/bo_procedures.md` |
| Look up a table schema (columns, PKs, FKs) | `search_graph(name_pattern=".*TABLE_NAME.*")` — indexed in `db/osfa_tables.md` / `db/bo_tables.md` |
| Read the full user guide | `OLIVES USER GUIDE_2021Updated2025.md` |
| Understand salesman workflow | `front-office/` (16 modules) |
| Administer the system | `back-office/` (15 modules) |
| Browse test databases | `test-db/` (4 SQL files) |
| Modify the web app UI | `olives/Olives/` (assets/plugins/vendors) |
| Configure Obsidian notes | `.obsidian/` (workspace, core-plugins, appearance) |
