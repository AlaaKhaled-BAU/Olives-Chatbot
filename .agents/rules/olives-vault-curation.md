# Olives Vault Curation & Enrichment Rules

These rules govern how the Obsidian Olives vault (`obsidian/olives/Olives_BO/`) must be maintained, enriched, trimmed, and compiled for the Olives SQL chatbot.

---

## 1. Safety & Architecture Guardrails

1. **Never Include Stored Procedure Bodies**:
   - Never paste `OBJECT_DEFINITION`, `CREATE PROCEDURE`, or `ALTER PROCEDURE` code into vault markdown files.
   - Procedure notes contain **metadata only**: Trigger, Purpose, Parameters, Tables Read/Written, and When to Run.
2. **Never Document Runtime SA or IIS `cds` Access**:
   - The chatbot executes read-only queries as `chatbot_ro` against tenant views (`t.TableName`) scoped server-side via `SESSION_CONTEXT('CompanyID')`.
   - Never instruct bypassing `core/gate.py`.
3. **No Customer PII or Secrets**:
   - Never store real customer names, phone numbers, or credentials in notes.

---

## 2. Integration & Third-Party ERP Trimming Rules

The vault must reflect the **authoritative Olives Back-Office (BO) core schema**, free from third-party sync and client-specific clutter.

### Exclusion Patterns:
Purge or exclude notes matching these patterns:
- **Third-Party ERP Integrations**: `SAP_*`, `ABS_*`, `Bonanza_*`, `AX_*`, `GP_*`, `AccPack_*`, `X3_*`, `Phenix_*`, `Wings_*`, `Yolande_*`, `Galaxy_*`, `JV_*`, `Motakaml_*`, `Shamel_*`, `ProTech_*`, `JoTax_*`, `Zatca_*`, `Niroukh_*`, `Falcon_*`, `Hammoudeh_*`, `Spartan_*`, etc.
- **Generic Integrations**: Any procedure or table matching `*Integ*` or `Integration*`.
- **Maintenance Module (`MMS_*`)**: Tables and procedures specific to external maintenance/technicians (`MMS_*`).
- **SMS Gateways**: `SMS_*` or `SMSSEND_*`.
- **Client-Specific ETL Dumps**: One-off customer extraction scripts.

---

## 3. Table Note Enrichment Standard

Every core business table note (`obsidian/olives/Olives_BO/Tables/<Name>.md`) must contain the following sections:

### 3.1 Business Purpose
- 3 to 8 concise sentences explaining what rows represent, data origin (mobile app vs. back-office), and core operational role.
- Keep under ~800 characters so compilation into `vault_cards.sqlite` does not truncate essential information.

### 3.2 Chatbot Semantics
Include a markdown table mapping how users speak (in natural Arabic) to exact columns and filtering logic:

```markdown
## Chatbot semantics
(Query `t.TableName` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| [Arabic intent] | [Columns] | [Filter / SQL condition] |
```

### 3.3 Disambiguation ("Do not confuse with")
Explicitly disambiguate commonly confused pairs:
- Live operational tables (`TransactionsHeaders`, `OrdersHeaders`) vs. Historical archives (`InvoiceHistoryHF`, `SalesOrderHistoryHF`).
- Workflow approval statuses (`WF_MasterLog.LastStatus` / `WF_SubLog.Action`) vs. `SystemCodes.Status` or `LogActionTransaction.ActionID`.
- Actual visits (`LogActionTransaction` with `ActionID = N'0'`) vs. planned route templates (`SalesPersonsRoutes`) vs. system logins (`ActionID = N'7'`).

### 3.4 Grain & Keys
- Detail the exact grain (e.g. one row per item serial in a transaction).
- Specify composite primary key columns and tenant key (`CompanyID` or `CompNo`).

### 3.5 Pipeline
- Detail the operational data flow: Mobile Handheld / OSFA table → Import Procedure name (wikilink) → Target BO Table → Workflow / Accounting Reconciliation.

---

## 4. Rebuilding the Build Pipeline After Edits

Whenever vault notes are edited, the pipeline must be executed:

```bash
cd /media/alaa/data/client-chatbot
set -a && source .env && set +a

CLIENT=105  # or target client
python3.13 setup/sync_vault_from_cache.py --client "$CLIENT"
python3.13 setup/compile_vault_cards.py --client "$CLIENT"
python3.13 setup/04_assemble_docs_corpus.py
python3.13 setup/05_index_docs.py --client "$CLIENT"
```
