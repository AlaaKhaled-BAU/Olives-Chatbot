---
type: procedure
database: OSFA_DB
name: OT_Payment_Checks_Insert
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_Payment_Checks]]
writes_to:
  - [[OT_Payment_Checks]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payment_Checks_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Payment_Checks. Writes OT_Payment_Checks. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @TransactionYear smallint
- @TransactionNo int
- @TransactionTypeID smallint
- @PaidTransBankID int
- @PaidTransBranchID int
- @PaidTransYear smallint
- @PaidTransNo int
- @PaidTransTypeID smallint
- @PaidTransCustomerID bigint
- @PaidTransChequeNo int
- @PaidAmount float
- @ErrNo SmallInt = 0 output
## Tables Read
- [[OT_Payment_Checks]]
## Tables Written
- [[OT_Payment_Checks]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Payment_Checks]]

**Tables Written**
- [[OT_Payment_Checks]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
