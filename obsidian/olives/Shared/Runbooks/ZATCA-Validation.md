---
type: shared
name: ZATCA-Validation
tags: [#runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# ZATCA-Validation

## Symptom
A KSA e-invoice (tax invoice / simplified tax invoice) is rejected by ZATCA — the tablet or BO shows a ZATCA validation/QR or clearance error, the invoice is not cleared, and the customer cannot get a compliant e-invoice. Errors reference XML schema, cryptographic stamp, or taxpayer/device registration.

## Why it happens
ZATCA requires each invoice to be validated and (for standard invoices) cleared through the JoTax/ZATCA API before it is compliant. The flow runs through [[Pro_JoTaxApi]] / [[Pro_ZatcaIntegrationApi]] which read invoice + taxpayer data from the Zatca config tables ([[ZatcaCompany]], [[ZatcaCustomer]], [[ZatcaMode]], [[ZatcaSalesPersons]]) and generate the signed XML via [[ZatcaResultGenerateXml]]. Failures occur when: the company/device is not registered in [[ZatcaCompany]]/[[ZatcaSalesPersons]], the customer VAT number is invalid in [[ZatcaCustomer]], the mode (simulation vs production) is wrong in [[ZatcaMode]], or the XML fails schema validation in [[JoTaxValidation]].

## Diagnosis
1. Identify the failing invoice and read the API error from [[IntegrationErrorLog]] (source = [[Pro_JoTaxApi]] or [[JoTax_Integ_SendTransaction]]).
2. Confirm ZATCA registration: check [[ZatcaCompany]] for the issuing company and [[ZatcaSalesPersons]] for the device/salesman.
3. Validate the buyer VAT in [[ZatcaCustomer]] and the mode in [[ZatcaMode]].
4. Re-run [[JoTaxValidation]] on the invoice to see the specific schema/QR failure, and inspect [[ZatcaResultGenerateXml]] for the produced XML.

## Fix
1. Correct the missing/wrong registration data in [[ZatcaCompany]] / [[ZatcaSalesPersons]] / [[ZatcaCustomer]].
2. Set the correct environment in [[ZatcaMode]] (sandbox vs production).
3. Regenerate and resend the XML via [[Pro_ZatcaIntegrationApi]]; confirm clearance in [[ZatcaResultGenerateXml]].
4. If the invoice was already posted, coordinate a credit/reissue through the normal invoicing flow.

## Prevention
- Validate ZATCA registration for every new company/device at onboarding.
- Pre-check buyer VAT format before submission.
- Monitor ZATCA reject rates via [[IntegrationErrorLog]] alerts.

## Related
- [[ZatcaCompany]]
- [[Pro_JoTaxApi]]
- [[Pro_ZatcaIntegrationApi]]
- [[JoTaxValidation]]
