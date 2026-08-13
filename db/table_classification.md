# Table classification (C0, 2026-07-26)

`db/02_tenant_views.sql` only builds a `t.` view for tables with a literal `CompanyID`
column. 60 of morec's 404 tables have none, and `schema_cache.json` lists all 404
regardless — so `introspect_schema` was advertising 60 tables the agent could
introspect but never query, a guaranteed dead-end (see FIXPLAN's MAX_TURNS 6→12 note,
likely caused by exactly this).

Classified all 60 by hand (name + full column list), not by pattern-matching the name
alone — several names lie (`CustomerData_Sample` has a real `CompNo` column but is
almost certainly demo data; `Table_2` has `Compno` too but the generic name is itself
a red flag). Three buckets:

## 1. Global reference data — unscoped `t.` view (safe, no tenant-varying data)

Pure lookup/config tables verified to carry no per-company rows at all (ID+Name/Desc
shape, or system-wide UI config):

`ActivityList`, `CustomerLoginActions`, `DeviceReportsList`, `ExcelReports`,
`Language`, `LanguageDictionary`, `LogActions`, `Menu`, `MIMETypes`,
`MMS_MaintenanceTechnicianPermissions_Def`, `MMS_OrderStatus`, `OlivesMenu`,
`OlivesPages`, `PromotionTypes`, `SystemCodes`, `TargetsTypes`, `TransactionsTypes`,
`WF_Functions`, plus `Currencies` (already had a bespoke `Companies`-style single-PK
view convention to follow).

## 2. Tenant data under a different column name — scoped `t.` view via `CompNo`/`Compno`/`compno`

Same `CompNo`/`CompanyID` interchangeability already documented in project memory
(`params.py`'s own resolution logic treats them as the same concept). These are real
business tables that just happened to predate whatever later convention settled on
`CompanyID`:

`CustomerChqList`, `CustomerReceivablesInfo`, `CustomerSalesByCategory`,
`DebitCreditNoteTrans`, `DeliveryRoute`, `InvoiceDeliveryDF`, `InvoiceDeliveryHF`,
`InvoiceHistoryDF`, `InvoiceHistoryHF`, `LogActionTransaction`,
`LogActionTransaction_` (legacy duplicate, harmless to include), `Pos_InvoiceOrderHF`,
`SalesOrderDeliveryDF`, `SalesOrderDeliveryHF`, `SalesOrderHistoryDF`,
`SalesOrderHistoryHF`, `Themar`, `TransactionsSuggestedItems`.

**`InvoiceHistoryHF`/`DF` and `SalesOrderHistoryHF`/`DF` are exactly the tables the
period-over-period sales use case (Phase 8 / C4) needs** — this bucket is a hard
prerequisite for that eval, not just cleanup.

## 3. Must stay blocked — no view built, `introspect_schema` must not list them either

- **`Clients`, `ClientsWFID`** — cross-client directories (the actual base tables list
  every other client). Blocking these is exactly right, unchanged from before C0.
- **`Users`** — has `UserPWD`. Never.
- **`Tech_CustomizationPerformedTasks`** — has `ClientID`/`ClientName`: this is
  Olives' own internal support-ops log of which customization was done for which
  *other* client. Cross-client confidentiality risk, same class as the `Clients`
  table, just less obviously named.
- **`IntegrationErrorLog`, `MMS_DV_ErrorLog`** — both have a company-scoping column
  (`CompanyCode`/`CompNo` respectively) and technically *could* be scoped, but their
  content is raw system diagnostics (`JsonData`, `ErrorMsg`, stack-trace-shaped
  text) — not appropriate for a customer-facing chat surface regardless of whose
  data it is. Same principle as never exposing proc bodies: internal implementation
  detail, not business data.
- **`MultiTargets`, `CustomersSalesFrom0toMax`, `SpecialCustomerTarget`, `OLV_PDC`,
  `KasihSurvey`** — genuinely real business data (sales targets, customer sales
  totals, post-dated checks, customer survey photos) with **no tenant-scoping
  column of any kind** — checked their full column lists, not just the first few.
  These can't be safely exposed at all without a real per-row tenant key; not a
  cleanup item, a standing gap. Do not "fix" by guessing a join path — verify one
  exists first if this is ever revisited.
- **`CustomerData_Sample`** — has `CompNo`, but the name says "Sample" and the
  columns (`CompNo`, `CustID`, `postion` — sic) are too thin to be real production
  data. Blocked despite technically being scopable.
- **`Table_1`, `Table_2`, `Table_3`, `Table_4`, `Excel`, `Excel2`, `temptax`, `trn`,
  `trn2`, `forupdateonly`** — scratch/staging tables by name and shape.
  `Table_2`/`forupdateonly` technically have a `Compno` column but the generic/
  scratch naming is itself the disqualifying signal, not the schema shape.

## Second client checked (rukn) — confirms the design, surfaces its own gaps honestly

Ran the same classification logic against rukn's schema (`chatbot_db2`, genuinely
different shape from morec — 410 vs 404 tables, no shared table-name assumption
relied on anywhere in this design). Also landed on 22 blocked tables — a coincidence
in the *count*, not the *set*: rukn is missing several morec-only scratch tables
(`Table_2/3/4`, `temptax`, `trn`, `trn2` don't exist in rukn's image at all) but has
6 tables that don't exist in morec's, none of which were individually reviewed the
way the 22 above were:

- **`ProcedureChangeLog`** — this is drift-tool's own attribution/lost-fix log table
  (who changed which procedure, when). Definitely not customer-facing; correctly
  blocked by the same deny-by-default logic, worth naming explicitly rather than
  leaving unexplained.
- `CustomerPhone`, `IntegrationPostedTransactions`, `MAZ_Route_EMAIL_Final`,
  `RecLinkInv`, `ZatcaMode` — **not individually reviewed**, blocked purely because
  they match neither the reference nor the company-col list. Safe (deny-by-default
  means an unreviewed table simply has no path to being queried, same guarantee as
  every table that was never classified at all before this phase), but honest
  status is "unreviewed", not "confirmed must-block" like the 22 above. Extend the
  three lists in `setup/02_introspect.py`/`db/02_tenant_views.sql` if any of these
  turn out to be safe reference data or real join-scopable business data once
  someone actually reads their column lists — same "extend as reviewed" pattern
  `core/catalog.py`'s `CLIENT_NAME_TOKENS` already uses for client-name detection.

## Guard against the obvious wrong fix

Do **not** relax any `t.` view predicate to `CompanyID = @x OR CompanyID IS NULL` to
"catch" nullable-CompanyID rows (a separate, already-flagged issue — 56 of the 344
already-scoped tables have nullable CompanyID). That would make every NULL-tenant row
visible to *every* client — a real cross-tenant leak, not a fix for under-reporting.
