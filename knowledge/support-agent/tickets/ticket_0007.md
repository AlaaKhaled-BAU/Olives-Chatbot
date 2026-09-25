# Ticket 0007: Sales Order Upload — Items/Stock Not Loading (System Options Off)

* **Date & Time**: 2026-07-20 (lodged)
* **Customer**: Luxury Items
* **System Component**: Back Office (Sales Order / Upload Order)
* **Symptom Category**: Configuration / Stock Availability
* **Reported Issue**:
  When the salesman creates an upload order and selects an item (for example item 1), the system loads the item itself but does not load its stock quantity — it reports "there are no items in the stock." Other items load their cases correctly but not the pieces. The salesman cannot complete the upload order because quantities appear unavailable.

* **Root Cause & Diagnosis**:
  - The behavior was caused by two System Options being turned off:
    1. **Sales Order Main Store With 999999** — without this, the order does not fall back to the main store (999999), so stock from the main warehouse is not considered available for the order.
    2. **Auto Refresh Qty In Sales Order** — without this, item quantities are not refreshed/loaded into the sales order line, so the stock check returns empty and items show as "no items in the stock," and pieces (as opposed to cases) are not populated.
  - Both options are required for the upload-order flow to correctly resolve and display stock quantities (cases and pieces) from the main store.

* **Proposed Solution**:
  - Enable the two System Options in Back Office:
    1. Turn **ON** `Sales Order Main Store With 999999`.
    2. Turn **ON** `Auto Refresh Qty In Sales Order`.
  - Save the options and have the salesman retry creating the upload order and selecting the item.

* **Verification Result**: After enabling both options, selecting an item in the upload order correctly loads its stock (cases and pieces) from the main store (999999), and the "no items in the stock" message no longer appears.

(End of file - total 21 lines)
