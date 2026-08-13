---
type: procedure
database: Olives_BO
name: Alpha_SendData
schema: dbo
tags: [#backoffice]
reads_from:
writes_to:
called_by:
  - [[Alpha_Integ_SendReceipts]]
  - [[Alpha_Integ_SendSalesInvoices]]
  - [[Alpha_Integ_SendSalesOrders]]
  - [[Alpha_Integ_SendTransfersOrders]]
  - [[OT_CustGalaryImages]]
  - [[OT_ImportCustomerGPS]]
  - [[OT_ImportCustStockTacking]]
  - [[OT_ImportReceipts]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_ImportSalesOrders]]
  - [[OT_ImportUploadOrders]]
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_SendData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Calls 11 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
_None_
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Alpha_Integ_SendReceipts]]
- [[Alpha_Integ_SendSalesInvoices]]
- [[Alpha_Integ_SendSalesOrders]]
- [[Alpha_Integ_SendTransfersOrders]]
- [[OT_CustGalaryImages]]
- [[OT_ImportCustomerGPS]]
- [[OT_ImportCustStockTacking]]
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportUploadOrders]]
## Impact / Dependencies

**Tables Read**
_None_

**Tables Written**
_None_

**Callers**
- [[Alpha_Integ_SendReceipts]]
- [[Alpha_Integ_SendSalesInvoices]]
- [[Alpha_Integ_SendSalesOrders]]
- [[Alpha_Integ_SendTransfersOrders]]
- [[OT_CustGalaryImages]]
- [[OT_ImportCustomerGPS]]
- [[OT_ImportCustStockTacking]]
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportUploadOrders]]

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
