---
type: procedure
database: OSFA_DB
name: OT_DirectInvoice
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - Invt_IntegRejTrans
writes_to:
called_by:
  - DB
  - Olives_BO
support_relevance: high
last_verified: 2026-07-05
---
# OT_DirectInvoice


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads Invt_IntegRejTrans. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @CmdType varchar(50)
- @ErrorNo int output
## Tables Read
- Invt_IntegRejTrans
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- DB
- Olives_BO
## Impact / Dependencies

**Tables Read**
- Invt_IntegRejTrans

**Tables Written**
_None_

**Callers**
- DB
- Olives_BO

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_PaymentsTypes]]
- [[OT_PriceList]]
- [[OT_RequestToChangeInvoicePaymentType]]
- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]

- [[OT_RequestToAddDiscountInOrder_Insert]]
- [[OT_GPSLogImages_Insert]]
- [[OT_Online_RptMultiStoreQty]]
- [[Glossary]]
