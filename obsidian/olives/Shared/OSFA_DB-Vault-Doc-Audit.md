---
type: shared
name: OSFA_DB-Vault-Doc-Audit
tags: [#reference, #shared, #audit]
---

# OSFA_DB — Vault Documentation Audit

> Generated: 2026-08-05
> Source: DB object lists from `osfa_PEEK` (restore of the "105" backup set, SQL Server 2022).
> Vault scope: `OSFA_DB/Tables/*.md` and `OSFA_DB/Procedures/*.md`.
> Method: case-insensitive name comparison, existence only. No content review.

## Summary

| Objects | DB count | Vault count | Missing in vault | Vault-only |
|---------|----------|-------------|------------------|------------|
| Tables  | 192      | 188         | 5                | 1          |
| Procs   | 212      | 205         | 7                | 0          |

> **Status: RESOLVED 2026-08-05** — all 5 missing tables and 7 missing procs have been documented (see [Documentation Generated](#documentation-generated-2026-08-05)). Vault now has 193 tables / 212 procs.

OSFA is in far better shape than Olives_BO: 30 vs 5 tables missing, 219 vs 7 procs missing.

---

## Tables missing in vault (5)

- OT_BankDepositDF
- OT_BankDepositHF
- OT_RequestToCancelPayment
- OT_StoreItemsQty_Main_ERP
- OrdersSMSSebd

Same payment/bank-deposit feature family that is undocumented in Olives_BO (`BankDepositDF/HF`, `RequestToCancelPayment`).

## Tables in vault but not in DB (1)

- AZOT_SystemOptions — likely renamed/merged in the current DB, or doc-only.

---

## Procs missing in vault (7)

- OT_BankDepositDF_CheckExist
- OT_BankDepositDF_Insert
- OT_BankDepositHF_CheckExist
- OT_BankDepositHF_Insert
- OT_RequestToCancelPayment_Insert
- Pro_SendOrderSMS
- Rpt_CompetitveItemsData

## Procs in vault but not in DB (0)

All vault procs exist in the DB.

---

## Notes
- The undocumented procs map 1:1 to the undocumented tables (bank deposit + request-to-cancel-payment import flow) — one feature, missing entirely from the vault.
- `Rpt_CompetitveItemsData` is also missing in Olives_BO vault — one report, two DBs.
- Full machine-readable lists for OSFA_DB are in the DB object dumps used to generate this file.
---

## Documentation Generated (2026-08-05)

All objects listed above as missing from the vault have now been documented with full metadata extracted from the DB:

### Created
- **5 table notes** in `OSFA_DB/Tables/` — columns/PK/FKs, procedures that read/write (incl. cross-DB callers from Olives_BO), estimated rows
- **7 procedure notes** in `OSFA_DB/Procedures/` — parameters, tables read/written, callers/callees
- **1 relation note** in `OSFA_DB/Relations/` — `OT_BankDepositDF--OT_BankDepositHF`

### Cross-DB links
- `OT_BankDepositDF/HF` notes show Olives_BO callers (`OT_ImportBankDeposit`, `OT_SendSalesmanData`, `OT_ImportRequestToCancelPayment`) linked via `[[Olives_BO/Procedures/X|X]]`
- OSFA proc notes show BO tables they reference (e.g. `Pro_SendOrderSMS` ↔ BO tables)

### Linking conventions
- Same as Olives_BO: proc frontmatter `reads_from`/`writes_to`/`called_by`, table frontmatter `foreign_keys`/`procedures_reading`, cross-DB links with full path + alias
- MOC updated: Tables (193), Procedures (212), Relations (9)

### Generation source
- Metadata extracted live from `osfa_PEEK` (snapshot of the 105 backup set); same method as Olives_BO
- ALL notes are AUTO-GENERATED — verify before trusting
