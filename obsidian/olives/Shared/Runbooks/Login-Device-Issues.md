---
type: shared
name: Login-Device-Issues
tags: [#runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# Login-Device-Issues

## Symptom
A salesman cannot log in on a new or existing tablet: the app rejects the credentials, says the device is not permitted, prompts for a passkey that never validates, or the user has no permissions for the actions they need.

## Why it happens
Login is gated by three controls. (1) User identity in [[Users]] must be active and linked to a salesman. (2) Device authorization is enforced by [[SalesPersonsDevicePermissions]] — a new device has no row, so login is blocked. (3) When [[CompanyParameters]] has `UsePassKeyWithTime = 1`, the app requires a time-based passkey; clock skew or an unissued passkey fails validation. Permissions/category scoping additionally flow through [[WF_SalesPersonItemsCategoryValues]] and [[Pro_OlivesUserPermissions]], so even a logged-in user may be blocked from items/categories.

## Diagnosis
1. Confirm the user exists and is active in [[Users]] and linked to the correct salesman.
2. Check [[SalesPersonsDevicePermissions]] for a row mapping this device (serial/IMEI) to the salesman; missing = blocked.
3. Inspect [[CompanyParameters]] for `UsePassKeyWithTime`; if enabled, verify the passkey issuance and device clock.
4. Check category/item scoping in [[WF_SalesPersonItemsCategoryValues]] and function permissions in [[Pro_OlivesUserPermissions]].

## Fix
1. Register the new device: add/enable a row in [[SalesPersonsDevicePermissions]] for the salesman + device.
2. If passkey is required, issue/reset the passkey and ensure device time is correct.
3. Grant missing permissions via [[Pro_OlivesUserPermissions]] or adjust [[WF_SalesPersonItemsCategoryValues]] scoping.
4. Re-attempt login; if still failing, capture the error from the device log and [[OT_ErrorLogInteg]].

## Prevention
- Pre-register devices in [[SalesPersonsDevicePermissions]] during salesman onboarding.
- Document passkey issuance when `UsePassKeyWithTime` is on.
- Periodically audit device-permission and permission assignments.

## Related
- [[Users]]
- [[SalesPersonsDevicePermissions]]
- [[CompanyParameters]]
- [[WF_SalesPersonItemsCategoryValues]]
