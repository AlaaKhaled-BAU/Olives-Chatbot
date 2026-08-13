---
type: procedure
database: OSFA_DB
name: OT_AddPaymentBankTransferImages
schema: dbo
tags: [#billing, #mobile, #order]
reads_from:
  - [[OT_PaymentsBankTransferImages]]
writes_to:
  - [[OT_PaymentsBankTransferImages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_AddPaymentBankTransferImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_PaymentsBankTransferImages. Writes OT_PaymentsBankTransferImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @BankTransferImage image
- @ErrNo SmallInt Output
## Tables Read
- [[OT_PaymentsBankTransferImages]]
## Tables Written
- [[OT_PaymentsBankTransferImages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_PaymentsBankTransferImages]]

**Tables Written**
- [[OT_PaymentsBankTransferImages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
