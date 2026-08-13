---
type: shared
name: Conflict-Report
tags: [#reference, #shared]
---

# Cross-Database Name Conflicts

> **Generated**: 2026-07-06
> **Scope**: Tables with identical names in Olives_BO and OSFA_DB

## Summary

| Total shared names | Ambiguity risk |
|---|---|
| 3 | Medium — disambiguated by folder context |

**Note**: The vault has 3 conflicting names (not 8 as previously estimated). The remaining 5 presumed conflicts are OSFA_DB tables with the `OT_` prefix (e.g. `OT_Checks`, `OT_Contracts`) which share a concept with an Olives_BO table `Checks`, `Contracts` but are *distinct filenames* and thus safe for wikilinks.

## Shared Table Names

| # | Table Name | Olives_BO | OSFA_DB | Conflict? |
|---|---|---|---|---|
| 1 | `Olives_BO/Tables/CompanyParameters\|CompanyParameters` | System-wide config flags for back office server (70+ columns: feature toggles, ERP integration, security policy) | System-wide config for field automation (4 columns: CompanyID, ImportTransInServerDate, NumberSavedFraction, TruncRoundValue) | **Yes** — different column sets despite same purpose |
| 2 | `Olives_BO/Tables/GapTransHeaders\|GapTransHeaders` | Server-side gap transaction headers (PK: GapTransNo, CompanyID, GapTransYear; includes IsDone flag) | Tablet-side gap transaction headers (PK: DeviceSysID, CompanyID; includes IsPosted flag) | **Yes** — different PK, different platform origin |
| 3 | `Olives_BO/Tables/GapTransTags\|GapTransTags` | Server-side gap transaction tags (PK: GapTransNo, CompanyID, GapTagID, GapTransYear) | Tablet-side gap transaction tags (PK: DeviceSysID, CompanyID, GapTagID; no GapTransNo) | **Yes** — different PK structure, device-scoped vs transaction-scoped |

## How to Disambiguate

When linking to a shared-name table, qualify with the database path:
- Use `Olives_BO/Tables/CompanyParameters|CompanyParameters` for BO version
- Use `OSFA_DB/Tables/CompanyParameters|CompanyParameters` for OSFA version

## Auto-Detection Query
```dataview
TABLE file.link AS Note, database AS DB, type
FROM ""
WHERE type = "table"
```
