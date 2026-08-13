---
type: shared
name: Schema-Drift-Log
tags: [#reference, #shared]
---

# Schema Drift Log

> Generated: 2026-07-05  
> Baseline: SQL backup files dated 2026-06-14  
> CSV matches the latest SQL schema used for note generation.

## Drift Summary
### Olives_BO
- **Tables**: SQL has 410, CSV has 410
  - No new tables
  - No dropped tables
- **Procedures**: SQL has 1446, CSV has 1450
  - No new procedures
  - Dropped from CSV: RPT_CUSTOMERSALESDETAILSBYITEMANDSALESPERSONNAME, RPT_SALESDETAILSCUSTOMERSBYVALUE, RPT_SUMMARYSALESAND, SMSSEND_ZUMOT
### OSFA_DB
- **Tables**: SQL has 188, CSV has 188
  - No new tables
  - No dropped tables
- **Procedures**: SQL has 205, CSV has 205
  - No new procedures
  - No dropped procedures

## Notes
- The Inventory-Master.csv was generated from the same SQL files used for note generation.
- True drift can only be detected against a live production database.
- To re-detect drift: re-extract schema from live DB and compare with this CSV.
